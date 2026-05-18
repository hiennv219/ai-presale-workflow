---
description: Generate presentation slide deck from finalized proposal
---

# /presale-deck <project-path>

Generate a Marp slide deck from a finalized proposal.

## Prerequisites

1. Resolve project path (e.g. `projects/2026-05-16-dailytools`).
2. `workspace/final-proposal.md` must exist and be non-empty.

If not met → report what's missing, do NOT generate.

## Steps

1. Read `workspace/final-proposal.md`.
2. Load skill: `.agent/skills/slide-deck/SKILL.md`.
3. Extract key content per slide (follow skill's Slide Structure table).
4. Write `workspace/slide-deck.md` in Marp format.
5. Export to HTML: `npx @marp-team/marp-cli workspace/slide-deck.md -o _delivery/slide-deck.html`.
6. Open in browser for preview.

## Dependencies

- `npx @marp-team/marp-cli` (auto-installed via npx)

## Output

```
Generated:
  - workspace/slide-deck.md (source)
  - _delivery/slide-deck.html (presentation)
  - Opened in browser for preview
```
