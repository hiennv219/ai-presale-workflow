---
description: Unified export — preview, finalize, HTML, PDF, and slides in one command
---

# /presale-export

## Trigger

User runs `/presale-export` with optional flags:
- `/presale-export` — interactive (asks what to export)
- `/presale-export --preview` — quick preview only (no finalization)
- `/presale-export --final` — run review gate + finalize + HTML export
- `/presale-export --slides` — generate slide deck Markdown
- `/presale-export --pdf` — finalize + PDF export
- `/presale-export --all` — finalize + HTML + PDF + slides
- `/presale-export <file-name>` — export specific file to HTML (e.g. `backlog-questions`, `wbs`)

## Step 0: Locate Project

1. Locate active project folder (most recent `projects/YYYY-MM-DD-*`).
2. Verify `workspace/proposal/` exists with at least 1 section file.
   - If not → report "No proposal sections found yet", stop.

## Mode: Preview (`--preview` or no flag + user chooses preview)

Quick concat without review gate:

1. Run: `python3 .agent/scripts/presale_cli.py --project <project_path> --concat`
2. Report output path and word count.
3. Does NOT update status.md or trigger review.

Output:
```
Preview generated:
  - workspace/proposal-full.md ({{word_count}} words, {{section_count}} sections)

This is a working draft. Use /presale-export --final when ready to finalize.
```

## Mode: Finalize (`--final`, `--pdf`, `--all`)

### Step 1: Review Gate

Delegate to [orchestrator](../skills/orchestrator/SKILL.md) → `review-finalize` skill.

Verify:
1. All sections in `workspace/proposal/_index.md` have status Done.
2. No critical open questions.
3. No pending unapproved scope changes.
4. Assumption Ledger: no High impact unconfirmed.

If not met → report findings table, do NOT export. User must fix via `/presale-update`.

### Step 2: Generate Final Files

1. Detect section format from `workspace/proposal/_index.md`.
2. Write/update `workspace/final-proposal.md`:
   - If file does NOT exist: concat all sections, prepend final metadata (version=final, date).
   - If file ALREADY exists: only replace section(s) that changed.
   - Path Fix: Replace `../assets/` with `assets/` for image paths.
3. Write `workspace/final-wbs.md` (from `workspace/wbs.md` + final metadata).
4. Update `status.md`: mark Final Proposal + Final WBS as Done.

### Step 3: Export to Format

**HTML** (default for `--final` and `--all`):
1. Run: `python3 .agent/scripts/presale_cli.py --project <project_path> --export`
2. Asset sync: copy `workspace/assets/` → `_delivery/assets/` if exists.
3. Output: `_delivery/final-proposal.html`, `_delivery/final-wbs.html`

**PDF** (`--pdf` or `--all`):
1. Run: `python3 .agent/scripts/presale_cli.py --project <project_path> --pdf`
2. Output: `_delivery/final-proposal.pdf`

### Step 4: Open in browser for preview.

## Mode: Slides (`--slides` or `--all`)

1. Read proposal content (final-proposal.md or concat sections).
2. Read `workspace/context.md` for client/project name.
3. Load skill: `.agent/skills/slides/SKILL.md`.
4. Generate `workspace/slides.md`.

Output:
```
Slides generated:
  - workspace/slides.md ({{slide_count}} slides)

Ready to copy into GPT / Gemini for visual slide generation.
```

## Mode: Single File (`/presale-export <file-name>`)

Export any workspace Markdown file to styled HTML:

1. Resolve path: name only (e.g. `backlog-questions`) → `workspace/backlog-questions.md`.
2. Convert: `npx marked <target_file>`.
3. Apply template: `references/designs/export-template.html`.
4. Output: `_delivery/<file-name>.html`.
5. Open in browser.

## Interactive Mode (no flags)

Ask user:
```
What would you like to export?
1. Preview (quick draft concat, no review)
2. Final proposal + WBS (review gate → HTML)
3. Slides (Markdown for GPT/Gemini)
4. Everything (final + HTML + PDF + slides)
5. Specific file (backlog-questions, wbs, etc.)
```

## Reusable CLI Script

```bash
python3 .agent/scripts/presale_cli.py --project projects/{{project-dir}} --all
python3 .agent/scripts/presale_cli.py --project projects/{{project-dir}} --concat
python3 .agent/scripts/presale_cli.py --project projects/{{project-dir}} --export
python3 .agent/scripts/presale_cli.py --project projects/{{project-dir}} --pdf
```
