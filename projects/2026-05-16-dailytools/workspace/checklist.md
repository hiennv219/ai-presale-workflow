# Internal Checklist — DailyTools

> This file is for internal validation only. It is NOT exported to the client.

## Overview

| # | Check | Status | Action if Failed |
| --- | --- | --- | --- |
| 1 | Scope Coverage | Pass | Add missing WBS tasks for orphan scope items |
| 2 | Role Registry | Pass | Align Proposal 7.1 with WBS roles |
| 3 | Milestone-WBS Mapping | Pass | Assign orphan tasks to milestones |
| 4 | Proposal ↔ WBS Scope | Pass | Sync scope between both artifacts |
| 5 | Risk Consistency | Pass | Unify risks across all artifacts |

**Legend**: Pass / Fail / N/A

---

## 1. Scope Coverage Check

Verify every `S-{n}` from the approved In-Scope register has at least 1 WBS task referencing it.

| Scope ID | Scope Item | WBS Coverage | Status |
| --- | --- | --- | --- |
| S-1 | Đăng nhập & Quản lý tài khoản PM | 1.1, 1.2, 2.1, 2.2, 2.3 | Covered |
| S-2 | Tải file cuộc họp (mp3, wav, txt) | 3.1, 3.2 | Covered |
| S-3 | Chuyển đổi âm thanh Whisper API | 3.3 | Covered |
| S-4 | Tóm tắt cuộc họp & Action Items GPT-4o API | 3.4 | Covered |
| S-5 | Dashboard danh sách & Lịch sử cuộc họp | 4.1, 4.2 | Covered |
| S-6 | Giao diện chi tiết tóm tắt cuộc họp | 3.5, 4.3, 4.4 | Covered |
| S-7 | Nút Sao chép nhanh (Copy) kết quả tóm tắt | 4.5 | Covered |

**Orphan scope items** (in-scope but no WBS task):
- (none)

## 2. Role Registry

Unique roles extracted from WBS. This list MUST match Proposal Section 7.1 (Resource Allocation table).

| Role | WBS Tasks | In Proposal 7.1? |
| --- | --- | --- |
| Frontend Developer | 2.1, 2.3, 3.1, 3.5, 4.1, 4.3, 4.5 | Yes |
| Backend Developer | 1.1, 1.2, 2.2, 3.2, 3.3, 3.4, 4.2, 4.4, 5.2 | Yes |
| QA Engineer | 5.1 | Yes |

## 3. Milestone-WBS Mapping

Each milestone must reference specific WBS IDs. No orphan tasks allowed.

| Milestone | WBS IDs | Unassigned Tasks |
| --- | --- | --- |
| M1 | 1.1, 1.2, 2.1, 2.2, 2.3 | (none) |
| M2 | 3.1, 3.2, 3.3, 3.4, 3.5 | (none) |
| M3 | 4.1, 4.2, 4.3, 4.4, 4.5 | (none) |
| M4 | 5.1, 5.2 | (none) |

## 4. Cross-Artifact Consistency

| Check | Status | Notes |
| --- | --- | --- |
| Proposal scope = WBS scope | Pass | Phạm vi S-1 đến S-7 đồng bộ hoàn toàn giữa Proposal và WBS. |
| WBS roles = Proposal 7.1 roles | Pass | Danh sách vai trò (FE, BE, QA) khớp chính xác, không có vai trò ảo hoặc bị thiếu. |
| Milestones cover all WBS tasks | Pass | Toàn bộ 17 task trong WBS được ánh xạ đầy đủ về 4 cột mốc Milestones. |
| Risks consistent across artifacts | Pass | Rủi ro về tiếng ồn và chi phí API đồng bộ trên tất cả tài liệu. |
