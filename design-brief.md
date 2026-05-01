# Delusional Illusions — Website Design Brief

**Brand:** Delusional Illusions (DSI)
**Artist:** Sage Grace
**Location:** Missoula, MT
**Site type:** One-page static portfolio + order CTA
**Date:** 2026-05-01

---

## 1. Color Palette

Derived from brand identity ("surrealist, creative, warm, direct, a bit surreal"), target audience (Missoula teens/young adults), and the edgy-artistic nail art style.

### Primary — Surreal Violet
`#8B5CF6`
The signature color. Carries the "delusional illusion" vibe — dreamlike, mystical, not corporate. Reads as creative and youthful without being juvenile. Bridges the purple/violet tones commonly found in nail art chrome and holographic finishes.

### Secondary — Deep Noir
`#1A1A2E`
Near-black with a violet-blue undertone. Not pure black (#000) — too harsh. This reads as midnight, adding depth and a gothic-adjacent edge without going full goth. Works for backgrounds, nav, and contrast areas.

### Accent — Hot Magenta / Electric Pink
`#EC4899`
The pop color. Ties directly to the pinks, magentas, and fuchsias prevalent in press-on nail art. High energy, attention-grabbing, perfect for CTAs ("Order a Custom Set"), hover states, and accent borders.

### Accent 2 — Holographic Silver
`#C4B5FD`
A lavender-silver that evokes chrome/holographic nail finishes. Use for secondary accents, card borders, tag backgrounds, and subtle shimmer effects (gradients, glows).

### Background — Smoky Lavender
`#1E1B2E`
Dark but not pure black. Carries the violet undertone throughout. Keeps the site feeling like a nighttime/creative space rather than a sterile dark-mode dashboard. Warm enough for the "local, warm, direct" brand promise.

### Card / Elevated Surface — Midnight Purple
`#2D2B55`
Slightly lighter than background for card surfaces, modals, and featured sections. Maintains the dark-creative aesthetic while providing clear visual hierarchy.

### Text — Soft White
`#F5F3FF`
Not pure white — a warm white with lavender tint. Easier on the eyes against dark backgrounds. Keeps the surreal, cohesive tone.

### Text Secondary — Muted Lavender
`#A78BFA`
For secondary text, captions, metadata, and subdued labels. Maintains the purple family throughout the entire palette.

### Success / Price Highlight — Amber Gold
`#F59E0B`
For pricing callouts, badge backgrounds, and "starting at $X" moments. Warm contrast against the cool palette, drawing the eye to commercial decision points.

---

### Complete Palette Reference

| Role | Color | Hex | Usage |
|------|-------|-----|-------|
| Primary | Surreal Violet | `#8B5CF6` | Brand color, headings, logo accent |
| Secondary | Deep Noir | `#1A1A2E` | Dark backgrounds, nav bar |
| Accent | Electric Pink | `#EC4899` | CTAs, hover states, highlights |
| Accent 2 | Holographic Silver | `#C4B5FD` | Borders, tags, subtle shimmer |
| Background | Smoky Lavender | `#1E1B2E` | Page background |
| Card Surface | Midnight Purple | `#2D2B55` | Cards, elevated sections |
| Text Primary | Soft White | `#F5F3FF` | Body text, headings |
| Text Secondary | Muted Lavender | `#A78BFA` | Captions, labels, secondary info |
| Highlight | Amber Gold | `#F59E0B` | Prices, badges, featured items |

---

## 2. Typography Recommendations

### Headings: Playfair Display (or similar high-contrast serif)
- **Weight:** 700 (Bold) for hero, 600 for section heads
- **Style:** Elegant serif with personality — not stuffy, not corporate
- **Reasoning:** Delusional Illusions sells *art*, not commodity. A serif heading font elevates the nail work from "product" to "wearable artwork" — the exact positioning the brand requires. Playfair Display specifically has a slightly surreal, dramatic quality that matches the brand name without being over-the-top.
- **Fallback:** Georgia, serif
- **Size scale:** Hero 3.5rem → Section 2rem → Subsection 1.25rem

### Body: Inter (or similar clean sans-serif)
- **Weight:** 400 (Regular), 500 (Medium for emphasis)
- **Style:** Clean, neutral, highly readable
- **Reasoning:** The body font should not compete with the art. Inter is legible at small sizes (FAQ, process steps, pricing details) and neutral enough to let the portfolio imagery dominate. It also reads as modern and tech-aware, which supports the "not a corporate salon, not fake influencer" positioning.
- **Fallback:** system-ui, -apple-system, sans-serif
- **Size:** 1rem base, 0.875rem for captions

### Accent Display: Cormorant Garamond (italic)
- **Usage sparingly:** Pull quotes, artist tagline, "handmade in Missoula" stamp
- **Reasoning:** An italic serif accent font adds the "surreal" touch — elegant and slightly dreamlike when used for short phrases. Not for blocks of text.

---

## 3. Overall Aesthetic Direction

**Dark, surrealist portfolio site** — a moody digital gallery that treats each nail art set as a small work of art, blending the dreamlike quality of the brand name with the bold, colorful energy of the work itself. Think "art gallery after hours" — not clinical and white, not chaotic and glitter-bombed, but a curated dark space where the nail art pops off the screen in full saturation.

The site should feel like stepping into Sage's creative space: intimate, artistic, slightly mysterious, but welcoming and clearly local. Every design choice reinforces: *this is handmade art, made in Missoula, by a real person — not a salon, not a factory*.

---

## 4. Layout & Style Notes

### Page Structure (One-Page Scroll)
Based on the approved Website Kit structure:

1. **Hero** — Full-viewport dark background with Surreal Violet gradient overlay. Large serif headline. Single CTA button (Electric Pink). Minimal. Let the typography breathe.

2. **Portfolio Gallery** — CSS grid, 3 columns on desktop, 2 on tablet, 1 on mobile. Images should be borderless or have a very subtle Holographic Silver border with rounded corners (8px). Hover: slight scale (1.02) + soft lavender glow. No captions on the grid — keep it visual. Optional lightbox on click.

3. **Social Proof** — Horizontal scroll or small card row. Past client quotes in Cormorant italic on Midnight Purple cards. Keep it real — text testimonials, not fabricated glamour shots.

4. **Packages** — Three cards (Ready-Made $25 / Custom $40 / Event $60) on Card Surface background. Middle card (Custom) slightly elevated/highlighted — this is "the sweet spot." Amber Gold for the price numbers. Each card: title, price, 2-3 bullet features, small CTA.

5. **How It Works** — Numbered steps (1-6) in a clean vertical timeline or horizontal stepper. Muted Lavender numbers, Soft White text. Simple icons optional — keep the focus on the clarity of the process.

6. **FAQ** — Accordion (collapsed by default). Inter font, compact spacing. This section is functional, not decorative.

7. **Order CTA** — Full-width section with bold Electric Pink background. White serif headline. Single action button (dark, reverses the color scheme). This is the "don't leave without acting" moment.

8. **Footer** — Minimal. Licensing-safe note ("Press-on nail art sets only — not a licensed salon service"). Instagram link. Email. "Made in Missoula, MT."

### Key Layout Principles
- **Dark-first design.** The entire site uses the dark palette as the canvas. This makes the colorful nail art photos the visual stars.
- **Generous whitespace.** Even on a dark background, negative space communicates quality. Don't cram.
- **Mobile-first.** Sage's audience (Missoula teens/young adults) lives on phones. The portfolio must swipe well.
- **One CTA per section max.** The site has two allowed CTAs ("Order a Custom Set" and "Send Me the Portfolio"). Use them strategically, don't dilute.
- **No stock imagery.** Every image is Sage's actual work. If portfolio photos are limited, use a "coming soon" placeholder in brand colors rather than generic nail art stock.
- **Subtle animations only.** A gentle fade-in on scroll for gallery items. A soft pulse on the CTA. Nothing bouncy, glittery, or auto-playing.

### Image Treatment
- Nail art photos should be displayed at high resolution, no filters, no overlays
- Optional: very subtle rounded corners (8-12px radius) to soften the grid
- No heavy drop shadows — the dark background already creates natural contrast
- Aspect ratio: allow mixed ratios (portrait nails, square sets) — use a masonry or flexible grid

---

## 5. Bridging Nail Art Style with Web Aesthetic

### The Tension
Sage's nail art is **bold, saturated, high-contrast, and maximalist** — pinks, chromes, holographics, character art, loud color combinations. Her web aesthetic instincts (based on the "Surrealist" reference and brand brain) lean **moody, dark, curated, and artistic** — think gallery, not disco.

### The Bridge Strategy
The website serves as the **dark gallery** that lets the **bright artwork** shine. This is not a contradiction — it's the same principle as a neon sign against a black wall, or a spotlight on a stage:

1. **Dark background = gallery wall.** The Smoky Lavender/Midnight Purple palette absorbs visual noise and makes every color in the nail art photos read as more vivid and intentional. This is how you make press-on nails look like *art*, not *product*.

2. **Electric Pink accents echo the nail art.** The CTA buttons and accent elements carry the energy of the nail art into the site's UI. Even without a photo on screen, the pink says "this brand is alive and bold."

3. **Holographic Silver references chrome finishes.** Many press-on sets feature chrome, holographic, or chrome-gradient effects. The lavender-silver accent in the palette mirrors this finish — it reads as the "digital version" of a chrome nail surface.

4. **Typography elevates the product.** A serif heading font ("Playfair Display") frames nail art as *wearable art*, not a beauty supply commodity. This directly serves the brand promise: "Professional-grade custom nail art, made locally, without salon prices."

5. **Restraint in UI = confidence in art.** The site is intentionally not as loud as the nail art. That's the point. The site doesn't need to compete — it needs to *present*. Clean layout, generous spacing, and minimal UI elements signal that the work is worth paying attention to.

### What to Avoid
- **Don't make the site as colorful as the nails.** The site should be the quiet frame, not a second painting.
- **Don't use generic "beauty" aesthetics** — soft pinks, marble textures, script fonts, gold accents. That's the salon aesthetic, and DSI is explicitly *not a salon*.
- **Don't go full goth.** Deep noir, yes — but the violet and pink accents keep it rooted in creative/arty, not dark/harsh.
- **Don't use glitter animations.** A CSS shimmer on hover is fine. Full sparkle effects undermine the gallery sophistication.

---

## Technical Notes

### Fonts (Google Fonts)
```html
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Inter:wght@400;500&family=Cormorant+Garamond:ital,wght@1,400&display=swap" rel="stylesheet">
```

### CSS Custom Properties
```css
:root {
  --color-primary: #8B5CF6;      /* Surreal Violet */
  --color-secondary: #1A1A2E;    /* Deep Noir */
  --color-accent: #EC4899;       /* Electric Pink */
  --color-accent-2: #C4B5FD;     /* Holographic Silver */
  --color-bg: #1E1B2E;           /* Smoky Lavender */
  --color-surface: #2D2B55;      /* Midnight Purple */
  --color-text: #F5F3FF;         /* Soft White */
  --color-text-muted: #A78BFA;   /* Muted Lavender */
  --color-highlight: #F59E0B;    /* Amber Gold */
  
  --font-heading: 'Playfair Display', Georgia, serif;
  --font-body: 'Inter', system-ui, sans-serif;
  --font-accent: 'Cormorant Garamond', Georgia, serif;
  
  --radius: 8px;
  --radius-lg: 16px;
}
```

### Color Analysis Script
A Python script (`analyze_both_folders.py`) is included in the project root to extract exact hex codes and color distributions from the reference images. Run it to validate and refine this palette against the actual photo data:
```bash
python3 /mnt/c/Users/Home/vault/projects/missoula-nail-art/analyze_both_folders.py
```

---

## Implementation Priority

1. **Set up design tokens first** (CSS custom properties above) — this is the Design System First approach
2. **Build the portfolio section** — this is the visual core and depends on having real photos
3. **Hero + CTA** — first screen, first impression
4. **Packages + Process** — commercial decision path
5. **FAQ + Footer** — compliance and detail

---

*This brief was compiled from brand vault documents, the approved Website Kit structure, launch kit handoffs, and the brand identity definition. Color palette is designed to be validated/refined against the image analysis script output when run.*