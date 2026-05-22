# 04 - Giả Định Chiến Lược & Quản Trị Rủi Ro

## 4.1 Giả Định Chiến Lược (Strategic Assumptions)

- **Tài khoản Gemini API:** Người dùng tự cung cấp Gemini API Key cá nhân và chịu trách nhiệm chi trả mọi chi phí phát sinh từ việc gọi API dịch thuật.
- **Chất lượng dịch thuật Gemini:** Gemini API hỗ trợ đầy đủ chức năng dịch thuật text-to-text với chất lượng tương đương hoặc tốt hơn các provider khác cho nhu cầu dịch thuật hàng ngày.
- **Hệ điều hành tối thiểu:** Hệ điều hành mục tiêu tối thiểu là macOS 14+ (Sonoma) để có sự hỗ trợ tốt nhất cho các API native và SwiftUI mới nhất.
- **Phân phối ứng dụng:** Khách hàng sở hữu tài khoản Apple Developer để ký số (Code Sign) và thực hiện quy trình phê duyệt Notarization từ Apple khi phát hành bản phân phối .dmg.

## 4.2 Rủi Ro & Biện Pháp Giảm Thiểu (Risk & Mitigation)

**Người dùng từ chối hoặc gặp khó khăn khi cấp quyền bảo mật hệ thống (Mức độ: Cao)**
Hệ điều hành macOS thắt chặt chính sách bảo mật, yêu cầu người dùng phải tự cấp quyền Accessibility (Trợ năng) thủ công để sử dụng tính năng phím tắt toàn cục dịch bôi đen.
*Biện pháp:* Thiết kế màn hình Onboarding hướng dẫn bằng hình ảnh động trực quan ngay khi mở ứng dụng lần đầu, chỉ dẫn chi tiết từng bước bật quyền trong System Settings.

**Giới hạn tốc độ kết nối internet khi gọi API dịch thuật (Mức độ: Thấp)**
Kết nối mạng bị gián đoạn hoặc Gemini API phản hồi chậm sẽ làm gián đoạn trải nghiệm dịch tức thời.
*Biện pháp:* Hiển thị trạng thái kết nối mạng trực quan trên bong bóng HUD và thiết lập cơ chế timeout hợp lý để thông báo lỗi rõ ràng thay vì để ứng dụng bị treo.
