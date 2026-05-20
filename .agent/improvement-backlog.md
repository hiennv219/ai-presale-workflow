# Pipeline Improvement Backlog

> Ghi nhận từ review ngày 2026-05-20. Sửa đổi khi có thời gian.

## Đã có / Đã implement

- [x] #7 — Cascade preview trước khi thực hiện update (presale-update Step 1 đã có impact summary + wait confirm)
- [x] #1 — Cho phép paste input trực tiếp trong `/presale-run` (updated presale-run.md + presale-init.md)
- [x] #2 — `/presale-preview` command chạy script concat on-demand, không cần gate (presale-preview.md + CLAUDE.md)
- [x] #3 — Deal complexity auto-classification sau Discovery (discovery SKILL.md + wbs SKILL.md, min level 3)
- [x] #4 — Thêm "Next Action" + "Blockers" + "Deal Complexity" vào status.md template (không cần command riêng)

## Cần sửa

### #5 — Question format linh hoạt
- **Vấn đề**: Bắt buộc 3 options + 1 rec cho mọi câu hỏi → câu hỏi open-ended bị ép format giả tạo
- **Giải pháp**: Cho phép 3 loại: open-ended, yes/no confirm, multi-option (giữ 3-option cho decisions)
- **Effort**: Thấp

### #6 — PDF export
- **Vấn đề**: Chỉ có HTML, presale cần PDF gửi email
- **Giải pháp**: Thêm `--pdf` flag vào presale_cli.py, dùng puppeteer (đã implement)
- **Effort**: Trung bình

### #8 — Slide deck generation ✅
- **Vấn đề**: Presale luôn cần deck cho meeting, hiện phải làm tay
- **Giải pháp**: `/presale-slides` — skill tóm tắt proposal → slide Markdown, handoff cho GPT/Gemini
- **Implemented**: workflow + skill (17 slides, co giãn theo nội dung)

### #10 — Multi-project dashboard
- **Vấn đề**: Presale handle 3-5 deal cùng lúc, không có overview
- **Giải pháp**: `/presale-dashboard` scan tất cả projects/, hiển thị table: deal, stage, last updated, blockers
- **Effort**: Cao

### #11 — Input Pruning (Chọn lọc Input động cho từng Section Proposal)
- **Vấn đề**: LLM đọc toàn bộ workspace (~100 KB) cho mọi section ở Stage 5, lãng phí token.
- **Giải pháp**: Cấu hình bảng Input Dependency trong `proposal/SKILL.md` để lọc file đầu vào tương ứng (Overview chỉ đọc context+scope, Budget chỉ đọc wbs, v.v.).
- **Effort**: Thấp (Tiết kiệm ~67% input token Stage 5)

### #12 — Offline Scope Coverage Matrix & Local Linter
- **Vấn đề**: Việc kiểm tra chéo Scope↔WBS và WBS↔Budget hiện do LLM thực hiện, gây tốn token và chậm.
- **Giải pháp**: Viết script Python local (tích hợp vào `presale_cli.py --lint`) để tự động hóa các checks có tính quy tắc cứng, chặn lỗi trước khi gọi Stage 6 Review.
- **Effort**: Trung bình (Tiết kiệm ~30k tokens/lượt review, tốc độ <1s)

### #13 — Batch Proposal Generation (Sinh nhiều Section trong 1 Turn)
- **Vấn đề**: Sinh 8 section bằng 8 API calls riêng lẻ gây lặp lại system prompt và rules lãng phí.
- **Giải pháp**: Cho phép LLM xuất nội dung của nhiều section cùng lúc trong 1 turn bằng các thẻ đánh dấu (`<!-- SECTION:XX -->`), sau đó dùng script local phân tách ra.
- **Effort**: Trung bình (Tiết kiệm ~96k tokens/dự án)

### #14 — Incremental Translation (Dịch theo Section)
- **Vấn đề**: Dịch thuật đang thực hiện trên toàn bộ file proposal-full lớn, mỗi lần sửa đổi nhỏ phải chạy lại toàn bộ.
- **Giải pháp**: Hỗ trợ dịch từng file section độc lập rồi concat sau, tránh dịch lại các phần không đổi.
- **Effort**: Thấp (Tiết kiệm ~20k tokens mỗi lần sửa dịch)

