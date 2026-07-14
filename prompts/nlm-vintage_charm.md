---
name: "Vintage Charm"
tags: [creative, playful, bold]
use_case: "Creative campaigns & pitches"
palette: "#E67E7E / #F8E1E1 / #4A3B3B / #D2C1A5"
fonts: []
source_url: https://github.com/YamilAyma/notebooklm-prompt-styles/tree/main
license: MIT
attribution: "Harvested verbatim from YamilAyma/notebooklm-prompt-styles (Creative & Playful)"
renderer: notebooklm
---
## [STYLE SPEC]
Romantic, nostalgic, and layered. Vintage scrapbook aesthetic. Typography — Heading: Elegant vintage serif (e.g., Playfair Display) · Body: Functional serif with a classic feel.
## [LAYOUT RULES]
Paste the full YAML design_system into NotebookLM Slides custom instructions verbatim. Keep the palette (#E67E7E, #F8E1E1, #4A3B3B, #D2C1A5) and typography identical on every slide; add only title, audience, and emphasis.
## [FORBIDDEN]
Do not change the specified palette or typography, invent data, or exaggerate. No off-brand decoration.
## [FULL PROMPT — verbatim]
```yaml
# Source: YamilAyma/notebooklm-prompt-styles (GitHub)
design_system:
  global_style:
    theme: "Romantic, nostalgic, and layered. Vintage scrapbook aesthetic."
    typography: 
      primary_heading: "Elegant vintage serif (e.g., Playfair Display)"
      secondary_heading: "Soft serif or clean traditional sans"
      body_text: "Functional serif with a classic feel"
    color_palette:
      primary_color: "#E67E7E"
      background: "#F8E1E1"
      text_main: "#4A3B3B"
      accent_color: "#D2C1A5"
    key_visual_elements: 
      - "Pink/Red ribbons and bows"
      - "Torn paper edges and layered textures"
      - "Vintage illustrations (floral/portraits)"
      - "Washi tape and pearls"

slide_layout_templates:
  - type: "Scrapbook_Header"
    usage: "Dynamic intro or section transitions"
  - type: "Layered_Referents"
    usage: "Showcasing aesthetic or historical references"
  - type: "Numbered_Vintage_Grid"
    usage: "Listing steps, characteristics, or points"
```
