# Inkpress Deck — Design System Spec

Single-file HTML presentation deck. Facts, product, analysis, methodology. Extremely calm, rational, academic. No hand-drawn elements, no noise, no decoration. Ink on paper — sharp, minimal, editorial.

---

## 1. Color Palettes

Pick exactly one of these 4 palettes — no mixing, no hex modifications:

| Palette | Accent | Paper | Ink | Use Case | Text Rule |
|---------|--------|-------|-----|----------|-----------|
| Klein Blue (IKB) | `#002FA7` | `#fafaf8` | `#0a0a0a` | Business / AI / design | — |
| Lemon Yellow | `#FFD500` | `#f7f5ee` (light cream) | `#0a0a0a` | Youth / retail / sports | Text must be black (never white) |
| Lemon Green / Neon | `#C5E803` | `#f7f5ee` | `#0a0a0a` | Sustainability / tech startups / Gen-Z | Text must be black |
| Safety Orange | `#FF6B35` | `#f7f5ee` | `#0a0a0a` | Industrial / automotive / urgent | Text in white + bold >= 600 |

---

## 2. Slide Layouts (22 Templates)

Do NOT invent or modify layouts. Slide count is driven by content — cover all user content completely (short content = 6-10 slides minimum; long content should far exceed that; the same layout may repeat across sections).

### S01 Cover
Full-bleed accent + ASCII breathing dot matrix + inverted title + metadata chrome (date / No / topic).

### S02 Vertical Timeline
Left dashed axis + dots; right nodes = year + KPI + description.

### S03 Statement
9.6vw centered giant text + generous left whitespace + bottom hairline + annotation.

### S04 Six Cells
2x3 grid, each cell: icon + number + short title + one-line description.

### S05 Three Sub-cards
Left hero title + right 3 horizontally stacked grey cards.

### S06 KPI Tower
4 variable-height accent-colored columns; icon on top; large number + label at bottom.

### S07 H-Bar Chart
Horizontal ranked bars, width reflects data, number at end.

### S08 Duo Compare
Vertical divider; left Before / right After.

### S09 Closing Manifesto
Left accent block + ASCII dot matrix + manifesto; right white + 3 bullet points.

### S10 Dot Matrix Statement
Centered statement + corner geometric dot matrix / ring matrix.

### S11 Horizontal Timeline
Top headline, middle hairline axis, evenly spaced nodes, step names below.

### S12 Manifesto + Ink Banner
Top half headline + explanation; bottom half full-width black banner + inverted small text.

### S13 Three Forces Cards
Left ink hero block; right 3 grey cards, each: large number + text.

### S14 Loop Diagram
Left numbered steps; right SVG concentric rings; center "LOOP" label.

### S15 Image Matrix + Hero Stat
4x3 equal-height cards (12 items) + bottom summary large number + label.

### S16 Multi-card Brief
3x2 micro-cards; main text top-left, footnote bottom-right, one card accent-highlighted.

### S17 System Diagram
Left headline + 3 description paragraphs; right SVG three concentric circles + external labels.

### S18 Why Now
3 columns, each: category label + headline + description + bottom number (last column in accent).

### S19 Four Cards
Top accent hairline + headline + 4 equal-width cards (metadata / title / body).

### S20 Stacked KPI Ledger
Vertical rows + hairline separators; left large number / center label / right icon.

### S21 Tech Spec Sheet
Left title block / center 3 KPI hairlines / right variable-height columns / bottom data.

### S22 Image Hero
Top 60% full-width image + white title block overlay; bottom 40% explanation + 3-column KPI.

---

## 3. Design Rules — Absolute Laws

- **Sharp corners only**: `border-radius: 0` everywhere. Rounded corners = immediate violation.
- **1px hairline borders**, black or accent; absolutely no shadows / gradients / blur.
- **16-column grid**: `grid-template-columns: repeat(16, 1fr); gap: 0`.
- **Fonts**: Inter Tight (Latin display) / Inter (body) / Noto Sans SC (CJK) / JetBrains Mono (data); no serifs, no decorative fonts.
- **Extreme type contrast**: cover uses 9.6vw display, body 14-16px, labels 11px uppercase letter-spacing 0.08em.
- **Keyboard navigation**: arrow left/right + hash sync; fixed corner badges: `No.N/N` bottom-right, topic label bottom-left.
- **No fabrication**: numbers must come from user input; chart bar heights = real data proportionally scaled.
- Output a single-file HTML. No external image URLs; decorative geometry (ASCII matrices / concentric circles) via pure CSS or inline SVG.

---

## 4. Technical Implementation

### Font Loading
```css
@import url('https://fonts.googleapis.com/css2?family=Inter+Tight:wght@400;700;900&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&family=Noto+Sans+SC:wght@400;700&display=swap');
```

### Base Grid
```css
.slide {
  display: grid;
  grid-template-columns: repeat(16, 1fr);
  gap: 0;
  width: 100vw;
  height: 100vh;
  overflow: hidden;
  border-radius: 0;
}
```

### Navigation
```javascript
document.addEventListener('keydown', (e) => {
  if (e.key === 'ArrowRight') nextSlide();
  if (e.key === 'ArrowLeft') prevSlide();
});
```

### Badge Positioning
```css
.badge-number {
  position: fixed;
  bottom: 1.5rem;
  right: 2rem;
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}
.badge-topic {
  position: fixed;
  bottom: 1.5rem;
  left: 2rem;
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}
```
