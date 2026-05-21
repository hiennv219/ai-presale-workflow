# Presale Rules

## 1. Stop Rule — Thông tin cốt lõi

Khi agent phát hiện thiếu thông tin thuộc danh sách Stop Rule của mình:
1. Dừng stage hiện tại
2. Đánh dấu status = HOLD
3. Gọi Comm Hub để format câu hỏi
4. Chờ khách trả lời trước khi tiếp tục

Ranh giới: "Nếu thông tin này SAI sẽ thay đổi scope, effort, hoặc cost → Stop Rule."

Mỗi agent có danh sách Stop Rule riêng — xem `agents/<agent>/AGENT.md`.

## 2. Assume Rule — Chi tiết phụ

Khi agent phát hiện thiếu thông tin thuộc danh sách Assume Rule của mình:
1. Chọn giá trị mặc định hợp lý
2. Gọi Assumption Ledger để ghi nhận (ID, nội dung, impact, status=Active)
3. Tiếp tục stage — không dừng, không hỏi khách

Ranh giới: "Nếu thông tin này SAI chỉ thay đổi implementation detail → Assume Rule."

### Escalation

- Assumption đã Active > 7 ngày + impact Medium → escalate lên Stop Rule ở stage tiếp theo
- Assumption bị Rejected bởi khách → trigger re-scope (loop back)

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
