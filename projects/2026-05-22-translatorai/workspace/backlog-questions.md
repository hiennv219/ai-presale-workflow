# Danh Sách Câu Hỏi Khảo Sát (Backlog Questions) — TranslatorAI

## Summary

### Open

| # | Topic | Type | Answer |
|---|-------|------|--------|
| — | — | — | — |

### Resolved

| # | Topic | Type | Answer | Answered by |
|---|-------|------|--------|-------------|
| Q1 | Kiến trúc & Phiên bản macOS hỗ trợ | Decision | B (Native Swift/AppKit, macOS 14+) | Client |
| Q2 | Lựa chọn bộ máy nhận diện OCR | Decision | A (Apple Vision Framework - Offline) | Client |
| Q3 | Trải nghiệm phím tắt & Hiển thị popup | Decision | A (Global shortcut & HUD Overlay) | Client |
| Q4 | Ngân sách & Tiến độ dự kiến | Decision | A (MVP gấp: 1-1.5 tháng) | Client |

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

### Q1. Công nghệ phát triển chính và Phiên bản hệ điều hành macOS hỗ trợ (Framework & Compatibility)

**Context:** Quyết định giữa công nghệ Native (Swift/AppKit) hay Cross-platform (Electron/Tauri) sẽ ảnh hưởng sâu sắc đến dung lượng tải về, tốc độ khởi động, độ trễ bắt phím tắt toàn hệ thống và mức độ tiêu thụ RAM của ứng dụng.

**Phương án lựa chọn:** B. Native Swift / AppKit hoặc SwiftUI (Hỗ trợ macOS 14 Sonoma trở lên, tối ưu cho cả Apple Silicon và Intel).

**Answer:** B (Native Swift/AppKit, macOS 14+)
**Answered by:** Client
**Notes:** Khách hàng đồng ý đi theo hướng phát triển native thuần túy để ứng dụng chạy cực nhẹ (dung lượng < 20MB, tiêu thụ RAM < 30MB), khởi động tức thời và truy cập trực tiếp các API hệ thống của Apple mà không cần cài thêm thư viện cồng kềnh.

---

### Q2. Công nghệ nhận diện ký tự quang học (OCR Engine Technology)

**Context:** Quyết định cách thức ứng dụng quét vùng ảnh để trích xuất văn bản chữ. Yêu cầu bảo mật cục bộ cao bắt buộc hạn chế gửi ảnh lên các API Cloud bên thứ ba.

**Phương án lựa chọn:** A. Tận dụng Apple Vision Framework (OCR tích hợp sẵn của hệ điều hành macOS, chạy offline hoàn toàn, không mất phí).

**Answer:** A (Apple Vision Framework - Offline)
**Answered by:** Client
**Notes:** Tối ưu hóa tính năng bảo mật tuyệt đối, hoạt động offline 100%, tốc độ nhận diện nhanh và hoàn toàn miễn phí, không phát sinh chi phí duy trì API OCR hàng tháng.

---

### Q3. Trải nghiệm phím tắt hệ thống và Hiển thị UI bản dịch (UX & Hotkey Behavior)

**Context:** Xác định cách thức người dùng kích hoạt dịch nhanh trên màn hình mà không bị đứt gãy luồng công việc hiện tại.

**Phương án lựa chọn:** A. Global Custom Hotkey (Ví dụ: Option + Space để dịch bôi đen, Option + Shift + S để chụp vùng dịch OCR) + Hiển thị bong bóng popup (HUD) ngay cạnh con trỏ chuột. Người dùng có thể chỉnh sửa văn bản gốc hoặc copy bản dịch nhanh.

**Answer:** A (Global shortcut & HUD Overlay)
**Answered by:** Client
**Notes:** Tạo trải nghiệm dịch thuật mượt mà và trực quan nhất cho người dùng macOS.

---

### Q4. Tiến độ và Ngân sách dự kiến (Timeline & Budget)

**Context:** Ràng buộc về lộ trình bàn giao sản phẩm để lập kế hoạch phân bổ nguồn nhân lực kỹ sư.

**Phương án lựa chọn:** A. Tiến độ bàn giao nhanh (1 - 1.5 tháng), Ngân sách ở mức tối ưu cho phiên bản sản phẩm tối thiểu khả thi (MVP).

**Answer:** A (MVP gấp: 1-1.5 tháng)
**Answered by:** Client
**Notes:** Tập trung nguồn lực xây dựng các tính năng cốt lõi chất lượng cao để nghiệm thu nhanh và đưa ra thị trường chạy thử.
