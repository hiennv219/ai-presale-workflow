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

- Discovery stage KHÔNG được đưa thẳng vào Assumptions mà chưa hỏi client trước.
- Quy trình: hỏi client → nếu không trả lời → chuyển thành assumption (ghi rõ "đã hỏi, chưa nhận phản hồi").
- Ngoại lệ: Technical details thuần túy (caching strategy, message queue choice, internal tooling) có thể assume luôn.
- Technical decisions ảnh hưởng lớn (rewrite vs upgrade, platform choice, architecture pattern) vẫn PHẢI hỏi trước.
- Mọi item trong Assumptions phải hoặc (a) đã được hỏi và chưa có phản hồi, hoặc (b) là technical detail thuần túy không ảnh hưởng lớn đến scope/effort.

## Conditional Sections

- Section 5.1 (AS-IS Architecture) và 5.3 (Migration Strategy) chỉ xuất hiện khi client có hệ thống hiện tại (brownfield).
- Nếu client xây mới hoàn toàn (greenfield): bỏ 5.1 AS-IS và 5.3 Migration, đánh số lại các section còn lại.
- Khi greenfield: section Technical Solutions bắt đầu trực tiếp với Target Architecture.
- Xác định brownfield/greenfield trong giai đoạn Discovery dựa trên input khách hàng.
- Với greenfield, AS-IS và Migration không có ý nghĩa — chỉ tạo noise trong proposal.

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

## Token Discipline

- Use compact deal context, not full chat history.
- Keep only: active facts, decisions, assumptions, risks, open questions, scope register, artifact summaries.
- Store history as change log or event summary.
- Revise affected sections, never regenerate entire artifacts.
