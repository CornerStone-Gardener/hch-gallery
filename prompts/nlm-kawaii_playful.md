---
name: "Kawaii Playful"
tags: [creative, playful, bold]
use_case: "Creative campaigns & pitches"
palette: "#4B6B4C / #F7F8E0 / #F48FB1"
fonts: []
source_url: https://github.com/YamilAyma/notebooklm-prompt-styles/tree/main
license: MIT
attribution: "Harvested verbatim from YamilAyma/notebooklm-prompt-styles (Creative & Playful)"
renderer: notebooklm
---
## [STYLE SPEC]
Playful, friendly, and ultra-cute 'Kawaii' aesthetic. Typography — Heading: Super-bold rounded bubble font (e.g., DynaPuff) · Body: Friendly rounded sans-serif.
## [LAYOUT RULES]
Paste the full YAML design_system into NotebookLM Slides custom instructions verbatim. Keep the palette (#4B6B4C, #F7F8E0, #F48FB1) and typography identical on every slide; add only title, audience, and emphasis.
## [FORBIDDEN]
Do not change the specified palette or typography, invent data, or exaggerate. No off-brand decoration.
## [FULL PROMPT — verbatim]
```yaml
# Source: YamilAyma/notebooklm-prompt-styles (GitHub)
design_system:
  global_style:
    theme: "Playful, friendly, and ultra-cute 'Kawaii' aesthetic."
    typography: 
      primary_heading: "Super-bold rounded bubble font (e.g., DynaPuff)"
      secondary_heading: "Clean, rounded sans-serif"
      body_text: "Friendly rounded sans-serif"
    color_palette:
      primary_color: "#4B6B4C"
      background: "#F7F8E0"
      accent_rose: "#F48FB1"
    key_visual_elements: 
      - "Chibi/Kawaii cat character illustrations"
      - "Subtle green notebook-style grid patterns"
      - "Pill-shaped containers for labels"
      - "Hand-drawn doodles (stars, sparkles)"

slide_layout_templates:
  - type: "Creative_Brainstorm"
    usage: "Opening slide for workshops"
  - type: "Strategic_Play"
    usage: "Outlining goals or objectives"
```
