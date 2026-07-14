---
name: "Ensign Corporate"
tags: [consulting-exec, corporate, data-dense]
use_case: "Executive & board decks"
palette: "#101D42 / #4A6CF7 / #FFB400 / #F5F7FA"
fonts: []
source_url: https://github.com/YamilAyma/notebooklm-prompt-styles/tree/main
license: MIT
attribution: "Harvested verbatim from YamilAyma/notebooklm-prompt-styles (Business & Executive)"
renderer: notebooklm
---
## [STYLE SPEC]
Modern corporate, dynamic, professional. Navy/Blue with Yellow accents. Typography — Heading: Bold geometric sans-serif, uppercase · Body: Clean sans-serif, business readability.
## [LAYOUT RULES]
Paste the full YAML design_system into NotebookLM Slides custom instructions verbatim. Keep the palette (#101D42, #4A6CF7, #FFB400, #F5F7FA) and typography identical on every slide; add only title, audience, and emphasis.
## [FORBIDDEN]
Do not change the specified palette or typography, invent data, or exaggerate. No off-brand decoration.
## [FULL PROMPT — verbatim]
```yaml
# Source: YamilAyma/notebooklm-prompt-styles (GitHub)
design_system:
  global_style:
    theme: "Modern corporate, dynamic, professional. Navy/Blue with Yellow accents."
    typography: 
      primary_heading: "Bold geometric sans-serif, uppercase"
      secondary_heading: "Medium-bold sans-serif, accent color"
      body_text: "Clean sans-serif, business readability"
      info_label: "Small bold uppercase pill labels"
    color_palette:
      primary_color: "#101D42"
      secondary_color: "#4A6CF7"
      accent_yellow: "#FFB400"
      background: "#F5F7FA"
    key_visual_elements: 
      - "Layered corner 'ribbons' (Navy and Blue stacking)"
      - "Pill-shaped accent backgrounds for labels"
      - "Bold circular iconography"
      - "Rounded cards for content blocks"

slide_layout_templates:
  - type: "Ensign_Cover"
    usage: "Professional business introduction"
  - type: "Ribbon_Team"
    usage: "Team introduction with individual roles"
  - type: "Icon_Service_Grid"
    usage: "Listing core services or features"
```
