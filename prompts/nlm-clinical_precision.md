---
name: "Clinical Precision"
tags: [consulting-exec, corporate, data-dense]
use_case: "Executive & board decks"
palette: "#2563EB / #000000 / #111111 / #FFFFFF"
fonts: []
source_url: https://github.com/YamilAyma/notebooklm-prompt-styles/tree/main
license: MIT
attribution: "Harvested verbatim from YamilAyma/notebooklm-prompt-styles (Business & Executive)"
renderer: notebooklm
---
## [STYLE SPEC]
Clinical Precision. High-tech medical style with dark contrast and blue glows. Typography — Heading: Helvetica World, sans-serif · Body: Helvetica, Arial, sans-serif.
## [LAYOUT RULES]
Paste the full YAML design_system into NotebookLM Slides custom instructions verbatim. Keep the palette (#2563EB, #000000, #111111, #FFFFFF) and typography identical on every slide; add only title, audience, and emphasis.
## [FORBIDDEN]
Do not change the specified palette or typography, invent data, or exaggerate. No off-brand decoration.
## [FULL PROMPT — verbatim]
```yaml
# Source: YamilAyma/notebooklm-prompt-styles (GitHub)
description: "A modern, high-tech medical aesthetic designed for clinical and healthcare presentations. It utilizes the objective Helvetica World typeface, deep black backgrounds, and vibrant blue light glows. Characterized by large typography and sharp minimalist icons, it conveys trust and scientific precision."
design_system:
  global_style:
    theme: "Clinical Precision. High-tech medical style with dark contrast and blue glows."
    typography: 
      primary_heading: "Helvetica World, sans-serif"
      secondary_heading: "Helvetica World, light"
      body_text: "Helvetica, Arial, sans-serif"
    color_palette:
      primary: "#2563EB" # Clinical Royal Blue
      background: "#000000" # Pure Black
      surface: "#111111" # Clinical Grey-Black
      accent_gradient: "Soft royal blue glow leaking from the edges"
      text_main: "#FFFFFF"
      text_secondary: "#A1A1AA"
    key_visual_elements: 
      - "Large minimalist arrow icons for calls to action"
      - "Subtle blue light leaks and glowing nodes on dark backgrounds"
      - "Thin 1px white horizontal dividers"
      - "Photography with clinical/modern medical subjects"

  image_generation_prompts:
    style_guidelines: "Modern medical photography, high-tech clinic environment, soft blue lighting glows, deep black backgrounds, clean professional medical aesthetic, sharp focus, Helvetica font vibe."
    themes:
      - target: "Medical Technology"
        prompt_elements: "Close-up of modern medical equipment with soft blue glow, clinical lighting, high-tech aesthetic, sharp focus."
      - target: "Care & Professionalism"
        prompt_elements: "A professional medical consultation in a modern clinic, soft blue ambient light, clean and trustworthy atmosphere."

slide_layout_templates:
  - type: "Medical_Title"
    usage: "Large title on a dark background with a massive arrow icon in the bottom right"
  - type: "Clinical_TOC"
    usage: "Table of contents with numbered list and soft blue background glow"
  - type: "Hospital_Timeline"
    usage: "Horizontal timeline with glowing nodes and blue spotlight effects"
  - type: "Data_Precision"
    usage: "Statistical highlights with large percentage numbers and subtle grid patterns"
```
