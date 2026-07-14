---
name: "Summer Collage"
tags: [editorial, magazine, elegant]
use_case: "Editorial features & reports"
palette: "#00A8CC / #FFFFFF / #1A1A1A / #F4D03F"
fonts: []
source_url: https://github.com/YamilAyma/notebooklm-prompt-styles/tree/main
license: MIT
attribution: "Harvested verbatim from YamilAyma/notebooklm-prompt-styles (Editorial & Magazine)"
renderer: notebooklm
---
## [STYLE SPEC]
Bright, energetic, and sun-drenched vacation vibe. Photo collages and handwritten accents. Typography — Heading: Extra-tall, bold, condensed sans-serif · Body: Clean minimalist sans-serif.
## [LAYOUT RULES]
Paste the full YAML design_system into NotebookLM Slides custom instructions verbatim. Keep the palette (#00A8CC, #FFFFFF, #1A1A1A, #F4D03F) and typography identical on every slide; add only title, audience, and emphasis.
## [FORBIDDEN]
Do not change the specified palette or typography, invent data, or exaggerate. No off-brand decoration.
## [FULL PROMPT — verbatim]
```yaml
# Source: YamilAyma/notebooklm-prompt-styles (GitHub)
design_system:
  global_style:
    theme: "Bright, energetic, and sun-drenched vacation vibe. Photo collages and handwritten accents."
    typography: 
      primary_heading: "Extra-tall, bold, condensed sans-serif"
      secondary_heading: "Elegant flowing script / handwritten font"
      body_text: "Clean minimalist sans-serif"
    color_palette:
      primary_color: "#00A8CC"
      background: "Pure White (#FFFFFF)"
      text_main: "#1A1A1A"
      accent_color: "#F4D03F"
    key_visual_elements: 
      - "Asymmetric photo grids and mosaics"
      - "Rotated 'Polaroid' style photo overlays"
      - "Hand-drawn doodle icons (hearts, arrows)"
      - "High-saturation lifestyle imagery"

slide_layout_templates:
  - type: "Vacation_Cover"
    usage: "High-impact mosaic intro with condensed typography"
  - type: "Polaroid_Memories"
    usage: "Reflective content with rotated photo frames"
  - type: "Condensed_Keyword"
    usage: "Bold section breaks or summary slides"
```
