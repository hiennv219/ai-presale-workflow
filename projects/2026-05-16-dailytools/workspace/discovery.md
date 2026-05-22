# Khảo Sát Dự Án (Discovery Analysis) — DailyTools

## 1. Tóm Tắt Đầu Vào Từ Khách Hàng (Client Input Summary)
Khách hàng muốn phát triển **DailyTools** - một công cụ quản lý nhằm hỗ trợ các Quản trị dự án (PM) tối ưu hóa và giảm thiểu nỗ lực làm việc. Giai đoạn đầu sẽ tập trung xây dựng một phiên bản sản phẩm tối thiểu khả thi (MVP) với tính năng cốt lõi là tóm tắt lại các nội dung chính của cuộc họp trong dự án.

## 2. Các Thực Tế Đã Xác Nhận (Confirmed Facts)
- **Tên dự án:** DailyTools
- **Mục tiêu sản phẩm:** Công cụ quản lý giúp PM tối ưu hóa quy trình làm việc.
- **Phạm vi MVP:** Tập trung duy nhất vào tính năng tóm tắt nội dung chính của các cuộc họp.

## 3. Checklist Thông Tin Thiếu (Missing Info Checklist)
Dựa trên yêu cầu của Senior BA, các thông tin sau đây cần làm rõ để xác định phạm vi công việc, thiết kế kiến trúc và ước lượng nỗ lực phát triển:
- [ ] **Business goals & Success criteria:** Chỉ số đo lường hiệu quả cụ thể của MVP.
- [ ] **Platform choice:** Nền tảng vận hành (Web, Mobile hay cả hai).
- [ ] **Input Source:** Cách thức hệ thống tiếp nhận nội dung họp (File ghi âm, text transcript, hay tích hợp bot tự động join cuộc họp).
- [ ] **Speech-to-Text (STT) & AI Integration:** Sử dụng API bên thứ ba hay tự deploy model bảo mật riêng.
- [ ] **User Roles:** Số lượng nhóm người dùng (chỉ PM hay cả member dự án).
- [ ] **Timeline & Budget:** Khung thời gian mong muốn bàn giao và giới hạn ngân sách.
- [ ] **Security & Compliance:** Các yêu cầu về bảo mật thông tin cuộc họp (dữ liệu hội thoại nhạy cảm).

## 4. Câu Hỏi Khảo Sát (Discovery Questions)
*(Chi tiết các câu hỏi khảo sát được đồng bộ tại file `workspace/backlog-questions.md`)*

Các câu hỏi thuộc nhóm **Stop Rule** (Thông tin cốt lõi bắt buộc phải xác nhận):
1. Nền tảng triển khai (Platform Choice)
2. Phương thức tiếp nhận đầu vào (Input Source)
3. Vai trò người dùng và phân quyền (User Roles)
4. Tích hợp công nghệ AI & STT (STT & AI Integration)
5. Ngân sách & Tiến độ dự kiến (Budget & Timeline)

---

## Deal Complexity: Light

**Reasoning:**
Dự án tập trung vào một module tính năng duy nhất (tóm tắt cuộc họp), đề xuất 1 platform (Web app), tối đa 1-2 user roles chính (PM/Member) và tích hợp API STT/LLM có sẵn từ bên thứ ba. Dự án không yêu cầu migration dữ liệu cũ hoặc tuân thủ các chứng chỉ bảo mật đặc thù phức tạp.

**Recommended pipeline adjustments:**
- **Skip Stage 3.5 (Technical):** Bỏ qua bước phân tích kiến trúc kỹ thuật chuyên sâu do kiến trúc Web App tích hợp API đơn giản và không có yêu cầu phi chức năng đặc thù.
- **WBS Decomposition:** Sử dụng phân rã công việc 3 cấp (Category → Module → Function) thay vì 4 cấp.
- **Proposal Adjustments:** Bỏ qua phần Wireframe phác thảo giao diện trong proposal để tập trung vào mô tả tính năng.
