---
name: discovery
description: Normalize raw customer input and generate clarification questions for presale discovery.
---

# Presale Discovery

## Procedure

1. Summarize raw input without adding unsupported facts.
2. Extract confirmed facts (explicitly stated by client).
3. Identify missing info affecting scope/WBS/proposal/timeline/cost/risk.
4. Generate clarification questions: 3 options, 1 recommendation each.
5. Output questions to both `discovery.md` (inline) and `backlog-questions.md` (standalone, client-facing).
6. Only after questions are posed and unanswered → promote to assumptions.

## Output Files

- `workspace/discovery.md` — full analysis (internal)
- `workspace/backlog-questions.md` — questions only, grouped by Open/Answered (client-facing)

## Assumptions

Follow Stop/Assume rules from `agents/senior-ba/AGENT.md`. When promoting unanswered questions to assumptions: mark as "Asked [date], no response → assumed [value]" and record in Assumption Ledger.

## Missing Info Checklist

Business goal, target users, current workflow, desired workflow, systems/integrations, data sources, reports/dashboards, roles/permissions, security/compliance, timeline, budget, success criteria, support/maintenance.

## Question Format

Use [references/backlog-questions.md](../../references/backlog-questions.md) for question format and the standalone client-facing file.

Prioritize questions that reduce delivery risk or scope ambiguity.

## Sync Rules

- `discovery.md` keeps questions inline for context (next to missing info/assumptions).
- `backlog-questions.md` is the single source of truth for question status (open/answered).
- When client answers → move question to "Answered" in backlog + update discovery (confirmed facts, assumptions, missing info) as needed.

## Deal Complexity Classification

After completing discovery analysis, classify the deal complexity based on confirmed facts:

| Signal | Light | Standard | Enterprise |
|--------|-------|----------|------------|
| Modules/features | 1-3 | 4-10 | 10+ |
| Platforms | 1 | 2 | Multi + admin |
| Integrations | 0-1 | 2-4 | 5+ or legacy |
| User roles | 1-2 | 3-5 | 5+ complex RBAC |
| Compliance | None | Basic | Required (PCI, HIPAA, SOC2) |
| Migration | None | Maybe | Required (brownfield) |

**Output** (append to discovery.md):

```
## Deal Complexity: {{Light / Standard / Enterprise}}

Reasoning: {{1-2 sentences citing signals above}}

Recommended pipeline adjustments:
- {{list of skips or additions}}
```

**Pipeline adjustments by profile:**

- **Light**: Skip Stage 3.5 (Technical). WBS uses 3-level decomposition (Category → Module → Function). Skip wireframe in proposal.
- **Standard**: Run all stages as normal. WBS uses 4-level decomposition.
- **Enterprise**: Run all stages. Add Compliance/Security and Migration sections to proposal. WBS uses 4-level decomposition.

Present classification to user for confirmation before proceeding to next stage.
