# Yêu cầu sản phẩm và nghiệm thu

Cập nhật: 2026-09-03. Tài liệu chuẩn về những gì skill phải đáp ứng.
Mục đích: [Mục tiêu](MUC-TIEU.md). Cách thực hiện: [Nguyên tắc](NGUYEN-TAC.md).
Trạng thái và quyết định chưa chốt: [Kế hoạch](KE-HOACH.md).

## 1. Năng lực ERM lõi

- **ERM-01 — Bối cảnh:** business model, chiến lược, mục tiêu, value chain, phạm vi
  tổ chức, materiality, horizon, jurisdiction và người ra quyết định.
- **ERM-02 — Risk Universe:** taxonomy có cấu trúc, hỗ trợ ngành và cấp tổ chức;
  tách danh mục rủi ro khỏi RiskInstance/Risk Register cụ thể.
- **ERM-03 — Cause–Event–Impact:** mô tả nguyên nhân, sự kiện, tác động, mục tiêu
  bị ảnh hưởng, exposure, owner và bằng chứng; tránh mô tả chỉ có tên chủ đề.
- **ERM-04 — Assessment:** inherent, current/residual và target risk theo phương
  pháp đã xác định; thể hiện căn cứ, uncertainty và mức đầy đủ của bằng chứng.
- **ERM-05 — Appetite:** capacity, appetite statement, tolerance, limits,
  early warning, ngưỡng chấp nhận/không chấp nhận, breach và escalation.
- **ERM-06 — Thang 5 mức:** thiết kế Impact và Likelihood theo loại hình, quy mô,
  ngành, horizon và năng lực doanh nghiệp, có căn cứ phương pháp và nguồn.
- **ERM-07 — Controls:** key controls, enterprise RCM và RCSA; phân biệt expected,
  designed và current controls, design adequacy và operating effectiveness.
- **ERM-08 — KRI:** định nghĩa, công thức, đơn vị, chiều tốt/xấu, nguồn dữ liệu,
  owner, tần suất, threshold, liên kết appetite và hành động escalation.
- **ERM-09 — Kiểm tra:** sensitivity, scenario, stress và reverse stress;
  thể hiện logic truyền dẫn, tham số, kết quả và giới hạn sử dụng.
- **ERM-10 — Xu hướng:** phân tích driver/exposure và dự báo phù hợp bằng chứng;
  phân biệt observed trend, forecast, scenario và emerging risk.
- **ERM-11 — Danh mục:** dependency, concentration, aggregation, common-mode,
  cascade, intercompany khi liên quan và kiểm soát double-counting.
- **ERM-12 — Treatment:** phương án ứng phó và control, chi phí/lợi ích, lead time,
  khả thi, rủi ro thứ cấp, owner, deadline, target và residual exposure dự kiến.
- **ERM-13 — Báo cáo:** risk profile, top risks, appetite/KRI breaches, xu hướng,
  scenario, treatment progress và các quyết định cần ban điều hành/HĐQT xử lý.

## 2. Sáu gói ngành chuyên sâu

- **IND-01 — FMCG:** nguyên liệu, giá–sản lượng–chi phí–biên lợi nhuận, nhu cầu,
  kênh/SKU, khuyến mại, tồn kho, chất lượng/thu hồi, công suất và danh tiếng.
- **IND-02 — Nông nghiệp:** thời tiết/khí hậu, mùa vụ, năng suất, đầu vào, đất/nước,
  dịch bệnh, giá hàng hóa và chuỗi cung ứng.
- **IND-03 — Chăn nuôi:** thức ăn, an toàn sinh học, dịch bệnh, mortality/FCR,
  chất lượng, phúc lợi động vật, giá đầu ra và chuỗi lạnh.
- **IND-04 — Logistics:** nhiên liệu, đội xe/kho, công suất/mạng lưới, cảng/hải quan,
  SLA, mất mát hàng, gián đoạn và tập trung khách hàng.
- **IND-05 — Retail:** nhu cầu, margin, shrinkage, inventory/stockout, markdown,
  cửa hàng/online, nhà cung cấp, thanh toán và an ninh mạng.
- **IND-06 — IT/gia công phần mềm:** utilization/bench, skill matching, bill rate,
  wage/FX, fixed-price EAC/overrun, rework/scope change, SLA, backlog/pipeline,
  DSO/unbilled revenue, attrition/key person, bảo mật/IP/privacy và tác động AI.
