# Proposal Sections

Proposal được tách thành các file riêng để tối ưu token. Mỗi file là một section độc lập (Cấu trúc 8 phần mới).

## Cấu trúc

```
workspace/proposal/
├── _index.md                        ← metadata + mục lục (luôn đọc đầu tiên)
├── 01-project-overview.md           ← Bối cảnh, Pain Points, Mục tiêu
├── 02-proposed-solution.md          ← Solution Overview, Key Features, User Flow, Wireframe
├── 03-project-scope.md              ← In-Scope, Out-of-Scope (Acceptance Criteria đã gộp vào Milestone)
├── 04-risks-assumptions.md          ← Strategic Assumptions, Rủi ro
├── 05-technical-architecture.md     ← Kiến trúc, Tech Stack, Data Flow, Capacity, Security (Toàn bộ dùng Prose/Bullets)
├── 06-execution-delivery.md         ← Roadmap, Milestones (có AC)
├── 07-budget-commercials.md         ← Resource Allocation & Cost, Chi phí Server, 3rd-Party Costs
├── 08-investment-summary.md         ← Development Cost, Payment Schedule
```

## Quy tắc

- Khi update: chỉ đọc và sửa section bị ảnh hưởng.
- Khi review/finalize: đọc `_index.md` + các section cần kiểm tra.
- Khi xuất bản full proposal: concat tất cả sections theo thứ tự 01→08.

## Format Guidelines (Table vs Prose)

**Tuyệt đối tuân thủ quy tắc Dạng Bảng vs Bullet points:**

1. **CHỈ DÙNG BẢNG cho 4 nội dung sau** (Bắt buộc phải có 1 đoạn văn mô tả ngắn ngay trước bảng để dẫn dắt):
   - **6.1 Roadmap**: Vẽ timeline các Phase.
   - **6.2 Milestones & Acceptance Criteria**: Ràng buộc Cột mốc và Tiêu chí nghiệm thu.
   - **7.1 Resource Allocation & Cost**: Bảng phân bổ FTE theo tháng và tổng chi phí.
   - **7.2 Operational Cost**: So sánh chi phí infra giữa các mốc scale.

2. **DÙNG PROSE / BULLET POINTS cho tất cả các phần còn lại**:
   - Section 1 & 2: Kể chuyện, mô tả tính năng (Business language).
   - Section 4 (Risks, Assumptions): Bullet list có in đậm title.
   - Section 5 (Tech Stack, Capacity, Security): Tuyệt đối dùng Bullet list, giải thích rõ "Tại sao chọn công nghệ này".
   
   - Section 7.3 (3rd-Party Costs): Bullet list.
