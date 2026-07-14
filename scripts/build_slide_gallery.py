"""Regenerate gallery/slide-prompts/site/index.html from prompts/*.md.

Usage: python scripts/build_slide_gallery.py

Renders each style as an actual mini slide mockup (real headline copy,
resolved background/ink/accent colors, a font pairing, and a CSS-generated
texture/duotone block standing in for photography — Artifacts can't fetch
external images). To add a new style: drop a new prompts/<slug>.md in the
existing frontmatter + [STYLE SPEC]/[LAYOUT RULES]/[FORBIDDEN] format, add
a SLIDE_CONTENT[slug] entry below with real kicker/headline/subhead copy,
then rerun this script.
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROMPTS_DIR = ROOT / "gallery" / "slide-prompts" / "prompts"
SITE_DIR = ROOT / "gallery" / "slide-prompts" / "site"

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.DOTALL)
SECTION_RE = re.compile(
    r"## \[STYLE SPEC\]\n(.*?)\n## \[LAYOUT RULES\]\n(.*?)\n## \[FORBIDDEN\]\n(.*?)"
    r"(?:\n## \[FULL PROMPT.*?\](?:\n(.*?))?)?\s*$",
    re.DOTALL,
)

# Named (non-hex) palette phrases -> hex, hand-mapped from each STYLE SPEC's own wording.
NAMED_COLOR_MAP = {
    "midnight navy": "#0B1B3A", "electric cyan": "#22D3EE", "violet": "#7C3AED", "white": "#FFFFFF",
    "black": "#111111", "international red": "#E1261C",
    "newsprint": "#F0EAE0", "ink black": "#1A1A1A", "muted burgundy": "#7A2333",
    "charcoal": "#2B2B2B", "copper": "#B87333", "signal green": "#3ECF8E", "off-white": "#F5F1EA",
    "dusty pink": "#D9A9A6", "shell pink": "#F3D9D3",
    "near-black": "#0D0D0D", "warm white": "#F5F1E8", "muted silver": "#B8B4AC",
    "academic blue": "#1E4E8C",
    "cream": "#F3E9D2", "varsity red": "#A3242A", "navy": "#1B2A4A", "warm gold": "#C9A227",
}


def resolve_palette(raw: str) -> list[str]:
    if not raw or raw.strip().lower() == "see prompt":
        return ["#3D3D3D", "#F2F2F2"]
    raw = raw.replace(" / ", ", ")
    parts = [p.strip() for p in raw.split(",") if p.strip()]
    hexes = []
    for p in parts:
        if p.startswith("#"):
            hexes.append(p)
        elif p.lower() in NAMED_COLOR_MAP:
            hexes.append(NAMED_COLOR_MAP[p.lower()])
        else:
            hexes.append(NAMED_COLOR_MAP.get(p.lower(), "#888888"))
    return hexes


def luminance(hexcolor: str) -> float:
    h = hexcolor.lstrip("#")
    if len(h) != 6:
        return 0.5
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))

    def lin(c):
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4

    r, g, b = lin(r), lin(g), lin(b)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def chroma(hexcolor: str) -> float:
    h = hexcolor.lstrip("#")
    if len(h) != 6:
        return 0
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return (max(r, g, b) - min(r, g, b)) / 255


def pick_roles(hexes: list[str]) -> dict:
    bg = hexes[0]
    bg_l = luminance(bg)
    rest = hexes[1:] or hexes
    ink = max(rest, key=lambda c: abs(luminance(c) - bg_l))
    remaining = [c for c in rest if c != ink] or rest
    accent = max(remaining, key=chroma)
    accent2_pool = [c for c in remaining if c != accent]
    accent2 = accent2_pool[0] if accent2_pool else accent
    return {"bg": bg, "ink": ink, "accent": accent, "accent2": accent2}


def font_role(fonts: list[str]) -> str:
    joined = " ".join(fonts).lower()
    if "mono" in joined:
        return "mono"
    if any(k in joined for k in ("serif", "garamond", "cormorant", "fraunces", "bodoni")):
        return "serif"
    return "sans"


FONT_STACKS = {
    "serif": "Georgia, 'Iowan Old Style', 'Palatino Linotype', 'Book Antiqua', serif",
    "sans": "-apple-system, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif",
    "mono": "ui-monospace, 'SFMono-Regular', Menlo, Consolas, 'Liberation Mono', monospace",
}

LAYOUT_PRIORITY = [
    ("editorial", ["editorial", "literary"]),
    ("tech", ["tech-product", "dark", "technical", "developer", "futuristic"]),
    ("diagonal", ["high-energy-pop", "sports", "retro"]),
    ("split", ["creative-portfolio"]),
    ("notebook", ["education"]),
    ("hero", ["pitch", "consulting-exec", "minimal-premium"]),
]


def pick_layout(tags: list[str]) -> str:
    for layout, keys in LAYOUT_PRIORITY:
        if any(k in tags for k in keys):
            return layout
    return "hero"


SLIDE_CONTENT = {
    "athletic-energy": ("PERFORMANCE REVIEW", "Q3 was our fastest season yet.", "Sprint times down 4.2% across every division."),
    "aurora": ("SERIES A", "The infrastructure layer for agentic finance.", "$2.4M ARR, 140% net revenue retention."),
    "basel": ("PORTFOLIO 04", "Form follows argument.", "Selected identity systems, 2023–2026."),
    "boardroom": ("STRATEGY REVIEW", "Consolidate three warehouses into one regional hub.", "Projected savings: $4.1M annually, break-even in 14 months."),
    "bold-signal": ("KEYNOTE", "Ship the thing that scares you.", "Three principles from four years of shipping."),
    "broadsheet": ("MARKET BRIEFING", "Rate cuts won’t save Q4 margins.", "A read on consumer credit ahead of the holiday season."),
    "circuit": ("SYSTEM DESIGN", "Route requests through the regional edge first.", "Latency: 340ms → 61ms at p99."),
    "creative-voltage": ("CAMPAIGN 002", "Loud enough to skip.", "A launch built for six-second attention spans."),
    "dark-botanical": ("REFLECTIONS", "What we chose not to build.", "Notes on restraint, three years in."),
    "electric-studio": ("PROPOSAL", "A new checkout, in six weeks.", "Scope, timeline, and the team we’d assign."),
    "mature-magazine": ("PROFILE", "The quiet return of analog mornings.", "How one founder built a business around slowness."),
    "modern-newspaper": ("TREND WATCH", "Everyone’s building an agent. Few are shipping one.", "A field report from 40 product teams."),
    "monolith": ("INVESTMENT MEMO", "One number matters here.", "92% gross margin, held for six consecutive quarters."),
    "neon-cyber": ("SECURITY", "The breach that didn’t happen.", "How anomaly detection caught it in 400ms."),
    "notebook-tabs": ("MODULE 3", "Reading a balance sheet in ten minutes.", "Workbook, exercises, and one worked example."),
    "paper-and-ink": ("LECTURE", "On the slow death of the footnote.", "Notes toward a defense of citation."),
    "pastel-geometry": ("GETTING STARTED", "Your first workspace, in three steps.", "No credit card, no setup call, five minutes."),
    "premium-mockup": ("PRODUCT LAUNCH", "Introducing Aperture, on every screen you own.", "Available today on iOS, web, and desktop."),
    "seminar": ("RESEARCH TALK", "Why attention collapses under long context.", "Evidence from 40 transformer checkpoints."),
    "split-pastel": ("WORKSHOP", "Let’s design your onboarding flow together.", "Bring a problem, leave with a prototype."),
    "swiss-modern": ("STRATEGY", "Precision is the strategy.", "A framework for decisions under uncertainty."),
    "terminal-green": ("POSTMORTEM", "22 minutes of downtime, one bad migration.", "What broke, what we shipped, what changes next."),
    "varsity": ("KICKOFF 2026", "One team, one scoreboard.", "Everything we’re building toward this season."),
    "vintage-editorial": ("ESSAY", "In defense of the boring meeting.", "Structure is not the enemy of creativity."),
    "glass-panel": ("PRODUCT REVEAL", "One dashboard, everything visible.", "Real-time metrics behind a single frosted pane."),
    "soft-relief": ("WELLNESS", "Slow down, on purpose.", "A four-week reset for teams running too hot."),
    "clay-capsule": ("WELCOME", "Let’s get you set up.", "Three taps, no jargon, five minutes."),
    "raw-mono": ("POSTMORTEM", "The build broke because we skipped a step.", "Root cause, fix, and the check we added."),
    "memphis-mono": ("COLLECTION 04", "Nothing extra.", "A monochrome study in restraint."),
    "frosted-aurora": ("LAUNCH", "Soft is the new loud.", "Introducing Aura, out this spring."),
    "warning-grid": ("SYSTEM ALERT", "This changes how you ship.", "Read before your next deploy."),
    "riso-print": ("ISSUE 03", "Made by hand, mostly.", "Notes from a year of small batches."),
    "block-world": ("HOW IT WORKS", "Three blocks, one pipeline.", "Ingest, transform, serve — visualized."),
    "poly-cube": ("DATA MODEL", "Every face tells a different story.", "Six facets of the same customer."),
    "gilded-line": ("10 YEARS", "A decade, quietly done well.", "An anniversary retrospective."),
    "cyanotype-plan": ("SYSTEM DESIGN", "Every component, to scale.", "Section view of the new platform."),
    "ink-wave": ("HERITAGE", "What travels with us.", "Notes on craft across three generations."),
}


def parse_frontmatter(text: str) -> dict:
    fields = {}
    for line in text.splitlines():
        if not line.strip() or ":" not in line:
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip()
        if value.startswith("[") and value.endswith("]"):
            items = [v.strip().strip('"') for v in value[1:-1].split(",") if v.strip()]
            fields[key] = items
        else:
            fields[key] = value.strip('"')
    return fields


def parse_card(path: Path) -> dict:
    raw = path.read_text(encoding="utf-8")
    m = FRONTMATTER_RE.match(raw)
    if not m:
        raise ValueError(f"{path} missing frontmatter")
    fm = parse_frontmatter(m.group(1))
    body = m.group(2)
    sm = SECTION_RE.search(body)
    if not sm:
        raise ValueError(f"{path} missing STYLE SPEC/LAYOUT RULES/FORBIDDEN sections")
    fm["slug"] = path.stem
    fm["style_spec"] = sm.group(1).strip()
    fm["layout_rules"] = sm.group(2).strip()
    fm["forbidden"] = sm.group(3).strip()
    fm["full_verbatim"] = sm.group(4).strip() if sm.group(4) else None
    fm["hexes"] = resolve_palette(fm.get("palette", ""))
    fm["roles"] = pick_roles(fm["hexes"])
    fm["font_role"] = font_role(fm.get("fonts", []))
    if not fm.get("preview_image"):
        auto_preview = PROMPTS_DIR.parent / "previews" / f"{fm['slug']}.webp"
        if auto_preview.exists():
            fm["preview_image"] = f"../previews/{fm['slug']}.webp"
    fm["layout"] = "photo" if fm.get("preview_image") else pick_layout(fm.get("tags", []))
    if fm["slug"] in SLIDE_CONTENT:
        fm["kicker"], fm["headline"], fm["subhead"] = SLIDE_CONTENT[fm["slug"]]
    else:
        fm["kicker"] = (fm.get("tags") or ["style"])[0].upper().replace("-", " ")
        fm["headline"] = fm["name"]
        fm["subhead"] = fm.get("use_case", "")
    return fm


def full_prompt_text(card: dict) -> str:
    text = (
        f"[STYLE SPEC]\n{card['style_spec']}\n\n"
        f"[LAYOUT RULES]\n{card['layout_rules']}\n\n"
        f"[FORBIDDEN]\n{card['forbidden']}"
    )
    if card.get("full_verbatim"):
        text += f"\n\n[FULL PROMPT — verbatim]\n{card['full_verbatim']}"
    return text


def texture_style(card: dict) -> str:
    """CSS background standing in for a photograph: layered gradients in the
    card's own accent/ink colors, since artifacts cannot fetch external images."""
    r = card["roles"]
    return (
        f"radial-gradient(circle at 30% 20%, {r['accent']}55, transparent 55%), "
        f"radial-gradient(circle at 75% 70%, {r['accent2']}66, transparent 60%), "
        f"linear-gradient(160deg, {r['ink']}22, {r['bg']})"
    )


