---
name: "The Seasons"
tags: [nature, wellness, soft]
use_case: "Wellness & lifestyle decks"
palette: "#3D3D29 / #8F564B / #F9F6F1 / #2D2D2D"
fonts: []
source_url: https://github.com/YamilAyma/notebooklm-prompt-styles/tree/main
license: MIT
attribution: "Harvested verbatim from YamilAyma/notebooklm-prompt-styles (Nature & Wellness)"
renderer: notebooklm
---
## [STYLE SPEC]
Organic, earthy wellness and high-end botanical branding. Typography — Heading: Classic, high-contrast serif (Playfair Display) · Body: Clean minimalist sans-serif.
## [LAYOUT RULES]
Paste the full YAML design_system into NotebookLM Slides custom instructions verbatim. Keep the palette (#3D3D29, #8F564B, #F9F6F1, #2D2D2D) and typography identical on every slide; add only title, audience, and emphasis.
## [FORBIDDEN]
Do not change the specified palette or typography, invent data, or exaggerate. No off-brand decoration.
## [FULL PROMPT — verbatim]
```yaml
# Source: YamilAyma/notebooklm-prompt-styles (GitHub)
design_system:
  global_style:
    theme: "Organic, earthy wellness and high-end botanical branding."
    typography: 
      primary_heading: "Classic, high-contrast serif (Playfair Display)"
      secondary_heading: "Refined italic serif or modern sans-serif"
      body_text: "Clean minimalist sans-serif"
    color_palette:
      primary_color: "#3D3D29"
      secondary_color: "#8F564B"
      background: "#F9F6F1"
      text_main: "#2D2D2D"
    key_visual_elements: 
      - "Macro botanical photography (eucalyptus, tropical leaves)"
      - "Stadium-shaped masks for images and content blocks"
      - "Shadow overlays of plant leaves for atmosphere"
      - "Earthy-toned data visualizations (Venn, bar charts)"

slide_layout_templates:
  - type: "Organic_Hero"
    usage: "Large Serif Title over botanical background bleed"
  - type: "Product_Inventory"
    usage: "Catalog list of stadium-shaped cards with portrait bleed"
  - type: "Data_Venn"
    usage: "Mapping brand values with terracotta and olive tones"
```
