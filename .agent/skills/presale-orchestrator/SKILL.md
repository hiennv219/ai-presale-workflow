---
name: presale-orchestrator
description: Route presale workflow to correct skill based on user input type.
---

# Presale Orchestrator

## Routing Table

| User input | Skill |
| --- | --- |
| Raw customer bullets | `presale-discovery` |
| Answers, notes, Q&A, feedback | `presale-context` |
| Need pain points, scope | `presale-scope` |
| Need tech analysis, no tech decisions in context | `presale-technical` |
| Need delivery plan, tasks | `presale-wbs` |
| Need proposal draft/revision | `presale-proposal` |
| Need review or finalization | `presale-review-finalize` |

## Procedure

1. Identify stage from user intent + available artifacts.
2. Load only that stage's skill.
3. State input used and output produced.
4. Update context before revising artifacts.
5. Flag scope impact before accepting new scope.
6. Recommend next stage.

## Standard Output Format

```
## Stage: {{stage}}
## Input Used: {{input}}
## Output Produced: {{output}}
## Result: {{content}}
## Context Updates: {{updates}}
## Scope Impact: {{none_or_impact}}
## Open Questions: {{questions}}
## Next Stage: {{stage}}
```
