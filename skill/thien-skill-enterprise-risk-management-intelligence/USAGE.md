# Sử dụng và mức kiểm chứng

**1.0.0 — Release**, bản hoàn thiện cục bộ từ nguồn 0.1.5 đã nghiệm thu trong
phạm vi dưới đây. Chỉ đổi VERSION và tài liệu bàn giao; mã, schema, hướng dẫn
nghiệp vụ, sáu pack ngành và assets giữ nguyên. Số phiên bản không xác nhận
mọi hành vi hoặc mọi nền tảng đã được kiểm chứng.

## Cấu trúc gói và nền tảng

Mỗi ZIP Claude/ChatGPT/Universal chứa một thư mục
`thien-skill-enterprise-risk-management-intelligence` ở gốc, không có lớp
`.agents/skills/`. Giữ nguyên thư mục để links, scripts, schema, logo và hồ sơ
pháp lý hoạt động cùng nhau. Ba gói dùng cùng nguồn; chỉ metadata đích khác nhau.

| Bề mặt | Bằng chứng đã có | Giới hạn cho 1.0.0 |
| --- | --- | --- |
| Claude Web | Từng quan sát Add skill và định dạng ZIP folder-root | Native install/trigger/runtime: **NOT_RUN** |
| Claude Code | Native explicit/implicit, core và Office 0.1.3 có giới hạn; hồi quy 0.1.4 nạp từ file, còn lỗi lời văn đã lưu | 1.0.0 chưa cài/native-test. Người dùng đã dừng kiểm thêm Claude; không đổi lỗi lịch sử thành PASS |
| ChatGPT Web | `Plugins → Skills → Create → Upload`; native logo/core/Office 0.1.3 có giới hạn. Bốn ca R06 trên 0.1.5 qua ZIP đính kèm ở phiên mới đạt | 0.1.5 là file-loaded, không thay bản đã cài; 1.0.0 chưa cài/native-test |
| ChatGPT Desktop | Chưa có bằng chứng cài và chạy trực tiếp | **NOT_RUN**; không dùng Codex task làm bằng chứng Desktop |
| Universal | Folder-root dùng cùng canonical bytes | Kiểm cấu trúc/manifest không chứng minh tương thích native trên một bề mặt mới |

Không cần plugin wrapper theo cơ chế đã kiểm. Chỉ xem lại khi có native evidence
yêu cầu khác. Có ZIP không tự cấp quyền cài, upload, gửi hoặc phát hành ra ngoài.

## Sử dụng

Gọi `$thien-skill-enterprise-risk-management-intelligence`, nêu câu hỏi/đầu ra,
người ra quyết định, organization scope, as-of, horizon, jurisdiction, currency,
unit và nguồn. Với câu hỏi hẹp, không cần tạo engagement đầy đủ.

Python standard library đủ cho validator, calculator và HTML report:

```bash
python3 scripts/validate_engagement.py engagement.json
python3 scripts/erm_core.py --input calculation.json --checked --text
python3 scripts/report.py engagement.json --out new-report-directory
```

Request calculator gồm `operation`, `parameters`, `context` có `unit`,
`currency`, `horizon`, `source_refs`; xem `--help` và
[Scenarios & portfolio](references/scenarios-portfolio.md). Bỏ `--checked`
giữ contract JSON gốc; `--output` tùy chọn lưu file. Script từ chối ghi đè.

Chế độ checked thực thi mới rồi sinh số liệu/lời giải và dấu vết nội dung.
`--compare prior.json` đối soát kết quả JSON gốc, không chấp nhận status tự khai.
**R05 được xử lý trong đường sinh calculator:** lời văn hoặc phép tính do host
viết thêm không thừa hưởng EXECUTED. Hash không là chữ ký hoặc chứng cứ lịch sử;
nguồn dữ liệu, giả định, appetite và model validation vẫn cần kiểm riêng.

`report.py` sinh `report.json` và HTML offline từ một snapshot. Office exporter
`scripts/export_office.mjs` là tùy chọn khi môi trường có đúng runtime
`@oai/artifact-tool` và `docx`; dùng bản copy tạm cùng dependency đã được phép.
Không tự cài package để ép chạy. `--check` kiểm số liệu/công thức nhưng không
thay render/visual QA. Excel giới hạn 15 chữ số có nghĩa và decimal round-trip;
số vượt độ chính xác bị từ chối, giữ nguyên trong JSON để quyết định rescale.
Không đổi ID thành số. Contract treatment/handoff tại
[Treatment & reporting](references/treatment-reporting.md) và
[Integration contracts](integration/contracts.md).

## Phạm vi nghiệm thu và giới hạn

- 120 phản hồi synthetic là bằng chứng lịch sử; không chạy lại toàn bộ trên
  1.0.0. 43 tests core/report và sáu ca CLI thuộc nguồn 0.1.5. Bốn ca R06 trên
  ChatGPT Web 0.1.5 đạt về ngưỡng thiếu, reverse stress, elasticity và AI benefit;
  do agent triển khai đánh giá, không phải reviewer độc lập hoặc chứng nhận native.
- Word ba trang đã xem trên 0.1.4; XLSX 16 sheets/PPTX 8 slides và đối soát chọn
  trường giữ bằng chứng 0.1.3. Renderer không đổi; không gọi đó là visual test mới.
- HTML có **USER_REPORTED_PASS** cho bốn mục smoke 0.1.3: utilization, trạng thái
  không áp dụng, search/filter/reset và thu hẹp cửa sổ. Keyboard và coverage
  responsive/visual rộng hơn chưa kiểm; không tuyên bố đã phủ mọi thiết bị.
- Handoff có kiểm kỹ thuật synthetic và acceptance gate; không chứng nhận dữ
  liệu doanh nghiệp, mọi engine DSMV hoặc production return. Kiểm capability
  thực tế trước mỗi lần chuyển việc. Source register phải được kiểm lại theo
  nhiệm vụ; metadata tiêu chuẩn không thay toàn văn hay nguồn pháp lý hiện hành.
- Cấu trúc skill đã kiểm bằng Ruby Psych và quy tắc tương đương; validator gốc
  skill-creator trước đây không chạy được vì thiếu PyYAML. Không đổi thành PASS.

Evidence chi tiết theo phiên bản ở `qa/RESULTS.json`, `qa/G9-NATIVE.json` và
trạng thái chuẩn ở `docs/KE-HOACH.md` trong repository phát triển; các file QA
không nằm trong ZIP cài đặt. PACKAGE-MANIFEST.json nhận diện payload từng gói.
Mọi đầu ra vẫn là dự thảo đến khi đúng người có thẩm quyền phê duyệt. Skill
không tự sửa skill khác, production threshold, accept breach hoặc gửi báo cáo.
