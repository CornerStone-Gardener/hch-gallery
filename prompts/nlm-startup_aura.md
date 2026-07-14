---
name: "Startup Aura"
tags: [tech-product, futuristic, technical]
use_case: "Product & tech decks"
palette: "#007BFF / #1A1A1A / #2D2D2D / #FFFFFF"
fonts: []
source_url: https://github.com/YamilAyma/notebooklm-prompt-styles/tree/main
license: MIT
attribution: "Harvested verbatim from YamilAyma/notebooklm-prompt-styles (Tech & Innovation)"
renderer: notebooklm
---
## [STYLE SPEC]
Startup Aura. Modern pitch deck with mesh gradients and tech-centric typography. Typography — Heading: Open Sauce, sans-serif · Body: Open Sauce Sans, light weight.
## [LAYOUT RULES]
Paste the full YAML design_system into NotebookLM Slides custom instructions verbatim. Keep the palette (#007BFF, #1A1A1A, #2D2D2D, #FFFFFF) and typography identical on every slide; add only title, audience, and emphasis.
## [FORBIDDEN]
Do not change the specified palette or typography, invent data, or exaggerate. No off-brand decoration.
## [FULL PROMPT — verbatim]
```yaml
# Source: YamilAyma/notebooklm-prompt-styles (GitHub)
description: "A high-end, tech-focused pitch deck aesthetic. It features soft 'mesh' gradients in blue tones, clean Open Sauce typography, and a professional dark-mode charcoal base. Designed for startups, product launches, and innovative business presentations."
design_system:
  global_style:
    theme: "Startup Aura. Modern pitch deck with mesh gradients and tech-centric typography."
    typography: 
      primary_heading: "Open Sauce, sans-serif"
      secondary_heading: "Open Sauce Sans, medium weight"
      body_text: "Open Sauce Sans, light weight"
    color_palette:
      primary: "#007BFF" # Electric Blue
      background: "#1A1A1A" # Deep Charcoal
      surface: "#2D2D2D" # Slate Grey
      accent_gradient: "Soft mesh gradient from blue to light grey"
      text_main: "#FFFFFF"
      text_secondary: "#B0B0B0"
    key_visual_elements: 
      - "Soft blue 'aura' mesh gradients as background accents"
      - "Thin 1px borders for content cards"
      - "Rounded rectangles with 12px-16px corners"
      - "Minimalist line icons and clean data visualization charts"

  image_generation_prompts:
    style_guidelines: "Modern tech aesthetic, soft blue mesh gradients, minimalist corporate photography, clean professional lighting, high-end startup presentation style, Open Sauce font vibe."
    themes:
      - target: "Innovation Backdrop"
        prompt_elements: "Soft blue and grey abstract mesh gradient, smooth transition, professional tech background, minimalist."
      - target: "Team & Tech"
        prompt_elements: "Close-up of a professional modern workspace with soft blue lighting, high-tech aesthetic, clean composition."

slide_layout_templates:
  - type: "Pitch_Hero"
    usage: "Main title slide with a large aura gradient accent on the right"
  - type: "Service_Grid"
    usage: "Features or services organized in outlined rounded cards"
  - type: "Data_Traction"
    usage: "Key metrics and growth charts with thin blue line accents"
  - type: "Timeline_Milestones"
    usage: "Company history or roadmaps using dotted line connectors and blue nodes"
```
