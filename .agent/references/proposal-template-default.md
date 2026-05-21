# Proposal Template (Default)

This file defines the default proposal structure. Copy it to `workspace/proposal-template.md` in each project. Users can add, remove, reorder, or rename sections freely.

## How to use
- Each H2 heading = one section in the final proposal
- `file`: output filename (prefix number controls concat order)
- `format`: output style (prose, table, bullets, mermaid)
- `source`: workspace artifacts to use as input data
- `structure`: subsections and their format within this section
- `content`: brief description of what to cover

---

## 01 - Project Overview & Business Value
- file: 01-project-overview.md
- format: prose
- source: context.md, scope.md
- structure: |
    ### 1.1 Context & Problem Statement
    Prose narrative (2-3 sentences current state) + bullet list of Core Pain Points (bold name: root cause. impact).
    ### 1.2 Goals & Business Impact
    Goal (1 sentence), Project Type, then bullet list of Business Benefits.
- content: Bối cảnh dự án, pain points của khách hàng, mục tiêu và giá trị kinh doanh.

## 02 - Proposed Solution & UX
- file: 02-proposed-solution.md
- format: prose, mermaid
- source: context.md, pain-scope.md
- structure: |
    ### 2.1 Solution Overview
    Prose (3-5 sentences) mô tả giải pháp tổng thể.
    ### 2.2 Key Features
    Prose theo business language, group by module. Reference Value Mapping từ pain-scope.md nhưng viết thành paragraphs (không copy table). Mỗi feature: pain → solution → business value.
    ### 2.3 User Flow
    Prose (2-3 sentences) + Mermaid diagram.
    ### 2.4 High-Level Wireframe
    Delegate to wireframe skill nếu cần.
- content: Giải pháp đề xuất, tính năng chính, luồng người dùng, wireframe.

## 03 - Project Scope
- file: 03-project-scope.md
- format: bullets
- source: pain-scope.md
- structure: |
    ### 3.1 In-Scope
    Bullet list: bold phase/module name + description.
    ### 3.2 Out-of-Scope
    Bullet list: bold item + reason for deferral.
- content: Phạm vi dự án (trong/ngoài scope).

## 04 - Risks & Strategic Assumptions
- file: 04-risks-assumptions.md
- format: prose, bullets
- source: context.md, scope.md
- structure: |
    ### 4.1 Strategic Assumptions
    Bullet list: bold category + assumption statement.
    ### 4.2 Risk & Mitigation
    Each risk: bold name (severity level), description paragraph, then Mitigation line.
- content: Giả định chiến lược và rủi ro kèm biện pháp giảm thiểu.

## 05 - Technical Architecture
- file: 05-technical-architecture.md
- format: bullets, diagram
- source: context.md, technical.md
- structure: |
    ### 5.1 Target Architecture
    ASCII box diagram hoặc Mermaid.
    ### 5.2 Tech Stack
    Bullets only (no tables): Frontend, Backend, Database, Infrastructure — mỗi item: bold tech + why.
    ### 5.3 Data Flow
    Mermaid sequenceDiagram.
    ### 5.4 Capacity & Sizing
    Bullets: Target Users, Concurrent Connections, Storage Strategy.
    ### 5.5 Security & Privacy
    Bullets: Transport, Storage, Auth.
- content: Kiến trúc kỹ thuật, tech stack, data flow, capacity, security. Bullets only — NO TABLES.

## 06 - Execution & Delivery Plan
- file: 06-execution-plan.md
- format: table, prose
- source: wbs.md, scope.md
- structure: |
    ### 6.1 Product Roadmap
    Prose (2-3 sentences) về timeline strategy, sau đó table: Phase | Feature | Duration | Timeline | Month columns.
    ### 6.2 Milestones & Acceptance Criteria
    Prose (2-3 sentences) về acceptance method, sau đó table: # | Milestone | Target Date | Key Deliverables | Acceptance Criteria.
- content: Roadmap, milestones và tiêu chí nghiệm thu.

## 07 - Budget & Commercials
- file: 07-budget.md
- format: table, prose
- source: wbs.md
- structure: |
    ### 7.1 Resource Allocation & Development Cost
    Prose explaining pricing model, sau đó table: Position | Seniority | Unit Price | Month columns | Total Effort | Total Cost.
    RULE: Table MUST include every role from WBS Role Registry — no phantom roles, no missing roles.
    ### 7.2 Operational Cost (Infra)
    Prose về cost optimization, sau đó table: Phase | Users | Infra Cost/month | Main Components.
    ### 7.3 3rd-Party Vendor Costs
    Bullet list: bold vendor + cost + note.
- content: Ngân sách nhân sự, chi phí vận hành, vendor costs.

## 08 - Development Cost & Payment Schedule
- file: 08-payment-schedule.md
- format: prose, bullets
- source: wbs.md
- structure: |
    Total Development Cost statement (MUST equal Section 7.1 Total exactly).
    Payment Schedule bullets: each milestone payment with conditions.
    RULE: Payment milestones must match Section 6.2 milestones (same names, same sequence).
- content: Tổng chi phí phát triển và lịch thanh toán theo milestone.

---

## Format Guidelines (Table vs Prose)

1. **CHỈ DÙNG BẢNG cho 4 nội dung sau** (bắt buộc có 1 đoạn văn dẫn dắt trước bảng):
   - 6.1 Roadmap, 6.2 Milestones & AC, 7.1 Resource Allocation & Cost, 7.2 Operational Cost.
2. **DÙNG PROSE / BULLET POINTS cho tất cả phần còn lại**:
   - Section 1 & 2: Business language, kể chuyện.
   - Section 4: Bullet list có bold title.
   - Section 5: Bullets only, giải thích "tại sao chọn".
   - Section 7.3: Bullet list.

## Humanization Checklist

1. Không dùng `---` giữa các heading.
2. Không dùng emoji trang trí (`💡`, `🔴`, `⭐`, `⚠️`) trong heading/blockquote.
3. Đa dạng hóa bullets — tránh lặp `- **Title** — Description`. Đan xen prose, dấu `:`, viết trực tiếp.
4. Loại bỏ hướng dẫn dạng ngoặc đơn `*(Illustrative...)*`.
5. Tránh cụm từ AI: "giải pháp đột phá", "kiến trúc tối tân", "seamless", "robust". Dùng ngôn từ thực tế.
