---
name: "Botanical Journal"
tags: [nature, wellness, soft]
use_case: "Wellness & lifestyle decks"
palette: "#7CB342 / #F9F7F1 / #D4E157"
fonts: []
source_url: https://github.com/YamilAyma/notebooklm-prompt-styles/tree/main
license: MIT
attribution: "Harvested verbatim from YamilAyma/notebooklm-prompt-styles (Nature & Wellness)"
renderer: notebooklm
---
## [STYLE SPEC]
Eco Scrapbook. Natural & Botanical. Typography — Heading: Bubbly hand-drawn sans-serif (e.g., Fredoka One) · Body: Clean legible sans-serif.
## [LAYOUT RULES]
Paste the full YAML design_system into NotebookLM Slides custom instructions verbatim. Keep the palette (#7CB342, #F9F7F1, #D4E157) and typography identical on every slide; add only title, audience, and emphasis.
## [FORBIDDEN]
Do not change the specified palette or typography, invent data, or exaggerate. No off-brand decoration.
## [FULL PROMPT — verbatim]
```yaml
# Source: YamilAyma/notebooklm-prompt-styles (GitHub)
design_system:
  global_style:
    theme: "Eco Scrapbook. Natural & Botanical."
    typography: 
      primary_heading: "Bubbly hand-drawn sans-serif (e.g., Fredoka One)"
      secondary_heading: "Friendly rounded sans-serif"
      body_text: "Clean legible sans-serif"
    color_palette:
      primary_color: "#7CB342"
      background: "#F9F7F1"
      accent_lime: "#D4E157"
    key_visual_elements: 
      - "Torn binder paper textures"
      - "Decorative washi tape strips"
      - "Hand-drawn botanical doodles"
      - "Circular or oval photo frames"

slide_layout_templates:
  - type: "Botanical_Hero"
    usage: "Main title or environmental intros"
  - type: "Notebook_Scrapbook"
    usage: "Detailed points or objectives"
  - type: "Eco_Profile"
    usage: "Nature focus or overviews"
```
