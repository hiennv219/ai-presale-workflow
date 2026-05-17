# Proposal Sections

Proposal được tách thành các file riêng để tối ưu token. Mỗi file là một section độc lập.

## Cấu trúc

```
workspace/proposal/
├── _index.md                        ← metadata + mục lục (luôn đọc đầu tiên)
├── 01-project-overview.md           ← Bối cảnh, Pain Points, Mục tiêu, Solution Overview, Showcase
├── 02-scope-solution.md             ← In-Scope, Out-of-Scope
├── 03-user-flow-wireframe.md        ← User Flow (Mermaid), Wireframe (ASCII via wireframe skill)
├── 04-risks-assumptions-acceptance.md ← Assumptions, Rủi ro, Tiêu chí nghiệm thu
├── 05-technical-architecture.md     ← Kiến trúc (ASCII via architecture skill), Tech Stack, Data Flow (Mermaid), Capacity
├── 06-implementation-plan.md        ← Roadmap tổng thể, Milestones, Delivery Plan
├── 07-wbs-resources.md              ← WBS, Resource Plan, Capacity
├── 08-budget-commercials.md         ← Budget, Infra Cost, 3rd-Party Costs
```

## Quy tắc

- Khi update: chỉ đọc và sửa section bị ảnh hưởng.
- Khi review/finalize: đọc `_index.md` + các section cần kiểm tra.
- Khi xuất bản full proposal: concat tất cả sections theo thứ tự 01→08.
- `_index.md` chứa metadata, version, và trạng thái từng section.
- Mỗi section file bắt đầu bằng heading cấp 2 (##) tương ứng với proposal.md.
