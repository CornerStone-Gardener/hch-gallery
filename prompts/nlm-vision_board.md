---
name: "Vision Board"
tags: [editorial, magazine, elegant]
use_case: "Editorial features & reports"
palette: "#F9F7F2 / #2D2D2D / #E0E0E0"
fonts: []
source_url: https://github.com/YamilAyma/notebooklm-prompt-styles/tree/main
license: MIT
attribution: "Harvested verbatim from YamilAyma/notebooklm-prompt-styles (Editorial & Magazine)"
renderer: notebooklm
---
## [STYLE SPEC]
Tactile, handmade scrapbooking aesthetic. Torn edges, tape accents, and paper textures. Typography — Heading: Extra-bold thick sans-serif (all caps) · Body: Clean professional sans-serif.
## [LAYOUT RULES]
Paste the full YAML design_system into NotebookLM Slides custom instructions verbatim. Keep the palette (#F9F7F2, #2D2D2D, #E0E0E0) and typography identical on every slide; add only title, audience, and emphasis.
## [FORBIDDEN]
Do not change the specified palette or typography, invent data, or exaggerate. No off-brand decoration.
## [FULL PROMPT — verbatim]
```yaml
# Source: YamilAyma/notebooklm-prompt-styles (GitHub)
design_system:
  global_style:
    theme: "Tactile, handmade scrapbooking aesthetic. Torn edges, tape accents, and paper textures."
    typography: 
      primary_heading: "Extra-bold thick sans-serif (all caps)"
      secondary_heading: "Marker-style / handwritten font"
      body_text: "Clean professional sans-serif"
    color_palette:
      primary_color: "#F9F7F2"
      background: "Crumpled paper texture"
      text_main: "#2D2D2D"
      accent_color: "#E0E0E0"
    key_visual_elements: 
      - "Realistic torn paper edge overlays"
      - "Washi tape and masking tape strips"
      - "Hand-drawn marker ovals and arrows"
      - "Multi-layered paper scrap aesthetic"

slide_layout_templates:
  - type: "Manifesto_Cover"
    usage: "Bold inspirational intro with layered photos"
  - type: "Concept_Tornado"
    usage: "Mapping areas with marker arrows and taped notes"
  - type: "Note_to_Self"
    usage: "Key takeaways or quotes on centered paper scraps"
```
