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

Principle: never stop at Level 2. **Minimum decomposition is Level 3** (Category → Module → Function).

- **Light deals**: Use 3-level (stop at Function). Only go to Level 4 if a function has genuinely distinct sub-steps.
- **Standard/Enterprise deals**: Use full 4-level. Never stop at Level 3 if a feature has multiple steps, inputs, or states.

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

After building WBS, create `workspace/checklist.md` (use [references/checklist.md](../../references/checklist.md) template). This file is internal only — never included in client-facing exports.

First pass (Stage 4) — fill these checks:
- **Scope Coverage**: every `S-{n}` from In-Scope register has at least 1 WBS task.
- **Role Registry**: extract unique roles from WBS.
- **Milestone-WBS Mapping**: every WBS task assigned to a milestone, no orphans.

Leave checks 4 and 5 (Cross-Artifact Consistency) as "—" — they will be completed at Stage 6 (Review).

These checks do NOT appear in the WBS artifact itself.

## Output

Use [references/wbs.md](../../references/wbs.md).
