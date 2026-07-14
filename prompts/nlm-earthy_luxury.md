---
name: "Earthy Luxury"
tags: [consulting-exec, corporate, data-dense]
use_case: "Executive & board decks"
palette: "#8C8C6C / #8D493A / #F9F6EE / #FFFFFF"
fonts: []
source_url: https://github.com/YamilAyma/notebooklm-prompt-styles/tree/main
license: MIT
attribution: "Harvested verbatim from YamilAyma/notebooklm-prompt-styles (Business & Executive)"
renderer: notebooklm
---
## [STYLE SPEC]
Earthy Luxury. Organic hospitality design with Mediterranean warmth. Typography — Heading: Arial Unicode, sans-serif · Body: Arial Unicode, regular.
## [LAYOUT RULES]
Paste the full YAML design_system into NotebookLM Slides custom instructions verbatim. Keep the palette (#8C8C6C, #8D493A, #F9F6EE, #FFFFFF) and typography identical on every slide; add only title, audience, and emphasis.
## [FORBIDDEN]
Do not change the specified palette or typography, invent data, or exaggerate. No off-brand decoration.
## [FULL PROMPT — verbatim]
```yaml
# Source: YamilAyma/notebooklm-prompt-styles (GitHub)
description: "An earthy and organic hospitality aesthetic designed for boutique hotels, luxury resorts, and Mediterranean-inspired lifestyle brands. It features the clean and balanced Arial Unicode typeface to maintain a modern, uncluttered look that focuses on atmosphere. Characterized by a palette of muted olive green, warm terracotta, and soft cream, it utilizes asymmetrical photo grids with rounded corners, organic line icons, and split-screen layouts to create a serene and high-end experience."
design_system:
  global_style:
    theme: "Earthy Luxury. Organic hospitality design with Mediterranean warmth."
    typography: 
      primary_heading: "Arial Unicode, sans-serif"
      secondary_heading: "Arial Unicode, bold"
      body_text: "Arial Unicode, regular"
    color_palette:
      primary: "#8C8C6C" # Muted Olive
      secondary: "#8D493A" # Terracotta/Clay
      background: "#F9F6EE" # Soft Cream
      surface: "#FFFFFF" # Pure White
      text_main: "#4A4A3A" # Dark Olive Text
      text_secondary: "#70705B" # Muted Green-Grey
    key_visual_elements: 
      - "Photos with soft rounded corners (20px) arranged in overlapping grids"
      - "Split-screen layouts balancing full-bleed images and clean text areas"
      - "Organic, minimalist icons like lotus flowers or waves"
      - "Text blocks with wide letter spacing for an airy feel"
      - "Subtle beige borders around key image containers"

  image_generation_prompts:
    style_guidelines: "Luxury hospitality photography, Mediterranean architecture, warm natural light, muted olive and terracotta palette, organic textures, Arial Unicode font vibe, serene and high-end."
    themes:
      - target: "Suite Experience"
        prompt_elements: "A bright hotel suite with linen curtains, olive green accents, and sunlight streaming through a window, warm and luxurious."
      - target: "Organic Wellness"
        prompt_elements: "Close-up of a spa area with smooth stones and a wooden bowl, soft cream background, terracotta details, peaceful and organic."

slide_layout_templates:
  - type: "Hospitality_Hero_Grid"
    usage: "Large Arial Unicode title on the left with a grid of 3 rounded-corner photos on the right"
  - type: "Organic_Split_Intro"
    usage: "A vertical split layout with a full-bleed terracotta-toned image on one side and clean cream text on the other"
  - type: "Feature_List_Minimal"
    usage: "Bulleted list using organic dot icons and muted olive text on a white surface"
  - type: "Booking_Contact_Clean"
    usage: "Contact information centered at the bottom with wide letter spacing and a subtle olive logo"
```
