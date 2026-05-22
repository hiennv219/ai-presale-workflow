# Bối Cảnh Dự Án (Deal Context) — TranslatorAI

## Metadata

- **Deal ID:** deal-translatorai-v1
- **Customer:** TranslatorAI
- **Context Version:** 1.2
- **Current Stage:** Stage 2: Context (Updated)
- **Last Updated:** 2026-05-22

## Rolling Summary

TranslatorAI là ứng dụng macOS desktop hỗ trợ dịch thuật tức thời dạng in-place (dịch tại chỗ qua bôi đen và phím tắt) nhằm bảo mật thông tin. Tính năng nhận diện chữ qua chụp màn hình (OCR) đã được lùi lại cho các giai đoạn phát triển trong tương lai. Ứng dụng sử dụng Gemini API (qua API key của khách hàng) làm nguồn dịch chính trong MVP, với kiến trúc multi-provider mở để dễ dàng bổ sung thêm nguồn dịch (OpenAI, Google Translate, v.v.) ở các giai đoạn sau. Dự án thuộc phân khúc độ phức tạp Light, phát triển native bằng Swift/AppKit cho macOS 14+, lộ trình bàn giao nhanh 1 - 1.5 tháng.

## Confirmed Requirements (Yêu cầu đã xác nhận)

| ID | Yêu cầu (Requirement) | Nguồn (Source) | Độ ưu tiên |
| --- | --- | --- | --- |
| CR1 | Chạy độc lập dưới dạng phần mềm macOS desktop. | Yêu cầu khách hàng | Must-have |
| CR2 | Dịch tại chỗ: Bôi đen chữ ở ứng dụng bất kỳ + ấn phím tắt $\rightarrow$ Hiện bong bóng popup bản dịch ngay cạnh con trỏ. | Yêu cầu khách hàng | Must-have |
| CR3 | [DEFERRED] Dịch OCR: Chụp vùng màn hình bất kỳ $\rightarrow$ Tự động quét chữ và dịch (Lùi lại ở giai đoạn tương lai). | Yêu cầu khách hàng | Future Phase |
| CR4 | Sử dụng Gemini API (qua API key của khách hàng) làm nguồn dịch chính trong MVP. Kiến trúc multi-provider mở để bổ sung thêm nguồn dịch ở giai đoạn sau. | Yêu cầu khách hàng | Must-have |
| CR5 | Bảo mật: Dữ liệu dịch không lưu trên server mà chỉ lưu lịch sử cục bộ trên máy tính của người dùng. | Yêu cầu khách hàng | Must-have |

## Unconfirmed Requirements

*(Không có)*

## Scope Register

### In Scope

| ID | Tính năng (Item) | Nguồn (Source) | Trạng thái |
| --- | --- | --- | --- |
| S1 | Kiến trúc Native Desktop App (Swift/AppKit) | D1 | Approved |
| S2 | Cơ chế lắng nghe Phím tắt hệ thống (dịch bôi đen) & Popup HUD cạnh con trỏ | CR2, D3 | Approved |
| S3 | Client dịch thuật: Gemini API (User Key), kiến trúc multi-provider mở | CR4 | Approved |
| S4 | Cơ sở dữ liệu SQLite lưu lịch sử dịch thuật cục bộ | CR5 | Approved |
| S5 | Màn hình cài đặt (Setting): cấu hình Gemini API key, quản lý lịch sử, đổi phím tắt | CR4, CR5 | Approved |

### Out Of Scope

| ID | Tính năng (Item) | Lý do |
| --- | --- | --- |
| O1 | Máy chủ trung tâm lưu lịch sử hoặc đồng bộ tài khoản | Vi phạm yêu cầu bảo mật cục bộ của khách hàng và làm tăng chi phí vận hành. |
| O2 | Tự phát hành API key miễn phí cho người dùng | Chi phí vận hành AI rất lớn, người dùng bắt buộc dùng key cá nhân nếu muốn dịch AI. |

### Future Phase