- **IND-07 — Ngành khác:** thích ứng lõi ERM theo mô hình kinh doanh và nguồn hiện
  hành; không tự tạo benchmark ngành hoặc mặc định chuẩn ngành khác áp dụng.

IT/gia công phần mềm phải phân biệt signed backlog, cancellable backlog và
unsigned pipeline; win probability với doanh thu đã cam kết; effort saving,
freed capacity và realized commercial benefit; tác động AI lên T&M với fixed-price.

## 3. Tính toán ERM trực tiếp

**CALC-01:** tự thực hiện mô hình minh bạch, tham số xác định được, thuộc phạm vi
năng lực thực tế; có công thức, đơn vị, nguồn, horizon và kiểm tra hợp lý:

- Price–volume–cost–margin và pass-through.
- Working capital, cash waterfall và liquidity runway.
- Credit exposure và concentration.
- Capacity–service–loss và gián đoạn hoạt động.
- Quality, rework, recall và incident/loss mapping.
- Inventory, stockout, obsolescence và markdown.
- Project cost–schedule, EAC và danh mục dự án.
- Appetite headroom, limit utilization và breach.
- Treatment economics và resource constraints cơ bản.
- Scenario, sensitivity, stress và mô phỏng phù hợp với tham số đã xác định.

**CALC-02:** có thể chạy mô hình đã được thẩm định khi đủ dữ liệu, tham số, quyền
sử dụng và hướng dẫn. Không tự thay method, distribution hoặc calibration rồi
tiếp tục gọi đó là cùng mô hình đã được thẩm định.

## 4. Handoff dữ liệu và mô hình nâng cao

**INT-01:** dùng Data Engineering & Quality khi cần profiling, cleaning,
reconciliation, transformation, schema drift/control hoặc lineage.

**INT-02:** kích hoạt Data Science & Model Validation khi cần xây dựng, ước lượng,
hiệu chỉnh, kiểm định hoặc uncertainty nâng cao cho:

- Classification/ranking, rare events, frequency/count, severity/loss.
- Time-series/exogenous, panel/hierarchical forecasting.
- Bayesian/partial pooling và survival/competing risks.
- Frequency–severity, Monte Carlo đa biến và dependency modelling.
- Copula, tail dependence, EVT và reverse-stress solver.
- Multivariate anomaly, early warning, calibration/backtest/drift/monitoring.
- Causal inference cho hiệu quả treatment.
- Constrained/robust/stochastic optimization.
- Discrete-event hoặc agent-based simulation khi phù hợp.

**INT-03:** handoff phải có câu hỏi quyết định, target/entity/segment, horizon,
data/as-of, giả định, ràng buộc, tiêu chí chấp nhận, uncertainty và output contract.
Kết quả nhận lại phải có method, validation status, giới hạn sử dụng, model card
hoặc bằng chứng tương đương và yêu cầu monitoring khi liên quan.

**INT-04:** kiểm tra năng lực và phiên bản skill tại thời điểm gọi. Route hoặc
hướng dẫn được mô tả không đồng nghĩa có engine end-to-end đã kiểm chứng.
Nếu thiếu năng lực, phải nói rõ phần chưa làm được và đề xuất nâng cấp cho người dùng.

**INT-05:** ERM giữ logic truyền dẫn kinh doanh, ánh xạ kết quả sang appetite,
treatment và kết luận điều hành. Skill phụ không tự phê duyệt quyết định kinh doanh.

**INT-06:** chuyển phân tích quy trình/control chi tiết sang Risk Control Process;
chuyển câu hỏi đa lĩnh vực vượt ERM cho Master Orchestrator khi phù hợp.

## 5. Báo cáo và thiết kế

- **OUT-01 — Excel:** universe/register, assessment, appetite, RCM/RCSA, KRI,
  scenario/stress, treatment tracker và dashboard dữ liệu.
- **OUT-02 — Word:** phương pháp, risk profile, báo cáo phân tích và báo cáo ERM.
- **OUT-03 — PowerPoint:** báo cáo ban điều hành và HĐQT.
- **OUT-04 — Dashboard:** risk profile, heatmap, appetite utilization, KRI breach,
  trend, concentration, scenario và treatment progress; công nghệ mặc định chưa chốt.
