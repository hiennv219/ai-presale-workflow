# Work Breakdown Structure (WBS) — DailyTools

## Metadata

- **Artifact ID:** wbs-dailytools-v1
- **Version:** 1.0
- **Status:** Draft
- **Context Version:** 1.0
- **Date:** 2026-05-21

## WBS

| # | Category | Module | Function | Sub-function | Description | Note |
| --- | --- | --- | --- | --- | --- | --- |
| 1.1 | Foundation | Project Setup | Repository Init | — | Khởi tạo Git repository, cấu hình project structure (Web App) và thiết lập CI/CD pipeline cơ bản.<br>**Role:** Backend Developer<br>**Estimate:** 1–2 days<br>**Scope Ref:** S-1 | User Story: Là lập trình viên, tôi muốn có cấu trúc mã nguồn chuẩn để bắt đầu phát triển hệ thống. |
| 1.2 | Foundation | Project Setup | Database Setup | — | Khởi tạo và thiết lập database (PostgreSQL/MongoDB), thiết kế cấu trúc bảng User, Meeting và Summary.<br>**Role:** Backend Developer<br>**Estimate:** 1–2 days<br>**Scope Ref:** S-1 | User Story: Là lập trình viên, tôi muốn cấu trúc cơ sở dữ liệu được định nghĩa sẵn để lưu trữ thông tin PM và lịch sử họp. |
| 2.1 | Common | Authentication | Login UI | — | Xây dựng giao diện trang đăng nhập cho PM với các ô nhập Email, Mật khẩu và thông báo lỗi.<br>**Role:** Frontend Developer<br>**Estimate:** 1–2 days<br>**Scope Ref:** S-1 | User Story: Là PM, tôi muốn có màn hình đăng nhập để điền thông tin tài khoản của mình. |
| 2.2 | Common | Authentication | Login API | — | Phát triển API đăng nhập, kiểm tra thông tin tài khoản và trả về JWT token để duy trì phiên làm việc.<br>**Role:** Backend Developer<br>**Estimate:** 1–2 days<br>**Scope Ref:** S-1 | User Story: Là PM, tôi muốn hệ thống xác thực tài khoản của tôi và cấp quyền truy cập Dashboard. |
| 2.3 | Common | Authentication | Logout | — | Xây dựng cơ chế đăng xuất, hủy JWT token ở client và chuyển hướng về màn hình đăng nhập.<br>**Role:** Frontend Developer<br>**Estimate:** 0.5 days<br>**Scope Ref:** S-1 | User Story: Là PM, tôi muốn đăng xuất khỏi hệ thống để bảo vệ tài khoản khi không sử dụng. |
| 3.1 | Core | Meeting Processing | File Upload UI | — | Xây dựng khu vực tải file kéo thả (drag-and-drop) trên Web, giới hạn dung lượng file (max 100MB) và kiểm tra định dạng (.mp3, .wav, .txt).<br>**Role:** Frontend Developer<br>**Estimate:** 1–2 days<br>**Scope Ref:** S-2 | User Story: Là PM, tôi muốn kéo thả file ghi âm cuộc họp trực tiếp trên Web để hệ thống bắt đầu xử lý. |
| 3.2 | Core | Meeting Processing | Upload API | — | Xây dựng API tiếp nhận file tải lên từ client, thực hiện lưu trữ tạm thời trên server hoặc cloud storage.<br>**Role:** Backend Developer<br>**Estimate:** 1–2 days<br>**Scope Ref:** S-2 | User Story: Là PM, tôi muốn file ghi âm của mình được tải lên máy chủ hệ thống ổn định, không bị ngắt quãng. |
| 3.3 | Core | Meeting Processing | Whisper Integration | — | Tích hợp OpenAI Whisper API để gửi file ghi âm tiếng Việt/tiếng Anh và nhận về văn bản thô (transcript).<br>**Role:** Backend Developer<br>**Estimate:** 2–3 days<br>**Scope Ref:** S-3 | User Story: Là hệ thống, tôi muốn chuyển đổi giọng nói trong cuộc họp thành văn bản dạng text để AI có thể đọc hiểu. |
| 3.4 | Core | Meeting Processing | GPT-4o Integration | — | Tích hợp OpenAI GPT-4o API để tóm tắt văn bản họp thành nội dung chính (Summary) và danh sách đầu việc (Action Items).<br>**Role:** Backend Developer<br>**Estimate:** 2–3 days<br>**Scope Ref:** S-4 | User Story: Là PM, tôi muốn AI tự động trích xuất các ý chính và công việc cần làm từ cuộc họp để tiết kiệm thời gian ghi chép. |
| 3.5 | Core | Meeting Processing | Transcript Edit UI | — | Xây dựng giao diện hiển thị text transcript gốc, cho phép PM chỉnh sửa văn bản trực tiếp trước khi gửi yêu cầu AI tóm tắt.<br>**Role:** Frontend Developer<br>**Estimate:** 1–2 days<br>**Scope Ref:** S-6 | User Story: Là PM, tôi muốn có thể chỉnh sửa lại các từ ngữ AI nhận diện sai trong transcript trước khi tạo tóm tắt cuối cùng. |
| 4.1 | Core | Dashboard & History | History List UI | — | Xây dựng màn hình Dashboard hiển thị danh sách các cuộc họp PM đã xử lý kèm thông tin ngày tháng, thời lượng, định dạng file.<br>**Role:** Frontend Developer<br>**Estimate:** 1–2 days<br>**Scope Ref:** S-5 | User Story: Là PM, tôi muốn nhìn thấy danh sách các cuộc họp cũ đã xử lý ngay khi đăng nhập vào hệ thống. |
| 4.2 | Core | Dashboard & History | History List API | — | Phát triển API truy vấn danh sách cuộc họp của tài khoản PM đang đăng nhập, hỗ trợ phân trang (pagination).<br>**Role:** Backend Developer<br>**Estimate:** 1–2 days<br>**Scope Ref:** S-5 | User Story: Là PM, tôi muốn danh sách cuộc họp cũ tải nhanh và có thể chuyển qua các trang lịch sử. |
| 4.3 | Core | Dashboard & History | Detail View UI | — | Thiết kế màn hình xem chi tiết kết quả tóm tắt cuộc họp gồm hai phần chính: Văn bản tóm tắt ý chính và Danh sách Action Items dạng checklist.<br>**Role:** Frontend Developer<br>**Estimate:** 1–2 days<br>**Scope Ref:** S-6 | User Story: Là PM, tôi muốn xem kết quả tóm tắt cuộc họp và danh sách việc cần làm một cách trực quan trên một màn hình. |
| 4.4 | Core | Dashboard & History | Detail View API | — | Phát triển API lấy thông tin chi tiết của một cuộc họp cụ thể dựa theo Meeting ID đã phân quyền.<br>**Role:** Backend Developer<br>**Estimate:** 1 day<br>**Scope Ref:** S-6 | User Story: Là PM, tôi muốn hệ thống tải thông tin chi tiết cuộc họp chính xác khi click chọn từ danh sách. |
| 4.5 | Core | Dashboard & History | Copy to Clipboard | — | Tích hợp tính năng nhấp chuột để sao chép nhanh (one-click copy) toàn bộ phần Tóm tắt hoặc danh sách Action Items vào clipboard.<br>**Role:** Frontend Developer<br>**Estimate:** 0.5–1 day<br>**Scope Ref:** S-7 | User Story: Là PM, tôi muốn copy nhanh kết quả tóm tắt cuộc họp để dán trực tiếp gửi cho team qua Zalo/Slack. |
| 5.1 | Testing | QA | Integration Testing | — | Thực hiện kiểm thử tích hợp toàn diện hệ thống: luồng đăng nhập, tải file, gọi API Whisper/GPT-4o, hiển thị và copy kết quả.<br>**Role:** QA Engineer<br>**Estimate:** 3–4 days<br>**Scope Ref:** All | User Story: Là đội dự án, tôi muốn kiểm thử kỹ toàn bộ tính năng để đảm bảo không có lỗi nghiêm trọng khi bàn giao. |
| 5.2 | Testing | Go-Live | Production Deployment | — | Triển khai Web App lên môi trường production (Vercel/AWS), cấu hình domain và cài đặt biến môi trường API OpenAI thực tế.<br>**Role:** Backend Developer<br>**Estimate:** 1–2 days<br>**Scope Ref:** All | User Story: Là PM, tôi muốn truy cập DailyTools thông qua một tên miền internet thực tế để sử dụng hàng ngày. |

