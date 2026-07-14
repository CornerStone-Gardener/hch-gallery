---
name: "Vibrant Corporate"
tags: [consulting-exec, corporate, data-dense]
use_case: "Executive & board decks"
palette: "#051C2C / #4CAF50 / #FFFFFF / #111111"
fonts: []
source_url: https://github.com/YamilAyma/notebooklm-prompt-styles/tree/main
license: MIT
attribution: "Harvested verbatim from YamilAyma/notebooklm-prompt-styles (Business & Executive)"
renderer: notebooklm
---
## [STYLE SPEC]
Modern, dynamic, and professional corporate aesthetic. Typography — Heading: Bold geometric sans-serif (Montserrat) · Body: Clean functional sans-serif.
## [LAYOUT RULES]
Paste the full YAML design_system into NotebookLM Slides custom instructions verbatim. Keep the palette (#051C2C, #4CAF50, #FFFFFF, #111111) and typography identical on every slide; add only title, audience, and emphasis.
## [FORBIDDEN]
Do not change the specified palette or typography, invent data, or exaggerate. No off-brand decoration.
## [FULL PROMPT — verbatim]
```yaml
# Source: YamilAyma/notebooklm-prompt-styles (GitHub)
design_system:
  global_style:
    theme: "Modern, dynamic, and professional corporate aesthetic."
    typography: 
      primary_heading: "Bold geometric sans-serif (Montserrat)"
      secondary_heading: "Medium weight sans-serif"
      body_text: "Clean functional sans-serif"
    color_palette:
      primary_color: "#051C2C"
      secondary_color: "#4CAF50"
      background: "#FFFFFF"
      text_main: "#111111"
    key_visual_elements: 
      - "Dynamic diagonal color blocks and chevron overlays"
      - "Circular icons with navy backgrounds"
      - "Chevron-shaped pointers for list items"
      - "Modern architectural and cityscape photography"

slide_layout_templates:
  - type: "Corporate_Cover"
    usage: "Bold navy and green diagonals for business plans"
  - type: "Timeline_History"
    usage: "Horizontal timeline with circular navy nodes"
  - type: "Objective_Chevron"
    usage: "List with green chevron markers and architectural bleed"
```
