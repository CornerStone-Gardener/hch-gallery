---
name: "Emerald Corporate"
tags: [consulting-exec, corporate, data-dense]
use_case: "Executive & board decks"
palette: "#0F3024 / #FFFFFF / #C0C0C0"
fonts: []
source_url: https://github.com/YamilAyma/notebooklm-prompt-styles/tree/main
license: MIT
attribution: "Harvested verbatim from YamilAyma/notebooklm-prompt-styles (Business & Executive)"
renderer: notebooklm
---
## [STYLE SPEC]
Professional, executive, and high-tech. Deep emerald green with metallic silver accents. Typography — Heading: Bold authoritative sans-serif, primarily uppercase · Body: Light-weight, highly legible sans-serif.
## [LAYOUT RULES]
Paste the full YAML design_system into NotebookLM Slides custom instructions verbatim. Keep the palette (#0F3024, #FFFFFF, #C0C0C0) and typography identical on every slide; add only title, audience, and emphasis.
## [FORBIDDEN]
Do not change the specified palette or typography, invent data, or exaggerate. No off-brand decoration.
## [FULL PROMPT — verbatim]
```yaml
# Source: YamilAyma/notebooklm-prompt-styles (GitHub)
design_system:
  global_style:
    theme: "Professional, executive, and high-tech. Deep emerald green with metallic silver accents."
    typography: 
      primary_heading: "Bold authoritative sans-serif, primarily uppercase"
      secondary_heading: "Medium weight sans-serif, clean"
      body_text: "Light-weight, highly legible sans-serif"
    color_palette:
      primary_color: "#0F3024"
      background: "Deep emerald with crystalline geometric shards"
      text_main: "#FFFFFF"
      accent_color: "#C0C0C0"
    key_visual_elements: 
      - "Sharp geometric shards with silver reflections"
      - "Pill-shaped gradient labels"
      - "Glassmorphic content cards"
      - "Professional office-centric photography"

slide_layout_templates:
  - type: "Executive_Cover"
    usage: "Authoritative intro with geometric framing"
  - type: "Pill_Grid_Methodology"
    usage: "Structured presentation of steps or research"
  - type: "Glassmorphic_Data"
    usage: "Data-heavy slides with visual clarity"
```
