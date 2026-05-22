# TranslatorAI

## General Information

| Field | Value |
| --- | --- |
| Client | TranslatorAI |
| Created | 2026-05-22 |
| Status | Finalized |
| Current Stage | Stage 6: Review & Finalize complete |
| Deal Complexity | Light |

## Progress

- [x] Received client input
- [x] Discovery completed
- [x] Context updated
- [x] Scope analyzed
- [x] WBS built
- [x] Proposal drafted
- [x] Review & Finalize

## Next Action

**What:** none (Presale documents fully exported and ready for delivery)
**Waiting on:** none
**Blockers:** none

## Artifacts

| Artifact | Status | Path |
| --- | --- | --- |
| Client Input | Done | `_source/client-input.md` |
| Discovery Output | Done | `workspace/discovery.md` |
| Context Update | Done | `workspace/context.md` |
| Scope Analysis | Done | `workspace/pain-scope.md` |
| WBS | Done | `workspace/wbs.md` |
| Proposal (sections) | Done | `workspace/proposal/_index.md` |
| Final Proposal (Markdown) | Done | `workspace/final-proposal.md` |
| Final WBS (Markdown) | Done | `workspace/final-wbs.md` |
| Final Proposal (HTML) | Done | `_delivery/final-proposal.html` |
| Final WBS (HTML) | Done | `_delivery/final-wbs.html` |
| Checklist (internal) | Done | `workspace/checklist.md` |

## Notes

### Change Log
- **2026-05-22 (v1.2):** Scope change — thay đổi nguồn dịch API trong MVP.
  - Chuyển sang Gemini API làm nguồn dịch duy nhất trong MVP (thay vì Google Translate + OpenAI).
  - Google Translate (miễn phí) và OpenAI dời sang Future Phase (FP-5, FP-6).
  - Kiến trúc multi-provider mở (protocol pattern) để dễ mở rộng sau.
  - Giảm effort xuống 26,5 person-days (17 Dev, 9.5 QA).
  - Giảm tổng chi phí xuống 65.250.000 VND (từ 70.500.000 VND).
  - Lịch thanh toán: Đợt 1: 19.575.000 VND, Đợt 2: 26.100.000 VND, Đợt 3: 19.575.000 VND.
- **2026-05-22 (v1.1):** Scope change update. Removed OCR (Apple Vision OCR and screen crop tool) from the MVP phase.
  - Adjusted development timeline to 4 weeks (from 5 weeks).
  - Adjusted WBS total effort to 28.5 person-days (18.5 Dev, 10.0 QA).
  - Adjusted total cost to 70,500,000 VND (from 99,750,000 VND).
  - Refactored milestone payments: Đợt 1: 21,150,000 VND, Đợt 2: 28,200,000 VND, Đợt 3: 21,150,000 VND.
