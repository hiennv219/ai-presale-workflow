---
description: Presale pipeline — raw input to Final Proposal + Final WBS
---

# /presale-run

## Trigger

1. Load `.agent/rules.md` (once per session).
2. Load orchestrator routing table.
3. If user provided input → run `presale-init` → Stage 1.
4. If no input → ask user to paste customer request, then run `presale-init`.
5. Resume at next logical stage if prior artifacts exist.
6. End each stage: state next stage, wait for user confirm.
7. Save output → `projects/YYYY-MM-DD-<client>/workspace/<stage>.md`.

## Stages

| # | Skill | In | Out | Gate |
|---|---|---|---|---|
| 1 | [presale-discovery](../skills/presale-discovery/SKILL.md) | Raw bullets, notes | Intake summary, confirmed facts, missing info, questions (3 opts, 1 rec) | Unknowns visible; no assumption as fact |
| 2 | [presale-context](../skills/presale-context/SKILL.md) | Answers, notes, Q&A, feedback | Updated deal context, decisions/assumptions/risks, change log | New info classified; scope-impact flagged |
| 3 | [presale-scope](../skills/presale-scope/SKILL.md) | Context, confirmed requirements, constraints | Pain points, solution direction, in/out/future scope, risks | Every item maps to requirement/decision/assumption |
| 3.5 | [presale-technical](../skills/presale-technical/SKILL.md) | Approved scope, constraints, NFRs | Architecture diagram, tech stack, tech decisions (proposed) | Optional — skip if tech in context |
| 4 | [presale-wbs](../skills/presale-wbs/SKILL.md) | Approved scope, solution direction, constraints | WBS draft, milestones, delivery assumptions | Every WBS item maps to in-scope |
| 5 | [presale-proposal](../skills/presale-proposal/SKILL.md) | Context, pain points, scope, WBS, risks | Proposal draft (multi-section) | Proposal scope = WBS scope |
| 6 | [presale-review-finalize](../skills/presale-review-finalize/SKILL.md) | Context, proposal, WBS, open questions | Review findings OR finalization approval | No critical open question; proposal ↔ WBS consistent |
