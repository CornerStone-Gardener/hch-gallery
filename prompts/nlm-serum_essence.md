---
name: "Serum Essence"
tags: [nature, wellness, soft]
use_case: "Wellness & lifestyle decks"
palette: "#8D6E63 / #E1BEE7 / #FDFCFB / #F5F5F5"
fonts: []
source_url: https://github.com/YamilAyma/notebooklm-prompt-styles/tree/main
license: MIT
attribution: "Harvested verbatim from YamilAyma/notebooklm-prompt-styles (Nature & Wellness)"
renderer: notebooklm
---
## [STYLE SPEC]
Serum Essence. Premium beauty and wellness design with an editorial, high-contrast serif look. Typography — Heading: TAN Mon Cheri, serif · Body: Open Sauce, light.
## [LAYOUT RULES]
Paste the full YAML design_system into NotebookLM Slides custom instructions verbatim. Keep the palette (#8D6E63, #E1BEE7, #FDFCFB, #F5F5F5) and typography identical on every slide; add only title, audience, and emphasis.
## [FORBIDDEN]
Do not change the specified palette or typography, invent data, or exaggerate. No off-brand decoration.
## [FULL PROMPT — verbatim]
```yaml
# Source: YamilAyma/notebooklm-prompt-styles (GitHub)
description: "A serene and sophisticated aesthetic designed for premium skincare, beauty, and wellness editorial content. It features the exquisite TAN Mon Cheri serif for headlines, bringing a touch of high-fashion elegance. Characterized by a palette of warm amber, soft cream, and muted lavender, it uses frosted glass textures, organic shadows, and macro photography of liquid textures to create a calming and professional atmosphere."
design_system:
  global_style:
    theme: "Serum Essence. Premium beauty and wellness design with an editorial, high-contrast serif look."
    typography: 
      primary_heading: "TAN Mon Cheri, serif"
      secondary_heading: "Open Sauce, regular"
      body_text: "Open Sauce, light"
    color_palette:
      primary: "#8D6E63" # Amber Brown
      secondary: "#E1BEE7" # Soft Lavender
      background: "#FDFCFB" # Pearl White
      surface: "#F5F5F5" # Frosted Glass Surface
      text_main: "#4E342E" # Deep Umber
      text_secondary: "#8D6E63"
    key_visual_elements: 
      - "Frosted glass (glassmorphism) containers for text"
      - "Macro photography of serum droplets and liquid textures"
      - "Organic, soft window shadows (leaf or architectural shadows)"
      - "Minimalist botanical icons and thin serif dividers"

  image_generation_prompts:
    style_guidelines: "High-end skincare photography, frosted glass textures, warm natural sunlight with soft shadows, amber glass bottles, pearl white and soft lavender palette, TAN Mon Cheri font vibe."
    themes:
      - target: "Product Purity"
        prompt_elements: "Close-up of a glass serum dropper with a clear droplet, soft morning light, frosted glass background, elegant and clean."
      - target: "Wellness Ritual"
        prompt_elements: "Minimalist bathroom shelf with amber glass bottles, soft shadows of a palm leaf, serene and luxurious atmosphere."

slide_layout_templates:
  - type: "Editorial_Glow_Cover"
    usage: "Large TAN Mon Cheri title over a frosted glass overlay and a macro liquid background"
  - type: "Serum_Process_Steps"
    usage: "Numbered list with thin serif dividers and soft lavender accent blocks"
  - type: "Texture_Focus_Split"
    usage: "Full-height product texture photo on one side with clean, airy text on the other"
  - type: "Skincare_Manifesto"
    usage: "A central quote in TAN Mon Cheri light surrounded by generous white space and soft shadows"
```
