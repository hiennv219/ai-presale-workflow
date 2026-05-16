---
name: presale-proposal
description: Create or revise presale proposal from context, scope, WBS, and risks. Always uses multi-section file structure.
---

# Presale Proposal

## Procedure

1. Reflect customer context and pain points before solution.
2. Use approved scope register.
3. Use WBS summary for implementation plan.
4. Include assumptions, risks, out-of-scope, next steps.
5. Never add deliverables missing from WBS.
6. For sections 4-5: use `workspace/technical.md` if available. If not, derive from scope + context.

## File Structure

All proposals use multi-section structure in `workspace/proposal/`. See [references/proposal-sections.md](../../references/proposal-sections.md).

### Creating

1. Create `workspace/proposal/` folder.
2. Create `_index.md` from [references/proposal-index.md](../../references/proposal-index.md).
3. Write each section to its own file following [references/proposal.md](../../references/proposal.md) structure.
4. Update section status in `_index.md`.

### Revising

1. Read `_index.md` for current state.
2. Read + edit only affected sections.
3. Update version, date, history in `_index.md`.

## Revision Rule

Revise affected sections only. Never regenerate full proposal unless scope/positioning changed significantly.

## Full Export

Only on `/presale-finalize`. Concat sections 01→08, prepend metadata, write `workspace/final-proposal.md`.

## Legacy Compatibility

If an existing project uses the old 13-section format (01-executive-summary.md → 13-next-steps.md), continue working in that format for that project. New projects always use the 8-section format.
