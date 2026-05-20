---
description: Initialize new presale project — only needs project name, auto-creates all folders and files
---

# /presale-init

## Trigger

User runs `/presale-init` or `/presale-init <project-name>`.

## Behavior

1. Ask for `<project-name>` if not provided inline.
2. Convert to slug: lowercase, hyphens, no diacritics.
3. Use current date as `YYYY-MM-DD`.
4. Auto-create all folders and files (no further questions).
5. Inform user to fill `_source/client-input.md` manually before running `/presale-run`.

## Steps

### Step 1: Create folder structure

```
projects/YYYY-MM-DD-<project-name>/
├── _source/
├── workspace/
└── _delivery/
```

### Step 2: Write client-input.md template

Path: `projects/YYYY-MM-DD-<project-name>/_source/client-input.md`

```markdown
# Client Input

## Source
<!-- email / meeting / brief / other -->

## Date
YYYY-MM-DD

## Content
<!-- Paste raw customer content here: email, brief, meeting notes, etc. -->

```

### Step 3: Create status.md

1. Read `.agent/references/status.md`.
2. Replace placeholders: `[Project Name]` → project name, `[Client name]` → project name, `[YYYY-MM-DD]` → date.
3. Update progress: uncheck "Received client input" (user hasn't filled it yet).
4. Write to `projects/YYYY-MM-DD-<project-name>/status.md`.

## Output

```
✓ Project initialized: projects/YYYY-MM-DD-<project-name>/

Structure:
  _source/client-input.md  ← customer info goes here
  workspace/               ← artifacts will go here
  _delivery/               ← final exports

→ Next: Run /presale-run and paste customer input directly, or fill _source/client-input.md first
```

## Gate

- `_source/`, `workspace/`, and `_delivery/` exist.
- `_source/client-input.md` exists (template is enough).
- `status.md` has no unresolved placeholders.

## Important

- Do NOT ask for customer content during init.
- Do NOT ask additional questions beyond project name.
- User can fill `client-input.md` in their editor OR paste directly when running `/presale-run`.
