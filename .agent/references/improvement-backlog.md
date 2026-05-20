# Pipeline Improvement Backlog

> Ghi nhận từ review ngày 2026-05-20. Sửa đổi khi có thời gian.

## Đã có sẵn

- [x] #7 — Cascade preview trước khi thực hiện update (presale-update Step 1 đã có impact summary + wait confirm)

## Cần sửa

### #1 — Cho phép paste input trực tiếp trong `/presale-run`
- **Vấn đề**: Phải tạo file `_source/client-input.md` trước rồi mới chạy run — thêm 1 bước không cần thiết
- **Giải pháp**: `/presale-run` detect nếu chưa có input file → cho user paste inline → AI tự tạo file
- **Effort**: Thấp

### #9 — Session handoff file (deal-context.md auto-maintained)
- **Vấn đề**: Đổi session mất toàn bộ context, AI phải re-read tất cả artifacts
- **Giải pháp**: Sau mỗi stage, auto-write/update `workspace/context.md` với rolling summary đủ để resume
- **Effort**: Trung bình

### #2 — Auto-generate proposal-full.md cho review (không cần pass gate)
- **Vấn đề**: Muốn đọc full proposal phải finalize → phải pass review → nhưng chưa review xong vì chưa đọc full
- **Giải pháp**: Tạo `proposal-full.md` tự động sau mỗi lần viết/update section, không yêu cầu gate
- **Effort**: Thấp

### #3 — Deal profile (light/standard/enterprise) ở init
- **Vấn đề**: Deal nhỏ vẫn phải chạy đủ 6 stage, quá nặng
- **Giải pháp**: `/presale-init` hỏi thêm deal size → auto-skip technical, wireframe, detailed WBS cho deal light
- **Effort**: Trung bình

### #4 — `/presale-status` command
- **Vấn đề**: Không có cách nhanh biết đang ở đâu, cần làm gì tiếp
- **Giải pháp**: Command đọc status.md + artifacts, output 1 block: stage hiện tại, % hoàn thành, next action, blockers
- **Effort**: Thấp

### #5 — Question format linh hoạt
- **Vấn đề**: Bắt buộc 3 options + 1 rec cho mọi câu hỏi → câu hỏi open-ended bị ép format giả tạo
- **Giải pháp**: Cho phép 3 loại: open-ended, yes/no confirm, multi-option (giữ 3-option cho decisions)
- **Effort**: Thấp

### #6 — PDF export
- **Vấn đề**: Chỉ có HTML, presale cần PDF gửi email
- **Giải pháp**: Thêm `--pdf` flag vào presale_helper.py, dùng puppeteer hoặc wkhtmltopdf
- **Effort**: Trung bình

### #8 — Slide deck generation
- **Vấn đề**: Presale luôn cần deck cho meeting, hiện phải làm tay
- **Giải pháp**: Skill mới tóm tắt proposal → slide structure (Marp hoặc reveal.js markdown)
- **Effort**: Cao

### #10 — Multi-project dashboard
- **Vấn đề**: Presale handle 3-5 deal cùng lúc, không có overview
- **Giải pháp**: `/presale-dashboard` scan tất cả projects/, hiển thị table: deal, stage, last updated, blockers
- **Effort**: Cao
