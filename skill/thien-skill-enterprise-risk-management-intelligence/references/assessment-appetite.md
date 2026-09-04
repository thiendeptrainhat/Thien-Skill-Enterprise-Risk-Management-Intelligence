# Assessment, thang 5 mức và appetite

## Thiết kế thang phù hợp doanh nghiệp

1. Xác định mục tiêu, scope, horizon, exposure denominator và quyết định dùng
   rating. Thu thập loss history, business plan, capacity và nghĩa vụ thực tế.
2. Chọn impact dimensions cần bảo vệ: cash/earnings, continuity/service, people
   safety, environment, legal và reputation. Không ép mọi dimension về tiền.
3. Thiết kế năm mức có mô tả không chồng lấn, boundary equality rõ. Ngưỡng tiền
   phải có currency/base (doanh thu, EBITDA, cash headroom...) và kỳ; thêm absolute
   floor nếu tỷ lệ mất ý nghĩa với doanh nghiệp lỗ/EBITDA gần 0.
4. Với Likelihood, định nghĩa event và exposure period. Chọn probability bands,
   frequency per exposure unit hoặc anchored expert judgment; không trộn ba loại.
   Không dùng “mỗi tháng” so với probability một năm nếu chưa có phép chuyển hợp lệ.
5. Cùng decision owner xác định matrix 5×5, non-compensatory dimensions và
   override rules. Không dùng bình quân để che safety/legal catastrophic impact.
6. Kiểm tra boundary, monotonicity, cách xử lý dữ liệu thiếu, past incidents và
   một số scenarios. Trình draft phương pháp, người phê duyệt, version/effective date.

Tên năm mức có thể là rất thấp→rất cao, nhưng không tự cấp numeric thresholds.
Với dữ liệu yếu, ghi khoảng mức plausible và lý do, không dùng số thập phân cho
ordinal. I×L chỉ là index phân loại nếu methodology cho phép, không phải EL.
Expected loss chỉ tính trên xác suất/exposure/severity có đơn vị và cơ sở phù hợp.

## Inherent, current/residual và target

- Inherent: nói rõ counterfactual thiếu control nào; không dùng một định nghĩa
  “không có bất cứ hoạt động nào” khiến business model không còn tồn tại.
- Current/residual: phơi nhiễm hiện tại sau những controls đang vận hành, dựa trên
  design và operating evidence. Không tính `inherent × (1 − control effectiveness%)`
  khi tỷ lệ effectiveness không được đo/mô hình hóa và kiểm định.
- Target: trạng thái dự kiến sau treatment cụ thể, có deadline, dependencies,
  feasibility và uncertainty. Không trình target như current đã đạt.

Nếu xảy ra incident hoặc control failure mới, đánh giá lại driver/exposure/OE;
không giữ rating chỉ vì owner chưa cập nhật RCSA. Với disagreement/override,
giữ kết quả phương pháp, ý kiến khác biệt, lý do và approval evidence riêng.

## Capacity → appetite → tolerance/limits → early warning

Capacity là sức chịu đựng tối đa theo tài chính, pháp lý, người và khả năng
thực thi. Appetite mô tả mức/loại risk sẵn sàng nhận để theo đuổi strategy;
tolerance/limits cụ thể hóa khoảng chấp nhận cho metric. Early warning phải có
lead time để phản ứng trước breach. Không suy capacity từ target của risk owner.

Mỗi metric phải có: formula, unit, entity, horizon, chiều tốt/xấu, thresholds,
cách xử lý đúng tại ngưỡng, measurement cadence, source, owner, escalation action,
authority, method version. Khi thiếu method, giữ direction/threshold chưa xác
định thay vì tự áp dụng hai phía; ngày mẫu số phải cùng kỳ với flow dữ liệu
(không mặc định 365 cho doanh thu chưa biết kỳ). Với metric hai phía (ví dụ độ lệch nhiệt độ), mỗi phía
có predicate riêng; không dùng một tỷ lệ utilization mơ hồ.

`scripts/erm_core.py` nhận danh sách rules với `op` (`>`, `>=`, `<`, `<=`),
`threshold` và `severity` (`warning`, `breach`, `capacity_breach`). Method
phải được đánh dấu approved mới kết luận trạng thái vận hành. Không có rules,
không có value, hoặc dữ liệu stale/missing → UNKNOWN; phương pháp draft → DRAFT.
Trong rules đã khớp, chọn severity cao nhất. Data completeness là trục riêng:
portfolio vẫn nêu confirmed breach dù metric khác UNKNOWN.

Headroom theo upper limit = limit − value; lower floor = value − floor.
Utilization value/upper limit chỉ có ý nghĩa khi limit dương và metric thích hợp;
không dùng với lower floor, signed FX exposure hoặc giới hạn bằng 0.
Với metric signed hoặc tỷ lệ không có ý nghĩa dù value đang dương, đặt
`utilization_applicable=false`. Hai phía và value âm không hiển thị một tỷ lệ
utilization chung; giữ headroom theo từng biên.

## Breach và acceptance

Xác minh nguồn/thời điểm, mức vượt, duration, affected objectives, nguyên nhân,
remedial action và người cần quyết định. Temporary exception phải có scope,
expiry, compensating controls, authority, monitoring; exception không xóa breach.
Target risk ngoài appetite vẫn cần treatment bổ sung hoặc risk acceptance đúng
thẩm quyền. Không coi một email “đồng ý báo cáo” là approval sửa risk limits.

Khung tham khảo: [S01–S04](sources.md). Không nguồn nào ở đây tạo ra bộ ngưỡng
5 mức hoặc appetite chung cho mọi doanh nghiệp.
