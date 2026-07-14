---
name: "Frosted Luxury"
tags: [minimal, modern, clean]
use_case: "Clean minimal decks"
palette: "#333333 / #A8A29E / #F5F2ED / #FFFFFF"
fonts: []
source_url: https://github.com/YamilAyma/notebooklm-prompt-styles/tree/main
license: MIT
attribution: "Harvested verbatim from YamilAyma/notebooklm-prompt-styles (Minimalist & Modern)"
renderer: notebooklm
---
## [STYLE SPEC]
Frosted Luxury. High-end minimalist style with warm beige tones and editorial layouts. Typography — Heading: Arial Nova, sans-serif · Body: Arial Nova, regular.
## [LAYOUT RULES]
Paste the full YAML design_system into NotebookLM Slides custom instructions verbatim. Keep the palette (#333333, #A8A29E, #F5F2ED, #FFFFFF) and typography identical on every slide; add only title, audience, and emphasis.
## [FORBIDDEN]
Do not change the specified palette or typography, invent data, or exaggerate. No off-brand decoration.
## [FULL PROMPT — verbatim]
```yaml
# Source: YamilAyma/notebooklm-prompt-styles (GitHub)
description: "A sophisticated and high-end minimalist aesthetic inspired by luxury fragrance advertising. It features the refined Arial Nova typeface, a warm palette of beige and charcoal, and airy layouts with ample negative space. Characterized by frosted glass effects, high-fashion photography, and elegant thin borders, it conveys exclusivity and timeless elegance."
design_system:
  global_style:
    theme: "Frosted Luxury. High-end minimalist style with warm beige tones and editorial layouts."
    typography: 
      primary_heading: "Arial Nova, sans-serif"
      secondary_heading: "Arial Nova, light"
      body_text: "Arial Nova, regular"
    color_palette:
      primary: "#333333" # Stone Charcoal
      secondary: "#A8A29E" # Warm Taupe
      background: "#F5F2ED" # Warm Sand Beige
      surface: "#FFFFFF" # Bone White
      text_main: "#1C1917"
      text_secondary: "#57534E"
    key_visual_elements: 
      - "Frosted glass (blur) overlays for sections"
      - "High-end minimalist product photography"
      - "Large negative space areas to create an 'airy' feel"
      - "Elegant 1px thin grey borders and dividers"

  image_generation_prompts:
    style_guidelines: "Luxury editorial photography, soft natural lighting, frosted glass textures, minimalist product staging, warm beige and neutral color grading, high-end fashion aesthetic, Arial Nova font vibe."
    themes:
      - target: "Visual Inspiration"
        prompt_elements: "Close-up of a glass perfume bottle with soft shadows, beige background, frosted glass texture, minimalist and elegant."
      - target: "Brand Messaging"
        prompt_elements: "Minimalist interior with a single design object, soft sunlight, neutral tones, high-end editorial feel."

slide_layout_templates:
  - type: "Luxury_Title"
    usage: "Large refined title on a sand background with a high-end product shot on the left"
  - type: "Editorial_Agenda"
    usage: "Numbered list with wide line-height and plenty of white space"
  - type: "Frosted_Concept"
    usage: "Image with a frosted glass overlay containing brief descriptive text"
  - type: "Minimalist_Metrics"
    usage: "Clean data points inside rounded white pills with thin grey borders"
```
