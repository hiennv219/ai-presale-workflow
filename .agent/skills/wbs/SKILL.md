---
name: wbs
description: Create or revise WBS from approved scope with phases, tasks, estimates, and traceability.
---

# Presale WBS

## Procedure

1. Use approved in-scope items only.
2. Decompose using 4-level structure (Category → Module → Function → Sub-function).
3. Fill WBS table with: description, note (user story / business logic).
4. Build Dependencies table separately.
5. Flag any task not mapped to approved scope.

## 4-Level Decomposition

| Level | Meaning | Example |
| --- | --- | --- |
| Level 1 | Category — major functional group | Common, Investor, Admin, Integrations |
| Level 2 | Module — business module | Authentication, Secondary Marketplace |
| Level 3 | Function — specific feature | Sign-in, Signup, Create Package |
| Level 4 | Sub-function — atomic action | Email registration, Social login (Google) |

Principle: never stop at Level 2 or 3 if a feature has multiple steps, inputs, or states.

## Rules

- No out-of-scope items.
- Estimate as range if detail incomplete.
- Mark customer dependencies explicitly.
- Trace every item to scope reference.
- **Table format** — Must use the 7-column table from `wbs.md` template, no custom formats.
- **Note = User Story** — Note column must contain a specific User Story or Business Logic, not generic descriptions.
- **No CRUD bundling** — View list, Filter, Search, Create, Edit, Delete must each be a separate row.
- **Atomic line items** — Each distinct action/state = 1 row in WBS.

## Consistency Rules (Rule #10)

- **Scope Coverage Check**: After building WBS, verify every `S-{n}` from the approved In-Scope register has at least 1 WBS task referencing it. List any orphan scope items — these indicate incomplete WBS coverage.
- **Role Registry**: After building WBS, extract the unique set of `Owner Role` values across all tasks. Output this as a **Role Registry** list at the bottom of the WBS. This becomes the definitive list of roles that MUST appear in Proposal Section 7.1 (Resource Allocation table).
- **Milestone-WBS Mapping**: Each milestone's "Key Deliverables" must map to specific WBS IDs. No milestone can reference deliverables that don't exist as WBS tasks. No WBS task can be unassigned to a milestone.

## Output

Use [references/wbs.md](../../references/wbs.md).
