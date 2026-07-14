---
name: "Clinical Doodles"
tags: [creative, playful, bold]
use_case: "Creative campaigns & pitches"
palette: "#1E3A8A / #F87171 / #E0F2FE / #FFFFFF"
fonts: []
source_url: https://github.com/YamilAyma/notebooklm-prompt-styles/tree/main
license: MIT
attribution: "Harvested verbatim from YamilAyma/notebooklm-prompt-styles (Creative & Playful)"
renderer: notebooklm
---
## [STYLE SPEC]
Clinical Doodles. Warm, hand-drawn medical aesthetic with a scrapbook feel. Typography — Heading: Schoolbell, cursive · Body: Schoolbell, regular.
## [LAYOUT RULES]
Paste the full YAML design_system into NotebookLM Slides custom instructions verbatim. Keep the palette (#1E3A8A, #F87171, #E0F2FE, #FFFFFF) and typography identical on every slide; add only title, audience, and emphasis.
## [FORBIDDEN]
Do not change the specified palette or typography, invent data, or exaggerate. No off-brand decoration.
## [FULL PROMPT — verbatim]
```yaml
# Source: YamilAyma/notebooklm-prompt-styles (GitHub)
description: "An approachable and empathetic medical aesthetic inspired by hand-drawn nursing journals. It features the playful Schoolbell handwriting font, a soft pastel blue palette, and a subtle grid paper texture. Characterized by charming doodle illustrations and organic cloud-like shapes, it humanizes clinical topics."
design_system:
  global_style:
    theme: "Clinical Doodles. Warm, hand-drawn medical aesthetic with a scrapbook feel."
    typography: 
      primary_heading: "Schoolbell, cursive"
      secondary_heading: "Schoolbell, regular"
      body_text: "Schoolbell, regular"
    color_palette:
      primary: "#1E3A8A" # Navy Outline
      secondary: "#F87171" # Warm Coral Accent
      background: "#E0F2FE" # Soft Sky Blue
      surface: "#FFFFFF" # Paper Surface
      text_main: "#1E293B"
      text_secondary: "#475569"
    key_visual_elements: 
      - "Subtle grid paper background pattern"
      - "Hand-drawn 'doodle' illustrations of medical staff"
      - "Organic blob and cloud-like containers"
      - "Decorative swirls and hand-drawn arrows"

  image_generation_prompts:
    style_guidelines: "Hand-drawn illustration style, colored pencil texture, soft clinical themes, friendly characters, pastel blue and navy color palette, scrapbook aesthetic, Schoolbell font vibe."
    themes:
      - target: "Nursing Care"
        prompt_elements: "A friendly hand-drawn illustration of a nurse helping an elderly patient, soft colors, clinical but warm atmosphere, doodle style."
      - target: "Medical Agenda"
        prompt_elements: "A hand-drawn desk with medical tools and an agenda, doodle style, soft blue and white colors, grid paper background."

slide_layout_templates:
  - type: "Doodle_Cover"
    usage: "Title in hand-drawn clouds with medical staff illustrations surrounding it"
  - type: "Grid_Content"
    usage: "Bullet points on a grid paper background with decorative swirls"
  - type: "Scrapbook_Image"
    usage: "Image contained in an organic hand-drawn frame with a small coral accent"
  - type: "Medical_Timeline_Doodle"
    usage: "A wavy line timeline with hand-drawn icons and nursing characters"
```
