---
name: "Creative Workshop"
tags: [creative, playful, bold]
use_case: "Creative campaigns & pitches"
palette: "#F48FB1 / #FFFFFF / #E1F5FE"
fonts: []
source_url: https://github.com/YamilAyma/notebooklm-prompt-styles/tree/main
license: MIT
attribution: "Harvested verbatim from YamilAyma/notebooklm-prompt-styles (Creative & Playful)"
renderer: notebooklm
---
## [STYLE SPEC]
Art Studio. Creative & Playful. Typography — Heading: Bold blocky sans-serif (Multi-color) · Body: Clean legible sans-serif.
## [LAYOUT RULES]
Paste the full YAML design_system into NotebookLM Slides custom instructions verbatim. Keep the palette (#F48FB1, #FFFFFF, #E1F5FE) and typography identical on every slide; add only title, audience, and emphasis.
## [FORBIDDEN]
Do not change the specified palette or typography, invent data, or exaggerate. No off-brand decoration.
## [FULL PROMPT — verbatim]
```yaml
# Source: YamilAyma/notebooklm-prompt-styles (GitHub)
design_system:
  global_style:
    theme: "Art Studio. Creative & Playful."
    typography: 
      primary_heading: "Bold blocky sans-serif (Multi-color)"
      secondary_heading: "Rounded friendly sans-serif"
      body_text: "Clean legible sans-serif"
    color_palette:
      primary_color: "#F48FB1"
      background: "#FFFFFF"
      grid_lines: "#E1F5FE"
    key_visual_elements: 
      - "Ruled background textures"
      - "Organic wavy pink blobs"
      - "Smiling art supply illustrations"
      - "Pill-shaped category tags"

slide_layout_templates:
  - type: "Workshop_Hero"
    usage: "Project titles or starters"
  - type: "Activity_Grid"
    usage: "Listing activities or topics"
  - type: "Showcase_Gallery"
    usage: "Highlighting events or work"
```
