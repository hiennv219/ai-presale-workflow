---
description: Initialize new presale project — create folders, save input, create status.md
---

# /presale-init

## Trigger

On `/presale-run` with customer input, or standalone `/presale-init`.

1. Determine `<client-name>` from user input (ask if unclear).
2. Use current date as `YYYY-MM-DD`.
3. Run steps below.
4. After completion → hand off to `/presale-run` Stage 1.

## Steps

### Step 1: Gather info

- `<client-name>`: lowercase slug, hyphens, no diacritics.
- Customer request content (raw bullets, email, brief, notes).
- Ask if missing.

### Step 2: Create folders

```
projects/YYYY-MM-DD-<client-name>/
├── _source/
├── workspace/
└── _delivery/
```

### Step 3: Write input file

Path: `projects/YYYY-MM-DD-<client-name>/_source/client-input.md`

```markdown
# Client Input
## Source
{{email / meeting / brief / other}}
## Date
{{YYYY-MM-DD}}
## Content
{{raw customer content, unedited}}
```

### Step 4: Create status.md

1. Read `.agent/references/status.md`.
2. Replace placeholders: `[Project Name]`, `[Client]`, `[YYYY-MM-DD]`.
3. Write to `projects/YYYY-MM-DD-<client-name>/status.md`.

## Output

```
Done: projects/YYYY-MM-DD-<client-name>/
  - _source/client-input.md saved
  - status.md created
→ Next: Stage 1 Discovery
```

## Gate

- `_source/`, `workspace/`, and `_delivery/` exist.
- `_source/client-input.md` has content.
- `status.md` has no unresolved placeholders.
