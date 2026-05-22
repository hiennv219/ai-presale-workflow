# Sổ Ghi Nhận Giả Định (Assumption Ledger)

## Overview

| Total | Active | Confirmed | Rejected | High Impact Unconfirmed |
|-------|--------|-----------|----------|------------------------|
| 3     | 1      | 2         | 0        | 0                      |

## Ledger

| ID | Giả định (Assumption) | Người tạo (Created By) | Giai đoạn (Stage) | Tác động (Impact) | Trạng thái (Status) | Ngày (Date) | Ghi chú (Note) |
|----|-----------|------------|-------|--------|--------|------|------|
| A-1 | Người dùng tự chịu chi phí API OpenAI khi chọn nguồn dịch AI. | Senior BA | Stage 2: Context | Medium | Confirmed | 2026-05-22 | Đã thống nhất ở câu hỏi khảo sát Q4. |
| A-2 | API Google Translate miễn phí (qua web wrapper) hoạt động ổn định và không bị chặn IP hàng loạt. | Senior BA | Stage 2: Context | Medium | Active | 2026-05-22 | Cần theo dõi thêm trong quá trình phát triển để lập cơ chế fallback. |
| A-3 | Người dùng chấp nhận ứng dụng chạy từ hệ điều hành macOS 14 (Sonoma) trở lên để dùng thư viện native. | Senior BA | Stage 2: Context | High | Confirmed | 2026-05-22 | Đã thống nhất ở câu hỏi khảo sát Q1. |

## Rules

- ID format: A-{n} (sequential, never reuse)
- Impact: Low / Medium / High
- Status: Active / Pending confirm / Confirmed / Rejected / Replaced
- High + unconfirmed $\rightarrow$ blocks finalization
- Medium + Active > 7 days $\rightarrow$ escalate to Stop Rule
