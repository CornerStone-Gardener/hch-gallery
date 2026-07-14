---
name: "Cobalt Editorial"
tags: [editorial, magazine, elegant]
use_case: "Editorial features & reports"
palette: "#2B59FF / #FDF5E6 / #000000"
fonts: []
source_url: https://github.com/YamilAyma/notebooklm-prompt-styles/tree/main
license: MIT
attribution: "Harvested verbatim from YamilAyma/notebooklm-prompt-styles (Editorial & Magazine)"
renderer: notebooklm
---
## [STYLE SPEC]
Bold editorial, Swiss-inspired. Electric Blue & Cream. Typography — Heading: Extra-bold brutalist sans-serif (e.g., Inter) · Body: Clean sans-serif, high legibility.
## [LAYOUT RULES]
Paste the full YAML design_system into NotebookLM Slides custom instructions verbatim. Keep the palette (#2B59FF, #FDF5E6, #000000) and typography identical on every slide; add only title, audience, and emphasis.
## [FORBIDDEN]
Do not change the specified palette or typography, invent data, or exaggerate. No off-brand decoration.
## [FULL PROMPT — verbatim]
```yaml
# Source: YamilAyma/notebooklm-prompt-styles (GitHub)
design_system:
  global_style:
    theme: "Bold editorial, Swiss-inspired. Electric Blue & Cream."
    typography: 
      primary_heading: "Extra-bold brutalist sans-serif (e.g., Inter)"
      secondary_heading: "Bold sans-serif, vertical layouts"
      body_text: "Clean sans-serif, high legibility"
    color_palette:
      primary_color: "#2B59FF"
      background: "#FDF5E6"
      text_main: "#000000"
    key_visual_elements: 
      - "Electric Blue asterisks (*) and plus signs (+)"
      - "Liquid, rippled, or smoky textures"
      - "Split-screen layouts"
      - "Pill-shaped buttons with blue outlines"

slide_layout_templates:
  - type: "Editorial_Split"
    usage: "Core sections or chapter starts"
  - type: "Vertical_Type_List"
    usage: "Detailed overviews or content lists"
  - type: "Modular_Brand_Focus"
    usage: "Presenting mission statements or pillars"
```
