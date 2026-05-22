# WBS - TranslatorAI

## Metadata

- Artifact ID: WBS-TranslatorAI
- Version: 1.2
- Status: Approved
- Context Version: 1.2
- Date: 2026-05-22

## WBS

| # | Category | Module | Function | Sub-function | Description | Note |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Phát triển Ứng dụng (Core App) | Menu Bar & Tích hợp hệ thống | Khởi tạo Status Item trên Menu Bar | Chạy ngầm và hiển thị icon ứng dụng | Thiết lập ứng dụng native macOS chạy ngầm, hiển thị icon trên hệ thống Menu Bar và menu drop-down nhanh.<br>Ước lượng: Dev: 2 ngày, QA: 1 ngày | Áp dụng cho: S-1. Đảm bảo ứng dụng khởi động mượt mà, chiếm ít RAM. |
| 1.2 | Phát triển Ứng dụng (Core App) | Menu Bar & Tích hợp hệ thống | Cấp quyền hệ thống (Permissions) | Kiểm tra và yêu cầu quyền Accessibility | Xây dựng logic kiểm tra và hướng dẫn người dùng cấp quyền Trợ năng (Accessibility) trong System Settings.<br>Ước lượng: Dev: 1 ngày, QA: 0.5 ngày | Áp dụng cho: S-1, R-1. Hướng dẫn trực quan hiển thị khi khởi chạy ứng dụng lần đầu. |
| 1.3 | Phát triển Ứng dụng (Core App) | Menu Bar & Tích hợp hệ thống | Lắng nghe Phím tắt toàn cục | Đăng ký global hotkey listener | Thiết lập listener lắng nghe phím tắt toàn hệ thống (Option + Space để dịch bôi đen).<br>Ước lượng: Dev: 1 ngày, QA: 0.5 ngày | Áp dụng cho: S-2. Lắng nghe phím tắt ngay cả khi ứng dụng đang chạy ngầm. |
| 2.1 | Giao diện người dùng (UI Components) | Floating HUD Overlays | Bong bóng Popup dịch nhanh | Hiển thị kết quả dịch sát con trỏ | Tạo cửa sổ popover không viền (HUD style) dạng mờ ảo (Acrylic background) xuất hiện ngay cạnh con trỏ chuột, tự động ẩn khi click ra ngoài.<br>Ước lượng: Dev: 3 ngày, QA: 1.5 ngày | Áp dụng cho: S-3. UI mượt mà, hỗ trợ bo góc, đổ bóng chuẩn Apple Design Guidelines. |
| 2.3 | Giao diện người dùng (UI Components) | Cấu hình Preferences | Giao diện Cài đặt (Preferences Panel) | Quản lý cấu hình dịch thuật và phím tắt | Thiết lập cửa sổ preferences gồm tab: Chung (Cài đặt phím tắt), API Gemini (Nhập Key, System Prompt, chọn model), Lịch sử (bật/tắt, xóa lịch sử).<br>Ước lượng: Dev: 3 ngày, QA: 1 ngày | Áp dụng cho: S-7, S-5, S-6. Lưu cấu hình an toàn trong NSUserDefaults hoặc SQLite. |
| 4.1 | Dịch thuật & Kết nối API | API Integration | Gemini API Client | Request dịch thuật qua Gemini API | Tích hợp Gemini API sử dụng API Key cá nhân của người dùng, hỗ trợ tùy chỉnh System Prompt để dịch văn bản tự nhiên. Thiết kế theo mô hình protocol/interface để dễ bổ sung provider sau.<br>Ước lượng: Dev: 2 ngày, QA: 1 ngày | Áp dụng cho: S-5, S-7. Dịch chất lượng cao, kiến trúc multi-provider mở. |
| 5.1 | Lưu trữ Dữ liệu cục bộ | SQLite Storage | Thiết lập Database cục bộ | Khởi tạo cấu trúc SQLite database | Cài đặt và khởi tạo file database SQLite cục bộ tại thư mục Application Support của ứng dụng.<br>Ước lượng: Dev: 1.5 ngày, QA: 0.5 ngày | Áp dụng cho: S-6. Tạo bảng và cấu trúc dữ liệu lưu lịch sử dịch thuật. |
| 5.2 | Lưu trữ Dữ liệu cục bộ | SQLite Storage | Quản lý lịch sử dịch thuật | Lưu trữ, truy vấn và xóa dữ liệu | Viết các truy vấn SQLite lưu bản dịch mới, hiển thị lịch sử trên UI và thực hiện xóa toàn bộ lịch sử khi người dùng yêu cầu.<br>Ước lượng: Dev: 1.5 ngày, QA: 0.5 ngày | Áp dụng cho: S-6, S-7. Đảm bảo dữ liệu được mã hóa cơ bản và chỉ lưu dưới local. |
| 6.1 | Quản lý dự án & Triển khai | Dự án & Đóng gói | Thiết lập môi trường | Khởi tạo repo và CI/CD cơ bản | Thiết lập Xcode project, cấu hình build target, và thiết lập workflow build tự động trên Xcode Cloud hoặc GitHub Actions.<br>Ước lượng: Dev: 1 ngày, QA: 0.5 ngày | Áp dụng cho: Quản lý dự án. Đảm bảo code được build sạch sẽ ngay từ đầu. |
| 6.2 | Quản lý dự án & Triển khai | Dự án & Đóng gói | Đóng gói sản phẩm | Build bản phân phối .dmg | Cấu hình code signing với Apple Developer Certificate và đóng gói ứng dụng thành file .dmg sẵn sàng để người dùng cài đặt.<br>Ước lượng: Dev: 1 ngày, QA: 0.5 ngày | Áp dụng cho: Phát hành. Ứng dụng phải được notarize bởi Apple để tránh cảnh báo bảo mật. |
| 7.1 | Kiểm thử & QA | Đảm bảo chất lượng | Kiểm thử Tích hợp & Bảo mật | Kiểm thử luồng phân quyền và API | Kiểm tra tính ổn định của hệ thống phân quyền (Accessibility) và bảo mật lưu trữ API keys.<br>Ước lượng: QA: 1 ngày | Áp dụng cho: R-1, S-7. Phát hiện lỗi chặn quyền và rò rỉ key. |
| 7.2 | Kiểm thử & QA | Đảm bảo chất lượng | Kiểm thử Hiệu năng & Rò rỉ | Kiểm tra CPU/RAM khi dịch | Đo lường mức chiếm dụng CPU khi thực hiện dịch thuật và kiểm tra rò rỉ bộ nhớ RAM khi chạy ngầm lâu ngày.<br>Ước lượng: QA: 1 ngày | Áp dụng cho: S-1. Bảo đảm ứng dụng cực nhẹ, không gây nóng máy hoặc tốn pin. |

