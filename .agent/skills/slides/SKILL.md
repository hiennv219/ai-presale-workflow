---
name: slides
description: Transform proposal into slide-deck Markdown structured for external AI handoff.
---

# Slide Deck Generator

## Purpose

Tóm tắt proposal thành Markdown có cấu trúc slide, sẵn sàng mang sang GPT/Gemini để tạo visual deck.

## Slide Structure (17 slides cố định + co giãn)

| # | Slide | Source | Nội dung | Giới hạn |
|---|-------|--------|----------|----------|
| 1 | Title | Metadata | Tên dự án, client, ngày, prepared by | 4-5 dòng |
| 2 | Agenda | — | Liệt kê các phần chính sẽ trình bày | 5-7 bullets |
| 3 | Project Overview | §1 (1.1 + 1.2) | Pain points + mục tiêu + business value | 4-5 bullets |
| 4 | Solution Overview | §2.1 | Mô tả giải pháp tổng quan | 2-3 câu + 2 bullets |
| 5 | Key Features | §2.2 | Features nổi bật, business value | 3-5 bullets (co giãn) |
| 6 | User Flow | §2.3 | Flow chính, gợi ý diagram | 3-4 bước |
| 7 | Scope: In-Scope | §3.1 | Deliverables theo nhóm | 3-5 bullets (co giãn) |
| 8 | Scope: Out-of-Scope | §3.2 | Không làm trong phase này | 2-4 bullets |
| 9 | Architecture | §5.1 | Kiến trúc high-level, gợi ý diagram | 3-5 bullets |
| 10 | Tech Stack | §5.2 | Stack chính + lý do chọn ngắn | 4-6 bullets |
| 11 | Risks | §4.2 | Top risks + mitigation | 3 items |
| 12 | Assumptions | §4.1 | Strategic assumptions | 3-4 bullets |
| 13 | Roadmap & Timeline | §6.1 | Phases + duration | 3-5 phases |
| 14 | Milestones | §6.2 | Milestone + key deliverables | 3-5 items |
| 15 | Team & Resources | §7.1 | Roles, composition | 3-5 bullets |
| 16 | Cost Summary | §7 + §8 | Tổng dev cost + operational + 3rd party | 3-5 dòng, con số rõ |
| 17 | Next Steps | — | Action items + timeline follow-up | 3-4 bullets |

## Quy tắc co giãn

- **Key Features** (slide 5): nếu >5 features hoặc chia theo module → tách thành nhiều slides, mỗi slide 1 module
- **Scope In-Scope** (slide 7): nếu >4 modules → tách slide theo nhóm module
- Các slide khác: giữ cố định 1 slide/topic
- Khi tách slide, đánh số phụ: 5a, 5b hoặc 7a, 7b

## Output Format

```markdown
# {{Project Name}} — Slide Deck

## Slide 1: Title

- **Project**: {{name}}
- **Client**: {{client}}
- **Date**: {{date}}
- **Prepared by**: {{author}}

---

## Slide 2: Agenda

- Project Overview
- Solution & Key Features
- ...

---

## Slide 3: Project Overview
...
```

## Nguyên tắc viết

1. Mỗi slide tối đa 5 bullets (trừ khi co giãn), mỗi bullet tối đa 2 dòng
2. Viết cho người nghe, không phải người đọc — ngắn, rõ, có impact
3. Ưu tiên con số và kết quả hơn mô tả process
4. Không lặp nguyên văn proposal — chỉ lấy điểm nhấn
5. Dùng business language, tránh jargon kỹ thuật (trừ slide 9, 10)
6. Nếu section proposal chưa có nội dung → bỏ qua slide đó, ghi note

## Quan điểm viết từng nhóm slide

| Nhóm | Góc nhìn |
|------|----------|
| 3-4 | Viết từ góc client: "vấn đề của bạn là gì, chúng tôi hiểu" |
| 5-6 | Viết từ góc product: "đây là thứ bạn sẽ nhận được" |
| 7-8 | Viết từ góc commitment: "đây là ranh giới rõ ràng" |
| 9-10 | Viết từ góc kỹ thuật: "nền tảng đáng tin cậy" |
| 11-12 | Viết từ góc minh bạch: "chúng tôi nhận diện rủi ro và giả định" |
| 13-16 | Viết từ góc execution: "đây là cách chúng tôi deliver" |
| 17 | Viết từ góc action: "bước tiếp theo cụ thể" |

## Xử lý thiếu dữ liệu

- Nếu proposal thiếu section → bỏ slide tương ứng, ghi `[Skipped — no data in proposal]`
- Nếu proposal có section nhưng nội dung mỏng → vẫn tạo slide với nội dung có sẵn
- KHÔNG bịa thêm thông tin
