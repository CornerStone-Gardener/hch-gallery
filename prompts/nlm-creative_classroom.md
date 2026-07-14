---
name: "Creative Classroom"
tags: [creative, playful, bold]
use_case: "Creative campaigns & pitches"
palette: "#557A68 / #FFF9E6 / #C4A484"
fonts: []
source_url: https://github.com/YamilAyma/notebooklm-prompt-styles/tree/main
license: MIT
attribution: "Harvested verbatim from YamilAyma/notebooklm-prompt-styles (Creative & Playful)"
renderer: notebooklm
---
## [STYLE SPEC]
Playful educational. Classroom & Doodles. Typography — Heading: Hand-drawn bold sans-serif (e.g., Fredoka One) · Body: Clean legible sans-serif.
## [LAYOUT RULES]
Paste the full YAML design_system into NotebookLM Slides custom instructions verbatim. Keep the palette (#557A68, #FFF9E6, #C4A484) and typography identical on every slide; add only title, audience, and emphasis.
## [FORBIDDEN]
Do not change the specified palette or typography, invent data, or exaggerate. No off-brand decoration.
## [FULL PROMPT — verbatim]
```yaml
# Source: YamilAyma/notebooklm-prompt-styles (GitHub)
design_system:
  global_style:
    theme: "Playful educational. Classroom & Doodles."
    typography: 
      primary_heading: "Hand-drawn bold sans-serif (e.g., Fredoka One)"
      secondary_heading: "Rounded friendly sans-serif"
      body_text: "Clean legible sans-serif"
    color_palette:
      primary_color: "#557A68"
      background: "#FFF9E6"
      accent_wood: "#C4A484"
    key_visual_elements: 
      - "Chalkboard-themed content frames"
      - "Flat, 2D vector illustrations (globes, books)"
      - "ABC alphabet blocks"
      - "Irregular hand-drawn edges"

slide_layout_templates:
  - type: "Classroom_Hero"
    usage: "Main title or module introductions"
  - type: "Informational_Board"
    usage: "Core lesson content or discussion"
  - type: "Object_Focus_Detail"
    usage: "Summaries or conceptual focuses"
```
