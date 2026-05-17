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

## Assumptions Rule

- Default: ASK first, assume later. Every item that affects scope/effort/timeline must be a Question before it can become an Assumption.
- Exception: Minor technical details (caching strategy, internal tooling, library choices) that don't significantly impact scope/cost may be assumed directly to avoid overwhelming non-tech clients.
- High-impact technical decisions (rewrite vs upgrade, platform choice, architecture pattern, DB strategy) MUST be asked even if client is non-tech.
- When promoting unanswered questions to assumptions, mark them: "Asked [date], no response → assumed [value]".

## Missing Info Checklist

Business goal, target users, current workflow, desired workflow, systems/integrations, data sources, reports/dashboards, roles/permissions, security/compliance, timeline, budget, success criteria, support/maintenance.

## Question Format

Use [references/backlog-questions.md](../../references/backlog-questions.md) for question format and the standalone client-facing file.

Prioritize questions that reduce delivery risk or scope ambiguity.

## Sync Rules

- `discovery.md` keeps questions inline for context (next to missing info/assumptions).
- `backlog-questions.md` is the single source of truth for question status (open/answered).
- When client answers → move question to "Answered" in backlog + update discovery (confirmed facts, assumptions, missing info) as needed.
