# Presale Rules

## 1. Separate facts from assumptions

- Classify every piece of information as: **fact**, **assumption**, **decision**, or **open question**.
- Never promote unconfirmed information to a requirement.
- An assumption may only be created when: (a) the client was asked and did not respond, or (b) it is a pure technical detail with no impact on scope/effort.

## 2. Ask the right way

- Missing required input → stop the stage, list exactly what is missing, ask user before continuing.
- Each question: exactly 3 options, 1 recommended with a short reason.
- State what the answer affects (scope / timeline / cost / risk).
- Do not ask what can be decided autonomously (pure technical details).

## 3. Every scope item needs a source

- Each item in scope must map to a confirmed requirement, decision, or accepted assumption.
- Adding scope → run impact check before accepting.
- Out-of-scope and future-phase must be stated explicitly, never implied.

## 4. Proposal ↔ WBS must match

- Same scope, same deliverables, same assumptions/risks.
- WBS must not contain out-of-scope work. Proposal must not promise deliverables missing from WBS.
- Mismatch → block finalization.

## 5. Never expand scope silently

- Scope-change triggers: new user group, new platform, integration, AI, migration, compliance, timeline shift.
- Trigger detected → stop, notify user, wait for decision.
- Never add scope without explicit approval.

## 6. Greenfield vs Brownfield

- Determine during Discovery based on client input.
- Greenfield: remove AS-IS Architecture and Migration Strategy — they are meaningless when building from scratch.
- Brownfield: AS-IS and Migration are mandatory.

## 7. Think before generating

- Before creating or regenerating a long artifact → output `[THINKING]` or `[PLAN]`.
- User reviews direction before AI generates.
- Applies to: proposal, WBS, technical solution.

## 8. Stages run in order, no skipping

- Stages must execute sequentially: 1 → 2 → 3 → 3.5 → 4 → 5 → 6.
- A stage cannot start until all prior required stages have their artifact on disk.
- Before starting Stage N: check that all required predecessor artifacts exist. If missing → stop, write them first.
- Optional stages may be skipped when their condition is met:
  - Stage 3.5 (Technical): skip if tech context already provided by SA or client.
  - Stage 2 (Context): skip if client input is complete with no open questions after Discovery.
- Skipping an optional stage → log reason in status.md Notes section.

## 9. Artifact must exist before marking Done

- Required order: write file → confirm file exists → update status.md.
- Output delivered only in chat (not persisted to file) → status remains "Pending".
- No exceptions.

## 10. Match the client's language

- Vietnamese input → Vietnamese output. English input → English output.
- Do not mix languages within the same artifact.
- Maintain professional, consistent tone throughout.

## 11. Conserve tokens

- Use compact deal context, not full chat history.
- Keep only: facts, decisions, assumptions, risks, open questions, scope register, artifact summaries.
- Revise affected sections — never regenerate entire artifacts.
