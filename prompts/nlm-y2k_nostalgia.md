---
name: "Y2K Nostalgia"
tags: [creative, playful, bold]
use_case: "Creative campaigns & pitches"
palette: "#FF85A1 / #FDEFF4 / #B19CD9"
fonts: []
source_url: https://github.com/YamilAyma/notebooklm-prompt-styles/tree/main
license: MIT
attribution: "Harvested verbatim from YamilAyma/notebooklm-prompt-styles (Creative & Playful)"
renderer: notebooklm
---
## [STYLE SPEC]
Retro Digital. Bubblegum & Holographic. Typography — Heading: Bold quirky block letters · Body: Clean legible monospace (e.g., Courier New).
## [LAYOUT RULES]
Paste the full YAML design_system into NotebookLM Slides custom instructions verbatim. Keep the palette (#FF85A1, #FDEFF4, #B19CD9) and typography identical on every slide; add only title, audience, and emphasis.
## [FORBIDDEN]
Do not change the specified palette or typography, invent data, or exaggerate. No off-brand decoration.
## [FULL PROMPT — verbatim]
```yaml
# Source: YamilAyma/notebooklm-prompt-styles (GitHub)
design_system:
  global_style:
    theme: "Retro Digital. Bubblegum & Holographic."
    typography: 
      primary_heading: "Bold quirky block letters"
      secondary_heading: "Pixellated or typewriter monospace"
      body_text: "Clean legible monospace (e.g., Courier New)"
    color_palette:
      primary_color: "#FF85A1"
      background: "#FDEFF4"
      accent_purple: "#B19CD9"
    key_visual_elements: 
      - "CD-ROM rainbow reflections"
      - "Holographic/Iridescent textures"
      - "3D plastic gummy bears and icons"
      - "Polaroid photo frames"

slide_layout_templates:
  - type: "Pop_Culture_Hero"
    usage: "Dynamic titles or mood setters"
  - type: "Digital_Dairy"
    usage: "Storytelling or personal anecdotes"
  - type: "Memory_Gallery"
    usage: "Photos or event highlights"
```
