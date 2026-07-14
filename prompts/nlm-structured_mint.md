---
name: "Structured Mint"
tags: [minimal, modern, clean]
use_case: "Clean minimal decks"
palette: "#557A68 / #FFFFFF / #B2EBF2 / #263238"
fonts: []
source_url: https://github.com/YamilAyma/notebooklm-prompt-styles/tree/main
license: MIT
attribution: "Harvested verbatim from YamilAyma/notebooklm-prompt-styles (Minimalist & Modern)"
renderer: notebooklm
---
## [STYLE SPEC]
Corporate, structured, and refreshing. Tiered corner frames and mint accents. Typography — Heading: Bold geometric sans-serif (e.g., Montserrat), uppercase · Body: Functional sans-serif, optimized for readability.
## [LAYOUT RULES]
Paste the full YAML design_system into NotebookLM Slides custom instructions verbatim. Keep the palette (#557A68, #FFFFFF, #B2EBF2, #263238) and typography identical on every slide; add only title, audience, and emphasis.
## [FORBIDDEN]
Do not change the specified palette or typography, invent data, or exaggerate. No off-brand decoration.
## [FULL PROMPT — verbatim]
```yaml
# Source: YamilAyma/notebooklm-prompt-styles (GitHub)
design_system:
  global_style:
    theme: "Corporate, structured, and refreshing. Tiered corner frames and mint accents."
    typography: 
      primary_heading: "Bold geometric sans-serif (e.g., Montserrat), uppercase"
      secondary_heading: "Medium sans-serif, clean"
      body_text: "Functional sans-serif, optimized for readability"
    color_palette:
      primary_color: "#557A68"
      background: "#FFFFFF"
      accent_mint: "#B2EBF2"
      text_main: "#263238"
    key_visual_elements: 
      - "Tiered corner frames (Mint and Teal accents)"
      - "Pill-shaped category tags"
      - "Numbered grid boxes"
      - "Vertical mint-green accent bars"

slide_layout_templates:
  - type: "Structured_Cover"
    usage: "Impactful intro with tiered frames"
  - type: "Grid_Methodology"
    usage: "Listing steps or structured points"
  - type: "Content_Focus_Split"
    usage: "Image and text side-by-side"
```
