---
name: "Scholar's Journal"
tags: [nature, wellness, soft]
use_case: "Wellness & lifestyle decks"
palette: "#3E4E63 / #D1D1D1 / #2D3436"
fonts: []
source_url: https://github.com/YamilAyma/notebooklm-prompt-styles/tree/main
license: MIT
attribution: "Harvested verbatim from YamilAyma/notebooklm-prompt-styles (Nature & Wellness)"
renderer: notebooklm
---
## [STYLE SPEC]
Academic, vintage, and scientific. Botanical engravings focus. Typography — Heading: Traditional serif or slab serif (e.g., Trocchi) · Body: Functional traditional serif.
## [LAYOUT RULES]
Paste the full YAML design_system into NotebookLM Slides custom instructions verbatim. Keep the palette (#3E4E63, #D1D1D1, #2D3436) and typography identical on every slide; add only title, audience, and emphasis.
## [FORBIDDEN]
Do not change the specified palette or typography, invent data, or exaggerate. No off-brand decoration.
## [FULL PROMPT — verbatim]
```yaml
# Source: YamilAyma/notebooklm-prompt-styles (GitHub)
design_system:
  global_style:
    theme: "Academic, vintage, and scientific. Botanical engravings focus."
    typography: 
      primary_heading: "Traditional serif or slab serif (e.g., Trocchi)"
      secondary_heading: "Classic serif, clean"
      body_text: "Functional traditional serif"
    color_palette:
      primary_color: "#3E4E63"
      background: "#D1D1D1"
      text_main: "#2D3436"
    key_visual_elements: 
      - "Etched/Engraved line art illustrations"
      - "Heavy coarse paper texture grain"
      - "Indigo on Parchment monochromatic scheme"

slide_layout_templates:
  - type: "Scholar_Intro"
    usage: "Title slides or section starts"
  - type: "Illustration_Focus"
    usage: "Presenting concepts with a visual anchor"
  - type: "Balanced_Journal"
    usage: "Summary or Q&A slides"
```
