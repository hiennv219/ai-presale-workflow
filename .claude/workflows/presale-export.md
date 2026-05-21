---
description: Export any Markdown file as styled HTML
---

# /presale-export <file-name-or-path>

Convert a Markdown file to styled, print-ready HTML.

## Prerequisites

1. Resolve target file path:
   - Name only (e.g. `backlog-questions`) → `workspace/backlog-questions.md`
   - Full path → use as-is
2. File must exist and be non-empty.

If not met → report what's missing, do NOT export.

## Steps

1. Read the target `.md` file.
2. Resolve project root path dynamically based on target file location.
3. Output path: place `.html` in `_delivery/` of the same project (create if needed).
4. Asset synchronization: If a `workspace/assets/` directory exists in the project root, copy it to `_delivery/assets/` to ensure relative image paths work in the exported HTML.
5. Convert markdown to HTML body: `npx marked <target_file>`.
6. Read `references/designs/export-template.html`. Replace `{{title}}` with document heading, `{{body}}` with converted HTML.
7. Write final HTML to output path.
8. Open in browser for preview.

## Dependencies

- `npx marked` (auto-installed via npx)

## Output

```
Exported:
  - {{output_html_path}} ({{file_size}})
  - Opened in browser for preview
```
