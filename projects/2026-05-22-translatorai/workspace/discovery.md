# Khảo Sát Dự Án (Discovery Analysis) — TranslatorAI

## 1. Tóm Tắt Đầu Vào Từ Khách Hàng (Client Input Summary)
Khách hàng mong muốn xây dựng **TranslatorAI** - một công cụ dịch thuật nhanh chạy trực tiếp trên màn hình máy tính dành cho hệ điều hành macOS. Sản phẩm hướng tới trải nghiệm dịch thuật tức thời, giúp người dùng không phải chuyển đổi qua lại giữa các cửa sổ ứng dụng hay tab trình duyệt. Các tính năng cốt lõi bao gồm dịch văn bản bôi đen qua phím tắt, chụp ảnh màn hình để nhận diện ký tự (OCR) rồi dịch, hỗ trợ nguồn dịch từ Google Translate (miễn phí) hoặc OpenAI API (người dùng tự điền key), và lưu trữ lịch sử hoàn toàn cục bộ trên thiết bị của người dùng để bảo mật thông tin.

## 2. Các Thực Tế Đã Xác Nhận (Confirmed Facts)
- **Tên dự án:** TranslatorAI
- **Nền tảng:** Hệ điều hành macOS (Desktop app).
- **Mục tiêu sản phẩm:** Dịch thuật tức thời ngay tại màn hình mà không cần chuyển đổi ứng dụng.
- **Tính năng dịch tại chỗ:** Bôi đen chữ bất kỳ + phím tắt $\rightarrow$ Hiện bong bóng popup bản dịch ngay cạnh con trỏ chuột.
- **Tính năng dịch OCR:** Chụp một vùng màn hình $\rightarrow$ Quét chữ từ ảnh/PDF/phụ đề/game $\rightarrow$ Dịch trực tiếp.
- **Nguồn dịch thuật:** Hỗ trợ Google Translate (miễn phí, không giới hạn) và dịch bằng AI qua OpenAI API key cá nhân của người dùng.
- **Bảo mật dữ liệu:** Không gửi dữ liệu dịch về server trung tâm, lịch sử dịch thuật chỉ lưu trữ cục bộ trên máy khách hàng.

## 3. Checklist Thông Tin Thiếu (Missing Info Checklist)
Dựa trên các Stop Rules của BA để định hình phạm vi, nỗ lực và chi phí phát triển:
- [ ] **macOS Target Version & Development Framework:** Khung phiên bản macOS tối thiểu cần hỗ trợ và công nghệ phát triển (Native Swift/AppKit vs Cross-platform Electron/Tauri).
- [ ] **OCR Engine Technology Selection:** Lựa chọn thư viện/API OCR (sử dụng thư viện offline cục bộ của Apple Vision API hay các dịch vụ Cloud OCR).
- [ ] **Hotkey & UX Customization:** Cách thức xử lý phím tắt hệ thống và hành vi hiển thị popup HUD.
- [ ] **Timeline & Budget:** Khung thời gian mong muốn và hạn mức ngân sách dự kiến của khách hàng.

## 4. Câu Hỏi Khảo Sát (Discovery Questions)
*(Các câu hỏi chi tiết về mặt kỹ thuật và nghiệp vụ được đồng bộ chi tiết tại file `backlog-questions.md`)*

---

## Deal Complexity: Light

Reasoning: Dự án phát triển một ứng dụng desktop chạy trên một nền tảng duy nhất (macOS), số lượng phân hệ tính năng tối giản (1-3 phân hệ bao gồm Dịch phím tắt, Dịch OCR, Quản lý Lịch sử/Cấu hình), chỉ có 1 vai trò người dùng cuối và không có cơ sở dữ liệu máy chủ hay yêu cầu bảo mật phức tạp nào.

Recommended pipeline adjustments:
- **Skip Stage 3.5 (Technical Analysis):** Bỏ qua giai đoạn thiết kế kiến trúc hệ thống backend phức tạp vì đây là ứng dụng client-only thuần túy.
- **3-Level WBS Decomposition:** Cấu trúc bảng phân rã công việc (WBS) ở mức gọn nhẹ: Category $\rightarrow$ Module $\rightarrow$ Function.
- **Skip Wireframes in Proposal:** Không đưa phác thảo màn hình chi tiết vào proposal khách hàng để đẩy nhanh tiến độ tài liệu, tập trung vào mô tả UX/UI ở phần Solution Overview.
