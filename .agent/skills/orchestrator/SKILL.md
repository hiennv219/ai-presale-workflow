---
name: orchestrator
description: Route presale workflow to correct agent and skill based on stage and user input.
---

# Presale Orchestrator

## Stage → Agent → Skill Mapping

| Stage | Agent | Skill |
|-------|-------|-------|
| 1. Discovery | Senior BA | `discovery` |
| 2. Context | Senior BA | `context` |
| 3. Scope | Solution Architect | `scope` |
| 3.5. Technical | Solution Architect | `technical` |
| 4. WBS | Senior PM | `wbs` |
| 5. Proposal | Senior PM | `proposal` |
| 6. Review | Senior PM | `review-finalize` |

## Input-Based Routing (fallback when status.md is missing)

| User input | Skill |
|---|---|
| Raw customer bullets | `discovery` |
| Answers, notes, Q&A, feedback | `context` |
| Need pain points, scope | `scope` |
| Need tech analysis, no tech decisions in context | `technical` |
| Need delivery plan, tasks | `wbs` |
| Need proposal draft/revision | `proposal` |
| Need review or finalization | `review-finalize` |
| Need slide deck from proposal | `slides` |
| Need document translation (EN/JA/VI) | `transale` |

## Routing Procedure (2 levels)

1. Read `workspace/status.md` → determine current stage
2. Map stage → agent (using the table above)
3. Load `agents/<agent>/AGENT.md` (persona + rules)
4. Load `skills/<skill>/SKILL.md` (procedure)
5. Agent executes the skill with Stop/Assume logic
6. Result handling:
   - Stage completed → verify handoff conditions → next stage/agent
   - Stop Rule triggered → load Comm Hub → HOLD
   - Assume Rule triggered → call Assumption Ledger → continue
   - Loop back needed → revert to previous agent

## Handoff Conditions

**BA → SA:**
- `workspace/discovery.md` EXISTS
- `workspace/deal-context.md` EXISTS
- No remaining unanswered Stop Rule questions

**SA → PM:**
- `workspace/pain-scope.md` EXISTS
- Scope register has ≥1 approved in-scope item
- `workspace/technical.md` EXISTS or skip condition met

**PM → Done:**
- Review gate PASS
- `workspace/assumption-ledger.md`: no items with impact=High + status≠Confirmed

## Loop Back Triggers

- SA → BA: scope item does not map to a requirement in deal-context
- PM → SA: WBS task does not map to a scope item, or scope conflict detected
- Any → same agent (retry): client provides answers after HOLD → resume stage

## Standard Output Format

```
## Stage: {{stage}}
## Agent: {{agent}}
## Input Used: {{input}}
## Output Produced: {{output}}
## Result: {{content}}
## Context Updates: {{updates}}
## Scope Impact: {{none_or_impact}}
## Assumptions Created: {{assumptions_or_none}}
## Open Questions: {{questions}}
## Next Stage: {{stage}}
```