- **OUT-05 — Thiết kế:** kết hợp UI/UX Ultra và Creative Diagram theo năng lực thực
  tế; dùng công cụ artifact chuyên dụng để tạo/kiểm tra file Office và chart.
- **OUT-06 — Nhất quán:** đối soát Risk ID, rating, appetite, KRI, scenario,
  treatment, as-of/version, số tổng hợp và narrative giữa các định dạng.
- **OUT-07 — Tính trung thực:** không gọi SVG/ảnh nhúng là native chart/shape có
  thể chỉnh sửa; nêu đúng dạng đầu ra và khả năng chỉnh sửa thực tế.

## 6. Ngôn ngữ, thương hiệu và giấy phép

- **BRAND-01:** mặc định tiếng Việt; ưu tiên ngôn ngữ của người dùng nếu khác.
- **BRAND-02:** dùng ảnh TDTN người dùng cung cấp làm logo/icon; một nguồn ảnh chuẩn,
  chỉ tạo biến thể khi có yêu cầu kỹ thuật thật.
- **LEGAL-01:** giấy phép mang tên “Tran Ngoc Thien's Skill”, dựa trên template
  Commercial Source Available License 2.0 được chỉ định; giữ nguyên bản chất
  điều khoản thương mại/source-available, không tự mở rộng quyền sử dụng.
- **LEGAL-02:** song ngữ Việt–Anh, tiếng Việt ưu tiên khi mâu thuẫn, áp dụng pháp
  luật và cơ quan tài phán Việt Nam.
- **LEGAL-03:** mọi ZIP có LICENSE, LICENSE-APPLICATION.md, LICENSE-VERSION,
  NOTICE và THIRD-PARTY-NOTICES.md; trường hành chính thiếu phải hỏi người dùng.

## 7. Đóng gói và tính di động

- **PKG-01:** một skill, một canonical source; không duy trì bản sao nghiệp vụ
  đầy đủ riêng theo nền tảng.
- **PKG-02:** ba ZIP Claude, ChatGPT và Universal trong `dist/<version>/`.
- **PKG-03:** Universal chứa trực tiếp thư mục skill, bỏ lớp `.agents/skills/`.
- **PKG-04:** mục tiêu là Claude Web, Claude Code, ChatGPT Web và ChatGPT Desktop.
  Không đồng nhất ChatGPT Desktop với Codex.
- **PKG-05:** chỉ tuyên bố cài đặt/khả năng native đã kiểm chứng. Cấu trúc cài ZIP
  trên ChatGPT Web/Desktop còn cần xác minh. Nếu cần plugin wrapper, trình người
  dùng quyết định sau khi có phương án cụ thể; không tự tạo plugin.
- **PKG-06:** packages có manifest/checksum, đủ tài nguyên/pháp lý, không có đường
  dẫn máy cá nhân, temp/cache và sai lệch với canonical source.

## 8. Nghiệm thu

- **QA-01:** mapping yêu cầu với các nhóm kiểm thử; bao phủ đủ 120 tình huống trong
  tài liệu tham khảo và các ca biên đã nhận diện, không tạo một file cho mỗi case.
- **QA-02:** tách static/structure, domain behavior, quantitative, integration,
  artifact và platform-native tests.
- **QA-03:** kiểm tra missing data, metric direction, methodology change,
  duplicate loss, source replacement, specialist unavailable, multinational
  và các đặc thù của sáu ngành.
- **QA-04:** phân biệt PASS, FAIL, NOT_RUN và bằng chứng lịch sử. Kiểm tra file
  tồn tại hoặc manifest không đủ chứng minh hành vi end-to-end.
- **QA-05:** dữ liệu synthetic được gắn nhãn; kiểm thử độc lập chỉ được gọi là
  độc lập khi điều kiện đánh giá thực tế đáp ứng.
- **QA-06:** kiểm tra công thức/kết quả trọng yếu, đối soát các định dạng và xem
  trực quan artifact khi định dạng có ý nghĩa đối với việc sử dụng.
- **QA-07:** cổng vệ sinh tại [Nguyên tắc](NGUYEN-TAC.md) phải đạt trước đóng gói.
- **QA-08:** không công bố hoàn tất khi còn lỗi chặn; giới hạn/NOT_RUN còn lại
  phải được nêu rõ trong bàn giao.
