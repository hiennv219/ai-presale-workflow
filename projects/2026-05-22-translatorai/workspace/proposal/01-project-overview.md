# 01 - Tổng Quan Dự Án & Giá Trị Kinh Doanh

## 1.1 Bối Cảnh & Vấn Đề (Context & Problem Statement)

Người dùng macOS thường xuyên phải dịch thuật văn bản khi đọc tài liệu, làm việc trên các ứng dụng như Slack, Zalo, WeChat hoặc trình duyệt, đòi hỏi phải chuyển đổi qua lại giữa các cửa sổ ứng dụng và trang web dịch thuật liên tục, gây gián đoạn công việc sâu. Ngoài ra, việc bảo mật các tài liệu nội bộ nhạy cảm khi dịch thuật vẫn còn gặp nhiều rào cản.

Các vấn đề cốt lõi:
- Gián đoạn luồng làm việc liên tục: Việc sao chép và chuyển đổi tab để dịch văn bản thô làm giảm hiệu suất và sự tập trung đáng kể.
- Rủi ro bảo mật dữ liệu nhạy cảm: Việc gửi toàn bộ dữ liệu dịch lên các máy chủ đám mây của bên thứ ba tăng nguy cơ rò rỉ thông tin mật của cá nhân và doanh nghiệp.

## 1.2 Mục Tiêu & Tác Động Kinh Doanh (Goals & Business Impact)

Dự án TranslatorAI hướng tới xây dựng một ứng dụng native gọn nhẹ trên hệ điều hành macOS, hỗ trợ phím tắt toàn hệ thống để dịch tức thời tại chỗ dạng in-place mà không gửi dữ liệu ra ngoài thiết bị.

Loại hình dự án: Phát triển sản phẩm mới (Native macOS Greenfield MVP).

Lợi ích kinh doanh:
- Tiết kiệm 90% thời gian thao tác dịch thuật: Người dùng nhận kết quả dịch ngay sát con trỏ chuột trong vòng chưa đầy 1 giây mà không cần chuyển ứng dụng.
- Bảo mật thông tin tuyệt đối: Dữ liệu lịch sử lưu trữ SQLite cục bộ và cơ chế gọi API trực tiếp giúp ngăn chặn hoàn toàn rủi ro rò rỉ thông tin mật.
