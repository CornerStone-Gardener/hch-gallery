---
name: "Architectural Mono"
tags: [tech-product, futuristic, technical]
use_case: "Product & tech decks"
palette: "#111111 / #E8E8E8 / #B0B0B0"
fonts: []
source_url: https://github.com/YamilAyma/notebooklm-prompt-styles/tree/main
license: MIT
attribution: "Harvested verbatim from YamilAyma/notebooklm-prompt-styles (Tech & Innovation)"
renderer: notebooklm
---
## [STYLE SPEC]
Modern brutalist, monochromatic, and architectural. High-contrast grayscale. Typography — Heading: Clean modern sans-serif (e.g., Inter, Helvetica), bold · Body: Functional sans-serif, technical feel.
## [LAYOUT RULES]
Paste the full YAML design_system into NotebookLM Slides custom instructions verbatim. Keep the palette (#111111, #E8E8E8, #B0B0B0) and typography identical on every slide; add only title, audience, and emphasis.
## [FORBIDDEN]
Do not change the specified palette or typography, invent data, or exaggerate. No off-brand decoration.
## [FULL PROMPT — verbatim]
```yaml
# Source: YamilAyma/notebooklm-prompt-styles (GitHub)
design_system:
  global_style:
    theme: "Modern brutalist, monochromatic, and architectural. High-contrast grayscale."
    typography: 
      primary_heading: "Clean modern sans-serif (e.g., Inter, Helvetica), bold"
      secondary_heading: "Refined sans-serif, standard weight"
      body_text: "Functional sans-serif, technical feel"
      accent_mono: "Monospace for technical labels"
    color_palette:
      primary_color: "#111111"
      background: "#E8E8E8"
      text_main: "#111111"
      accent_gray: "#B0B0B0"
    key_visual_elements: 
      - "High-contrast grayscale architectural photography"
      - "Large year stamps (e.g., '20 | 25')"
      - "Thin horizontal technical dividers"
      - "Thin arrow icons (→)"
      - "Vertical section labels"

slide_layout_templates:
  - type: "Architectural_Cover"
    usage: "Impactful intro with full-page imagery"
  - type: "Mission_Grid"
    usage: "Masonry grid for multiple references"
  - type: "Sliver_About"
    usage: "Vertical image sliver presentation"
```
