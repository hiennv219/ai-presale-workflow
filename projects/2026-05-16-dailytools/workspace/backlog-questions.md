# Danh Sách Câu Hỏi Khảo Sát (Backlog Questions) — DailyTools

## Summary

### Open

| # | Topic | Type | Answer |
|---|-------|------|--------|
| — | — | — | — |

### Resolved

| # | Topic | Type | Answer | Answered by |
|---|-------|------|--------|-------------|
| Q1 | Nền tảng triển khai (Platform Choice) | Decision | A (Web App) | Client |
| Q2 | Phương thức nhận đầu vào (Input Source) | Decision | A (Upload file trực tiếp) | Client |
| Q3 | Phân quyền người dùng (User Roles) | Decision | A (Đơn vai trò - PM) | Client |
| Q4 | Tích hợp dịch vụ STT & AI (Integrations) | Decision | A (Cloud APIs: Whisper & GPT-4o) | Client |
| Q5 | Ngân sách & Tiến độ (Budget & Timeline) | Decision | A (Gấp: 1-1.5 tháng, tối ưu) | Client |

**Type legend:**
- **Decision** — Khách hàng chọn một trong các phương án đề xuất.
- **Confirm** — Đội dự án đề xuất giải pháp, khách hàng xác nhận.

---

## Decision (client must decide)

*(Không còn câu hỏi chưa giải quyết)*

---

## Confirm (needs client verification)

*(Không còn câu hỏi chưa giải quyết)*

---

## Resolved

### Q1. Nền tảng triển khai chính cho DailyTools (Platform Choice)

**Context:** Xác định nền tảng chạy ứng dụng giúp định hình kiến trúc phát triển và tối ưu hóa chi phí.

**Phương án lựa chọn:** A. Web Application (Chạy trên trình duyệt máy tính & mobile, responsive)

**Answer:** A (Web App)
**Answered by:** Client
**Notes:** Khách hàng đồng ý với đề xuất Web App để tối ưu chi phí và nâng cấp nhanh chóng.

---

### Q2. Phương thức tiếp nhận thông tin cuộc họp đầu vào (Input Source)

**Context:** Quyết định cách thức hệ thống lấy dữ liệu họp để thực hiện tóm tắt.

**Phương án lựa chọn:** A. Tải file âm thanh/văn bản trực tiếp: Người dùng ghi âm bằng công cụ khác rồi tải file (mp3, wav, txt) lên hệ thống.

**Answer:** A (Upload file trực tiếp)
**Answered by:** Client
**Notes:** Đơn giản hóa phần tiếp nhận thông tin cho MVP.

---

### Q3. Phân quyền và Vai trò người dùng (User Roles)

**Context:** Xác định các nhóm đối tượng sử dụng để thiết kế luồng quản lý tài khoản và phân quyền dữ liệu.

**Phương án lựa chọn:** A. Đơn vai trò (Single Role - PM): Chỉ PM đăng nhập, tải file và xem tóm tắt.

**Answer:** A (Đơn vai trò - PM)
**Answered by:** Client
**Notes:** PM là đối tượng sử dụng duy nhất của bản MVP.

---

### Q4. Tích hợp công nghệ Chuyển đổi giọng nói & AI (STT & AI Integration)

**Context:** Xác định nguồn công nghệ xử lý âm thanh tiếng Việt và mô hình ngôn ngữ lớn để tóm tắt.

**Phương án lựa chọn:** A. Sử dụng API dịch vụ bên thứ ba (Cloud APIs): Tận dụng các Cloud API hàng đầu như OpenAI (Whisper + GPT-4o).

**Answer:** A (Cloud APIs: Whisper & GPT-4o)
**Answered by:** Client
**Notes:** Tận dụng giải pháp API có sẵn để đảm bảo chất lượng tiếng Việt tốt và thời gian phát triển ngắn nhất.

---

### Q5. Ngân sách & Tiến độ dự kiến (Budget & Timeline)

**Context:** Ràng buộc về thời gian và chi phí để định hình cấu trúc nhân sự phát triển và lộ trình bàn giao.

**Phương án lựa chọn:** A. Tiến độ gấp (1-1.5 tháng), Ngân sách tối ưu.

**Answer:** A (Tiến độ gấp: 1-1.5 tháng, tối ưu)
**Answered by:** Client
**Notes:** Bàn giao sản phẩm MVP nhanh để kiểm chứng thị trường.
