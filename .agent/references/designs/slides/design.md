# Slide Deck Design System (Marp Presentation)

This document defines the official design system, themes, and layout rules for Marp presentation slide decks. All HTML slide compilations (`slide-deck.html`) for clients must adhere to these specifications to guarantee an engaging, highly professional executive presentation.

---

## 1. Core Slide Settings

*   **Marp Engine**: Enabled (`marp: true`).
*   **Theme**: Default (`theme: default`).
*   **Pagination**: Enabled (`paginate: true`).
*   **Headers & Footers**:
    *   **Header**: Standardized title of the proposal (e.g., `Proposal: [Client Name] Modernization`).
    *   **Footer**: Copyright statement (e.g., `© 2026 Sotek Engineering — Confidential`).

---

## 2. Layout & Typography Rules

*   **Font Family**: `-apple-system`, `BlinkMacSystemFont`, `"Segoe UI"`, `Roboto`, sans-serif (clean, high-legibility sans-serif fonts).
*   **Primary Brand Color**: Navy Blue (`#001f3f`) for headings.
*   **Secondary Brand Accent**: Blue (`#0074D9`) for borders, links, and highlights.
*   **Backgrounds**: Light gray-blue (`#f4f6f8`) for structural containers.
*   **Slide Transitions**: Simple, professional slide flow.

---

## 3. Custom Structural Components (CSS Classes)

Marp slides are built using these custom inline style helper components to create visually rich layouts:

### A. Column Layout (Double Column)
To split a slide into two equal halves:
```html
<div class="columns">
<div class="column">

### Left Column Content

</div>
<div class="column">

### Right Column Content

</div>
</div>
```

### B. Information Cards
For highlighted takeaways, risks, or key business metrics:
```html
<div class="card">
<h3>Card Header</h3>
<p>Card content bullet points or prose.</p>
</div>
```

### C. Highlighted Text
To draw emphasis to metrics (such as costs, timelines, or effort hours):
```html
Total Effort: <span class="highlight">134–194 man-days</span>
```

---

## 4. Marp Directive Stylesheet

The standard global style block written inside the frontmatter of `slide-deck.md`:

```css
section {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
}
h1, h2, h3 {
  color: #001f3f;
}
h1 {
  font-size: 2.5em;
  border-bottom: 4px solid #0074D9;
  padding-bottom: 0.2em;
  margin-bottom: 1em;
}
h2 {
  font-size: 2em;
  border-left: 5px solid #0074D9;
  padding-left: 0.4em;
}
blockquote {
  border-left: 4px solid #0074D9;
  padding-left: 1rem;
  color: #555;
  background: #f4f6f8;
  border-radius: 4px;
  font-style: italic;
}
.columns {
  display: flex;
  gap: 2rem;
}
.column {
  flex: 1;
}
.card {
  background: #f4f6f8;
  padding: 1.5rem;
  border-radius: 8px;
  margin-bottom: 1rem;
  border-left: 4px solid #0074D9;
}
.highlight {
  color: #0074D9;
  font-weight: 700;
}
table {
  width: 100%;
  border-collapse: collapse;
}
th {
  background-color: #001f3f;
  color: white;
}
td, th {
  padding: 12px;
  border-bottom: 1px solid #ddd;
}
```
