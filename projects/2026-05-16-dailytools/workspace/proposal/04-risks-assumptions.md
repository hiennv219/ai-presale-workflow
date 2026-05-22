# 04 - Giả Định Chiến Lược & Quản Trị Rủi Ro

## 4.1 Giả Định Chiến Lược (Strategic Assumptions)

- **Chi phí API bên thứ ba:** Khách hàng cung cấp tài khoản và chịu toàn bộ chi phí sử dụng OpenAI API (Whisper + GPT-4o) trong quá trình phát triển, thử nghiệm và vận hành.
- **Ngôn ngữ cuộc họp:** Hệ thống hỗ trợ Tiếng Việt và Tiếng Anh — hai ngôn ngữ có độ chính xác cao nhất với OpenAI hiện tại.
- **Giới hạn thời lượng:** File ghi âm tối đa 2 giờ/file để đảm bảo nằm trong context window của GPT-4o và tránh timeout API.
- **Hạ tầng deployment:** Khách hàng cung cấp quyền truy cập hosting (Vercel, AWS hoặc tương đương) từ tuần thứ 3 để cấu hình staging và production.

## 4.2 Rủi Ro & Biện Pháp Giảm Thiểu (Risk & Mitigation)

**Chất lượng nhận diện giọng nói giảm do tiếng ồn (Mức độ: Trung bình)**
Môi trường ghi âm nhiều tạp âm, micro xa hoặc nói đè giọng có thể làm Whisper dịch sai.
*Biện pháp:* Khuyến cáo chất lượng ghi âm trên màn hình upload; Transcript Editor cho PM sửa từ sai trước khi tóm tắt.

**Chi phí API OpenAI tăng đột biến (Mức độ: Thấp)**
Sử dụng tần suất cao hoặc file dung lượng lớn liên tục có thể đẩy chi phí API ngoài kiểm soát.
*Biện pháp:* Hướng dẫn khách hàng cấu hình giới hạn chi tiêu (hard limit/soft limit) trên OpenAI Dashboard ngay từ ngày đầu.
