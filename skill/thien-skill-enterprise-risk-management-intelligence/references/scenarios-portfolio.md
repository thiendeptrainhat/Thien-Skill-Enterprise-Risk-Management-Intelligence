# Phép tính, scenarios, trend và danh mục

## Chọn mức độ phân tích

Lõi ERM xử lý deterministic calculations và simulation với input/distribution
đã xác định rõ. Nếu cần ước lượng/calibration/validation nâng cao, xem
[integration contract](../integration/contracts.md). Có code mô phỏng không
đồng nghĩa đã có mô hình đáng tin cho doanh nghiệp. Không sửa tham số của model
đã thẩm định rồi gọi đó là cùng phiên bản validated.

`scripts/erm_core.py` chạy JSON qua `--input`/`--output`; `--help` có operations.
Pure functions được import bởi validator/report/test; không network, không cài
package, không đọc credential, không tự ghi đè output. Decimal cho phép tính tiền;
mỗi output kèm operation/formula/input, đơn vị và context từ request.

| Operation | Công thức / ý nghĩa / giới hạn |
| --- | --- |
| arithmetic | Hai toán hạng left/right và operator +, -, *, /; dùng cho phép tính hẹp như backlog hoặc weighted pipeline. Caller phải bảo đảm cùng basis/đơn vị; kết quả không tự trở thành committed revenue |
| margin | Revenue=price×volume; contribution=(price−unit_cost)×volume; profit=contribution−fixed_cost; margin=profit/revenue nếu revenue≠0 |
| pass_through | New price=price + cost_change×pass_through; new cost=cost+cost_change; volume_new=volume×(1+volume_change). Tỷ lệ do caller cung cấp, không ước lượng elasticity |
| working_capital | AR=sales×DSO/days; inventory=COGS×DIO/days; AP=COGS×DPO/days; NWC=AR+inventory−AP; delta NWC là cash absorbed |
| cash_waterfall | Closing=opening+sum(inflows)−sum(outflows). Runway=available cash/net burn per period nếu burn>0; nếu burn≤0 thì không suy runway hữu hạn |
| credit | Net exposure=max(gross−eligible_collateral,0); EL=net exposure×PD×LGD. PD horizon/LGD cùng định nghĩa và nguồn; không tự tính eligibility hoặc PD từ score |
| concentration | Share từng nonnegative exposure / total; HHI=sum(share²), top share. Đây là concentration measure, không phải xác suất default |
| disruption | Lost units=max(demand−available_capacity,0); lost contribution=lost units×unit contribution; add incremental recovery/penalty costs. Không thêm lost revenue lần nữa |
| quality | Rework=units×rework rate×unit rework cost; recall=recall units×unit recall cost; add incremental incident cost; inputs phải non-overlapping |
| inventory | Shortfall=max(demand−stock,0); loss=shortfall×unit contribution + obsolete units×unit carrying cost + markdown units×unit discount; buckets không overlap |
| project_eac | EAC=actual cost+ETC; cost variance=budget−EAC; delay=max(forecast finish−baseline finish,0) ở unit ngày đã chuẩn hóa |
| headroom | Upper ceiling/ lower floor theo Assessment reference; không tự dùng ratio với lower limit |
| treatment | NPV=sum((benefit−cost)/(1+r)^t)−initial cost; flows relative to no-action. Budget/available resource check chỉ kiểm tra feasibility, không tối ưu portfolio |
| aggregate_losses | Deduplicate economic loss ID; record trùng ID nhưng dữ liệu khác bị reject. Require same currency/horizon/scope; intercompany internal eliminations rõ |
| simulate_margin | Seeded independent triangular price/cost/volume với ranges đã định; percentiles minh họa conditional assumptions, không calibrated enterprise forecast |

Các operation dùng positive/nonnegative constraints, rate range và denominator
guards; không chuyển missing/NaN thành 0. `simulation` dùng float cho sampling,
còn deterministic finance dùng Decimal. Không trộn currency/unit hoặc basis.
Nếu assumption không phù hợp (negative input prices, volume/cost phân phối phụ
thuộc...), không ép vào engine; giải thích giới hạn và xây scenario minh bạch
hoặc handoff. Synthetic fixture dùng đơn vị nhất quán và không là benchmark.

## Đối soát số liệu trong câu trả lời

Với kết luận định lượng trọng yếu, khi có runtime phải thực thi calculator hoặc
script tính tương đương, kể cả khi chỉ trả lời trong chat. Không yêu
cầu engagement/file bàn giao nếu câu hỏi không cần. Nếu không có runtime, trình
công thức và phần chưa kiểm; số chưa thực thi là UNCHECKED, không gắn nhãn
đã đối soát tay/validated hoặc dùng nó như kết quả đã xác nhận cho quyết định.

Đối soát từng tích, dấu, đơn vị, mẫu số, baseline/scenario và tổng thành phần
với delta trước khi viết lời giải. Giữ scale tiền ở cả đơn giá và tổng (ví dụ
triệu VND/đơn vị × số đơn vị = triệu VND); không đổi nhãn thành VND khi chưa
chuyển đổi số. Break-even chỉ là ranh giới toán học của giả định, không chứng
minh doanh nghiệp an toàn hay trong appetite. Khi phân rã price–volume–cost, ghi rõ volume
hoặc margin basis cho từng phần để phân bổ interaction một lần. `pass_through`
trả `profit_bridge` với factors/amount và reconciliation; dùng cùng basis cho
bảng và diễn giải. Mọi phép tính thêm ngoài output (tỷ lệ, break-even, bridge
khác) cũng cần kiểm lại; tổng cuối đúng không chứng minh từng dòng đúng.

