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

## Input-Based Routing (fallback khi không có status.md)

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

## Routing Procedure (2 tầng)

1. Đọc `workspace/status.md` → xác định current stage
2. Map stage → agent (bảng trên)
3. Load `agents/<agent>/AGENT.md` (persona + rules)
4. Load `skills/<skill>/SKILL.md` (procedure)
5. Agent chạy skill với Stop/Assume logic
6. Kết quả:
   - Stage hoàn thành → kiểm tra handoff conditions → next stage/agent
   - Stop Rule triggered → load Comm Hub → HOLD
   - Assume Rule triggered → gọi Assumption Ledger → tiếp tục
   - Loop back needed → quay lại agent trước

## Handoff Conditions

**BA → SA:**
- `workspace/discovery.md` EXISTS
- `workspace/deal-context.md` EXISTS
- Không còn Stop Rule question chưa trả lời

**SA → PM:**
- `workspace/pain-scope.md` EXISTS
- Scope register có ≥1 approved in-scope item
- `workspace/technical.md` EXISTS hoặc skip condition met

**PM → Done:**
- Review gate PASS
- `workspace/assumption-ledger.md`: không có impact=High + status≠Confirmed

## Loop Back Triggers

- SA → BA: scope item không map về requirement trong deal-context
- PM → SA: WBS task không map về scope item, hoặc scope conflict detected
- Any → same agent (retry): khách trả lời sau HOLD → resume stage

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
