# 03 - Phạm Vi Dự Án

## 3.1 Trong Phạm Vi Phát Triển (In-Scope)

- **Quản lý tài khoản PM (Authentication):** Luồng đăng nhập/đăng xuất bảo mật, API xác thực JWT bảo vệ dữ liệu lịch sử họp cá nhân.
- **Dashboard lịch sử họp:** Giao diện danh sách cuộc họp đã xử lý theo thời gian, API truy vấn phân trang và hiển thị trạng thái.
- **Upload file cuộc họp:** Giao diện kéo thả cho file âm thanh (.mp3, .wav) hoặc văn bản (.txt), kiểm tra dung lượng (tối đa 100MB) và định dạng hợp lệ.
- **Speech-to-Text:** Tích hợp OpenAI Whisper API chuyển file ghi âm thành transcript thô tiếng Việt/tiếng Anh.
- **Transcript Editor:** Giao diện xem và chỉnh sửa thủ công văn bản thô trước khi gửi lệnh tóm tắt.
- **AI Summary & Action Items:** Tích hợp OpenAI GPT-4o phân tích transcript, tạo báo cáo tóm tắt và danh sách đầu việc dạng checkbox.
- **Meeting Detail & Quick Copy:** Giao diện chi tiết kết quả tóm tắt, nút sao chép nhanh riêng cho Tóm tắt và Action Items.

## 3.2 Ngoài Phạm Vi MVP (Out-of-Scope)

- **Ghi âm trực tiếp từ trình duyệt:** Không hỗ trợ thu âm qua microphone trên Web App để tối giản giao diện và tránh rủi ro kỹ thuật quyền truy cập thiết bị.
- **Bot tham gia cuộc họp trực tuyến:** Không phát triển bot tự động join Zoom, Google Meet hoặc Teams — cấu trúc tích hợp phức tạp, vượt khung thời gian MVP.
- **Phân quyền đa cấp (RBAC):** Chỉ quản lý 1 loại tài khoản PM duy nhất, không hỗ trợ Admin/Member/Guest.
- **Đồng bộ công cụ bên thứ ba:** Không gọi API trực tiếp đẩy task sang Jira/Trello hoặc gửi tin nhắn Slack tự động. PM sử dụng tính năng Sao chép nhanh thay thế.
