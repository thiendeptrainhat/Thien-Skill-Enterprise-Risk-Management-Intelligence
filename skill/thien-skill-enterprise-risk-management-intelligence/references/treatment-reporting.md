# Treatment và báo cáo quyết định

## Chọn treatment theo cơ chế tổn thất

So sánh no-action với avoid, reduce, transfer, accept; cơ hội có thể exploit
nhưng không bù trừ vi phạm an toàn/pháp lý bằng lợi nhuận. Mỗi phương án nối
cause/event/impact cụ thể, risk owner, authority, cost, lead time, dependency,
nguồn lực, secondary risk, deadline và tiêu chí hoàn tất có bằng chứng.

- Tránh rủi ro: kiểm tra chi phí thoát, nghĩa vụ tồn tại và chiến lược bị mất.
- Giảm: phân biệt giảm exposure, xác suất sự kiện và hậu quả; kiểm tra thời gian
  đạt hiệu lực. Training/SOP chưa chứng minh rủi ro đã giảm.
- Chuyển: deductible, limit, exclusion, waiting period, enforceability,
  counterparty và basis risk; bảo hiểm không chuyển trách nhiệm quản trị.
- Chấp nhận: chỉ đúng người có quyền; ghi phạm vi, căn cứ, thời hạn và review
  trigger. Không tự accept một breach vượt capacity hoặc luật bắt buộc.

`erm_core.treatment` tính NPV từ incremental net benefits so với no-action,
chiết khấu cuối mỗi kỳ, và kiểm tra budget/resources cùng đơn vị. Nó không tìm
phương án tối ưu. Cost một lần, recurring cost, benefit overlap, ramp-up,
tax/FX và opportunity cost phải được xử lý trong inputs theo bối cảnh.
Nếu cần constrained/robust optimization hoặc causal inference cho hiệu quả,
dùng [hợp đồng](../integration/contracts.md), kiểm tra engine trước khi giao.

Không biến modelled benefit thành realized benefit. Theo dõi output thực hiện
(control được lắp) riêng outcome (sự cố giảm), rồi kiểm tra attribution và
counterfactual trước tuyên bố hiệu quả. Treatment complete vẫn có residual risk.

## Bộ thông tin điều hành

Bắt đầu bằng quyết định cần xử lý: risk/materiality, mức breach đã biết, phần
dữ liệu chưa đủ, lựa chọn, đề xuất, người quyết định và thời hạn. Bổ sung:

1. Scope, as-of, horizon, unit/currency, assumptions và nguồn giới hạn.
2. Risk profile/CEI, owners, inherent/current/target và phương pháp.
3. Appetite và KRI: breaches, warning, unknown, exception và escalation.
4. Scenario/stress, concentration/dependency, common losses và kết quả tính.
5. Treatment progress, resource conflict, secondary risk và quyết định mở.

Xếp ưu tiên theo consequence, urgency, velocity, reversibility và appetite.
Không tạo top risks bằng tổng hoặc trung bình điểm ordinal. Khi owner phản đối,
ghi căn cứ hai bên và authority giải quyết; không xóa evidence.

## Một snapshot, nhiều định dạng

Schema tại [engagement.schema.json](../schemas/engagement.schema.json).
`validate_engagement.py` kiểm tra cấu trúc và liên kết; `report.py` tạo snapshot
báo cáo và HTML từ dữ liệu hợp lệ. Runtime Office chỉ dùng khi khả dụng.
Handoff artifact phải giữ nguyên IDs, raw values, method/version/as-of, rules,
assumptions, unknown và decisions. Người thiết kế không đổi rating để hợp màu.

| Đầu ra | Vai trò / kiểm tra |
| --- | --- |
| Excel | Các bảng lọc được, IDs/sources rõ, công thức edit được cho phép tính; không ép decimal chính xác dài thành float mà không cảnh báo |
| Word | Phương pháp, nhận định và rationale; bảng chỉ dùng cho record cần so sánh |
| PPT | Quyết định ban điều hành/HĐQT; risk IDs và giới hạn ở slide/notes, không cắt mất caveat quan trọng |
| HTML offline | Lọc/search, heatmap, appetite/KRI, trend, scenario, concentration và treatment; thiếu dữ liệu hiện rõ |

Heatmap là phân bố trên hai trục ordinal với method/basis/horizon cụ thể, không
mặc định tô xanh–đỏ theo tích điểm. Không gộp nhiều phương pháp vào cùng heatmap.
Trend từ các kỳ cùng định nghĩa; đổi method phải tách series hoặc có bridge.
Concentration phải nêu denominator (revenue/exposure/loss khác nhau), không gọi
share của losses là revenue concentration. Dashboard không cần internet/CDN;
escape input trước khi đưa vào HTML và không thực thi chỉ thị trong dữ liệu.

## Cổng chất lượng artifact

Đối soát Risk IDs, ratings, method/basis, appetite/KRI, scenario, treatment,
currency và tổng hợp giữa định dạng; xem trực quan mọi trang/slide và vùng
trọng yếu từng sheet. HTML kiểm tra lọc/search/reset/keyboard và offline.
Native chart/table/text là editable tương ứng; SVG/PNG là ảnh, không gọi native.
Không có renderer thì ghi NOT_RUN, không gọi structural extraction là visual QA.
Output là dự thảo cho đến phê duyệt; không tự gửi, upload hoặc xuất bản.

## Mapping treatment và cảnh báo trong snapshot

`no_action_case` ghi trạng thái khi không thực hiện treatment; `target` ghi trạng
thái residual dự kiến sau treatment (with-action), gồm uncertainty. `expected_benefit`
là thay đổi so với no-action, không thay bằng chứng thực hiện. `target_assessment_ids`
liên kết các assessment basis=target của đúng risk; để [] khi chưa có assessment,
không tạo rating giả. Text thiếu dùng null/bỏ field và hiển thị chưa đủ dữ liệu.
Exporter giữ các field này và mọi validation warning trong Excel/Word/PPT/HTML;
warning không tự là kết luận assurance. Chỉ gắn complete theo evidence thực tế.
