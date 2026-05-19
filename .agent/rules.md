# Presale Rules

## Input/Output

- State input used and output produced for every stage.
- Separate facts, assumptions, recommendations, open questions, decisions.
- Ask for clarification when required input is missing.
- Never convert unconfirmed info into confirmed requirement.

## Clarification Questions

- Exactly 3 options per question.
- Exactly 1 recommended option with short reason.
- State why answer matters for scope/WBS/proposal/timeline/cost/risk.

## Assumptions vs Questions

- Discovery stage must NOT push items directly into Assumptions without asking the client first.
- Process: ask client → if no response → convert to assumption (note "asked, no response received").
- Exception: Pure technical details (caching strategy, message queue choice, internal tooling) can be assumed directly.
- High-impact technical decisions (rewrite vs upgrade, platform choice, architecture pattern) MUST be asked first.
- Every item in Assumptions must either (a) have been asked with no response, or (b) be a pure technical detail with no significant impact on scope/effort.

## Conditional Sections

- Section 5.1 (AS-IS Architecture) and 5.3 (Migration Strategy) only appear when client has an existing system (brownfield).
- If client is building from scratch (greenfield): remove 5.1 AS-IS and 5.3 Migration, renumber remaining sections.
- For greenfield: Technical Solutions section starts directly with Target Architecture.
- Determine brownfield/greenfield during Discovery based on client input.
- For greenfield, AS-IS and Migration are meaningless — they only create noise in the proposal.

## Scope Control

- Every scope item must map to confirmed requirement, decision, or accepted assumption.
- Scope-change candidates: new user groups, platforms, integrations, reports, AI, migration, compliance, timeline, support.
- Scope changes require impact check before acceptance.
- Out-of-scope and future-phase must be explicit.

## Consistency

- Proposal and WBS must use same scope.
- WBS must not contain out-of-scope work.
- Proposal must not promise deliverables missing from WBS.
- Risks/assumptions consistent across artifacts.
- Final artifacts require finalization review.

## Language Guardrail

- Output language follows client input language (VIE → VIE, ENG → ENG).
- Do not mix languages within the same artifact.
- Maintain professional, consistent tone throughout.

## Think-Before-Act

- Must output [THINKING] or [PLAN] before creating/regenerating long artifacts.
- User reviews direction before AI generates.
- Applies to: proposal, WBS, slide deck, technical solution.

## Token Discipline

- Use compact deal context, not full chat history.
- Keep only: active facts, decisions, assumptions, risks, open questions, scope register, artifact summaries.
- Store history as change log or event summary.
- Revise affected sections, never regenerate entire artifacts.
