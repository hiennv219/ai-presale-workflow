# Proposal Sections

Proposal được tách thành các file riêng để tối ưu token. Mỗi file là một section độc lập.

## Cấu trúc

```
workspace/proposal/
├── _index.md                        ← metadata + mục lục (luôn đọc đầu tiên)
├── 01-project-overview.md           ← Bối cảnh, Pain Points, Mục tiêu
├── 02-project-scope.md              ← In-Scope, Out-of-Scope, Giả định
├── 03-solution-approach.md          ← Rủi ro, Tiêu chí nghiệm thu
├── 04-technical-requirements.md     ← Design Principles, Capacity Planning
├── 05-technical-solutions.md        ← AS-IS, TO-BE, Migration, Tech Stack, UI/UX
├── 06-product-roadmap.md            ← Roadmap tổng thể, Delivery Plan
├── 07-master-schedule.md            ← Timeline, Milestones Phase 1
├── 08-wbs-quotations.md             ← WBS, Resource Plan, Estimation, Budget
```

## Quy tắc

- Khi update: chỉ đọc và sửa section bị ảnh hưởng.
- Khi review/finalize: đọc `_index.md` + các section cần kiểm tra.
- Khi xuất bản full proposal: concat tất cả sections theo thứ tự 01→08.
- `_index.md` chứa metadata, version, và trạng thái từng section.
- Mỗi section file bắt đầu bằng heading cấp 2 (##) tương ứng với proposal_template.md.