| ID | Tính năng (Item) | Lý do |
| --- | --- | --- |
| FP1 | Hỗ trợ hệ điều hành Windows | Hiện tại tập trung 100% tài nguyên tối ưu cho người dùng macOS. |
| FP2 | Tích hợp dịch giọng nói thời gian thực (Speech Translation) | Đòi hỏi tài nguyên lớn, không nằm trong MVP. |
| FP3 | Module Chụp vùng màn hình & Tích hợp Apple Vision OCR (Offline) | Khách hàng quyết định dời tính năng OCR sang giai đoạn sau để rút ngắn thời gian phát hành MVP. |
| FP4 | Trình chỉnh sửa văn bản gốc trực tiếp trên Popup | Đi kèm với tính năng OCR, dời sang giai đoạn sau. |
| FP5 | Tích hợp Google Translate (miễn phí) | Khách hàng quyết định ưu tiên Gemini API trước, Google Translate sẽ bổ sung ở phase sau. |
| FP6 | Tích hợp OpenAI API | Bổ sung thêm provider dịch AI sau khi MVP ổn định với Gemini. |

### Pending Scope Changes

*(Không có)*

## Assumptions (Giả định)

| ID | Giả định (Assumption) | Trạng thái | Tác động nếu sai (Impact) |
| --- | --- | --- | --- |
| A1 | Người dùng tự chịu chi phí API Gemini khi sử dụng dịch thuật AI. | Active | Người dùng không dùng được tính năng dịch nếu không có key. |
| A2 | Gemini API hỗ trợ đầy đủ chức năng dịch thuật text-to-text với chất lượng tương đương hoặc tốt hơn các provider khác. | Active | Nếu chất lượng dịch kém, cần bổ sung provider khác sớm hơn dự kiến. |
| A3 | Khách hàng chấp nhận ứng dụng chạy từ macOS 14 (Sonoma) trở lên để dùng thư viện native mượt mà. | Active | Nếu cần hỗ trợ macOS cũ hơn (ví dụ 10.15), nỗ lực phát triển native sẽ tăng do API thay đổi. |

## Risks (Rủi ro)

| ID | Rủi ro (Risk) | Mức độ | Biện pháp giảm thiểu (Mitigation) |
| --- | --- | --- | --- |
| R1 | Hệ thống macOS yêu cầu cấp quyền Accessibility (Trợ năng) để lắng nghe phím tắt toàn cục và lấy chữ bôi đen. | Medium | Xây dựng màn hình Onboarding hướng dẫn trực quan từng bước cho người dùng cấp quyền trong System Settings khi mở app lần đầu. |

## Decisions (Quyết định)

| ID | Quyết định (Decision) | Nguồn (Source) | Ngày | Tác động |
| --- | --- | --- | --- | --- |
| D1 | Phát triển native bằng Swift/AppKit cho macOS 14+. | Khảo sát | 2026-05-22 | Ứng dụng siêu nhẹ (<20MB), hiệu năng tối đa. |
| D2 | Tạm hoãn OCR để làm ở giai đoạn tương lai. | Khảo sát | 2026-05-22 | Giảm thời gian phát triển và độ phức tạp cho phiên bản MVP. |
| D3 | Hiển thị dạng cửa sổ HUD Popup không viền cạnh con trỏ chuột. | Khảo sát | 2026-05-22 | Tối ưu hóa trải nghiệm tiện ích tại chỗ. |
| D4 | Tiến độ 1 - 1.5 tháng cho phiên bản MVP. | Khảo sát | 2026-05-22 | Phân bổ đội ngũ tinh gọn (1 Dev + 1 QA). |
| D5 | Sử dụng Gemini API làm nguồn dịch duy nhất trong MVP, kiến trúc multi-provider mở. Google Translate và OpenAI dời sang phase sau. | Khách hàng | 2026-05-22 | Giảm scope tích hợp API, loại bỏ rủi ro Google Translate bị chặn IP. |

## Open Questions

*(Không còn câu hỏi chưa giải quyết)*

## Latest Artifact Summaries

| Artifact | Phiên bản | Trạng thái | Tóm tắt |
| --- | --- | --- | --- |
| discovery.md | 1.0 | Done | Khảo sát ban đầu và phân loại độ phức tạp Light. |
| backlog-questions.md | 1.0 | Done | Giải quyết xong 4 câu hỏi định hướng kiến trúc & tiến độ. |
