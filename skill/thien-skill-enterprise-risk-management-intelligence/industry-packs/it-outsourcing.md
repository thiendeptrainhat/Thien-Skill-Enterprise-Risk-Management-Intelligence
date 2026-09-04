# IT / gia công phần mềm

## Đơn vị phân tích và doanh thu

Xác định T&M, fixed-price, managed service hoặc hybrid theo contract/project;
location, currency, billable hours, paid/available hours, leave/training,
seniority/skill match, bill rate, wage và subcontractor. Utilization phải ghi
denominator và billable/recognized/collected revenue là ba đại lượng khác nhau.

| Driver / CEI | Evidence / KRI | Kiểm tra và treatment |
| --- | --- | --- |
| Bench/skill mismatch → ít billable hours → margin/cash giảm | Available vs billable hours, skill demand, aging bench | Hours × realized rate − labor/delivery/fixed cost; staffing/training có lag |
| Wage/FX/discount → delivery margin giảm | Contract currency, payroll currency, rate resets, hedge evidence | Pass-through/FX scenario trên cash flows, không tự forecast FX |
| Scope creep/rework → ETC tăng → fixed-price overrun | Approved baseline, change orders, actuals, remaining effort, acceptance | EAC = actual + ETC; remaining duration/capacity riêng; discount sunk cost khỏi quyết định continue/exit |
| Backlog cancellation/client concentration → revenue gap | Signed commitments, cancellation rights, funded scope, customer credit | Tách noncancellable/cancellable; pipeline chưa ký không là committed revenue |
| Unbilled/milestone acceptance/DSO → cash delay → liquidity breach | Contract assets/AR aging, disputes, delivery acceptance, collections | Working capital/cash waterfall; invoicing milestone không bằng collection |
| Attrition/key person/access failure → delivery/SLA/IP loss | Succession coverage, access review, knowledge transfer evidence | Capacity và quality loss; privacy/IP/cyber depth chuyển specialist |
| AI adoption → effort/quality/commercial model đổi → benefit hoặc margin risk | Task baseline, actual accepted output, rework/security reviews, contract terms | Đo effort saving, freed capacity và realized benefit riêng; S10/S11 là điểm tra cứu |

## Backlog và pipeline không được trộn

Signed backlog cần ngày, remaining scope, price, acceptance, cancellation và
delivery timing. Cancellable backlog là signed nhưng có downside riêng.
Unsigned pipeline phải giữ stage/win probability và calibration evidence;
weighted pipeline chỉ là planning estimate. Không cộng weighted pipeline với
committed revenue rồi gọi tổng là bảo đảm. Deal đã chuyển signed phải bỏ khỏi
pipeline dùng tổng hợp. Forecast cần capacity/skills và collection bridge.

## AI: phân biệt năng suất với lợi ích thương mại

Dùng baseline effort B và phần giờ tiết kiệm E sau quality/rework của chính
nhiệm vụ; effort saving = E/B, không lấy số từ ví dụ khác thay input người dùng.
Chỉ có freed capacity nếu đội ngũ có thể dùng E; chỉ có realized commercial
benefit khi đã redeploy/cut cost hoặc tạo output được khách hàng chấp nhận và
thu được giá trị. Giữ cả costs AI/license/review.

T&M: nếu chỉ bill B−E thay vì B giờ, revenue có thể giảm dù productivity tăng;
redeploy E giờ cần demand/contract và skill match. Fixed-price: fee có thể giữ,
nhưng salaried cost không tự giảm bằng E × wage/hour; lợi ích có thể là capacity,
delivery speed hoặc avoided overtime, phải có bằng chứng thực hiện.
Đối soát lợi nhuận theo cùng baseline và kỳ: Δprofit = Δrecognized revenue
+ chi phí thực sự tránh được − chi phí tăng thêm (AI, delivery, review/rework).
Chỉ tính wage saving khi giảm được chi phí hoặc tránh chi phí có căn cứ; không
dùng E × wage/hour làm net saving chung cho nhân viên hưởng lương cố định.
Chi phí lương đã giữ nguyên ở baseline không bị trừ lần nữa như incremental
cost khi redeploy. Chưa biết các thành phần thì benefit chưa xác định, không
khẳng định bằng 0 hoặc suy dấu chỉ từ loại hợp đồng.
Không suy quan hệ nhân quả từ before/after nếu mix/skills/scope cùng đổi.

Scenario tích hợp attrition, bench, wage, bill rate, FX, rework, cancellation và
cash theo project/customer rồi khử intercompany/double-count. Mô hình forecast
pipeline, survival/churn hoặc causal AI benefit cần DSMV có engine và validation;
không nhận kết quả chỉ vì skill có route. Xem [hợp đồng](../integration/contracts.md).
