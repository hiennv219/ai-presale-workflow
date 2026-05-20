---
description: Presale pipeline — raw input to Final Proposal + Final WBS
---

# /presale-run

## Trigger

1. Load `.agent/rules.md` (once per session).
2. Load orchestrator routing table.
3. Locate active project folder (most recent `projects/YYYY-MM-DD-*`).
4. Check `_source/client-input.md` has real content (not just template placeholders).
   - If empty/template-only AND user provided content inline (in the same message as `/presale-run`) → write that content to `_source/client-input.md`, then continue.
   - If empty/template-only AND no inline content → ask user to paste content now (accept in chat). Write response to `_source/client-input.md`, then continue.
   - Do NOT stop and tell user to open the file manually.
5. Resume at next logical stage if prior artifacts exist.
6. End each stage: state next stage, wait for user confirm.
7. Save output → `projects/YYYY-MM-DD-<client>/workspace/<stage>.md`.

## Stages

| # | Skill | In | Out | Gate |
|---|---|---|---|---|
| 1 | [discovery](../skills/discovery/SKILL.md) | Raw bullets, notes | Intake summary, confirmed facts, missing info, questions (3 opts, 1 rec) | Unknowns visible; no assumption as fact |
| 2 | [context](../skills/context/SKILL.md) | Answers, notes, Q&A, feedback | Updated deal context, decisions/assumptions/risks, change log | New info classified; scope-impact flagged |
| 3 | [scope](../skills/scope/SKILL.md) | Context, confirmed requirements, constraints | Pain points, solution direction, in/out/future scope, risks | Every item maps to requirement/decision/assumption |
| 3.5 | [technical](../skills/technical/SKILL.md) | Approved scope, constraints, NFRs | Architecture diagram, tech stack, tech decisions (proposed) | Optional — skip if tech in context |
| 4 | [wbs](../skills/wbs/SKILL.md) | Approved scope, solution direction, constraints | WBS draft, milestones, delivery assumptions | Every WBS item maps to in-scope |
| 5 | [proposal](../skills/proposal/SKILL.md) | Context, pain points, scope, WBS, risks | Proposal draft (multi-section) | Proposal scope = WBS scope |
| 6 | [review-finalize](../skills/review-finalize/SKILL.md) | Context, proposal, WBS, open questions | Review findings OR finalization approval | No critical open question; proposal ↔ WBS consistent |
