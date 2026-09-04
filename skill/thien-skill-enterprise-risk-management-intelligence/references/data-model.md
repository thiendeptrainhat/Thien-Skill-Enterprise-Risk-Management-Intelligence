# Context, taxonomy và dữ liệu ERM

## Xác định phạm vi

Ghi câu hỏi quyết định, mục tiêu đo được, risk owner/decision owner, business
model, kỳ báo cáo và horizon. Site/sản phẩm/dự án chỉ đi sâu khi có ý nghĩa với
mục tiêu doanh nghiệp; nêu tiêu chí materiality và lý do chọn/loại. Với tập đoàn,
xác định pháp nhân, địa lý, đồng tiền chức năng/báo cáo và phạm vi consolidation.
Không coi thiếu số liệu là “không trọng yếu”. Dùng range/hypothesis nếu phù hợp.

## Taxonomy seed mở

L0 = lĩnh vực rủi ro; L1 = nhóm; L2 = chủ đề chi tiết có định nghĩa và exclusions.
Những dòng sau là seed, không phải danh sách đóng hoặc các risk đã xảy ra:

| L0 | L1 gợi ý | L2 minh họa |
| --- | --- | --- |
| Strategy & business model | Competitive position; portfolio | Channel displacement; product obsolescence |
| Market & commercial | Demand; pricing; customer | Demand contraction; discount leakage; buyer concentration |
| Financial | Cash; credit; FX/rate/commodity | Liquidity shortfall; debtor default; input price exposure |
| Operations & supply chain | Capacity; supplier; service | Single-source outage; bottleneck; SLA interruption |
| Product, safety & environment | Quality; harm; resources | Recall; worker/consumer harm; water constraint |
| People & organization | Workforce; capabilities; conduct | Attrition; key-person loss; incentive conflict |
| Technology & information | Availability; security; data/AI | Critical platform outage; data loss; AI model misuse |
| Legal, regulatory & integrity | Compliance; contractual; fraud | License restriction; contract exposure; misconduct |
| External & resilience | Natural hazard; geopolitics; infrastructure | Flood; trade disruption; power loss |
| Governance & reputation | Decision rights; information; trust | Unreliable reporting; weak oversight; loss of stakeholder trust |

Một sự kiện có nhiều impacts/cause có thể cần một RiskInstance với nhiều links.
Chỉ tách khi event, owner, horizon hoặc treatment khác về bản chất. Ghi primary
taxonomy_id và related topics bằng links, không sao risk thành nhiều dòng để đếm.
Không xếp cùng một node vừa là cause vừa là event mà không định nghĩa role.

## Cause–event–impact

Viết: “Do [driver/exposure và điều kiện], có thể xảy ra [event cụ thể] trong
[horizon], dẫn đến [impact có unit/range nếu đủ căn cứ], ảnh hưởng [objective].”
Nêu exposure, control context, event boundary, owner và evidence. Nếu event
chưa rõ, trình hypothesis và câu hỏi kiểm tra; không tự cấp rating chính xác.

Ví dụ giả định: phụ thuộc một nhà cung cấp bao bì → dừng giao hàng 14 ngày →
thiếu năng lực xuất hàng và giảm contribution margin → hụt mục tiêu doanh thu.
“Giá nguyên liệu” chỉ là topic; “biên lợi nhuận giảm” là impact, chưa đủ event.

## Một nguồn dữ liệu, nhiều biểu diễn

[engagement.schema.json](../schemas/engagement.schema.json) là contract máy đọc;
validator kiểm tra cấu trúc và bất biến tham chiếu. JSON là một interchange
format, không bắt người dùng phải cung cấp JSON khi họ chỉ có chat/SOP/Excel.
Chuyển input sang snapshot với provenance; không tự sửa dữ liệu nguồn.

| Collection | Sở hữu / relations |
| --- | --- |
| context | Decision, entities/objectives, as_of, horizon, currency, materiality |
| sources | Source ID, location, version, accessed/as_of, lifecycle và replacement |
| taxonomy | ID, level, parent, definition; không owner/rating của doanh nghiệp |
| risks | ID, taxonomy/entity/objectives, causes/event/impacts, owner, evidence |
| assessments | Risk ID, basis, method_id/version, evidence, Impact/Likelihood, category |
| methods | Scale definition và matrix 5×5, authority; không hardcode ngưỡng chung |
| metrics | Appetite/KRI definition, formula, unit, bad direction, rule predicates, owner/frequency/action |
| observations | Metric ID, value/null, unit, entity, horizon, as_of, evidence, quality |
| controls | Risk IDs, expected/designed/current, design/OE evidence và conclusion |
| scenarios | Baseline, parameter assumptions, transmission, outputs, limitations |
| losses | Một economic loss ID, amount, currency, horizon, scope; risk_ids nhiều-nhiều |
| dependencies | Cause/dependency links giữa risk IDs, type và evidence; không tự gán correlation |
| treatments | Risk links, owner/deadline, no_action_case, target (with-action), target_assessment_ids, cost/status |
| handoffs | Contract tại [integration](../integration/contracts.md) |

Mỗi object có `id`; references dùng ID, không join theo tên hiển thị. Source
và method version bất biến trong một snapshot. Khi thay đổi methodology giữa
kỳ, giữ snapshot cũ, tạo snapshot mới, giải thích bridge: exposure movement,
source revision và method change; không trình cả ba là risk trend thuần túy.

## Dữ liệu thiếu và chất lượng

`null` = chưa có giá trị; kèm quality `missing` và gap cần xử lý. `0` là giá trị
đã đo. Text unknown dùng null hoặc ghi rõ trong narrative; không tạo fake owner.
`evidence_ids=[]` là chưa có nguồn, không phải “không cần bằng chứng”. Đánh dấu
judgment/scenario và confidence khi dùng nhận định không có observation.

Kiểm tra grain/business key, units, signs, cut-off, duplicate, source lifecycle
và coverage. Evidence superseded không âm thầm thay vào kết luận cũ; liên kết
replaced_by, chạy lại phần phụ thuộc và so sánh trước/sau. Nếu source mới không
truy cập được, giữ bản đã dùng với hạn chế thay vì tuyên bố đã cập nhật.

Nhận một dataset khác đồng tiền/horizon phải đối soát conversion và scope trước
tổng hợp. Không quy đổi ordinal. FX conversion cần rate, ngày, nguồn, method;
công cụ lõi yêu cầu amount đã cùng tiền tệ, không tự tìm hay giả lập tỷ giá.
