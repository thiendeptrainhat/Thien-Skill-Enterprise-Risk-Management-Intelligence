# Capability-first handoff

## Discovery tại thời điểm gọi

Kiểm tra đúng skill/tool đang khả dụng; ghi tên, version hoặc content hash,
entrypoint, method/engine hỗ trợ, input/output, runtime/dependencies, quyền và
evidence của lần chạy phù hợp. Catalogue/description/route chỉ chứng minh có
hướng dẫn, không chứng minh engine hoặc end-to-end completion.

| Nhu cầu | Tuyến ưu tiên | Điều kiện nhận lại |
| --- | --- | --- |
| Profiling/cleaning/ETL/reconciliation/lineage | Data Engineering & Quality | Grain/keys, DQ checks, exceptions, mapping, source checksums/control totals, no silent repair |
| Build/calibrate/validate advanced models | Data Science & Model Validation | Target/time split/leakage, baseline, metrics/calibration/uncertainty, validation status, model card, limitations/monitoring |
| Process/control/SoD/SPOF chi tiết | Risk Control Process | Process scope, current evidence vs expected, controls/testing/gaps, residual exposure mechanism |
| Đa lĩnh vực vượt ERM | Master Orchestrator | Phân vai rõ, interfaces và conflicts, ERM giữ câu hỏi kinh doanh thuộc phạm vi mình |
| Design HTML/report hierarchy | UI/UX Ultra | Supported surface, design rationale, accessibility, visual QA; không suy native Office/calculation |
| Diagram | Creative Diagram | Đúng semantic type/profile/renderer; exact relationships/units, evidence/limits; không thay heatmap 5×5 bằng quadrant |
| Excel/Word/PPT/PDF | Artifact skills/tools hiện có | Formula/data reconciliation, format/editability thật, render/visual review |

Các lĩnh vực BCP, Internal Audit, Investigation, Legal, Finance, Cyber/OT,
Crisis Communication, Third-Party Risk và Issue Management: tìm capability
thực tế theo nhu cầu, không bịa tên skill/công cụ vắng mặt. BCP xử lý BIA/recovery;
IA xử lý assurance, investigation xử lý allegations/evidence; pháp lý xử lý
luật/jurisdiction; ERM giữ exposure, appetite và quyết định điều hành.

Snapshot discovery lịch sử tại G1 (2026-09-03): DEQ 1.1.1 có CSV/TSV helpers;
DSMV 1.2.0 có validation metrics, chưa chứng minh mọi fitted engine; UI/UX Ultra
2.0.1 loại trừ native Office/spreadsheet calculation; Creative Diagram 2.5.0 có
SVG profiles, chưa có profile riêng heatmap/bow-tie/waterfall/fan. Không dùng
snapshot này thay discovery tại runtime hoặc mặc định mọi nền tảng cài cùng bản.

## Input contract

Gửi một handoff có `id`, `decision_question`, `target`, `entity`, `segment`,
`horizon`, `data_as_of`, `input_refs` (location/version/hash), `assumptions`,
`constraints` (units, currency, privacy, resource, permissions),
`acceptance_criteria`, `uncertainty_required`, `output_contract`,
`capability_evidence` và `requested_scope`. Thiếu field thì nêu unknown/gap;
không cấp cho skill phụ quyền vượt yêu cầu người dùng.

Ví dụ synthetic: forecast default trong 12 tháng của khách hàng bán chịu; PD
cần calibration/out-of-time, không leakage do labels sau forecast origin;
trả PD theo entity cùng intervals và validation report, không tự đưa quyết định
cắt credit limit. ERM ánh xạ PD vào net exposure/EL, headroom và treatment.

## Return contract và acceptance gate

Kết quả cần `handoff_id`, `method_version`, `data_version`, `scope`, `as_of`,
`outputs`, `units`, `validation_status`, `validation_evidence`, `limitations`,
`model_card_ref` khi liên quan, `monitoring`, `unresolved_gaps`, `actions_taken`.
So sánh ID/scope/horizon/unit/data hash với yêu cầu; thiếu hoặc mismatch thì
quarantine phần output, hỏi sửa, không ghép vào báo cáo như đã accepted.

Không chấp nhận chỉ “PASS” không có test/method/sample/time evidence. Với model
đã validated: kiểm tra phiên bản, use limits, drift và applicability. Return
validation không thay production approval hoặc business decision authority.

## Specialist unavailable hoặc engine thiếu

Nêu chính xác chưa làm được phần nào. Tiếp tục context/CEI, deterministic
scenario, chất lượng dữ liệu và decision options có căn cứ. Trả bounded handoff
spec hoặc đề xuất nâng cấp để người dùng quyết định. Không giả vờ đã gọi skill,
đã fit/calibrate/backtest, không tự cài hay sửa skill phụ.

Không chuyển toàn bộ ERM cho specialist chỉ vì một phép tính cần hỗ trợ. Sau
khi nhận kết quả phù hợp, ERM vẫn giải thích mechanism, appetite impact,
treatment choices, uncertainty và quyết định cần người dùng phê duyệt.

## Snapshot acceptance trong bản 0.1.3

`handoffs[].validation_status` dùng PASS, PASS_WITH_LIMITS, FAIL, NOT_RUN hoặc
null. `result_status=validated` chỉ được dùng với PASS/PASS_WITH_LIMITS, capability
verified, method không trống và `validation_evidence_ids` tham chiếu ít nhất một
source current. Evidence phải mô tả test/method/sample/time và giới hạn trong
source/return contract; validator kiểm tham chiếu và trạng thái, không tự chứng
nhận tính đúng của tài liệu. Kết quả FAIL/NOT_RUN giữ received/rejected/not_run.
Snapshot cũ chưa có evidence IDs vẫn đọc được nếu chưa gọi kết quả là validated.
