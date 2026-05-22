# Bối Cảnh Dự Án (Deal Context) — DailyTools

## Metadata

- **Deal ID:** DailyTools-MVP
- **Khách hàng:** DailyTools
- **Phiên bản:** 1.0
- **Giai đoạn hiện tại:** Stage 2: Context
- **Cập nhật lần cuối:** 2026-05-21

## Rolling Summary
Khách hàng muốn xây dựng DailyTools MVP - một Web App hỗ trợ PM tóm tắt các cuộc họp dự án từ các file âm thanh/văn bản tải lên trực tiếp (mp3, wav, txt). Hệ thống sử dụng dịch vụ Cloud API của OpenAI (Whisper cho STT và GPT-4o cho tóm tắt). Dự án có độ phức tạp Light, thời gian triển khai 1-1.5 tháng, chỉ phục vụ vai trò PM và tối giản các chức năng phân quyền, tích hợp.

## Confirmed Requirements (Yêu cầu đã xác nhận)

| ID | Yêu cầu | Nguồn | Ưu tiên |
| --- | --- | --- | --- |
| R-1 | Hệ thống chạy dưới dạng Web Application (responsive trên máy tính và thiết bị di động). | Q1 | High |
| R-2 | Tiếp nhận đầu vào là các file âm thanh (mp3, wav) hoặc file văn bản (txt) cuộc họp tải lên trực tiếp. | Q2 | High |
| R-3 | Chỉ quản lý và phục vụ duy nhất 1 vai trò người dùng (PM) đăng nhập để sử dụng công cụ. | Q3 | High |
| R-4 | Tích hợp dịch vụ API bên thứ ba (OpenAI Whisper & GPT-4o) để chuyển đổi STT và tóm tắt nội dung chính + Action Items. | Q4 | High |
| R-5 | Tiến độ bàn giao gấp trong vòng 1 - 1.5 tháng với ngân sách tối ưu. | Q5 | High |

## Unconfirmed Requirements (Yêu cầu chưa xác nhận)
*(Không có)*

## Scope Register (Phân định Phạm vi)

### In Scope (Trong Phạm vi MVP)

| ID | Tính năng / Công việc | Nguồn | Trạng thái |
| --- | --- | --- | --- |
| S-1 | Đăng nhập & Quản lý tài khoản (Đơn giản cho PM) | R-3 | Approved |
| S-2 | Module tải file cuộc họp lên hệ thống (hỗ trợ mp3, wav, txt) | R-2 | Approved |
| S-3 | Tích hợp API OpenAI Whisper để chuyển đổi audio thành text | R-4 | Approved |
| S-4 | Tích hợp API OpenAI GPT-4o để tóm tắt cuộc họp và xuất danh sách Action Items | R-4 | Approved |
| S-5 | Giao diện Dashboard hiển thị lịch sử cuộc họp, chi tiết văn bản tóm tắt & tính năng sao chép nhanh | R-1 | Approved |

### Out Of Scope (Ngoài Phạm vi MVP)

| ID | Tính năng / Nội dung | Lý do tạm hoãn |
| --- | --- | --- |
| O-1 | Ghi âm cuộc họp trực tiếp trên Web | Giảm độ phức tạp kỹ thuật liên quan đến Microphone API của trình duyệt. |
| O-2 | Bot tự động tham gia các ứng dụng họp trực tuyến (Zoom, Meet, Teams) | Tích hợp phức tạp, vượt quá thời gian bàn giao 1.5 tháng. |
| O-3 | Phân quyền vai trò người dùng phức tạp (Member/Admin) | MVP chỉ tập trung phục vụ đối tượng PM. |
| O-4 | Tích hợp tạo task trực tiếp trên Jira/Trello hoặc gửi Slack | Tránh phình to phạm vi (scope creep) ở giai đoạn đầu. |

### Future Phase (Các Giai đoạn Tiếp theo)
- Tự động hóa tích hợp bot họp trực tuyến (Zoom, Meet, Teams).
- Quản lý phân quyền cho cả thành viên tham gia cuộc họp truy cập xem tóm tắt.
- Tích hợp với các công cụ quản lý dự án (Jira, Trello, Slack).

### Pending Scope Changes
*(Không có)*

## Assumptions (Các Giả định Chiến lược)

| ID | Giả định | Trạng thái | Mức độ ảnh hưởng nếu sai |
| --- | --- | --- | --- |
| A-1 | Khách hàng trực tiếp chi trả chi phí API OpenAI thông qua tài khoản của khách hàng. | Active | High |
| A-2 | Dữ liệu cuộc họp tải lên chủ yếu sử dụng ngôn ngữ Tiếng Việt và Tiếng Anh. | Active | Medium |
| A-3 | Thời lượng cuộc họp không quá 2 giờ/file để đảm bảo nằm trong giới hạn xử lý token của mô hình AI. | Active | Medium |

## Risks (Rủi ro & Biện pháp Giảm thiểu)

| ID | Rủi ro | Mức độ | Biện pháp giảm thiểu |
| --- | --- | --- | --- |
| Risk-1 | Chất lượng chuyển giọng nói thành văn bản (STT) thấp do file âm thanh bị ồn hoặc giọng địa phương quá nặng. | Medium | Khuyến cáo chất lượng ghi âm đầu vào trên giao diện; Hỗ trợ PM tự chỉnh sửa văn bản gốc trước khi tóm tắt nếu cần. |
| Risk-2 | Chi phí API vượt quá ngân sách nếu số lượng cuộc họp phát sinh quá lớn. | Low | Thiết lập hạn mức mức trần (spending limits) trên tài khoản API OpenAI của khách hàng. |

## Decisions (Quyết định đã thống nhất)

| ID | Quyết định | Nguồn | Ngày thống nhất | Ảnh hưởng |
| --- | --- | --- | --- | --- |
| D-1 | Phát triển Web Application thay vì Mobile App | Q1 | 2026-05-21 | Tối ưu chi phí, giao diện dễ thao tác. |
| D-2 | Nhận đầu vào là file tải lên (mp3, wav, txt) | Q2 | 2026-05-21 | Bỏ qua phần Microphone API phức tạp. |
| D-3 | Hệ thống chỉ có 1 vai trò người dùng (PM) | Q3 | 2026-05-21 | Đơn giản hóa kiến trúc bảo mật & cơ sở dữ liệu. |
| D-4 | Sử dụng Cloud API của OpenAI (Whisper + GPT-4o) | Q4 | 2026-05-21 | Tốc độ dev nhanh, chất lượng dịch tiếng Việt tốt nhất hiện tại. |
| D-5 | Tiến độ phát triển 1-1.5 tháng | Q5 | 2026-05-21 | Tập trung hoàn toàn vào phạm vi tối giản, không phát sinh tính năng phụ. |

## Latest Artifact Summaries

| Artifact | Phiên bản | Trạng thái | Tóm tắt |
| --- | --- | --- | --- |
| Client Input | v1.0 | Done | Yêu cầu gốc về MVP DailyTools tóm tắt cuộc họp. |
| Discovery Output | v1.0 | Done | Khảo sát BA và phân loại độ phức tạp Light. |
| Backlog Questions | v2.0 | Done | Danh sách 5 câu hỏi Stop Rule đã được phản hồi và giải quyết hoàn toàn. |
| Context Update | v1.0 | Done | Deal Context ghi nhận bối cảnh, yêu cầu, phạm vi và giả định đã thống nhất. |
