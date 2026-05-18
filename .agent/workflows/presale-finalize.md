---
description: Export Final Proposal and Final WBS — user-triggered only
---

# /presale-finalize

## Prerequisites

Before export, verify:
1. All sections in `workspace/proposal/_index.md` have status Done.
2. No critical open questions.
3. No pending unapproved scope changes.

If not met → report what's missing, do NOT export.

## Steps

1. Detect format:
   - Read `workspace/proposal/_index.md`.
   - If sections are 01→07 (newest format): concat 01→07.
   - If sections are 01→08 (mid format): concat 01→08.
   - If sections are 01→13 (legacy format): concat 01→13.
2. Write or update `workspace/final-proposal.md`:
   - **If file does NOT exist**: concat all sections, prepend final metadata (version=final, date).
   - **If file ALREADY exists**: only replace the section(s) that changed. Find heading boundary (e.g. `## 5.` → `## 6.`) and replace that range with new content from the corresponding section file. Do NOT re-concat all files.
   - **Path Fix**: Replace any `../assets/` string with `assets/` so image paths render correctly in the combined file.
3. Write `workspace/final-wbs.md` (from `workspace/wbs.md` + final metadata).
4. Update `status.md`: mark Final Proposal + Final WBS as Done.

## Reusable Automation Script (Recommended)

To save thousands of LLM context tokens and prevent manual errors, a Python script is available at `.agent/scripts/presale_helper.py`.

Run this script to automatically execute proposal concatenation, WBS finalization, and styled HTML/Marp slide-deck compilation for any project:
```bash
# To run all steps (concat, wbs, and html/marp export):
python3 .agent/scripts/presale_helper.py --project projects/{{project-dir}} --all

# To run specific steps:
python3 .agent/scripts/presale_helper.py --project projects/{{project-dir}} --concat
python3 .agent/scripts/presale_helper.py --project projects/{{project-dir}} --wbs
python3 .agent/scripts/presale_helper.py --project projects/{{project-dir}} --export
```

## Output

```
Exported:
  - workspace/final-proposal.md ({{word_count}} words)
  - workspace/final-wbs.md
  - status.md updated
```
