---
name: "Creative Notebook"
tags: [creative, playful, bold]
use_case: "Creative campaigns & pitches"
palette: "#FAD9C5 / #333333 / #D1E3E9"
fonts: []
source_url: https://github.com/YamilAyma/notebooklm-prompt-styles/tree/main
license: MIT
attribution: "Harvested verbatim from YamilAyma/notebooklm-prompt-styles (Creative & Playful)"
renderer: notebooklm
---
## [STYLE SPEC]
Creative, academic-journalistic, and organized. Scrapbook aesthetic with grid textures and organic pastel shapes. Typography — Heading: Bold, clean sans-serif, primarily sentence case · Body: Clean, highly legible sans-serif, airy spacing.
## [LAYOUT RULES]
Paste the full YAML design_system into NotebookLM Slides custom instructions verbatim. Keep the palette (#FAD9C5, #333333, #D1E3E9) and typography identical on every slide; add only title, audience, and emphasis.
## [FORBIDDEN]
Do not change the specified palette or typography, invent data, or exaggerate. No off-brand decoration.
## [FULL PROMPT — verbatim]
```yaml
# Source: YamilAyma/notebooklm-prompt-styles (GitHub)
design_system:
  global_style:
    theme: "Creative, academic-journalistic, and organized. Scrapbook aesthetic with grid textures and organic pastel shapes."
    typography: 
      primary_heading: "Bold, clean sans-serif, primarily sentence case"
      secondary_heading: "Medium weight sans-serif"
      body_text: "Clean, highly legible sans-serif, airy spacing"
    color_palette:
      primary_color: "#FAD9C5"
      background: "White with light gray grid and organic pastel blobs"
      text_main: "#333333"
      accent_color: "#D1E3E9"
    key_visual_elements: 
      - "Graph paper/grid background pattern"
      - "Organic pastel blobs (Peach, Blue, Pink)"
      - "Numbered list items in colored circles"
      - "Post-it note elements with paperclips"

slide_layout_templates:
  - type: "Cover_Journal"
    usage: "Impactful intro with grid and organic framing"
  - type: "Horizontal_Cards"
    usage: "Presenting mission, vision, or core objectives"
  - type: "Sticker_Note_Split"
    usage: "Idea origin or highlighted conceptual points"
```
