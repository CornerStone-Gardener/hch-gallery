---
name: "Architectural Portfolio"
tags: [editorial, magazine, elegant]
use_case: "Editorial features & reports"
palette: "#8B9B7B / #F4F4F4 / #333333 / #A0522D"
fonts: []
source_url: https://github.com/YamilAyma/notebooklm-prompt-styles/tree/main
license: MIT
attribution: "Harvested verbatim from YamilAyma/notebooklm-prompt-styles (Editorial & Magazine)"
renderer: notebooklm
---
## [STYLE SPEC]
Modern architectural and geometric. Modular bento-grid layouts. Typography — Heading: Bold geometric sans-serif (Montserrat/Inter) · Body: Light-weight minimalist sans-serif.
## [LAYOUT RULES]
Paste the full YAML design_system into NotebookLM Slides custom instructions verbatim. Keep the palette (#8B9B7B, #F4F4F4, #333333, #A0522D) and typography identical on every slide; add only title, audience, and emphasis.
## [FORBIDDEN]
Do not change the specified palette or typography, invent data, or exaggerate. No off-brand decoration.
## [FULL PROMPT — verbatim]
```yaml
# Source: YamilAyma/notebooklm-prompt-styles (GitHub)
design_system:
  global_style:
    theme: "Modern architectural and geometric. Modular bento-grid layouts."
    typography: 
      primary_heading: "Bold geometric sans-serif (Montserrat/Inter)"
      secondary_heading: "Medium sans-serif, clean"
      body_text: "Light-weight minimalist sans-serif"
    color_palette:
      primary_color: "#8B9B7B"
      background: "Off-White (#F4F4F4)"
      text_main: "#333333"
      accent_color: "#A0522D"
    key_visual_elements: 
      - "Complex pill-shaped and circular photo masks"
      - "Modular Bento-grid content organization"
      - "Minimalist sage green star icons in corners"
      - "Thin horizontal separators and asymmetric clusters"

slide_layout_templates:
  - type: "Portfolio_Cover"
    usage: "Bold intro with complex geometric photo masking"
  - type: "Bento_Index"
    usage: "Modular TOC or overview with circular masks"
  - type: "Contact_Modular"
    usage: "Final contact info with terracotta accents"
```
