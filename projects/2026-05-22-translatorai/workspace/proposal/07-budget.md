# 07 - Ngân Sách & Phân Bổ Nhân Sự

## 7.1 Chi Phí Phát Triển Nhân Sự (Resource Allocation & Development Cost)

Chi phí phát triển được tính toán theo mô hình giá cố định (Fixed Price) dựa trên tổng nỗ lực thực tế được phân rã trong WBS. Chúng tôi phân bổ đội ngũ bao gồm một lập trình viên macOS Native App Developer cấp cao (Senior) và một kỹ sư kiểm thử QA Engineer cấp trung (Middle) để thực hiện dự án này trong vòng 4 tuần, tối ưu hóa tối đa nhân sự cho dòng sản phẩm native desktop client-only.

Dưới đây là bảng tổng hợp chi phí nhân sự phát triển chi tiết cho dự án TranslatorAI (được tính bằng Việt Nam Đồng - VND):

| Vai trò (Position) | Cấp bậc (Seniority) | Đơn giá / ngày (Unit Price) | Tháng 1 (Effort) | Tổng nỗ lực (Total Effort) | Tổng chi phí (Total Cost) |
| --- | --- | --- | --- | --- | --- |
| **macOS Developer** | Senior | 3.000.000 VND | 17,0 ngày | 17,0 ngày | 51.000.000 VND |
| **QA Engineer** | Middle | 1.500.000 VND | 9,5 ngày | 9,5 ngày | 14.250.000 VND |
| **Tổng cộng** | — | — | **26,5 ngày** | **26,5 ngày** | **65.250.000 VND** |

## 7.2 Chi Phí Vận Hành Hạ Tầng (Operational Cost - Infra)

Do TranslatorAI được xây dựng theo kiến trúc local-first (ưu tiên xử lý cục bộ), ứng dụng chạy trực tiếp trên thiết bị của người dùng mà không cần kết nối tới một máy chủ trung tâm nào. Điều này giúp loại bỏ hoàn toàn chi phí thuê máy chủ, dịch vụ đám mây hay bảo trì cơ sở dữ liệu hàng tháng cho nhà phát triển sản phẩm.

Dưới đây là ước tính chi phí hạ tầng vận hành hàng tháng của hệ thống:

| Giai đoạn | Số lượng người sử dụng | Chi phí hạ tầng / tháng | Các thành phần chính |
| --- | --- | --- | --- |
| **Vận hành MVP** | Không giới hạn người dùng | **0 VND** | Ứng dụng chạy trực tiếp trên máy khách hàng, không sử dụng server trung tâm. Lịch sử dịch lưu cục bộ bằng SQLite. |

## 7.3 Chi Phí Dịch Vụ Bên Thứ Ba (3rd-Party Vendor Costs)

Để đưa ứng dụng vào hoạt động thực tế trên thiết bị macOS của người dùng mà không gặp các cảnh báo bảo mật nghiêm ngặt từ Apple, dự án cần phát sinh các khoản chi phí dịch vụ bên thứ ba dưới đây:
- **Tài khoản Apple Developer (Cá nhân hoặc Doanh nghiệp)**: Chi phí khoảng 2.500.000 VND/năm ($99/năm) trả trực tiếp cho Apple để ký số (Code Sign) và thực hiện quy trình phê duyệt Notarization cho ứng dụng, đảm bảo người cài đặt không bị thông báo phần mềm độc hại ngăn chặn.
- **Gemini API Key**: Chi phí trả tiền theo dung lượng sử dụng thực tế (pay-as-you-go). Người dùng sử dụng API key cá nhân của họ. Chi phí ước tính rất thấp cho mỗi lượt dịch thuật AI, thanh toán trực tiếp qua tài khoản Google Cloud/AI Studio của người dùng.
