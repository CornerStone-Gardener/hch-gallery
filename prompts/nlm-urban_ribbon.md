---
name: "Urban Ribbon"
tags: [tech-product, futuristic, technical]
use_case: "Product & tech decks"
palette: "#333333 / #D9C5B2 / #5C4B41 / #1A1A1A"
fonts: []
source_url: https://github.com/YamilAyma/notebooklm-prompt-styles/tree/main
license: MIT
attribution: "Harvested verbatim from YamilAyma/notebooklm-prompt-styles (Tech & Innovation)"
renderer: notebooklm
---
## [STYLE SPEC]
Authoritative urban aesthetic. 3D-folded ribbons and diagonal slices. Typography — Heading: Bold authoritative sans-serif (League Spartan) · Body: Clean functional sans-serif.
## [LAYOUT RULES]
Paste the full YAML design_system into NotebookLM Slides custom instructions verbatim. Keep the palette (#333333, #D9C5B2, #5C4B41, #1A1A1A) and typography identical on every slide; add only title, audience, and emphasis.
## [FORBIDDEN]
Do not change the specified palette or typography, invent data, or exaggerate. No off-brand decoration.
## [FULL PROMPT — verbatim]
```yaml
# Source: YamilAyma/notebooklm-prompt-styles (GitHub)
design_system:
  global_style:
    theme: "Authoritative urban aesthetic. 3D-folded ribbons and diagonal slices."
    typography: 
      primary_heading: "Bold authoritative sans-serif (League Spartan)"
      secondary_heading: "Professional sans-serif"
      body_text: "Clean functional sans-serif"
    color_palette:
      primary_color: "#333333"
      secondary_color: "#D9C5B2"
      background_dark: "#5C4B41"
      text_main: "#1A1A1A"
    key_visual_elements: 
      - "3D-folded 'ribbon' overlays for titles and labels"
      - "Sharp diagonal background slices and parallelogram containers"
      - "Golden-hour urban landscapes and skyscraper photography"
      - "High-contrast charcoal and warm beige palette"

slide_layout_templates:
  - type: "Executive_Pitch"
    usage: "Professional business cover with urban backdrop and ribbon accents"
  - type: "Leadership_Grid"
    usage: "Team profiles with parallelogram-shaped portrait cards"
  - type: "Strategic_Comparison"
    usage: "Comparative data with diagonal dividers and vertical image bleeds"
```
