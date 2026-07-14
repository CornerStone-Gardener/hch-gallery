---
name: "Hand-Drawn Scrapbook"
tags: [creative, playful, bold]
use_case: "Creative campaigns & pitches"
palette: "#A2B276 / #FDFCF0 / #F9A8A8 / #F9D97D"
fonts: []
source_url: https://github.com/YamilAyma/notebooklm-prompt-styles/tree/main
license: MIT
attribution: "Harvested verbatim from YamilAyma/notebooklm-prompt-styles (Creative & Playful)"
renderer: notebooklm
---
## [STYLE SPEC]
Whimsical, Kawaii-inspired aesthetic. Soft pastel palettes, hand-drawn stickers, and a playful gingham grid. Typography — Heading: Baloo Thambi 2, display · Body: Inter, sans-serif.
## [LAYOUT RULES]
Paste the full YAML design_system into NotebookLM Slides custom instructions verbatim. Keep the palette (#A2B276, #FDFCF0, #F9A8A8, #F9D97D) and typography identical on every slide; add only title, audience, and emphasis.
## [FORBIDDEN]
Do not change the specified palette or typography, invent data, or exaggerate. No off-brand decoration.
## [FULL PROMPT — verbatim]
```yaml
# Source: YamilAyma/notebooklm-prompt-styles (GitHub)
description: "A whimsical, Kawaii-inspired aesthetic characterized by soft pastel palettes, hand-drawn stickers, and a playful gingham grid. Perfect for educational projects, creative journals, or friendly presentations."
design_system:
  global_style:
    theme: "Whimsical, Kawaii-inspired aesthetic. Soft pastel palettes, hand-drawn stickers, and a playful gingham grid."
    typography: 
      primary_heading: "Baloo Thambi 2, display"
      secondary_heading: "Rounded friendly sans-serif"
      body_text: "Inter, sans-serif"
    color_palette:
      primary_color: "#A2B276"
      background: "#FDFCF0"
      accent_pink: "#F9A8A8"
      accent_yellow: "#F9D97D"
      text_main: "#4A4A4A"
    key_visual_elements: 
      - "Subtle gingham grid in pastel hues"
      - "Doodle flowers, Soft hearts, Friendly worm"
      - "Washi tape ribbon banners"
      - "Hand-drawn, slightly irregular strokes"

  image_generation_prompts:
    style_guidelines: "Whimsical hand-drawn illustrations, flat vector art, sticker aesthetic, Kawaii style, pastel colors, 2D illustration."
    themes:
      - target: "Creative Student"
        prompt_elements: "A person writing in a colorful journal with stickers and doodles, flat vector art."

slide_layout_templates:
  - type: "Sticker_Hero"
    usage: "Title slide with floating decorative elements and center title"
  - type: "Washi_Team"
    usage: "Team members showcased with ribbon-style name tags"
  - type: "Doodle_Grid"
    usage: "Content organized in rounded 'bento' boxes with hand-drawn borders"
```
