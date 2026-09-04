# Enterprise controls, RCSA và KRI

## Enterprise RCM

Nối objective → RiskInstance → control objective → key control → evidence/test
→ gap → action. Một control có thể bảo vệ nhiều risks, nhưng không nhân bản
benefit hoặc độc lập giả khi controls cùng dựa vào một người/hệ thống/data source.
Phân tích SoD, step-by-step process, process mining hoặc testing sâu chuyển
Risk Control Process/IA theo [contract](../integration/contracts.md).

| Phân biệt | Cần bằng chứng gì |
| --- | --- |
| Expected control | Risk mechanism và lý do control nên tồn tại; không gọi là current |
| Designed control | Policy/configuration/workflow, owner, frequency, coverage, exception path |
| Implemented/current | Bằng chứng triển khai tại entity/time/scope đang xét |
| Design adequacy | Có chặn/phát hiện/giảm đúng cause/event/impact với timing phù hợp không |
| Operating effectiveness | Execution population, period, sample/coverage, exceptions, reperformance/logs |

Key control là control mà thất bại gây tăng enterprise exposure đáng kể hoặc
vi phạm ràng buộc trọng yếu; không gán “key” cho mọi policy. SOP, chữ ký owner,
certification hoặc checklist có sẵn không tự chứng minh OE. Thiếu OE evidence
ghi `not_tested`/`unknown`; không khấu trừ risk theo design intention.

## RCSA có challenge

Risk owner đánh giá self-assessment và dẫn evidence; ERM challenge assumptions,
history, incidents, near misses, overdue actions và dependency chung. Giữ người
tự đánh giá, người challenge, scope, thời điểm, kết luận design/OE và limitations.
Không coi RCSA là kết luận kiểm toán độc lập. Khi owner tự đánh giá thấp trái
incident/KRI, ghi inconsistency, hỏi bằng chứng và escalation; không tự ép một
rating tùy ý để “bù” thiếu dữ liệu.

## KRI specification

KRI phải báo exposure hoặc khả năng/tác động risk, không chỉ thành tích hoạt động.
Một KPI có thể là KRI khi có transmission link và lead time phù hợp. Ví dụ
delivery on time đo hiệu suất; tỷ lệ đơn hàng cam kết vượt capacity khả dụng
có thể cảnh báo risk SLA. Kiểm tra mối quan hệ thay vì đổi tên KPI thành KRI.

Ghi cùng metric: formula/numerator/denominator, grain, unit, direction,
frequency, cut-off/latency, source, quality rules, owner, Risk IDs, appetite link,
warning/breach predicates và cụ thể ai làm gì khi ngưỡng bị vượt. Denominator=0
thì UNKNOWN/undefined với giải thích, không trả 0 để tô xanh.

- Leading: concentration, overdue preventive maintenance, capacity gap.
- Lagging: realized loss, complaints/incident frequency, SLA penalties.
- Phân biệt rate/count/amount; denominator và period thay đổi cần normalized
  comparison và explanation. Population thay đổi không tự là risk improvement.
- Threshold do doanh nghiệp duyệt sau evidence; ngoài case synthetic không
  tự áp dụng con số “phổ biến”. Early warning phải dẫn tới action khả thi.
- False positive/negative: cần event definition, outcomes, label availability,
  time split, alert lead time và costs/capacity. Handoff DSMV nếu calibration,
  backtest hoặc alert model vượt deterministic rule đang dùng.
- KRI vượt capacity: escalation ưu tiên, không chỉ tô màu. Thiếu dữ liệu KRI
  trọng yếu là data gap cần owner, không được biến thành within appetite.

RCSA, incident, assessment và KRI dùng cùng snapshot as-of; nếu khác kỳ, trình
reconciliation bridge thay vì âm thầm ghép thành cùng một trạng thái hiện tại.
