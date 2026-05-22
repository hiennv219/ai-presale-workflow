# 03 - Phạm Vi Dự Án

## 3.1 Trong Phạm Vi Phát Triển (In-Scope)

- **Kiến trúc Native Menu Bar App:** Ứng dụng native chạy ẩn dưới dạng biểu tượng Menu Bar hệ thống trên macOS 14+.
- **Hệ thống phím tắt toàn cục:** Thiết lập lắng nghe các tổ hợp phím tắt từ bất kỳ ứng dụng nào đang mở trên màn hình để khởi động nhanh chức năng dịch thuật.
- **Bong bóng Popup HUD:** Hiển thị kết quả dịch ngay cạnh con trỏ chuột với giao diện mờ, tự biến mất khi nhấp chuột ra ngoài.
- **Kết nối API dịch thuật:** Gọi API Google Translate miễn phí hoặc API OpenAI GPT-4o sử dụng khóa API cá nhân của người dùng để nhận kết quả dịch.
- **Lưu trữ SQLite cục bộ:** Khởi tạo cơ sở dữ liệu SQLite dưới máy người dùng để lưu và quản lý lịch sử bản dịch một cách an toàn.
- **Giao diện Cài đặt (Preferences View):** Cung cấp các tab cấu hình OpenAI API key, quản lý lịch sử dịch và thiết lập tổ hợp phím tắt.

## 3.2 Ngoài Phạm Vi Phát Triển (Out-of-Scope)

- **Đồng bộ đám mây (Cloud Sync):** Không hỗ trợ đồng bộ hóa lịch sử dịch thuật giữa các thiết bị thông qua máy chủ đám mây để đảm bảo an toàn thông tin tối đa.
- **Cung cấp OpenAI API Key miễn phí:** Không phát triển hệ thống chia sẻ hay tự cấp API key OpenAI miễn phí cho người dùng nhằm kiểm soát chi phí hạ tầng.

## 3.3 Kế Hoạch Phát Triển Tương Lai (Future Phase)

- **Module Chụp vùng màn hình & Quét chữ OCR offline (FP-3):** Tích hợp Apple Vision Framework để nhận diện ký tự từ ảnh chụp màn hình trực tiếp mà không cần internet.
- **Trình chỉnh sửa văn bản gốc trực tiếp trên Popup (FP-4):** Cho phép sửa văn bản gốc trực tiếp ngay trên Popup HUD trước khi bấm dịch để sửa lỗi nhận diện của OCR.
- **Phiên bản Windows OS (FP-1):** Phát triển phiên bản tương thích với hệ điều hành Windows.
- **Dịch thuật giọng nói thời gian thực (Speech-to-Speech) (FP-2):** Hỗ trợ dịch giọng nói trực tiếp từ microphone.
