---
name: "Academic Edge"
tags: [editorial, magazine, elegant]
use_case: "Editorial features & reports"
palette: "#D00000 / #FFFFFF / #F8F9FA / #1A1A1A"
fonts: []
source_url: https://github.com/YamilAyma/notebooklm-prompt-styles/tree/main
license: MIT
attribution: "Harvested verbatim from YamilAyma/notebooklm-prompt-styles (Editorial & Magazine)"
renderer: notebooklm
---
## [STYLE SPEC]
Academic Edge. Editorial research style with B&W imagery and crimson accents. Typography — Heading: Codec Pro, sans-serif · Body: Inter, sans-serif.
## [LAYOUT RULES]
Paste the full YAML design_system into NotebookLM Slides custom instructions verbatim. Keep the palette (#D00000, #FFFFFF, #F8F9FA, #1A1A1A) and typography identical on every slide; add only title, audience, and emphasis.
## [FORBIDDEN]
Do not change the specified palette or typography, invent data, or exaggerate. No off-brand decoration.
## [FULL PROMPT — verbatim]
```yaml
# Source: YamilAyma/notebooklm-prompt-styles (GitHub)
description: "A sophisticated academic and editorial aesthetic inspired by thesis defenses and research portfolios. It balances high-contrast black and white photography with bold red accents and soft warm 'aura' gradients. Powered by the geometric Codec Pro typeface."
design_system:
  global_style:
    theme: "Academic Edge. Editorial research style with B&W imagery and crimson accents."
    typography: 
      primary_heading: "Codec Pro, sans-serif"
      secondary_heading: "Codec Pro, light"
      body_text: "Inter, sans-serif"
    color_palette:
      primary: "#D00000" # Academic Red
      background: "#FFFFFF" # Pure White
      surface: "#F8F9FA" # Ultra Light Grey
      accent_gradient: "Soft grainy gradient from peach to soft red"
      text_main: "#1A1A1A"
      text_secondary: "#4A4A4A"
    key_visual_elements: 
      - "High-contrast black and white photography"
      - "Bold red arrows and list bullets"
      - "Subtle film grain on background gradients"
      - "Minimalist horizontal dividers"

  image_generation_prompts:
    style_guidelines: "Editorial photography style, high-contrast black and white, minimalist composition, soft warm aura light leaks, architectural and nature details, professional academic aesthetic, Codec Pro font vibe."
    themes:
      - target: "Research & Detail"
        prompt_elements: "Close-up of architectural structures in high-contrast black and white, sharp lines, minimalist."
      - target: "Atmospheric Academic"
        prompt_elements: "Abstract soft warm aura gradient with light film grain, crimson accents, professional and clean."

slide_layout_templates:
  - type: "Thesis_Hero"
    usage: "Large bold title on the left with a vertical aura gradient on the right"
  - type: "Step_Process"
    usage: "Horizontal flow using B&W images connected by bold red arrows"
  - type: "Editorial_Results"
    usage: "Data charts with red bars and clean B&W background image integration"
  - type: "Recommendation_Cards"
    usage: "Split layout with B&W photos on top and red headings below"
```
