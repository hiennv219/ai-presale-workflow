# AI Presale Workflow

Markdown skill workspace — not a software app.
Skills: `.agent/` | Artifacts: `projects/` | Pipeline: Discovery → Context → Scope → Technical → WBS → Proposal → Review

## Slash Commands

READ the corresponding `.agent/workflows/<name>.md` BEFORE executing:

| Command | Action |
|---|---|
| `/presale-run` | Start new deal (auto-init) or resume pipeline → proposal + WBS |
| `/presale-update` | Revise any section from feedback, scope changes, or corrections |
| `/presale-export` | Preview, finalize, HTML/PDF/slides — all output in one command |

## Load Order

1. Read `.agent/rules.md`
2. Read `.agent/workflows/presale-run.md`
3. Use `.agent/skills/orchestrator/SKILL.md` to route to the correct skill
4. Load only the current stage's skill
5. Use `.agent/references/` only when producing that artifact

## Routing

| User Input | Skill |
|---|---|
| Raw customer bullets, briefs, emails | `discovery` |
| Answers, notes, Q&A, feedback | `context` |
| Pain points or scope definition | `scope` |
| Delivery plan or task breakdown | `wbs` |
| Proposal draft or revision | `proposal` |
| Review or finalization | `review-finalize` |
| Document translation (EN/JA/VI) | `transale` |

Agent details: [.agent/README.md](.agent/README.md)

## Core Contract

After each stage, state: current stage, input used, output produced, context updates, scope impact, open questions, next stage.

## Non-Negotiables

- Do not invent customer facts.
- Do not silently expand scope.
- Do not let proposal and WBS drift apart.
- Revise sections, not full artifacts.
- No final output until finalization review passes.
