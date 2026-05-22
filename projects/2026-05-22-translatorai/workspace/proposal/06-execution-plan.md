# 06 - Kế Hoạch Triển Khai & Bàn Giao

## 6.1 Lộ Trình Phát Triển Sản Phẩm (Product Roadmap)

Để đảm bảo TranslatorAI hoạt động native mượt mà và an toàn trên macOS, chúng tôi đề xuất lộ trình triển khai cuốn chiếu trong vòng 4 tuần. Tiến độ được chia thành các giai đoạn tập trung phát triển kiến trúc hệ thống, xây dựng giao diện bong bóng hiển thị, kết nối các API dịch thuật đám mây và tối ưu hóa hiệu năng tài nguyên hệ thống trước khi đóng gói phân phối.

Dưới đây là bảng phân bổ lộ trình phát triển chi tiết cho các phân hệ tính năng qua từng tuần triển khai:

| Giai đoạn | Phân hệ tính năng chính | Thời gian dự kiến | Phân bổ nhân sự |
| --- | --- | --- | --- |
| **Tuần 1** | Khởi tạo Xcode project, Menu Bar app core, hệ thống phím tắt toàn cục và quản lý quyền hệ thống. | 5 – 7 ngày | macOS Developer, QA Engineer |
| **Tuần 2** | Phát triển bong bóng Popup HUD sát con trỏ chuột và thiết lập database SQLite cục bộ để lưu trữ lịch sử dịch thuật. | 5 – 7 ngày | macOS Developer, QA Engineer |
| **Tuần 3** | Kết nối Gemini API client, xây dựng Preferences Panel và hoàn thiện luồng dịch thuật. | 5 – 7 ngày | macOS Developer, QA Engineer |
| **Tuần 4** | Thực hiện kiểm thử tích hợp (QA), tối ưu hóa CPU/RAM, sửa lỗi, Notarize và đóng gói bản phát hành .dmg. | 5 – 7 ngày | QA Engineer, macOS Developer |

## 6.2 Các Mốc Bàn Giao & Tiêu Chí Nghiệm Thu (Milestones & Acceptance Criteria)

Quy trình nghiệm thu sản phẩm được thực hiện minh bạch tại cuối mỗi mốc bàn giao (Milestone). Khách hàng sẽ trực tiếp chạy thử bản build ứng dụng trên thiết bị macOS (phiên bản 14+) để kiểm tra tính năng và xác nhận các tiêu chí chất lượng dưới đây trước khi tiến hành bàn giao mã nguồn.

Dưới đây là danh sách chi tiết 4 mốc bàn giao của dự án kèm sản phẩm đầu ra và tiêu chí nghiệm thu tương ứng:

| # | Mốc bàn giao (Milestone) | Thời gian dự kiến | Sản phẩm bàn giao chính | Tiêu chí nghiệm thu (Acceptance Criteria) |
| --- | --- | --- | --- | --- |
| **M1** | Khởi động & Tích hợp hệ thống | Cuối Tuần 1 | Mã nguồn Xcode project; Status item chạy trên Menu Bar; Module kiểm tra và hướng dẫn cấp quyền hệ thống. | Dự án build thành công không lỗi; ứng dụng chạy ngầm trên Menu Bar; màn hình Onboarding hướng dẫn xin quyền Accessibility hiển thị thành công. |
| **M2** | Core HUD & Database SQLite | Cuối Tuần 2 | Bong bóng Popup HUD; Khởi tạo SQLite Database cục bộ. | Bong bóng Popup HUD hiển thị cạnh con trỏ chuột đúng vị trí và hiển thị được chữ gốc; khởi tạo database SQLite cục bộ thành công. |
| **M3** | API Dịch thuật & Cài đặt | Cuối Tuần 3 | Gemini API client; Cấu trúc database SQLite cục bộ; Cửa sổ Preferences Panel. | Dịch thành công qua Gemini API; lưu cấu hình Gemini API key cá nhân vào Preferences panel; lịch sử dịch thuật lưu được vào SQLite cục bộ và cho phép hiển thị/xóa. |
| **M4** | Kiểm thử, Tối ưu & Đóng gói | Cuối Tuần 4 | Báo cáo kiểm thử QA Report; File cài đặt TranslatorAI.dmg đã được Notarize bởi Apple. | 100% kịch bản kiểm thử cốt lõi vượt qua; RAM tĩnh khi chạy ngầm dưới 30MB, CPU peak khi dịch thuật dưới 5%; file cài đặt chạy tốt không bị cảnh báo bảo mật macOS. |
