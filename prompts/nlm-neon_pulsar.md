---
name: "Neon Pulsar"
tags: [tech-product, futuristic, technical]
use_case: "Product & tech decks"
palette: "#FFFFFF / #000000 / #00F2FF / #7000FF"
fonts: []
source_url: https://github.com/YamilAyma/notebooklm-prompt-styles/tree/main
license: MIT
attribution: "Harvested verbatim from YamilAyma/notebooklm-prompt-styles (Tech & Innovation)"
renderer: notebooklm
---
## [STYLE SPEC]
Futuristic, high-energy, tech-focused. Dark mode neon. Typography — Heading: Extra-bold modern sans-serif (e.g., Inter) · Body: Clean sans-serif for dark mode.
## [LAYOUT RULES]
Paste the full YAML design_system into NotebookLM Slides custom instructions verbatim. Keep the palette (#FFFFFF, #000000, #00F2FF, #7000FF) and typography identical on every slide; add only title, audience, and emphasis.
## [FORBIDDEN]
Do not change the specified palette or typography, invent data, or exaggerate. No off-brand decoration.
## [FULL PROMPT — verbatim]
```yaml
# Source: YamilAyma/notebooklm-prompt-styles (GitHub)
design_system:
  global_style:
    theme: "Futuristic, high-energy, tech-focused. Dark mode neon."
    typography: 
      primary_heading: "Extra-bold modern sans-serif (e.g., Inter)"
      secondary_heading: "Medium sans-serif, high contrast"
      body_text: "Clean sans-serif for dark mode"
    color_palette:
      primary_color: "#FFFFFF"
      background: "#000000"
      accent_cyan: "#00F2FF"
      accent_purple: "#7000FF"
      accent_magenta: "#FF00E5"
    key_visual_elements: 
      - "Blurred neon gradient spheres"
      - "Concentric rings and digital orbits"
      - "Pill-shaped containers"
      - "Glassmorphic cards with neon borders"

slide_layout_templates:
  - type: "Tech_Startup_Hero"
    usage: "Main title or key announcement"
  - type: "Service_Orbits"
    usage: "Showing features around a core concept"
  - type: "Neon_Bento_Grid"
    usage: "Showcasing tech specs or team members"
```
