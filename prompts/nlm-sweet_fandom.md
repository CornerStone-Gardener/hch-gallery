---
name: "Sweet Fandom"
tags: [creative, playful, bold]
use_case: "Creative campaigns & pitches"
palette: "#F48FB1 / #A5D6A7 / #FFF9C4 / #F8BBD0"
fonts: []
source_url: https://github.com/YamilAyma/notebooklm-prompt-styles/tree/main
license: MIT
attribution: "Harvested verbatim from YamilAyma/notebooklm-prompt-styles (Creative & Playful)"
renderer: notebooklm
---
## [STYLE SPEC]
Sweet Fandom. Charming and dessert-inspired design for cozy games and playful fan events. Typography — Heading: KG Primary Penmanship, sans-serif · Body: Inter, regular.
## [LAYOUT RULES]
Paste the full YAML design_system into NotebookLM Slides custom instructions verbatim. Keep the palette (#F48FB1, #A5D6A7, #FFF9C4, #F8BBD0) and typography identical on every slide; add only title, audience, and emphasis.
## [FORBIDDEN]
Do not change the specified palette or typography, invent data, or exaggerate. No off-brand decoration.
## [FULL PROMPT — verbatim]
```yaml
# Source: YamilAyma/notebooklm-prompt-styles (GitHub)
description: "A charming and cozy aesthetic that transforms social games into a kawaii bakery or tea party experience. It features the friendly KG Primary Penmanship font for a handwritten, approachable feel. Characterized by a palette of pastel pink, mint green, and cream, it uses adorable illustrations of desserts, strawberries, and lemonade jars to create a sweet and playful community atmosphere."
design_system:
  global_style:
    theme: "Sweet Fandom. Charming and dessert-inspired design for cozy games and playful fan events."
    typography: 
      primary_heading: "KG Primary Penmanship, sans-serif"
      secondary_heading: "KG Primary Penmanship, medium"
      body_text: "Inter, regular" # Using Inter for body text to ensure long questions are readable
    color_palette:
      primary: "#F48FB1" # Pastel Pink
      secondary: "#A5D6A7" # Mint Green
      background: "#FFF9C4" # Soft Cream / Yellow
      surface: "#F8BBD0" # Lighter Pink Surface
      text_main: "#795548" # Soil Brown for a soft contrast
      text_secondary: "#F48FB1"
    key_visual_elements: 
      - "Adorable hand-drawn illustrations of cakes, donuts, and cupcakes"
      - "Cozy lifestyle elements like lemonade jars and strawberries"
      - "Bubbly cloud shapes for rule boxes and featured questions"
      - "Checkered or soft pattern backgrounds for a picnic/bakery feel"

  image_generation_prompts:
    style_guidelines: "Kawaii bakery aesthetic, pastel pink and mint green palette, dessert illustrations, hand-drawn stickers, KG Primary Penmanship font vibe, cozy and playful atmosphere."
    themes:
      - target: "Game Start"
        prompt_elements: "A delicious strawberry shortcake on a pastel pink plate, mint green background, cute hand-drawn hearts, sweet and cozy vibe."
      - target: "Winner Celebration"
        prompt_elements: "A variety of colorful donuts with sprinkles, soft cream background, joyful and sugary aesthetic."

slide_layout_templates:
  - type: "Sweet_Bakery_Cover"
    usage: "Large brown KG Primary title on a pink checkered background with dessert stickers in the corners"
  - type: "Dessert_Rule_Box"
    usage: "A slide with a large white cloud shape containing text, decorated with a small cake icon"
  - type: "Picnic_Grid"
    usage: "A grid of photos framed in mint green with strawberry icons as separators"
  - type: "Sweet_Thank_You"
    usage: "Centered 'Thanks for playing' in pink script font surrounded by cute treat illustrations"
```
