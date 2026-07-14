---
name: "Architectural Cobalt"
tags: [tech-product, futuristic, technical]
use_case: "Product & tech decks"
palette: "#304FFE / #111111 / #FFFFFF"
fonts: []
source_url: https://github.com/YamilAyma/notebooklm-prompt-styles/tree/main
license: MIT
attribution: "Harvested verbatim from YamilAyma/notebooklm-prompt-styles (Tech & Innovation)"
renderer: notebooklm
---
## [STYLE SPEC]
Technical, dark architectural, blueprint-inspired. Deep charcoal with cobalt blue. Typography — Heading: Bold high-contrast sans-serif · Body: Functional sans-serif, optimized for dark mode.
## [LAYOUT RULES]
Paste the full YAML design_system into NotebookLM Slides custom instructions verbatim. Keep the palette (#304FFE, #111111, #FFFFFF) and typography identical on every slide; add only title, audience, and emphasis.
## [FORBIDDEN]
Do not change the specified palette or typography, invent data, or exaggerate. No off-brand decoration.
## [FULL PROMPT — verbatim]
```yaml
# Source: YamilAyma/notebooklm-prompt-styles (GitHub)
design_system:
  global_style:
    theme: "Technical, dark architectural, blueprint-inspired. Deep charcoal with cobalt blue."
    typography: 
      primary_heading: "Bold high-contrast sans-serif"
      secondary_heading: "Medium sans-serif, clean"
      body_text: "Functional sans-serif, optimized for dark mode"
      technical_label: "Small uppercase sans-serif, spaced"
    color_palette:
      primary_color: "#304FFE"
      background: "#111111"
      text_main: "#FFFFFF"
      accent_overlay: "rgba(48, 79, 254, 0.2)"
    key_visual_elements: 
      - "Circular crosshair/sight icons"
      - "Vibrant cobalt blue gradient overlays"
      - "Dark, high-shadow architectural photography"
      - "Thin white structural grid lines"

slide_layout_templates:
  - type: "Cobalt_Impact_Cover"
    usage: "Impactful intro with technical structural visuals"
  - type: "Dark_Project_Detail"
    usage: "Showcasing projects with technical metadata"
  - type: "Expertise_Profile"
    usage: "Team introduction or profile highlights"
```
