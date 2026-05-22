# Internal Checklist

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
| S-1 | Kiến trúc Native Menu Bar App | 1.1, 1.2, 7.2 | Covered |
| S-2 | Hệ thống lắng nghe Phím tắt toàn cục | 1.3 | Covered |
| S-3 | Bong bóng Popup HUD cạnh con trỏ chuột | 2.1 | Covered |
| S-5 | Client kết nối API Google & OpenAI | 2.3, 4.1, 4.2 | Covered |
| S-6 | Lưu trữ lịch sử cục bộ bằng SQLite | 2.3, 5.1, 5.2 | Covered |
| S-7 | Giao diện cài đặt (Preferences View) | 2.3, 4.2, 5.2, 7.1 | Covered |

**Orphan scope items** (in-scope but no WBS task):
- (none)

## 2. Role Registry

Unique roles extracted from WBS. This list MUST match Proposal Section 7.1 (Resource Allocation table).

| Role | WBS Tasks | In Proposal 7.1? |
| --- | --- | --- |
| Dev (macOS Native App Developer) | 1.1, 1.2, 1.3, 2.1, 2.3, 4.1, 4.2, 5.1, 5.2, 6.1, 6.2 | Yes |
| QA (Quality Assurance Engineer) | 1.1, 1.2, 1.3, 2.1, 2.3, 4.1, 4.2, 5.1, 5.2, 6.1, 6.2, 7.1, 7.2 | Yes |

## 3. Milestone-WBS Mapping

Each milestone must reference specific WBS IDs. No orphan tasks allowed.

| Milestone | WBS IDs | Unassigned Tasks |
| --- | --- | --- |
| M1: Khởi động & Tích hợp hệ thống | 1.1, 1.2, 1.3, 6.1 | (none) |
| M2: Core HUD & Database SQLite | 2.1, 5.1 | (none) |
| M3: APIs Dịch thuật & Cài đặt | 2.3, 4.1, 4.2, 5.2 | (none) |
| M4: Kiểm thử, Tối ưu & Đóng gói | 6.2, 7.1, 7.2 | (none) |

## 4. Cross-Artifact Consistency

| Check | Status | Notes |
| --- | --- | --- |
| Proposal scope = WBS scope | Pass | Checked that all S-1 to S-7 mapping matched Section 3.1 and WBS. |
| WBS roles = Proposal 7.1 roles | Pass | Extracted roles (macOS Developer, QA Engineer) match Section 7.1 resource cost table. |
| Milestones cover all WBS tasks | Pass | verified that M1 to M4 Milestones mapped to WBS and Section 6.2 milestones perfectly. |
| Risks consistent across artifacts | Pass | Risk ID list (R-1, R-2) and mitigation match Section 4.2. |