### Sinh phần kết quả có kiểm chứng

`erm_core.py --input calculation.json --checked --text` thực thi rồi sinh phần
số liệu/lời giải cố định để đưa vào chat. Bỏ `--text` để nhận JSON gồm
`calculation`, `verification`, `text`; không cần engagement hoặc file bàn giao.
Ví dụ input cho câu hỏi backlog hẹp (dữ liệu synthetic, không là forecast):

```json
{"operation":"arithmetic","parameters":{"left":80,"operator":"-","right":20},"context":{"unit":"tỷ VND","currency":"VND","horizon":"Q4/2026","source_refs":["SYN1"]}}
```

Chế độ checked luôn tính mới. `--compare prior.json` tùy chọn đối soát toàn bộ
kết quả calculator dạng gốc (operation/parameters/context/formula_reference/
outputs) với lần tính mới; phải khớp cả biểu diễn JSON, đơn vị, kỳ và source_refs.
Không nhận một status PASS, JSON null hay envelope checked thay kết quả gốc.
Thiếu/sai input hoặc comparison: CLI exit 2, báo UNCHECKED và không xuất kết quả
được xác nhận. Không có comparison thì chỉ ghi EXECUTED, không nhận đã đối soát
với một kết quả khác. Hash input/calculation/engine và VERSION giúp truy nguyên
nội dung; không là chữ ký, xác minh nguồn hoặc chứng cứ một lần chạy trong quá khứ.

Giữ nguyên khối số liệu engine sinh. Phần diễn giải thêm ngoài khối đó không
thừa hưởng trạng thái EXECUTED; phép tính thêm phải chạy riêng. Lỗi/không có
runtime thì ghi chưa kiểm, không tự dựng packet hoặc nhãn thay cho tool output.
Đây là cổng trong calculator, không chặn lời văn tự do của host, không xác nhận
nguồn/assumption/appetite và không thay validation của mô hình nâng cao.

## Scenario, sensitivity, stress, reverse stress

- Sensitivity: thay một driver có baseline/ceteris paribus, giải thích partial
  effect. Driver tương tác thì thêm combined scenario, tránh cộng effects phi tuyến.
- Scenario: coherent driver set, horizon, trigger, mechanism, dependencies,
  exposure, control behavior và limits. Trình baseline + adverse + opportunity
  khi phù hợp câu hỏi; không ép số lượng kịch bản cố định.
- Stress: đưa pressure đến severe nhưng plausible dựa trên nguồn/assumption;
  nhận diện control/capacity/market nonlinearities và tipping points.
- Reverse stress: bắt đầu từ failure condition (cash floor, capacity, covenant,
  critical objective), tìm combination làm breach. Lõi có thể giải đại số hoặc
  enumerate grid nhỏ được chỉ định; solver/optimization/dependency nâng cao
  phải capability-check DSMV. Thiếu failure condition thì hỏi điều kiện đó;
  vẫn có thể tính forward scenario và gọi đúng tên. Ngưỡng thất bại giả định
  chỉ dùng khi được yêu cầu đề xuất, có nhãn minh họa và không là appetite đã duyệt.
  Không gọi một shock tùy ý là reverse stress.

Ghi method version, input snapshot, unit, source, seed khi có sampling, output
range và limitations. Scenario assumptions không có probability nếu chưa có
cơ sở; percentiles conditional không phải confidence interval của tham số.
Tỷ lệ biến động lượng/giá được giả định trong scenario chỉ là tỷ lệ hàm ý của
kịch bản, không phải elasticity đã ước lượng hoặc bằng chứng quan hệ nhân quả;
không kết luận cao/thấp so với ngành khi chưa có nguồn và hiệu chỉnh phù hợp.
Giữ giá cố định khi stress sản lượng không có nghĩa elasticity bằng 0: đây là
phân tích ceteris paribus, không ước lượng quan hệ cầu–giá.

## Trend và forecast

Trend observed: so sánh exposure/driver trên cùng grain/horizon/unit/method.
Tách observed change, method reclassification và source revision. Forecast:
cần target, forecast origin, horizon, training/out-of-sample windows, availability
as-of và baseline. Không extrapolate rating 1–5. Emerging risk là hypothesis
monitoring với triggers và gaps, không phải event xác nhận. Treatment completion
không tự giảm forecast exposure nếu chưa có measured effect/validated mechanism.

## Tổng hợp và dependency

Không cộng ordinal ratings, probability các event overlap hoặc EL trái horizon.
Theo dõi common supplier/customer/site/platform, concentration, common-mode và
cascade. Tách root event khỏi intermediate consequence để không tính cùng loss
hai lần. Một dependency graph có cycle không tự là lỗi; phải mô tả feedback/time.

Group view cần entity scope, consolidation boundary, currency translation,
intercompany elimination và risk transfer. Transfer chỉ chuyển phần loss trong
coverage/limit/deductible; giữ counterparty, exclusions, recovery delay và basis
risk. Không cộng gross insured loss và insurer payment như hai lợi ích độc lập.

Output portfolio gồm confirmed breaches, unknown/stale critical metrics,
concentrations, scenario total có reconciliation và limitations. “Top risks”
chọn theo objective/appetite/materiality/urgency với rationale; không dùng bảng
sắp xếp ordinal như mô hình dự báo tổn thất.
