---
name: "Luxury Editorial"
tags: [editorial, magazine, elegant]
use_case: "Editorial features & reports"
palette: "#2D2926 / #D4AF37 / #3C2F2F / #FFFFFF"
fonts: []
source_url: https://github.com/YamilAyma/notebooklm-prompt-styles/tree/main
license: MIT
attribution: "Harvested verbatim from YamilAyma/notebooklm-prompt-styles (Editorial & Magazine)"
renderer: notebooklm
---
## [STYLE SPEC]
High-end fashion magazine aesthetic. Deep espresso and gold. Typography — Heading: Elegant condensed serif (Didot-style) · Body: Minimalist sans-serif with wide tracking.
## [LAYOUT RULES]
Paste the full YAML design_system into NotebookLM Slides custom instructions verbatim. Keep the palette (#2D2926, #D4AF37, #3C2F2F, #FFFFFF) and typography identical on every slide; add only title, audience, and emphasis.
## [FORBIDDEN]
Do not change the specified palette or typography, invent data, or exaggerate. No off-brand decoration.
## [FULL PROMPT — verbatim]
```yaml
# Source: YamilAyma/notebooklm-prompt-styles (GitHub)
design_system:
  global_style:
    theme: "High-end fashion magazine aesthetic. Deep espresso and gold."
    typography: 
      primary_heading: "Elegant condensed serif (Didot-style)"
      accent_script: "Refined flowing cursive"
      body_text: "Minimalist sans-serif with wide tracking"
    color_palette:
      primary_color: "#2D2926"
      secondary_color: "#D4AF37"
      background: "#3C2F2F"
      text_main: "#FFFFFF"
    key_visual_elements: 
      - "Subtle gold sparkle/star vector accents"
      - "Macro photography of luxury textures (silk, jewelry)"
      - "Asymmetric split-screen layouts"
      - "Overlaying script text on top of serif titles"

slide_layout_templates:
  - type: "Editorial_Cover"
    usage: "Fashion collection intro with full-bleed luxury imagery"
  - type: "Brand_Narrative"
    usage: "Split-screen layout for brand stories or mission"
  - type: "Visual_Lookbook"
    usage: "Grid-based display for styling ideas or products"
```
