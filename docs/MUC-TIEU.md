# Mục tiêu dự án

Cập nhật: 2026-09-03. Tài liệu chuẩn về mục đích và phạm vi sản phẩm.
Điểm vào: [CLAUDE.md](../CLAUDE.md).

## Sản phẩm cần xây dựng

Xây dựng một skill duy nhất: **Thiện's Skill — Enterprise Risk Management Intelligence**.
Mã kỹ thuật đã chốt là `thien-skill-enterprise-risk-management-intelligence`;
metadata phát hành được chốt theo [Kế hoạch](KE-HOACH.md).

Skill điều phối và thực hiện nghiệp vụ Enterprise Risk Management (ERM) như một
chuyên gia rủi ro có góc nhìn điều hành: từ bối cảnh kinh doanh, nhận diện và đánh
giá đến appetite, kiểm soát, mô hình, ứng phó và báo cáo.

Kết quả phải giúp người dùng hiểu rủi ro ảnh hưởng mục tiêu nào, qua cơ chế nào,
mức độ ra sao, bằng chứng đến đâu, cần quyết định gì và hành động nào phù hợp.

## Vị trí trong hệ sinh thái

- Chỉ điều phối toàn bộ nghiệp vụ ERM; không thay thế `Thien-Skill-Master-Orchestrator`.
- ERM sở hữu câu hỏi kinh doanh, logic rủi ro, phép tính lõi, diễn giải và kết luận.
- Chuyển phần việc chuyên sâu cho skill phù hợp khi cần; không phụ thuộc skill
  phụ để thực hiện toàn bộ năng lực ERM lõi.
- Không quá tập trung vào quy trình như `Thien-Skill-Risk-Control-Process`.
  Phân tích control ở cấp ERM; chuyển phần quy trình chi tiết khi có nhu cầu.

## Phạm vi tổ chức và địa lý

Phân tích ở cấp tập đoàn, doanh nghiệp, công ty, pháp nhân và đơn vị kinh doanh.
Chấp nhận đi sâu đến nhà máy/site, sản phẩm, dịch vụ hoặc dự án trọng yếu khi
tác động có ý nghĩa ở cấp doanh nghiệp. Không biến mọi rủi ro tác nghiệp nhỏ
thành một risk cấp doanh nghiệp.

Phạm vi đa quốc gia, không giới hạn địa lý. Mỗi nhiệm vụ phải xác định bối cảnh
pháp nhân, quốc gia, đồng tiền, kỳ báo cáo và yêu cầu pháp lý liên quan.

## Ngành và người sử dụng

Chuyên sâu sáu ngành: **FMCG, nông nghiệp, chăn nuôi, logistics, retail,
IT/gia công phần mềm**. Đồng thời có phương pháp thích ứng để tư vấn ngành khác.

Đầu ra phục vụ risk owner, bộ phận ERM, ban điều hành và HĐQT. Khuyến nghị phải
phù hợp chiến lược, mô hình kinh doanh, quy mô và năng lực thực thi của doanh nghiệp.

## Kết quả cần đạt

- Bao phủ chuỗi nghiệp vụ ERM quy định trong [Yêu cầu](YEU-CAU.md).
- Tự tính được các mô hình ERM minh bạch và mô phỏng phù hợp năng lực.
- Nhận diện đúng khi cần Data Science & Model Validation hoặc chuyên môn khác;
  nói rõ năng lực chưa có thay vì giả vờ đã thực hiện.
- Tạo Excel, Word, PowerPoint và dashboard có số liệu, trạng thái và thông điệp
  nhất quán; có thể truy nguyên về dữ liệu và phương pháp.
- Mặc định tiếng Việt; ưu tiên ngôn ngữ người dùng khi họ dùng ngôn ngữ khác.
- Một nguồn skill chuẩn, các gói cài đặt dễ dùng, khả năng nền tảng được kiểm chứng.
- Dự án tinh gọn, không có file rác/mồ côi không giải thích, không có bản sao
  nghiệp vụ theo từng nền tảng, dễ đọc và bảo trì qua nhiều phiên làm việc.

## Ranh giới mục tiêu

Không tự thay người có thẩm quyền phê duyệt appetite, limits, risk acceptance
hoặc báo cáo chính thức. Không mặc định nhận định rủi ro là kết luận pháp lý,
kết luận kiểm toán độc lập hay chứng nhận tuân thủ.

Nâng cấp các skill khác là công việc riêng khi người dùng cho phép. Dự án ERM
thiết kế giao diện chuyển giao và chỉ ra khoảng trống năng lực, không tự mở rộng
thành dự án xây mọi engine Data Science hoặc công cụ đồ họa.
