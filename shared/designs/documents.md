# Design System Spec: Microsoft Word (DOCX) Style for Web

This document defines the Design System specifications that precisely simulate the visual appearance of a Microsoft Word document (A4 paper size) on the Web. The objective is to guide the AI to generate standardized HTML/CSS optimized for long-form textual content, tables, images, and charts, maintaining standard Word typography while enhancing the heading colors with a polished corporate look.

---

## 1. Core Principles

*   **Skeuomorphic A4 Simulation:** Displays the web page as one or more A4 paper sheets placed on a high-contrast canvas background with a subtle drop shadow.
*   **Standard Administrative Typography:** Uses traditional Serif fonts (`Times New Roman`), fully justified text alignment, and mandatory first-line indentation for all body paragraphs in standard black text.
*   **Heading Accent Separation:** Heading and sub-heading elements are styled with a clean Deep Navy and Steel Blue executive color palette to provide excellent reading structure.
*   **Print-Friendly Layout:** Ensures optimal CSS page-break rules so that when users print the page (Ctrl + P) or export to PDF, headings, table rows, and charts are not split across pages.

---

## 2. Page & Layout Specifications

The AI must implement the document page structure based on a wrapper class (`.word-page`) with these fixed parameters:

*   **System Canvas Background:** `#E2E7EC` (The signature blue-gray background of MS Word workspace).
*   **Paper Background:** `#FFFFFF` (Pure white).
*   **A4 Paper Dimensions:** Width `210mm`, Minimum Height `297mm`.
*   **Standard Office Margins:**
    *   Top Margin: `20mm`
    *   Bottom Margin: `20mm`
    *   Left Margin: `30mm` (Wider to accommodate binding/gilding)
    *   Right Margin: `20mm`
*   **Page Shadow (Box-shadow):** `0 4px 10px rgba(0, 0, 0, 0.15)`

---

## 3. Typography & Color Standards

*   **Default Font Stack:** `"Times New Roman"`, Times, serif.
*   **Base Font Size (Body):** `14px` (equivalent to standard 14pt in Word - the regulatory standard for administrative documents).
*   **Line Height:** `1.5` (equivalent to 1.5 lines spacing standard).
*   **Base Text Color:** Pure Black (`#000000`) for standard administrative documents.
*   **Paragraph Format (`<p>`):**
    *   Alignment: `text-align: justify;`
    *   First-line Indentation: `text-indent: 1.27cm;` (equivalent to 0.5 inches).
    *   Bottom Spacing: `padding-bottom: 8pt;` (Do not use margin-top to avoid indentation collapse/conflicts).
*   **Headings & Spacing:**
    *   `h1`: Font size `20pt`, bold, centered (`text-align: center`), uppercase (`text-transform: uppercase`), deep navy (`#1b365d`), with `24pt` bottom margin.
    *   `h2` (Sections): Font size `16pt`, bold, deep navy blue (`#1b365d`), with a custom light-blue bottom separator line (`border-bottom: 2px solid #cbd5e1`), `18pt` top margin, `8pt` bottom margin.
    *   `h3` (Sub-sections): Font size `14pt`, bold, vibrant steel blue (`#2b6cb0` or `#3182ce`), normal style (non-italic), `18pt` top margin, `6pt` bottom margin.

---

## 4. Special Component Specifications

### A. Tables
*   **Width:** Always occupies `100%` of the margin container width.
*   **Borders:** `border-collapse: collapse;` with a thin black border `1px solid #000000` on all cells (`th`, `td`).
*   **Font Size inside Tables:** `13px` (one size smaller than the body text).
*   **Table Header (`<th>`):** Light gray background (`#F2F2F2`), bold face, centered, color `#1b365d`.
*   **Container (`.table-container`):** Allows horizontal scrolling on mobile devices (`overflow-x: auto`).

### B. Images & Charts (Media Containers)
*   **Outer Wrapper (`.media-container`):** `margin: 18pt 0; display: flex; flex-direction: column; align-items: center;`
*   **Media Elements (`img`, `.chart-mockup`):** `max-width: 100%;` with a thin gray frame border `#D0D0D0`.
*   **Caption (`.caption`):** Placed immediately below the image/table. Font size `12px`, italic, dark gray `#333333`, centered. Format: *"Figure X.Y: [Caption text]"*.

---

## 5. Core CSS Code (AI Reference Code)

The AI can use this CSS block directly to construct the interface:

```css
* { box-sizing: border-box; }

body {
  font-family: "Times New Roman", Times, serif;
  font-size: 14px;
  line-height: 1.5;
  color: #000000; /* Reverted to standard black */
  background-color: #E2E7EC;
  margin: 0;
  padding: 40px 10px;
  display: flex;
  justify-content: center;
}

.word-page {
  background-color: #FFFFFF;
  width: 210mm;
  min-height: 297mm;
  padding: 20mm 20mm 20mm 30mm; /* Top Right Bottom Left */
  box-shadow: 0 4px 10px rgba(0,0,0,0.15);
}

h1 { 
  font-size: 20pt; 
  color: #1b365d; /* Deep Navy */
  text-align: center; 
  text-transform: uppercase; 
  margin-bottom: 24pt; 
  page-break-after: avoid; 
}

h2 { 
  font-size: 16pt; 
  color: #1b365d; /* Deep Navy */
  border-bottom: 2px solid #cbd5e1; /* Custom light-blue bottom separator */
  padding-bottom: 4px;
  margin-top: 24pt;
  margin-bottom: 8pt;
  page-break-after: avoid; 
}

h3 { 
  font-size: 14pt; 
  color: #2b6cb0; /* Vibrant Steel Blue */
  font-weight: bold;
  margin-top: 18pt;
  margin-bottom: 6pt;
  page-break-after: avoid;
}

p { 
  text-indent: 1.27cm; 
  text-align: justify; 
  padding-bottom: 8pt; 
  margin: 0; 
}

ul, ol {
  margin-top: 0;
  margin-bottom: 12pt;
  padding-left: 1.5cm;
}

li {
  margin-bottom: 4pt;
  text-align: justify;
}

table { 
  width: 100%; 
  border-collapse: collapse; 
  font-size: 13px; 
  margin: 12pt 0; 
}

th, td { 
  border: 1px solid #000000; 
  padding: 6px 8px; 
}

th { 
  background-color: #F2F2F2; 
  color: #1b365d;
  font-weight: bold; 
  text-align: center; 
}

.media-container { 
  width: 100%; 
  margin: 18pt 0; 
  display: flex; 
  flex-direction: column; 
  align-items: center; 
}

.media-container img { 
  max-width: 100%; 
  height: auto; 
  border: 1px solid #D0D0D0; 
}

.caption { 
  font-size: 12px; 
  font-style: italic; 
  text-align: center; 
  margin-top: 6pt; 
  color: #333333; 
}

/* Print and PDF Export Optimization */
@media print {
  body { background-color: #FFFFFF; padding: 0; margin: 0; }
  .word-page { width: 100%; box-shadow: none; padding: 0; }
}
```
