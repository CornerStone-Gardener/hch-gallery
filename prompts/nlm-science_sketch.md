---
name: "Science Sketch"
tags: [creative, playful, bold]
use_case: "Creative campaigns & pitches"
palette: "#3F51B5 / #FFD54F / #FFFDF0 / #E3F2FD"
fonts: []
source_url: https://github.com/YamilAyma/notebooklm-prompt-styles/tree/main
license: MIT
attribution: "Harvested verbatim from YamilAyma/notebooklm-prompt-styles (Creative & Playful)"
renderer: notebooklm
---
## [STYLE SPEC]
Science Sketch. Clean academic illustration style with bold blue and yellow tones. Typography — Heading: Schoolbell, sans-serif · Body: Schoolbell, regular.
## [LAYOUT RULES]
Paste the full YAML design_system into NotebookLM Slides custom instructions verbatim. Keep the palette (#3F51B5, #FFD54F, #FFFDF0, #E3F2FD) and typography identical on every slide; add only title, audience, and emphasis.
## [FORBIDDEN]
Do not change the specified palette or typography, invent data, or exaggerate. No off-brand decoration.
## [FULL PROMPT — verbatim]
```yaml
# Source: YamilAyma/notebooklm-prompt-styles (GitHub)
description: "A clean and vibrant academic aesthetic inspired by high school science projects and textbook sketches. It features the hand-drawn Schoolbell typeface paired with the condensed Pompiere for subtitles. Characterized by thick-lined blue vector doodles filled with bright yellow, and accents like graph paper grids and wavy lines, it conveys a sense of organized learning and active discovery."
design_system:
  global_style:
    theme: "Science Sketch. Clean academic illustration style with bold blue and yellow tones."
    typography: 
      primary_heading: "Schoolbell, sans-serif"
      secondary_heading: "Pompiere, regular"
      body_text: "Schoolbell, regular"
    color_palette:
      primary: "#3F51B5" # Indigo Blue
      secondary: "#FFD54F" # Sunflower Yellow
      background: "#FFFDF0" # Light Cream
      surface: "#E3F2FD" # Sky Blue Surface
      text_main: "#283593"
      text_secondary: "#3F51B5"
    key_visual_elements: 
      - "Clean vector doodles with thick indigo outlines and yellow fills"
      - "Graph paper (grid) patterns in the corners or background"
      - "Wavy horizontal lines (sine waves) as decorative accents"
      - "Soft color blobs acting as backgrounds for key scientific icons"

  image_generation_prompts:
    style_guidelines: "Clean vector doodle, thick blue outlines, bright yellow highlights, cream background, graph paper textures, educational icons, Schoolbell font vibe."
    themes:
      - target: "Methodology"
        prompt_elements: "Microscope and test tubes in a clean vector style, indigo and yellow palette, academic and bright."
      - target: "Findings"
        prompt_elements: "A bar chart on a graph paper background, thick-lined doodles of a magnifying glass, vibrant educational aesthetic."

slide_layout_templates:
  - type: "Sketch_Cover"
    usage: "Large Schoolbell title with thick outlines, surrounded by atoms, books, and yellow wavy lines"
  - type: "Grid_Content"
    usage: "Text placed on a clean area with a subtle graph paper grid pattern in the background"
  - type: "Method_Focus"
    usage: "Central image with rounded corners and a thick border, surrounded by scientific doodles"
  - type: "Academic_Summary"
    usage: "Summary list where each item is marked by a small yellow filled indigo circle"
```
