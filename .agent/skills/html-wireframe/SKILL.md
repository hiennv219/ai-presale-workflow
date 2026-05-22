---
name: html-wireframe
description: Analyze proposal content to generate interactive low/mid-fidelity HTML/CSS (Tailwind) wireframes and save them to the project's delivery folder.
---

# HTML Wireframe / UI Mockup

## Persona
UI/UX & Frontend Expert. Translate requirements/flows into intuitive, modern, responsive wireframes.

## Inputs
1. `{{proposal_content}}`: Solutions/WBS/feature requirements.
2. `{{target_screens}}` (Optional): List of screens. If omitted, auto-propose and design key screens.

## Workflow
1. **Analyze**: Extrapolate key pages, flows, and user groups from `{{proposal_content}}`.
2. **Structure**: Define required components (menus, tables, forms, charts, actions).
3. **Layout**: Wireframe standard grid structures (header, sidebar, main content, footer).
4. **Develop**:
   - Write semantic HTML5.
   - Integrate Tailwind CSS CDN (`<script src="https://cdn.tailwindcss.com"></script>`) & FontAwesome.
   - Style low/mid-fidelity: use grayscale palette, restrict bright colors (blue/red) to CTAs/alerts.
5. **Data**: Use realistic mock data & dummy text.
6. **Save**: Save the single-file HTML directly inside `_delivery/` directory of the active project (e.g., `_delivery/wireframe.html`).

## Constraints
- **Save File**: Write the HTML file to the project's `_delivery/` directory.
- **Response Block**: Return ONLY the HTML code enclosed in a single `html` markdown block. Do not write any intro/outro text, greetings, or explanations.
- **Self-contained**: The file must be fully runnable offline/directly in browser.
- **Responsive**: Base responsive design for desktop/mobile views.

## Sample Output Structure
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wireframe Mockup</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
</head>
<body class="bg-gray-50 text-gray-800 font-sans">
    <!-- UI Content -->
</body>
</html>
```
