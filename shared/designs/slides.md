# DESIGN SPECIFICATIONS

## 1. Layout Overview
* **Aspect Ratio**: 16:9 (Standard widescreen presentation - Equivalent to base resolution `1920x1080` or `1280x720`).
* **Grid System**: 12-column flexible grid system.
* **Common Layouts**:
    * *Two-Column (50-50 or 60-40)*: Flexbox `flex-row` or Grid `grid-cols-2`. One side for charts, the other for text blocks.
    * *Multi-Column Grid*: `grid-cols-3` or `grid-cols-4` for concise data categories (e.g., planet names: Mercury, Venus, Mars...).
* **Content Flow**:
    * *Header*: Top-left corner (Slide Title).
    * *Body (Main Content)*: Centered, occupying 70-80% of the area, containing charts and metrics.
    * *Footer*: Bottom edge (usually right-aligned), containing the copyright text *"This template has been created by Slidesgo"*.

## 2. Color Palette
Monochromatic blue palette for a professional, analytical, and tech-driven feel.


| Element | HEX Code | Role / Application |
| :--- | :--- | :--- |
| **Main Background** | `#FFFFFF` | Slide background. |
| **Data 1 (Darkest)** | `#2A3A93` | High-priority data, Period 1. |
| **Data 2 (Medium)** | `#4B65FF` | Secondary data, Period 2. |
| **Data 3 (Light)** | `#A3B5FF` | Muted data, Period 3. |
| **Data 4 (Very Light)** | `#DCE4FF` | Chart background or minor data bars. |
| **Primary Text** | `#202124` | Titles (H1, H2), emphasized text. |
| **Secondary Text** | `#5F6368` | Body text, chart X/Y axis labels. |
| **Borders & Gridlines** | `#E0E0E0` | Coordinate axes, divider lines. |

## 3. Typography
Neo-Grotesque Sans-serif font family, clean and readable (Recommended: **Inter** or **Roboto** for web use).

*Note: Sizes below are converted based on a 16px web base font.*

* **Main Title (Slide Title / H1)**:
    * `font-family`: Inter, sans-serif
    * `font-size`: 2.25rem (36px)
    * `font-weight`: 700 (Bold)
    * `line-height`: 1.2
    * `letter-spacing`: -0.02em
* **Block Title / Category Name (H2 / H3)**:
    * `font-family`: Inter, sans-serif
    * `font-size`: 1.125rem (18px) - 1.25rem (20px)
    * `font-weight`: 600 (Semi-Bold)
    * `line-height`: 1.4
* **Body Text**:
    * `font-family`: Inter, sans-serif
    * `font-size`: 0.875rem (14px)
    * `font-weight`: 400 (Regular)
    * `line-height`: 1.5
* **Captions / Axis Labels / Footer (Small Text)**:
    * `font-family`: Inter, sans-serif
    * `font-size`: 0.75rem (12px)
    * `font-weight`: 400 (Regular)
    * *Note*: Footer text can be italicized depending on the style.

## 4. Component Specifications
* **Header Block**:
    * Left-aligned (`text-align: left`).
    * Spacing from top and left of the slide: 40px (2.5rem).
* **Chart Gridlines**:
    * Horizontal lines: `border-bottom: 1px solid #E0E0E0`.
    * Vertical chart gridlines (Y-axis) are usually HIDDEN, keeping text labels only.
* **Bar Chart Items**:
    * Sharp corners: `border-radius: 0px` (Some variations use a subtle 2px radius, but the core design is flat and sharp).
    * No `box-shadow`.
* **Legend**:
    * Displayed via Flexbox (`display: flex; align-items: center; justify-content: center`).
    * Color square indicators: `width: 16px; height: 16px; border-radius: 2px`. Gap between the color block and text is 8px.
* **Text Blocks**:
    * Vertical layout (`flex-col`).
    * Block titles (e.g., "Mercury") use a `gap: 4px` or `margin-bottom: 8px` before the description text below.

## 5. Spacing System
All spacing values are multiples of 8px or 4px.

* **Safe Slide Padding**: 40px (Top/Bottom) and 48px (Left/Right), equivalent to `py-10 px-12`.
* **Main Title Margin-Bottom**: Distance from "Bar Graph Infographics" to content: 32px (`2rem` / `mb-8`).
* **Column Gap**: 32px to 48px (`gap-8` to `gap-12`) depending on content density.
* **Row Gap (Text Lists)**: 24px (`gap-6`).
