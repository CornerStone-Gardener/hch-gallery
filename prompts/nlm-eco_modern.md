---
name: "Eco Modern"
tags: [nature, wellness, soft]
use_case: "Wellness & lifestyle decks"
palette: "#D4FF00 / #5D8AA8 / #000000 / #FFFFFF"
fonts: []
source_url: https://github.com/YamilAyma/notebooklm-prompt-styles/tree/main
license: MIT
attribution: "Harvested verbatim from YamilAyma/notebooklm-prompt-styles (Nature & Wellness)"
renderer: notebooklm
---
## [STYLE SPEC]
Sustainable, modern nature aesthetic. Dark mode with glassmorphism. Typography — Heading: Extra-bold geometric sans-serif (Codec Pro) · Body: Highly legible functional sans-serif.
## [LAYOUT RULES]
Paste the full YAML design_system into NotebookLM Slides custom instructions verbatim. Keep the palette (#D4FF00, #5D8AA8, #000000, #FFFFFF) and typography identical on every slide; add only title, audience, and emphasis.
## [FORBIDDEN]
Do not change the specified palette or typography, invent data, or exaggerate. No off-brand decoration.
## [FULL PROMPT — verbatim]
```yaml
# Source: YamilAyma/notebooklm-prompt-styles (GitHub)
design_system:
  global_style:
    theme: "Sustainable, modern nature aesthetic. Dark mode with glassmorphism."
    typography: 
      primary_heading: "Extra-bold geometric sans-serif (Codec Pro)"
      secondary_heading: "Clean bold sans-serif"
      body_text: "Highly legible functional sans-serif"
    color_palette:
      primary_color: "#D4FF00"
      secondary_color: "#5D8AA8"
      background_dark: "#000000"
      text_main: "#FFFFFF"
    key_visual_elements: 
      - "Full-bleed high-saturation nature photography"
      - "Frosted glass containers for text overlays"
      - "Large rounded corners on all UI elements"
      - "Signature lime-green accent dot after titles"

slide_layout_templates:
  - type: "Immersive_Hero"
    usage: "High-impact cover with full-bleed nature backdrop"
  - type: "Frosted_Agenda"
    usage: "Agenda points inside a glassmorphic container"
  - type: "Eco_Action_Grid"
    usage: "Practical tips with alternating rounded image/text blocks"
```