## Milestones

| Milestone | Description | Exit Criteria |
| --- | --- | --- |
| M1: Khởi động & Tích hợp hệ thống | Thiết lập cấu trúc dự án cơ bản, tạo Menu Bar icon và xử lý hệ thống quyền truy cập cùng phím tắt toàn hệ thống. | - Xcode project sẵn sàng, build chạy ngầm trên Menu Bar.<br>- Nhấn hotkey Option+Space nhận biết được sự kiện bôi đen.<br>- Màn hình xin quyền Accessibility hiển thị thành công. |
| M2: Core HUD & Database SQLite | Phát triển bong bóng dịch Popup HUD và thiết lập database SQLite lưu trữ lịch sử. | - Bong bóng Popup HUD hiển thị cạnh con trỏ chuột đúng vị trí và hiển thị được chữ gốc.<br>- Khởi tạo database SQLite cục bộ thành công. |
| M3: API Dịch thuật & Cài đặt | Tích hợp Gemini API client và hoàn thiện Preferences Panel cùng SQLite lưu trữ lịch sử. | - Dịch thành công qua Gemini API.<br>- Lưu cấu hình Gemini API Key cá nhân vào Preferences panel.<br>- Lịch sử dịch thuật được lưu vào SQLite cục bộ và hiển thị/xóa được từ giao diện cài đặt. |
| M4: Kiểm thử, Tối ưu & Đóng gói | Kiểm thử hiệu năng, tối ưu bộ nhớ, kiểm tra bảo mật, notarize và đóng gói thành file .dmg phân phối. | - Không có lỗi nghiêm trọng (Critical/Blocker).<br>- CPU tiêu hao khi dịch thấp (<5% peak), bộ nhớ RAM tĩnh chạy ngầm <30MB.<br>- Notarize thành công từ Apple và xuất file cài đặt TranslatorAI.dmg chạy tốt trên macOS 14+. |

## Dependencies

| # | From (WBS #) | To (WBS #) | Type | Description |
| --- | --- | --- | --- | --- |
| 1 | 1.3 (Lắng nghe Phím tắt) | 2.1 (Popup dịch nhanh) | FS | Phải tích hợp được phím tắt toàn cục trước khi kích hoạt bong bóng dịch nhanh Popup HUD. |
| 2 | 2.1 (Popup dịch nhanh) | 4.1 (API Integration) | FS | Cửa sổ HUD phải sẵn sàng để nhận dữ liệu dịch thuật từ Gemini API và hiển thị lên cho người dùng. |
| 3 | 5.1 (Database SQLite) | 5.2 (Lưu trữ lịch sử) | FS | Phải khởi tạo xong cấu trúc database SQLite cục bộ trước khi thực hiện các truy vấn lưu trữ và truy vấn lịch sử dịch thuật. |
| 4 | Tất cả các tính năng chính | 6.2 (Đóng gói DMG) | FS | Toàn bộ các module chức năng phải được hoàn thành và kiểm thử trước khi tiến hành đóng gói phiên bản phát hành chính thức. |

## Delivery Assumptions

| ID | Assumption | Status | Impact If False |
| --- | --- | --- | --- |
| DA-1 | Gemini API hỗ trợ đầy đủ chức năng dịch thuật text-to-text với chất lượng tốt và thời gian phản hồi nhanh. | Hoạt động (Active) | Nếu chất lượng dịch kém hoặc API không ổn định, cần bổ sung provider khác sớm hơn dự kiến. |
| DA-2 | Không phát sinh trong MVP vì tính năng OCR đã được dời sang giai đoạn tương lai. | Không áp dụng (N/A) | Không ảnh hưởng đến phiên bản MVP hiện tại. |
| DA-3 | Khách hàng sẵn lòng tự cấu hình Gemini API Key cá nhân của họ để sử dụng dịch thuật AI. | Đã xác nhận (Confirmed) | Nếu không, chúng tôi sẽ phải thiết lập proxy server và hệ thống thanh toán để quản lý token, tăng chi phí và thay đổi hoàn toàn kiến trúc offline của app. |