## Milestones

| Milestone | Description | Exit Criteria |
| --- | --- | --- |
| **M1: Foundation & Auth** | Thiết lập môi trường dự án và hoàn thiện đăng nhập | Khởi tạo xong Repository, DB; hoàn thiện giao diện và API đăng nhập PM. (WBS 1.1, 1.2, 2.1, 2.2, 2.3) |
| **M2: Core Processing** | Hoàn thành tích hợp API OpenAI Whisper & GPT-4o | Hoàn thiện module tải file ghi âm, API Speech-to-Text Whisper, API tóm tắt GPT-4o và trình sửa transcript. (WBS 3.1, 3.2, 3.3, 3.4, 3.5) |
| **M3: Dashboard & History** | Hoàn thiện Dashboard lịch sử họp và chia sẻ | Hoàn thiện màn hình danh sách cuộc họp, xem chi tiết tóm tắt và tính năng Sao chép nhanh. (WBS 4.1, 4.2, 4.3, 4.4, 4.5) |
| **M4: QA & Go-Live** | Kiểm thử tích hợp và đưa ứng dụng lên internet | 100% kịch bản kiểm thử tích hợp vượt qua; deploy thành công ứng dụng lên server production. (WBS 5.1, 5.2) |

## Dependencies

| # | From (WBS #) | To (WBS #) | Type | Description |
| --- | --- | --- | --- | --- |
| 1 | 2.1 (Login UI) | 1.1 (Repo Init) | FS (Finish-to-Start) | Cần có repo để code giao diện đăng nhập. |
| 2 | 2.2 (Login API) | 1.2 (DB Setup) | FS (Finish-to-Start) | Cần cấu hình DB trước khi viết API xác thực. |
| 3 | 3.2 (Upload API) | 1.1 (Repo Init) | FS (Finish-to-Start) | Cần repo để triển khai API upload file. |
| 4 | 3.3 (Whisper API) | 3.2 (Upload API) | FS (Finish-to-Start) | API chuyển giọng nói cần file đã tải lên thành công để xử lý. |
| 5 | 3.4 (GPT-4o API) | 3.3 (Whisper API) | FS (Finish-to-Start) | Cần văn bản transcript từ Whisper để AI tiến hành tóm tắt. |
| 6 | 3.5 (Transcript Edit UI) | 3.1 (Upload UI) & 3.3 (Whisper) | FS (Finish-to-Start) | Cần giao diện tải file và văn bản transcript từ Whisper để PM chỉnh sửa. |
| 7 | 4.1 (History List UI) | 1.1 (Repo Init) | FS (Finish-to-Start) | Cần repo để phát triển trang Dashboard. |
| 8 | 4.2 (History List API) | 1.2 (DB Setup) | FS (Finish-to-Start) | Cần DB để truy vấn danh sách cuộc họp cũ. |
| 9 | 4.3 (Detail UI) | 4.1 (History List UI) | FS (Finish-to-Start) | Trang chi tiết kế thừa cấu trúc trang Dashboard lịch sử. |
| 10 | 4.4 (Detail API) | 4.2 (History List API) | FS (Finish-to-Start) | API chi tiết phụ thuộc vào cấu trúc API danh sách lịch sử. |
| 11 | 4.5 (Copy Clipboard) | 4.3 (Detail UI) | FS (Finish-to-Start) | Cần có giao diện chi tiết để tích hợp nút Sao chép nhanh. |
| 12 | 5.1 (Integration Testing) | Tất cả phát triển | FS (Finish-to-Start) | Cần hoàn thành toàn bộ code tính năng trước khi chạy test tích hợp. |
| 13 | 5.2 (Production Deploy) | 5.1 (QA) | FS (Finish-to-Start) | Hệ thống phải vượt qua QA trước khi deploy lên internet cho PM sử dụng. |

## Delivery Assumptions

| ID | Giả định | Trạng thái | Mức độ ảnh hưởng nếu sai |
| --- | --- | --- | --- |
| DA1 | Tài khoản API OpenAI của khách hàng đã nạp sẵn số dư và được cấu hình từ ngày đầu tiên. | Active | Trễ tiến độ kiểm thử tích hợp các tính năng AI (STT & GPT-4o). |
| DA2 | Khách hàng sẵn sàng cung cấp các file âm thanh cuộc họp thực tế bằng tiếng Việt (khoảng 3-5 file) làm dữ liệu mẫu để QA test chất lượng tóm tắt. | Active | Kết quả tóm tắt thực tế có thể không khớp với kỳ vọng của PM nếu chỉ dùng file mẫu giả lập. |
| DA3 | Môi trường production (Vercel/AWS) do khách hàng cung cấp quyền truy cập trong tuần thứ 3. | Active | Trễ tiến độ deploy go-live ở Milestone 4. |
