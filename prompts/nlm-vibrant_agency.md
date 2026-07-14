---
name: "Vibrant Agency"
tags: [nature, wellness, soft]
use_case: "Wellness & lifestyle decks"
palette: "#FF7A21 / #FFB392 / #FFFFFF / #1A1A1A"
fonts: []
source_url: https://github.com/YamilAyma/notebooklm-prompt-styles/tree/main
license: MIT
attribution: "Harvested verbatim from YamilAyma/notebooklm-prompt-styles (Nature & Wellness)"
renderer: notebooklm
---
## [STYLE SPEC]
High-energy, playful marketing and creative agency aesthetic. Typography — Heading: Bold friendly sans-serif (Montserrat) · Body: Clean legible sans-serif.
## [LAYOUT RULES]
Paste the full YAML design_system into NotebookLM Slides custom instructions verbatim. Keep the palette (#FF7A21, #FFB392, #FFFFFF, #1A1A1A) and typography identical on every slide; add only title, audience, and emphasis.
## [FORBIDDEN]
Do not change the specified palette or typography, invent data, or exaggerate. No off-brand decoration.
## [FULL PROMPT — verbatim]
```yaml
# Source: YamilAyma/notebooklm-prompt-styles (GitHub)
design_system:
  global_style:
    theme: "High-energy, playful marketing and creative agency aesthetic."
    typography: 
      primary_heading: "Bold friendly sans-serif (Montserrat)"
      secondary_heading: "Approachable modern sans-serif"
      body_text: "Clean legible sans-serif"
    color_palette:
      primary_color: "#FF7A21"
      secondary_color: "#FFB392"
      background: "#FFFFFF"
      text_main: "#1A1A1A"
    key_visual_elements: 
      - "Large rounded 'bubble' background elements"
      - "Wavy and curved dividers for section transitions"
      - "Studio-style photography with vibrant monochromatic backgrounds"
      - "Circular progress indicators and playful donut charts"

slide_layout_templates:
  - type: "Campaign_Cover"
    usage: "Impactful title for marketing pitches with bubble accents"
  - type: "Strategy_Cards"
    usage: "Grid of large rounded cards with orange icons"
  - type: "Performance_Kpis"
    usage: "Visualizing metrics with orange donut progress charts"
```
