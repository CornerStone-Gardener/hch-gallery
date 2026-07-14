---
name: "Kawaii Wellness"
tags: [creative, playful, bold]
use_case: "Creative campaigns & pitches"
palette: "#F48FB1 / #FFF59D / #81D4FA / #FFFDF0"
fonts: []
source_url: https://github.com/YamilAyma/notebooklm-prompt-styles/tree/main
license: MIT
attribution: "Harvested verbatim from YamilAyma/notebooklm-prompt-styles (Creative & Playful)"
renderer: notebooklm
---
## [STYLE SPEC]
Kawaii Wellness. Cute and whimsical pastel design for friendly fitness content. Typography — Heading: TT Firs Neue, bold · Body: Sniglet, regular.
## [LAYOUT RULES]
Paste the full YAML design_system into NotebookLM Slides custom instructions verbatim. Keep the palette (#F48FB1, #FFF59D, #81D4FA, #FFFDF0) and typography identical on every slide; add only title, audience, and emphasis.
## [FORBIDDEN]
Do not change the specified palette or typography, invent data, or exaggerate. No off-brand decoration.
## [FULL PROMPT — verbatim]
```yaml
# Source: YamilAyma/notebooklm-prompt-styles (GitHub)
description: "An ultra-cute and cheering aesthetic that makes fitness feel approachable and fun. It features the modern TT Firs Neue typeface against a whimsical pastel world. Characterized by adorable chubby characters (kawaii style) engaged in exercises, pink and yellow checkered patterns, and twinkling stars, it brings a sense of joy and sweetness to health and daily movement content."
design_system:
  global_style:
    theme: "Kawaii Wellness. Cute and whimsical pastel design for friendly fitness content."
    typography: 
      primary_heading: "TT Firs Neue, bold"
      secondary_heading: "TT Firs Neue, regular"
      body_text: "Sniglet, regular" # Friendly rounded body text
    color_palette:
      primary: "#F48FB1" # Pastel Pink
      secondary: "#FFF59D" # Pastel Yellow
      accent: "#81D4FA" # Pastel Blue
      background: "#FFFDF0" # Creamy White
      text_main: "#424242"
      text_secondary: "#F48FB1"
    key_visual_elements: 
      - "Chubby, kawaii characters performing fitness activities"
      - "Checkered patterns (pink/white or yellow/white)"
      - "Twinkling stars and sparkles as background decorations"
      - "Dashed-line containers and rounded bubble shapes"

  image_generation_prompts:
    style_guidelines: "Kawaii character design, pastel color palette, chubby white mochi-style characters, pink checkered patterns, cheerful and cute atmosphere, stars and sparkles."
    themes:
      - target: "Daily Workout"
        prompt_elements: "A cute round character lifting a tiny dumbbell, pastel pink background with stars, kawaii fitness style."
      - target: "Healthy Habits"
        prompt_elements: "Adorable characters sleeping and eating apples, yellow checkered border, whimsical and sweet wellness aesthetic."

slide_layout_templates:
  - type: "Kawaii_Wellness_Cover"
    usage: "Bold title surrounded by stars and a large illustration of an exercising mochi character"
  - type: "Bubble_Card"
    usage: "Text placed inside a soft-edged pink bubble with a cute character peeking from the side"
  - type: "Step_by_Step_Pastel"
    usage: "Sequential items marked by different pastel stars (pink, yellow, blue)"
  - type: "Checkered_Slide"
    usage: "Content area with a checkered pattern border and a large cheerful illustration"
```
