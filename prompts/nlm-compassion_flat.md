---
name: "Compassion Flat"
tags: [consulting-exec, corporate, data-dense]
use_case: "Executive & board decks"
palette: "#3B82F6 / #7EB1D1 / #FFFFFF / #F8FAFC"
fonts: []
source_url: https://github.com/YamilAyma/notebooklm-prompt-styles/tree/main
license: MIT
attribution: "Harvested verbatim from YamilAyma/notebooklm-prompt-styles (Business & Executive)"
renderer: notebooklm
---
## [STYLE SPEC]
Compassion Flat. Modern 2D medical illustration style with a professional blue palette. Typography — Heading: Poppins, sans-serif · Body: Poppins, light.
## [LAYOUT RULES]
Paste the full YAML design_system into NotebookLM Slides custom instructions verbatim. Keep the palette (#3B82F6, #7EB1D1, #FFFFFF, #F8FAFC) and typography identical on every slide; add only title, audience, and emphasis.
## [FORBIDDEN]
Do not change the specified palette or typography, invent data, or exaggerate. No off-brand decoration.
## [FULL PROMPT — verbatim]
```yaml
# Source: YamilAyma/notebooklm-prompt-styles (GitHub)
description: "A professional yet warm medical aesthetic utilizing modern flat 2D illustrations. It features the clean Poppins typeface, a serene palette of sky and navy blues, and large symbolic icons like medical crosses and hearts. Organized with rounded containers and soft shadows, it conveys institutional excellence with a human touch."
design_system:
  global_style:
    theme: "Compassion Flat. Modern 2D medical illustration style with a professional blue palette."
    typography: 
      primary_heading: "Poppins, sans-serif"
      secondary_heading: "Poppins, semi-bold"
      body_text: "Poppins, light"
    color_palette:
      primary: "#3B82F6" # Corporate Blue
      secondary: "#7EB1D1" # Sky Blue Matte
      background: "#FFFFFF" # Pure White
      surface: "#F8FAFC" # Light Slate Surface
      text_main: "#0F172A"
      text_secondary: "#475569"
    key_visual_elements: 
      - "Modern flat vector illustrations of healthcare professionals"
      - "Large decorative medical cross icons (+)"
      - "Rounded rectangular containers with subtle 1px borders"
      - "Clean, organized layouts with ample white space"

  image_generation_prompts:
    style_guidelines: "Flat 2D vector illustration, clean lines, no gradients, minimal shadows, corporate medical theme, professional characters, sky blue and white palette, Poppins font vibe."
    themes:
      - target: "Patient Care"
        prompt_elements: "A flat 2D illustration of a doctor talking to a patient, warm and professional vibe, clean vector style, blue and white tones."
      - target: "Medical Technology"
        prompt_elements: "Flat 2D illustration of a microscope and medical monitor, clean minimalist lines, medical blue accents, white background."

slide_layout_templates:
  - type: "Flat_Medical_Cover"
    usage: "Large title with a professional doctor illustration and a massive blue cross icon"
  - type: "Info_Card_Layout"
    usage: "Text contained in a rounded white card with a subtle shadow and sky blue title"
  - type: "Step_By_Step_Flat"
    usage: "Horizontal steps using circular icons and flat illustration characters"
  - type: "Medical_Components_Grid"
    usage: "A 2x2 grid of info cards with flat icons for each healthcare component"
```
