# 07 - Ngân Sách & Phân Bổ Nhân Sự

## 7.1 Chi Phí Phát Triển Nhân Sự (Resource Allocation & Development Cost)

Chi phí phát triển được tính toán dựa trên mô hình giá cố định (Fixed Price) tương ứng với thời lượng và nỗ lực thực tế được phân rã trong WBS. Chúng tôi phân bổ đội ngũ nhân sự tối giản và chuyên môn hóa cao bao gồm một lập trình viên Backend cấp cao (Senior), một lập trình viên Frontend cấp trung (Middle) và một kỹ sư kiểm thử (QA Middle) để đảm bảo chất lượng kỹ thuật cao nhất và tiến độ bàn giao trong vòng 1 tháng.

Dưới đây là bảng tổng hợp chi phí nhân sự phát triển chi tiết cho dự án DailyTools MVP (được tính bằng Việt Nam Đồng - VND):

| Vai trò (Position) | Cấp bậc (Seniority) | Đơn giá / ngày (Unit Price) | Tháng 1 (Effort) | Tổng nỗ lực (Total Effort) | Tổng chi phí (Total Cost) |
| --- | --- | --- | --- | --- | --- |
| **Backend Developer** | Senior | 3.000.000 VND | 15 ngày | 15 ngày | 45.000.000 VND |
| **Frontend Developer** | Middle | 2.000.000 VND | 10 ngày | 10 ngày | 20.000.000 VND |
| **QA Engineer** | Middle | 1.500.000 VND | 5 ngày | 5 ngày | 7.500.000 VND |
| **Tổng cộng** | — | — | **30 ngày** | **30 ngày** | **72.500.000 VND** |

## 7.2 Chi Phí Vận Hành Hạ Tầng (Operational Cost - Infra)

Để tối ưu hóa chi phí vận hành cho phiên bản MVP, kiến trúc hệ thống tận dụng tối đa các chương trình miễn phí (Free Tier) từ các nhà cung cấp dịch vụ cloud. Frontend ứng dụng Next.js được triển khai miễn phí trên hạ tầng Vercel. Máy chủ API Backend và PostgreSQL Database được khuyến nghị chạy trên các gói server nhỏ gọn phù hợp với lượng người dùng nội bộ thấp.

Dưới đây là ước tính chi phí hạ tầng vận hành hàng tháng của hệ thống:

| Giai đoạn | Số lượng PM sử dụng | Chi phí hạ tầng / tháng | Các thành phần chính |
| --- | --- | --- | --- |
| **MVP Vận hành** | 1 – 5 người dùng | Khoảng 0 – 350.000 VND (0 - $15) | Frontend deploy miễn phí trên Vercel; Backend & PostgreSQL DB chạy trên AWS Free Tier hoặc gói basic của Render/DigitalOcean. |

## 7.3 Chi Phí Dịch Vụ Bên Thứ Ba (3rd-Party Vendor Costs)

Bên cạnh chi phí phát triển và hạ tầng máy chủ, hệ thống có phát sinh các chi phí sử dụng dịch vụ API dịch thuật và phân tích của OpenAI:
- **Dịch vụ OpenAI API (STT Whisper & GPT-4o)**: Chi phí thanh toán dựa trên lượng sử dụng thực tế (pay-as-you-go). Chi phí ước tính rất thấp, khoảng 500 VND cho mỗi phút dịch âm thanh (Whisper) và 1.000 - 2.000 VND cho mỗi cuộc gọi tóm tắt văn bản (GPT-4o). Ước tính tổng chi phí sử dụng thực tế khoảng 50.000 - 100.000 VND/PM/tháng. Dịch vụ này sẽ được thanh toán trực tiếp qua tài khoản thẻ liên kết OpenAI của khách hàng.
- **Chi phí mua tên miền (Domain Name)**: Khoảng 250.000 VND/năm (chi phí phát sinh nếu khách hàng chưa sở hữu sẵn tên miền riêng).
