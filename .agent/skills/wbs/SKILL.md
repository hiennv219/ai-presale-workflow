---
name: wbs
description: Create or revise WBS from approved scope with phases, tasks, estimates, and traceability.
---

# Presale WBS

## Procedure

1. Use approved in-scope items only.
2. Group into delivery phases.
3. Break each phase into tasks with: deliverable, owner role, dependency, assumption, estimate range, acceptance criteria, scope ref.
4. Flag any task not mapped to approved scope.

## Rules

- No out-of-scope items.
- Estimate as range if detail incomplete.
- Mark customer dependencies explicitly.
- Trace every item to scope reference.

## Consistency Rules (Rule #10)

- **Scope Coverage Check**: After building WBS, verify every `S-{n}` from the approved In-Scope register has at least 1 WBS task referencing it. List any orphan scope items — these indicate incomplete WBS coverage.
- **Role Registry**: After building WBS, extract the unique set of `Owner Role` values across all tasks. Output this as a **Role Registry** list at the bottom of the WBS. This becomes the definitive list of roles that MUST appear in Proposal Section 7.1 (Resource Allocation table).
- **Milestone-WBS Mapping**: Each milestone's "Key Deliverables" must map to specific WBS IDs. No milestone can reference deliverables that don't exist as WBS tasks. No WBS task can be unassigned to a milestone.

## Output

Use [references/wbs.md](../../references/wbs.md).
