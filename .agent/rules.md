# Presale Rules

## 1. Stop Rule — Core Information

When the agent detects that core information in its Stop Rule list is missing:
1. Stop the current stage.
2. Mark the status as HOLD.
3. Call the Communication Hub to format the clarifying questions.
4. Wait for the user's response before proceeding.

Boundary: "If this information being WRONG would change the scope, effort, or cost → it is a Stop Rule."

Each agent has its own list of Stop Rules — see `agents/<agent>/AGENT.md`.

## 2. Assume Rule — Minor Details

When the agent detects that minor details in its Assume Rule list are missing:
1. Select a reasonable default value.
2. Call the Assumption Ledger to record it (ID, description, impact, status=Active).
3. Proceed with the current stage — do not stop, and do not ask the client.

Boundary: "If this information being WRONG would only change the implementation details → it is an Assume Rule."

### Escalation

- An active assumption that remains Active for > 7 days with a Medium impact is escalated to a Stop Rule in the next stage.
- If an assumption is Rejected by the client, it triggers a re-scope loop (loop back).

## 3. Classify information

- Classify every piece of information as: **fact**, **assumption**, **decision**, or **open question**.
- Never promote unconfirmed information to a requirement.

## 4. Every scope item needs a source

- Each item in scope must map to a confirmed requirement, decision, or accepted assumption.
- Adding scope → run impact check before accepting.
- Out-of-scope and future-phase must be stated explicitly, never implied.

## 5. Proposal ↔ WBS must match

- Same scope, same deliverables, same assumptions/risks.
- WBS must not contain out-of-scope work. Proposal must not promise deliverables missing from WBS.
- Mismatch → block finalization.

## 6. Never expand scope silently

- Scope-change triggers: new user group, new platform, integration, AI, migration, compliance, timeline shift.
- Trigger detected → stop, notify user, wait for decision.
- Never add scope without explicit approval.

## 7. Greenfield vs Brownfield

- Determine during Discovery based on client input.
- Greenfield: remove AS-IS Architecture and Migration Strategy — they are meaningless when building from scratch.
- Brownfield: AS-IS and Migration are mandatory.

## 8. Think before generating

- Before creating or regenerating a long artifact → output `[THINKING]` or `[PLAN]`.
- User reviews direction before AI generates.
- Applies to: proposal, WBS, technical solution.

## 9. Stages run in order, no skipping

- Stages must execute sequentially: 1 → 2 → 3 → 3.5 → 4 → 5 → 6.
- A stage cannot start until all prior required stages have their artifact on disk.
- Before starting Stage N: check that all required predecessor artifacts exist. If missing → stop, write them first.
- Handoff between agents requires conditions met (see `agents/<agent>/AGENT.md`).
- Optional stages may be skipped when their condition is met:
  - Stage 3.5 (Technical): skip if tech context already provided by SA or client.
  - Stage 2 (Context): skip if client input is complete with no open questions after Discovery.
- Skipping an optional stage → log reason in status.md Notes section.

## 10. Artifact must exist before marking Done

- Required order: write file → confirm file exists → update status.md.
- Output delivered only in chat (not persisted to file) → status remains "Pending".
- No exceptions.

## 11. Match the client's language

- Vietnamese input → Vietnamese output. English input → English output.
- Do not mix languages within the same artifact.
- Maintain professional, consistent tone throughout.

## 12. Conserve tokens

- Use compact deal context, not full chat history.
- Keep only: facts, decisions, assumptions, risks, open questions, scope register, artifact summaries.
- Revise affected sections — never regenerate entire artifacts.
