---
name: "Midnight Tactical"
tags: [tech-product, futuristic, technical]
use_case: "Product & tech decks"
palette: "#C6FF00 / #000000 / #FFFFFF"
fonts: []
source_url: https://github.com/YamilAyma/notebooklm-prompt-styles/tree/main
license: MIT
attribution: "Harvested verbatim from YamilAyma/notebooklm-prompt-styles (Tech & Innovation)"
renderer: notebooklm
---
## [STYLE SPEC]
Modern tech-utilitarian. Matte Black & Lime Green. Typography — Heading: Bold geometric sans-serif (e.g., Space Grotesk) · Body: Clean sans-serif for dark backgrounds.
## [LAYOUT RULES]
Paste the full YAML design_system into NotebookLM Slides custom instructions verbatim. Keep the palette (#C6FF00, #000000, #FFFFFF) and typography identical on every slide; add only title, audience, and emphasis.
## [FORBIDDEN]
Do not change the specified palette or typography, invent data, or exaggerate. No off-brand decoration.
## [FULL PROMPT — verbatim]
```yaml
# Source: YamilAyma/notebooklm-prompt-styles (GitHub)
design_system:
  global_style:
    theme: "Modern tech-utilitarian. Matte Black & Lime Green."
    typography: 
      primary_heading: "Bold geometric sans-serif (e.g., Space Grotesk)"
      secondary_heading: "Medium sans-serif, high contrast white"
      body_text: "Clean sans-serif for dark backgrounds"
      accent_mono: "Monospace for technical labels"
    color_palette:
      primary_color: "#C6FF00"
      background: "#000000"
      text_main: "#FFFFFF"
    key_visual_elements: 
      - "Tilted lime green highlight boxes (fractional labels)"
      - "Pill-shaped labels in dark green"
      - "Double chevron accents (<<)"
      - "Rounded-corner modular grid containers"

slide_layout_templates:
  - type: "Tactical_Hero"
    usage: "Section headers or main announcements"
  - type: "Utility_Agenda"
    usage: "Agenda or multi-point summaries"
  - type: "Textured_Gallery"
    usage: "Showcasing visual references or products"
```
