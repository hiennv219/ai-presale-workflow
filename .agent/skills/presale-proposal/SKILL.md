---
name: presale-proposal
description: Create or revise presale proposal from context, scope, WBS, and risks. Always uses multi-section file structure.
---

# Presale Proposal

## Procedure

1. Reflect customer context and pain points before solution.
2. Use approved scope register. Ensure features are grouped by MoSCoW priority, and include the generated Mermaid User Flow and High-Level Wireframe descriptions.
3. For new features or greenfield projects: include User Flow in section 2.3 with Mermaid diagram + short description explaining the flow. Skip for upgrade-only projects with no logic changes.
4. Use WBS summary for implementation plan.
5. Include assumptions, risks, out-of-scope, next steps.
6. Never add deliverables missing from WBS.
7. For section 4: use `workspace/technical.md` if available. If not, derive from scope + context. Ensure 3rd-Party Services and Pass-through Costs are explicitly detailed.

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

Only on `/presale-finalize`. Concat sections 01→07, prepend metadata, write `workspace/final-proposal.md`.

## Legacy Compatibility

If an existing project uses the old 13-section format or 8-section format, continue working in that format for that project. New projects always use the 7-section format.
