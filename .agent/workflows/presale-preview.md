---
description: Quick preview — concat proposal sections into proposal-full.md without review gate
---

# /presale-preview

## Trigger

User runs `/presale-preview` to read the full proposal as a single file without passing the review gate.

## Behavior

1. Locate active project folder (most recent `projects/YYYY-MM-DD-*`).
2. Verify `workspace/proposal/` directory exists with at least 1 section file.
   - If not → report "No proposal sections found yet", stop.
3. Run: `python3 scripts/presale_cli.py --project <project_path> --concat`
4. Report output path and word count.

## Output

```
Preview generated:
  - workspace/proposal-full.md ({{word_count}} words, {{section_count}} sections)

Note: This is a working draft — not finalized. Run /presale-finalize after review gate passes.
```

## Rules

- No gate required. This is a convenience command for reading/reviewing.
- Does NOT update status.md or mark anything as Done.
- Does NOT trigger review checks.
- Overwrites previous proposal-full.md if it exists.
