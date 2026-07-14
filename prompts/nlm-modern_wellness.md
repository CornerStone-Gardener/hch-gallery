---
name: "Modern Wellness"
tags: [nature, wellness, soft]
use_case: "Wellness & lifestyle decks"
palette: "#263238 / #2E7D32 / #FF8F00 / #FFFFFF"
fonts: []
source_url: https://github.com/YamilAyma/notebooklm-prompt-styles/tree/main
license: MIT
attribution: "Harvested verbatim from YamilAyma/notebooklm-prompt-styles (Nature & Wellness)"
renderer: notebooklm
---
## [STYLE SPEC]
Modern Wellness. Professional and geometric design for contemporary lifestyle presentations. Typography — Heading: TT Firs Neue, sans-serif · Body: Inter, regular.
## [LAYOUT RULES]
Paste the full YAML design_system into NotebookLM Slides custom instructions verbatim. Keep the palette (#263238, #2E7D32, #FF8F00, #FFFFFF) and typography identical on every slide; add only title, audience, and emphasis.
## [FORBIDDEN]
Do not change the specified palette or typography, invent data, or exaggerate. No off-brand decoration.
## [FULL PROMPT — verbatim]
```yaml
# Source: YamilAyma/notebooklm-prompt-styles (GitHub)
description: "A sleek and professional aesthetic for contemporary health and lifestyle content. It utilizes the geometric TT Firs Neue typeface to convey precision and modernity. Featuring a balanced palette of deep slate, forest green, and amber orange, it combines clean photography with minimalist vector shapes and ample white space for a premium corporate wellness feel."
design_system:
  global_style:
    theme: "Modern Wellness. Professional and geometric design for contemporary lifestyle presentations."
    typography: 
      primary_heading: "TT Firs Neue, sans-serif"
      secondary_heading: "TT Firs Neue, medium"
      body_text: "Inter, regular"
    color_palette:
      primary: "#263238" # Deep Slate
      secondary: "#2E7D32" # Forest Green
      accent: "#FF8F00" # Amber Orange
      background: "#FFFFFF" # Pure White
      text_main: "#263238"
      text_secondary: "#546E7A"
    key_visual_elements: 
      - "Clean, high-quality lifestyle photography"
      - "Minimalist flat vector illustrations of healthy activities"
      - "Geometric accents (rounded corners, circles, thick lines)"
      - "Modern info-boxes with subtle colored headers"

  image_generation_prompts:
    style_guidelines: "Modern minimalist photography, flat vector accents, deep green and amber color scheme, geometric composition, clean and professional atmosphere, white space."
    themes:
      - target: "Healthy Habits"
        prompt_elements: "A person practicing yoga in a bright modern room, minimalist green and orange graphic overlays, premium wellness vibe."
      - target: "Nutrition Guide"
        prompt_elements: "Close-up of fresh vegetables on a white table, geometric slate blue frames, clean and technical look."

slide_layout_templates:
  - type: "Modern_Wellness_Cover"
    usage: "Large TT Firs Neue title centered with a geometric green accent and a lifestyle photo background"
  - type: "Icon_List"
    usage: "Bullet points accompanied by clean flat icons in amber and forest green"
  - type: "Split_Visual"
    usage: "One side with a large photo, the other with organized text on a clean white background"
```
