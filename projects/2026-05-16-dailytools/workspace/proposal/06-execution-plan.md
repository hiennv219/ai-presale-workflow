# 06 - Kế Hoạch Triển Khai & Bàn Giao

## 6.1 Lộ Trình Phát Triển Sản Phẩm (Product Roadmap)

Để đảm bảo sản phẩm MVP được bàn giao nhanh nhất và kiểm chứng hiệu quả thực tế của ý tưởng, chúng tôi đề xuất lộ trình triển khai cuốn chiếu trong vòng 4 tuần (1 tháng). Quy trình phát triển được phân chia thành các giai đoạn tập trung, mỗi giai đoạn giải quyết một nhóm tính năng độc lập và có sự phối hợp chặt chẽ giữa đội ngũ Frontend và Backend.

Dưới đây là bảng phân bổ lộ trình phát triển chi tiết cho các phân hệ tính năng qua từng tuần triển khai:

| Giai đoạn | Phân hệ tính năng chính | Thời gian dự kiến | Phân bổ nhân sự |
| --- | --- | --- | --- |
| **Tuần 1** | Khởi tạo dự án, thiết lập cơ sở dữ liệu và hoàn thiện phân hệ Đăng nhập/Đăng xuất cho PM. | 5 – 7 ngày | Backend Developer, Frontend Developer |
| **Tuần 2** | Phát triển module Tải file cuộc họp, tích hợp API OpenAI Whisper chuyển âm thanh sang văn bản và trình biên tập transcript. | 7 – 10 ngày | Backend Developer, Frontend Developer |
| **Tuần 3** | Tích hợp API OpenAI GPT-4o tóm tắt nội dung họp, xây dựng Dashboard lịch sử và tính năng Sao chép nhanh kết quả. | 5 – 8 ngày | Backend Developer, Frontend Developer |
| **Tuần 4** | Thực hiện kiểm thử tích hợp (QA), rà soát lỗi hệ thống và triển khai đưa ứng dụng lên internet (Go-live). | 4 – 6 ngày | QA Engineer, Backend Developer |

## 6.2 Các Mốc Bàn Giao & Tiêu Chí Nghiệm Thu (Milestones & Acceptance Criteria)

Quy trình nghiệm thu sản phẩm được thực hiện minh bạch tại cuối mỗi mốc bàn giao (Milestone). Khách hàng sẽ trực tiếp chạy thử các tính năng trên môi trường kiểm thử (Staging) để xác nhận hệ thống hoạt động ổn định và đáp ứng đầy đủ các tiêu chí nghiệp vụ dưới đây trước khi chuyển sang giai đoạn tiếp theo.

Dưới đây là danh sách chi tiết 4 mốc bàn giao của dự án kèm sản phẩm đầu ra và tiêu chí nghiệm thu tương ứng:

| # | Mốc bàn giao (Milestone) | Thời gian dự kiến | Sản phẩm bàn giao chính | Tiêu chí nghiệm thu (Acceptance Criteria) |
| --- | --- | --- | --- | --- |
| **M1** | Thiết lập hệ thống & Hoàn thiện Đăng nhập | Cuối Tuần 1 | Mã nguồn khung dự án trên GitHub; Cấu hình cơ sở dữ liệu PostgreSQL; Trang đăng nhập PM hoàn chỉnh. | Mã nguồn build thành công không lỗi; PM có thể đăng nhập bằng tài khoản demo được cấu hình sẵn trong DB và chuyển hướng vào Dashboard. |
| **M2** | Tích hợp AI & Chuyển đổi cuộc họp | Cuối Tuần 2 | Module upload file (mp3, wav, txt); Tích hợp API OpenAI Whisper; Giao diện Transcript Editor. | PM tải lên file ghi âm .mp3/.wav thành công; hệ thống trả về văn bản dịch thô (transcript) trên màn hình để PM chỉnh sửa văn bản. |
| **M3** | Dashboard lịch sử & Sao chép nhanh | Cuối Tuần 3 | Dashboard danh sách cuộc họp cũ; Giao diện xem chi tiết Tóm tắt & Action Items; Nút sao chép một chạm. | PM xem được danh sách lịch sử họp cũ; xem báo cáo tóm tắt cuộc họp; click nút Copy và dán được nội dung sang các ứng dụng chat (Zalo/Slack) bình thường. |
| **M4** | QA & Triển khai Production | Cuối Tuần 4 | Báo cáo kiểm thử QA Report; Ứng dụng Web chạy chính thức trên internet (Production). | 100% kịch bản kiểm thử cốt lõi vượt qua; ứng dụng hoạt động ổn định trên môi trường production của khách hàng dưới tên miền internet chính thức. |
