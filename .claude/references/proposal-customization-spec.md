# Spec & Context: Customizable Proposal Template implementation

Tài liệu này tóm tắt kết quả thảo luận và thiết kế về việc cho phép tùy biến cấu trúc Proposal theo từng dự án cụ thể. Mục đích là để AI ở phiên chat mới có thể đọc file này và tiếp tục công việc lập tức.

---

## 1. Vấn đề cần giải quyết
Hiện tại, cấu trúc Proposal (8 sections) đang bị hard-code cố định trong:
- Quy tắc hướng dẫn của LLM (`.agent/skills/proposal/SKILL.md`)
- File template của hệ thống (`.agent/references/proposal.md`)
- Header mặc định trong script (`.agent/scripts/presale_cli.py`)

Điều này khiến quy trình presale thiếu linh hoạt khi gặp các khách hàng có yêu cầu khác nhau (ví dụ: Startup chỉ cần proposal 4 phần ngắn gọn, hoặc Doanh nghiệp lớn yêu cầu thêm phần Giới thiệu năng lực công ty).

---

## 2. Giải pháp thống nhất (Dynamic Template)
Thay vì dùng một cấu trúc cứng hoặc lựa chọn đóng khung, chúng ta sẽ chuyển quyền kiểm soát hoàn toàn cho người dùng thông qua cơ chế tự định nghĩa template trong từng dự án:

1. **Khởi tạo (`/presale-init`)**:
   - Khi tạo một dự án mới, hệ thống tự động copy file cấu hình mặc định từ `.agent/references/proposal-template-default.md` vào thư mục của dự án tại: `projects/YYYY-MM-DD-<project-name>/workspace/proposal-template.md`.
   
2. **Người dùng tùy biến**:
   - Người dùng có thể mở file `workspace/proposal-template.md` này để thêm, bớt, đổi tên, hoặc sắp xếp lại các section theo mong muốn của khách hàng.
   
3. **Sinh Proposal (Stage 5)**:
   - LLM khi chạy Stage 5 sẽ đọc trực tiếp file `workspace/proposal-template.md` của dự án đang chạy để biết cấu trúc cần tạo là gì.
   - LLM sinh ra các file section tương ứng trong thư mục `workspace/proposal/` theo các chỉ thị định dạng và nguồn dữ liệu ghi trong template.
   
4. **Gom file & Xuất bản (`/presale-finalize`)**:
   - Script `presale_cli.py` đã có sẵn cơ chế gom file động (dynamic concat): Tự động quét toàn bộ file `.md` trong `workspace/proposal/` (loại bỏ `_index.md`) và sắp xếp theo bảng chữ cái (alphabet) để gộp lại. Do đó, chỉ cần người dùng đặt tiền tố số cho tên file (ví dụ: `01-xxx.md`, `02-xxx.md`), script sẽ hoạt động hoàn hảo mà không cần sửa đổi lớn.

---

## 3. Bản thiết kế chi tiết file `proposal-template.md`
Mỗi Section trong template được cấu trúc bằng thẻ tiêu đề H2 và các trường metadata phụ để LLM hiểu rõ nhiệm vụ:

```markdown
## 01 - Project Overview & Business Value
- file: 01-project-overview.md
- format: prose
- source: context.md, scope.md
- content: Bối cảnh dự án, Pain points và mục tiêu.
```

- **file**: Tên file đích LLM cần tạo ra (bắt buộc bắt đầu bằng prefix số để đảm bảo thứ tự concat).
- **format**: Định dạng output (prose, table, bullets, diagram).
- **source**: Các artifact làm dữ liệu nguồn (giúp tối ưu hóa token đầu vào - Input Pruning).
- **content**: Tóm tắt yêu cầu nội dung cần có.

---

## 4. Các bước triển khai tiếp theo (Next Steps)
Khi AI mới tiếp tục chat, hãy thực hiện các bước sau theo [Implementation Plan](file:///Users/rng/.gemini/antigravity/brain/a74eac9f-08ea-45df-9059-badcd83e6c12/implementation_plan.md):

1. **Tạo file template mặc định**: `.agent/references/proposal-template-default.md` (chứa cấu trúc 8 section hiện tại).
2. **Cập nhật workflow init**: Sửa `.agent/workflows/presale-init.md` để sao chép file mặc định trên vào thư mục dự án khi khởi chạy.
3. **Cập nhật proposal skill**: Sửa `.agent/skills/proposal/SKILL.md` đổi chỉ dẫn từ cấu trúc 8 phần cố định sang đọc động file `workspace/proposal-template.md` của dự án.
4. **Sửa đổi nhỏ trong CLI**: Cập nhật hàm `get_proposal_header` trong `.agent/scripts/presale_cli.py` (loại bỏ chuỗi cứng `8-Section Standardized`).
5. **Chạy thử nghiệm (Dry run)** để xác minh toàn bộ luồng hoạt động chính xác.
