---
description: Export styled PDF from proposal or WBS
---

# /presale-export-pdf [file-name]

Convert a finalized document to styled PDF via HTML intermediate.

## Prerequisites

1. Resolve target:
   - No argument → export all HTML files in `_delivery/`
   - Name provided (e.g. `final-proposal`) → target that specific file
2. HTML file must exist in `_delivery/`. If not, run `/presale-export` first automatically.
3. Node.js available on system.

## Steps

1. Determine project path (most recent in `projects/` or from context).
2. Check if target HTML exists in `<project>/_delivery/`:
   - If not, run the export step first: `python .agent/scripts/presale_cli.py --export --project <project_path>`
3. Run PDF conversion:
   ```bash
   python .agent/scripts/presale_cli.py --pdf --project <project_path>
   ```
   Or for a single file:
   ```bash
   node .agent/scripts/html-to-pdf.js <project>/_delivery/<name>.html <project>/_delivery/<name>.pdf
   ```
4. Confirm output file exists and report size.

## Dependencies

- `puppeteer` (auto-installed if missing)
- `.agent/scripts/html-to-pdf.js`

## Output

```
Exported PDF:
  - {{output_pdf_path}} ({{file_size}})
```