def render_slide(card: dict) -> str:
    r = card["roles"]
    font = FONT_STACKS[card["font_role"]]
    layout = card["layout"]
    kicker, headline, subhead = card["kicker"], card["headline"], card["subhead"]
    style_vars = (
        f"--s-bg:{r['bg']};--s-ink:{r['ink']};--s-accent:{r['accent']};--s-accent2:{r['accent2']};"
        f"--s-font:{font};"
    )
    texture = texture_style(card)

    if layout == "photo":
        img = card["preview_image"]
        scrim = f"linear-gradient(180deg, transparent 40%, {r['bg']}f0 92%)"
        return f"""
      <div class="slide slide--photo" style="{style_vars}">
        <span class="badge-real">real sample</span>
        <img class="s-photo-real" src="{img}" alt="{card['name']} sample" loading="lazy" />
        <div class="s-scrim" style="background:{scrim}"></div>
        <div class="s-content s-content--photo">
          <div class="s-kicker">{kicker}</div>
          <h3 class="s-headline">{headline}</h3>
          <p class="s-subhead">{subhead}</p>
        </div>
      </div>"""

    if layout == "hero":
        body = f"""
        <div class="s-kicker">{kicker}</div>
        <div class="s-rule"></div>
        <h3 class="s-headline">{headline}</h3>
        <p class="s-subhead">{subhead}</p>"""
    elif layout == "editorial":
        body = f"""
        <div class="s-kicker">{kicker}</div>
        <h3 class="s-headline s-headline--editorial">{headline}</h3>
        <p class="s-subhead">{subhead}</p>
        <div class="s-byline">Source: internal analysis</div>"""
    elif layout == "tech":
        body = f"""
        <div class="s-kicker s-kicker--mono">// {kicker}</div>
        <h3 class="s-headline s-headline--tech">{headline}</h3>
        <p class="s-subhead s-subhead--mono">{subhead}</p>
        <div class="s-node"></div>"""
    elif layout == "diagonal":
        body = f"""
        <div class="s-band"></div>
        <div class="s-kicker">{kicker}</div>
        <h3 class="s-headline s-headline--diagonal">{headline}</h3>
        <p class="s-subhead">{subhead}</p>"""
    elif layout == "split":
        body = f"""
        <div class="s-split-left" style="background:{texture}"></div>
        <div class="s-split-right">
          <div class="s-kicker">{kicker}</div>
          <h3 class="s-headline">{headline}</h3>
          <p class="s-subhead">{subhead}</p>
        </div>"""
    else:  # notebook
        body = f"""
        <div class="s-tabs"><span></span><span></span><span></span></div>
        <div class="s-kicker">{kicker}</div>
        <h3 class="s-headline">{headline}</h3>
        <p class="s-subhead">{subhead}</p>"""

    photo_block = "" if layout == "split" else f'<div class="s-photo" style="background:{texture}"></div>'

    return f"""
      <div class="slide slide--{layout}" style="{style_vars}">
        {photo_block}
        <div class="s-content">{body}</div>
      </div>"""


TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<title>HKTK Slide Prompt Gallery</title>
<meta name="viewport" content="width=device-width, initial-scale=1" />
<style>
:root {{
  --bg: #eef0ea;
  --bg-raised: #ffffff;
  --ink: #17191c;
  --ink-soft: #52584f;
  --line: #d6d9cf;
  --accent: #2a5c74;
  --accent-ink: #ffffff;
  --chip-bg: #e2e6da;
  --chip-active-bg: #2a5c74;
  --chip-active-ink: #ffffff;
  --mono: ui-monospace, "SFMono-Regular", Menlo, Consolas, "Liberation Mono", monospace;
  --sans: -apple-system, "Segoe UI", "Helvetica Neue", Arial, sans-serif;
  --serif: Georgia, "Iowan Old Style", "Palatino Linotype", "Book Antiqua", serif;
}}
@media (prefers-color-scheme: dark) {{
  :root {{ --bg:#14161a; --bg-raised:#1c1f24; --ink:#eceee9; --ink-soft:#a7ada1; --line:#333730; --accent:#7fb8c9; --accent-ink:#0d1113; --chip-bg:#23261f; --chip-active-bg:#7fb8c9; --chip-active-ink:#0d1113; }}
}}
:root[data-theme="dark"] {{ --bg:#14161a; --bg-raised:#1c1f24; --ink:#eceee9; --ink-soft:#a7ada1; --line:#333730; --accent:#7fb8c9; --accent-ink:#0d1113; --chip-bg:#23261f; --chip-active-bg:#7fb8c9; --chip-active-ink:#0d1113; }}
:root[data-theme="light"] {{ --bg:#eef0ea; --bg-raised:#ffffff; --ink:#17191c; --ink-soft:#52584f; --line:#d6d9cf; --accent:#2a5c74; --accent-ink:#ffffff; --chip-bg:#e2e6da; --chip-active-bg:#2a5c74; --chip-active-ink:#ffffff; }}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--bg); color: var(--ink); font-family: var(--sans); line-height: 1.5; }}
header {{ position: sticky; top: 0; z-index: 5; background: var(--bg); border-bottom: 1px solid var(--line); padding: 1.5rem clamp(1rem, 4vw, 3rem) 1rem; }}
h1 {{ font-family: var(--serif); font-weight: 400; font-size: clamp(1.6rem, 3vw, 2.2rem); margin: 0 0 0.25rem; text-wrap: balance; }}
.subtitle {{ color: var(--ink-soft); margin: 0 0 1rem; max-width: 62ch; }}
.filters {{ display: flex; flex-wrap: wrap; gap: 0.5rem; align-items: center; }}
.chip {{ font-family: var(--mono); font-size: 0.75rem; letter-spacing: 0.02em; padding: 0.35rem 0.7rem; border-radius: 999px; background: var(--chip-bg); color: var(--ink-soft); border: 1px solid transparent; cursor: pointer; user-select: none; }}
.chip[aria-pressed="true"] {{ background: var(--chip-active-bg); color: var(--chip-active-ink); }}
.chip:focus-visible {{ outline: 2px solid var(--accent); outline-offset: 2px; }}
.count {{ font-family: var(--mono); font-size: 0.75rem; color: var(--ink-soft); margin-left: auto; }}
main {{ padding: 1.5rem clamp(1rem, 4vw, 3rem) 4rem; }}
.grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 1.25rem; }}
.card {{ background: var(--bg-raised); border: 1px solid var(--line); border-radius: 10px; overflow: hidden; display: flex; flex-direction: column; }}

/* --- slide mockup (16:9) --- */
.slide {{ position: relative; aspect-ratio: 16/9; background: var(--s-bg); color: var(--s-ink); overflow: hidden; display: flex; }}
.s-photo {{ position: absolute; inset: 0; opacity: 0.9; }}
.s-content {{ position: relative; z-index: 1; padding: 7% 8%; display: flex; flex-direction: column; justify-content: center; gap: 0.4em; width: 100%; }}
.s-kicker {{ font-family: var(--mono); font-size: 0.62rem; letter-spacing: 0.12em; color: var(--s-accent); text-transform: uppercase; }}
.s-kicker--mono {{ color: var(--s-accent); }}
.s-rule {{ width: 2.5rem; height: 2px; background: var(--s-accent); margin: 0.3em 0; }}
.s-headline {{ font-family: var(--s-font); font-weight: 700; font-size: clamp(1rem, 2.6vw, 1.5rem); line-height: 1.15; margin: 0; text-wrap: balance; max-width: 18ch; }}
.s-headline--editorial {{ font-weight: 400; font-style: italic; max-width: 20ch; }}
.s-headline--tech {{ font-family: var(--mono); font-weight: 600; }}
.s-headline--diagonal {{ font-weight: 800; text-transform: uppercase; letter-spacing: -0.01em; }}
.s-subhead {{ font-size: 0.72rem; color: var(--s-ink); opacity: 0.75; margin: 0; max-width: 26ch; }}
.s-subhead--mono {{ font-family: var(--mono); }}
.s-byline {{ font-family: var(--mono); font-size: 0.58rem; opacity: 0.6; margin-top: 0.6em; }}
.s-node {{ position: absolute; right: 8%; bottom: 10%; width: 10px; height: 10px; border-radius: 50%; background: var(--s-accent); box-shadow: 0 0 0 6px color-mix(in srgb, var(--s-accent) 25%, transparent); }}
.s-band {{ position: absolute; inset: -10% -20%; background: var(--s-accent); transform: skewY(-6deg); opacity: 0.14; }}
.s-tabs {{ position: absolute; top: 10%; right: 6%; display: flex; flex-direction: column; gap: 6px; }}
.s-tabs span {{ width: 22px; height: 8px; border-radius: 3px; background: var(--s-accent); opacity: 0.7; }}
.s-tabs span:nth-child(2) {{ background: var(--s-accent2); }}
.slide--photo {{ padding: 0; }}
.s-photo-real {{ position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; }}
.s-scrim {{ position: absolute; inset: 0; }}
.s-content--photo {{ justify-content: flex-end; padding-bottom: 8%; }}
.badge-real {{ position: absolute; top: 3%; left: 3%; z-index: 2; font-family: var(--mono); font-size: 0.58rem; letter-spacing: 0.08em; text-transform: uppercase; background: color-mix(in srgb, var(--s-bg) 55%, transparent); color: var(--s-ink); padding: 0.15rem 0.5rem; border-radius: 4px; }}
.slide--split {{ padding: 0; }}
.s-split-left {{ width: 42%; height: 100%; }}
.s-split-right {{ width: 58%; padding: 8% 7%; display: flex; flex-direction: column; justify-content: center; gap: 0.4em; }}

.card-body {{ padding: 0.85rem 1rem 1rem; display: flex; flex-direction: column; gap: 0.45rem; flex: 1; }}
.card h2 {{ font-family: var(--serif); font-weight: 400; font-size: 1.05rem; margin: 0; }}
.use-case {{ color: var(--ink-soft); font-size: 0.8rem; margin: 0; }}
.tags {{ display: flex; flex-wrap: wrap; gap: 0.3rem; }}
.tag {{ font-family: var(--mono); font-size: 0.65rem; color: var(--ink-soft); background: var(--chip-bg); padding: 0.15rem 0.45rem; border-radius: 4px; }}
.fonts {{ font-family: var(--mono); font-size: 0.68rem; color: var(--ink-soft); }}
.palette-row {{ display: flex; gap: 4px; }}
.palette-row span {{ width: 14px; height: 14px; border-radius: 3px; border: 1px solid var(--line); }}
details {{ margin-top: 0.3rem; border-top: 1px solid var(--line); padding-top: 0.45rem; }}
summary {{ cursor: pointer; font-size: 0.76rem; color: var(--accent); }}
pre {{ white-space: pre-wrap; font-family: var(--mono); font-size: 0.7rem; background: var(--bg); border: 1px solid var(--line); border-radius: 6px; padding: 0.6rem; margin: 0.5rem 0 0; max-width: 100%; overflow-x: auto; }}
.card-actions {{ display: flex; gap: 0.5rem; margin-top: 0.3rem; }}
button.copy {{ font-family: var(--mono); font-size: 0.7rem; background: var(--accent); color: var(--accent-ink); border: none; border-radius: 6px; padding: 0.4rem 0.7rem; cursor: pointer; }}
button.copy:focus-visible {{ outline: 2px solid var(--ink); outline-offset: 2px; }}
.source {{ font-size: 0.66rem; color: var(--ink-soft); display: flex; gap: 0.4rem; align-items: center; }}
.source a {{ color: inherit; }}
.license-tag {{ font-family: var(--mono); font-size: 0.6rem; padding: 0.08rem 0.4rem; border-radius: 3px; }}
.license-mit {{ background: #dcefe0; color: #1c5c33; }}
.license-internal {{ background: #f3e0c8; color: #6b4a15; }}
@media (prefers-color-scheme: dark) {{
  .license-mit {{ background: #16301f; color: #7fd99a; }}
  .license-internal {{ background: #3a2c12; color: #e0b567; }}
}}
:root[data-theme="dark"] .license-mit {{ background: #16301f; color: #7fd99a; }}
:root[data-theme="dark"] .license-internal {{ background: #3a2c12; color: #e0b567; }}
.library-banner {{ display: flex; justify-content: space-between; align-items: center; gap: 1rem; background: var(--chip-bg); border-radius: 8px; padding: 0.6rem 0.9rem; margin-top: 0.9rem; font-size: 0.8rem; }}
.library-banner a {{ color: var(--accent); font-weight: 600; text-decoration: none; }}
footer {{ padding: 1rem clamp(1rem, 4vw, 3rem) 3rem; color: var(--ink-soft); font-size: 0.75rem; max-width: 70ch; }}
@media (prefers-reduced-motion: no-preference) {{
  .card {{ transition: transform 0.15s ease, border-color 0.15s ease; }}
  .card:hover {{ transform: translateY(-2px); border-color: var(--accent); }}
}}
</style>
</head>
<body>
<header>
  <h1>HKTK Slide Prompt Gallery</h1>
  <p class="subtitle">{count} slide styles rendered as real mockups — background, type, and mood as they'll actually look. {mit_count} are openly licensed (MIT) and safe to redistribute; {internal_count} are adapted from HKTK's internal 301-sample style library for personal use. Expand a card for the full prompt and copy it into Claude, Codex, or AGY.</p>
  <div class="filters" id="filters">
    <button class="chip" data-tag="all" aria-pressed="true">all</button>
    {chip_html}
    <span class="count" id="count"></span>
  </div>
  <div class="library-banner">
    <span>Looking for more effects &amp; moods (glassmorphism, brutalism, ukiyo-e, 170+ more)?</span>
    <a href="../../banana-prompts/site/index.html">Browse the full 301-sample style library &rarr;</a>
  </div>
</header>
<main>
  <div class="grid" id="grid">
    {card_html}
  </div>
</main>
<footer>
  Photo/texture areas are CSS-generated duotone gradients in each style's own accent colors — this page is a self-contained artifact and cannot fetch external images. Sources: SlideSpeak <code>presentation-design-prompts</code>, <code>awesome-notebookLM-prompts</code>, and the local <code>frontend-slides</code> skill's <code>STYLE_PRESETS.md</code> — all MIT-licensed. Full attribution in <a href="../LICENSES.md">LICENSES.md</a>. Generated by <code>scripts/build_slide_gallery.py</code> from <code>gallery/slide-prompts/prompts/*.md</code>.
</footer>
<script>
const DATA = {data_json};
const grid = document.getElementById('grid');
const countEl = document.getElementById('count');
function updateCount() {{
  const visible = [...grid.children].filter(c => c.style.display !== 'none').length;
  countEl.textContent = visible + ' / {count}';
}}
document.getElementById('filters').addEventListener('click', (e) => {{
  const btn = e.target.closest('.chip');
  if (!btn) return;
  document.querySelectorAll('.chip').forEach(c => c.setAttribute('aria-pressed', 'false'));
  btn.setAttribute('aria-pressed', 'true');
  const tag = btn.dataset.tag;
  [...grid.children].forEach(card => {{
    const tags = card.dataset.tags.split(',');
    card.style.display = (tag === 'all' || tags.includes(tag)) ? '' : 'none';
  }});
  updateCount();
}});
grid.addEventListener('click', (e) => {{
  const btn = e.target.closest('.copy');
  if (!btn) return;
  const text = DATA[btn.dataset.slug].prompt;
  navigator.clipboard.writeText(text).then(() => {{
    const old = btn.textContent;
    btn.textContent = 'copied';
    setTimeout(() => btn.textContent = old, 1200);
  }});
}});
updateCount();
</script>
</body>
</html>
"""


def render_card(card: dict) -> str:
    tags = card.get("tags", [])
    all_tags = tags + [card["license"].lower()]
    tag_html = "".join(f'<span class="tag">{t}</span>' for t in tags)
    fonts = ", ".join(card.get("fonts", []))
    palette_html = "".join(f'<span style="background:{c}"></span>' for c in card["hexes"][:6])
    slide_html = render_slide(card)
    license_class = "license-mit" if card["license"] == "MIT" else "license-internal"
    source_link = card["source_url"] if card["source_url"].startswith("http") else "../" + card["source_url"]
    return f"""
    <article class="card" data-slug="{card['slug']}" data-tags="{','.join(all_tags)}">
      {slide_html}
      <div class="card-body">
        <h2>{card['name']}</h2>
        <p class="use-case">{card['use_case']}</p>
        <div class="palette-row">{palette_html}</div>
        <div class="tags">{tag_html}</div>
        <div class="fonts">{fonts}</div>
        <details>
          <summary>full prompt</summary>
          <pre>{full_prompt_text(card)}</pre>
        </details>
        <div class="card-actions">
          <button class="copy" data-slug="{card['slug']}">copy prompt</button>
        </div>
        <p class="source"><span class="license-tag {license_class}">{card['license']}</span> &middot; <a href="{source_link}">source</a></p>
      </div>
    </article>"""


def build():
    cards = sorted(
        (parse_card(p) for p in PROMPTS_DIR.glob("*.md")),
        key=lambda c: c["name"],
    )
    all_tags = sorted({t for c in cards for t in c.get("tags", []) + [c["license"].lower()]})
    chip_html = "".join(
        f'<button class="chip" data-tag="{t}" aria-pressed="false">{t}</button>' for t in all_tags
    )
    card_html = "".join(render_card(c) for c in cards)
    data_json = json.dumps({c["slug"]: {"prompt": full_prompt_text(c)} for c in cards})
    mit_count = sum(1 for c in cards if c["license"] == "MIT")
    html = TEMPLATE.format(
        count=len(cards),
        mit_count=mit_count,
        internal_count=len(cards) - mit_count,
        chip_html=chip_html,
        card_html=card_html,
        data_json=data_json,
    )
    SITE_DIR.mkdir(parents=True, exist_ok=True)
    (SITE_DIR / "index.html").write_text(html, encoding="utf-8")
    print(f"wrote {SITE_DIR / 'index.html'} with {len(cards)} cards, {len(all_tags)} tags")


if __name__ == "__main__":
    build()
