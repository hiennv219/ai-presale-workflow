---
name: proposal
description: Create or revise presale proposal from context, scope, WBS, and risks. Uses 7-section file structure.
---

# Presale Proposal

## Procedure

1. Dùng cấu trúc 8 phần. Lồng ghép "Company Showcase" làm Phụ lục nếu cần.
2. **Customer Feedback Priority**: Truy xuất các yêu cầu có mức độ ưu tiên **Critical** từ bảng `Confirmed Requirements` trong Deal Context. Những ý này PHẢI ĐƯỢC ƯU TIÊN lồng ghép tự nhiên lên đầu hoặc bôi đậm (Highlight) tại các mục Pain Points (1.1), Key Features (2.2), và Risks (4.2). Khách hàng sẽ đánh giá cao khi thấy ta tập trung vào đúng trọng tâm của họ.
3. Section 2.2 Key Features = business language (non-tech stakeholder phải hiểu). 
4. Section 2.3/2.4: Mermaid user flow & Wireframe. Delegate wireframes to `wireframe` skill.
5. Section 3: Chỉ chứa In-Scope và Out-of-Scope.
6. Section 4: Assumptions → Risks.
7. Section 5: Architecture → Tech Stack → Capacity → Security. Tuyệt đối dùng Bullet Points, KHÔNG DÙNG BẢNG ở phần này.
8. Section 6: Execution & Delivery Plan (gộp Roadmap, Milestones+AC).
9. Section 7: Budget & Commercials.
10. Section 8: Development Cost & Payment Schedule. Chứa chi phí phát triển và lịch thanh toán.

## Format & Tone (Table vs Prose Strict Rules)

- **Tables (Bảng)**: Chỉ dùng cho Roadmap (6.1), Milestones (6.2), Resource Allocation & Cost (7.1), và Operational Cost (7.2). Mọi bảng ĐỀU PHẢI có một đoạn văn (prose) mô tả ngắn gọn ngay phía trên bảng để dẫn dắt người đọc.
- **Prose/Bullets**: Dùng cho toàn bộ các phần còn lại. Khi liệt kê (Tech Stack, Vendors, Team Roles, Risks), bắt buộc dùng Bullet points (`- **Title**: Description`).
