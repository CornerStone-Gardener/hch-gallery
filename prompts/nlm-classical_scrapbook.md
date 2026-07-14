---
name: "Classical Scrapbook"
tags: [nature, wellness, soft]
use_case: "Wellness & lifestyle decks"
palette: "#8C7156 / #A68E74 / #403024 / #D9C5B2"
fonts: []
source_url: https://github.com/YamilAyma/notebooklm-prompt-styles/tree/main
license: MIT
attribution: "Harvested verbatim from YamilAyma/notebooklm-prompt-styles (Nature & Wellness)"
renderer: notebooklm
---
## [STYLE SPEC]
Classical art history meets scrapbook collage. Layered tactile materials. Typography — Heading: Elegant flowing cursive script · Body: Clean legible serif.
## [LAYOUT RULES]
Paste the full YAML design_system into NotebookLM Slides custom instructions verbatim. Keep the palette (#8C7156, #A68E74, #403024, #D9C5B2) and typography identical on every slide; add only title, audience, and emphasis.
## [FORBIDDEN]
Do not change the specified palette or typography, invent data, or exaggerate. No off-brand decoration.
## [FULL PROMPT — verbatim]
```yaml
# Source: YamilAyma/notebooklm-prompt-styles (GitHub)
design_system:
  global_style:
    theme: "Classical art history meets scrapbook collage. Layered tactile materials."
    typography: 
      primary_heading: "Elegant flowing cursive script"
      secondary_heading: "Classic high-contrast serif"
      body_text: "Clean legible serif"
    color_palette:
      primary_color: "#8C7156"
      background: "#A68E74"
      text_main: "#403024"
      accent_color: "#D9C5B2"
    key_visual_elements: 
      - "Overlapping kraft and white paper with torn edges"
      - "Classical sculpture and impressionist painting cutouts"
      - "Washi tape, paper-clips, and sparkle accents"
      - "Circular timeline nodes and framed artwork"

slide_layout_templates:
  - type: "Cover_Collage"
    usage: "Tactile intro with cursive title and classical artifacts"
  - type: "Timeline_Historical"
    usage: "Chronological events with statue cutouts"
  - type: "Ending_Statement"
    usage: "Final slide with landscape bleed and torn edges"
```
