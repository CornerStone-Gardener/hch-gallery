---
name: "Classical Gallery"
tags: [editorial, magazine, elegant]
use_case: "Editorial features & reports"
palette: "#8B9B7B / #E6E1D3 / #4B5320 / #F4C2C2"
fonts: []
source_url: https://github.com/YamilAyma/notebooklm-prompt-styles/tree/main
license: MIT
attribution: "Harvested verbatim from YamilAyma/notebooklm-prompt-styles (Editorial & Magazine)"
renderer: notebooklm
---
## [STYLE SPEC]
Classical museum-like, historical and refined. Parchment textures and elegant scrollwork. Typography — Heading: Bold clean sans-serif for modern contrast · Body: Highly legible sans-serif.
## [LAYOUT RULES]
Paste the full YAML design_system into NotebookLM Slides custom instructions verbatim. Keep the palette (#8B9B7B, #E6E1D3, #4B5320, #F4C2C2) and typography identical on every slide; add only title, audience, and emphasis.
## [FORBIDDEN]
Do not change the specified palette or typography, invent data, or exaggerate. No off-brand decoration.
## [FULL PROMPT — verbatim]
```yaml
# Source: YamilAyma/notebooklm-prompt-styles (GitHub)
design_system:
  global_style:
    theme: "Classical museum-like, historical and refined. Parchment textures and elegant scrollwork."
    typography: 
      primary_heading: "Bold clean sans-serif for modern contrast"
      secondary_heading: "Medium weight sans-serif"
      body_text: "Highly legible sans-serif"
    color_palette:
      primary_color: "#8B9B7B"
      background: "Textured parchment (#E6E1D3)"
      text_main: "#4B5320"
      accent_color: "#F4C2C2"
    key_visual_elements: 
      - "Elegant ornamental filigree and scrollwork"
      - "Sage green color blocks for sidebars"
      - "Marble sculptures and Renaissance-style sketches"
      - "High-texture parchment background"

slide_layout_templates:
  - type: "Museum_Cover"
    usage: "Classical intro with symmetric filigree framing"
  - type: "Classical_Split"
    usage: "Art-focused layouts with large color blocks"
  - type: "Percentage_Highlight"
    usage: "Key metrics or summaries with historical framing"
```
