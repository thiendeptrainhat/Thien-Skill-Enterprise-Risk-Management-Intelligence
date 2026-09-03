# Giải pháp và kế hoạch tổng thể

Cập nhật: 2026-09-03. Tài liệu chuẩn về kiến trúc, trình tự, trạng thái và quyết định.
Phạm vi: [Mục tiêu](MUC-TIEU.md). Năng lực/acceptance: [Yêu cầu](YEU-CAU.md).
Bất biến và hygiene gate: [Nguyên tắc](NGUYEN-TAC.md).

## 1. Trạng thái hiện tại

- **DOCUMENTATION_BASELINE:** đã lưu bộ định hướng gồm CLAUDE.md và bốn file docs.
- **IMPLEMENTATION:** chưa bắt đầu; chưa được người dùng cho phép bắt đầu.
- **RELEASE/INSTALLATION:** chưa tạo, chưa kiểm thử và chưa công bố.
- Phê duyệt ngày 2026-09-03 cho phép lưu giải pháp/kế hoạch và commit bộ tài liệu
  vào Git cục bộ; chưa cho phép triển khai skill.
- Bước tiếp theo: người dùng duyệt hoặc chỉnh các điểm còn mở; chỉ bắt đầu triển
  khai khi có yêu cầu rõ ràng. Không tự mở sang nâng cấp các skill liên quan.

## 2. Giải pháp kiến trúc

Một canonical skill source, tổ chức theo progressive disclosure:

- `SKILL.md`: định vị, intake, chọn tuyến ERM, decision gates và liên kết tài nguyên.
- Tài liệu phương pháp: taxonomy/data model, assessment/appetite, controls/KRI,
  scenario/trend/aggregation và treatment/reporting; gom theo trách nhiệm.
- Sáu industry packs: áp dụng lõi phương pháp theo từng ngành; không copy toàn bộ
  lõi vào mỗi pack. Ngành khác dùng adaptive workflow.
- Schema/template dùng chung: metadata lõi gọn, trường theo từng object;
  RiskTaxonomy L0–L2 dự kiến, RiskInstance tách riêng.
- Calculator ERM: logic truyền dẫn kinh doanh, công thức minh bạch và kiểm tra.
- Integration contracts: data preparation, model work, process deep dive và artifacts.
- Reporting layer: cùng dữ liệu/semantics, sinh nhiều định dạng và đối soát.
- Packaging layer: sinh gói đích từ nguồn chuẩn; không có ba codebase nền tảng.

Luồng xử lý chính:

1. Xác định câu hỏi, quyết định, context, scope, horizon, materiality và jurisdiction.
2. Kiểm tra dữ liệu/bằng chứng; đánh dấu thiếu và dùng skill dữ liệu khi cần.
3. Chọn nghiệp vụ ERM và gói ngành; tái sử dụng taxonomy/object model chung.
4. Phân tích/tính toán trong năng lực; handoff có contract nếu cần chuyên môn sâu.
5. Kiểm tra kết quả, uncertainty, appetite/treatment và quyền quyết định.
6. Sinh artifact, đối soát số liệu, kiểm tra trực quan và bàn giao có giới hạn rõ.

## 3. Ranh giới tích hợp

| Thành phần | Trách nhiệm trong giải pháp |
| --- | --- |
| Master Orchestrator | Điều phối yêu cầu đa lĩnh vực ở cấp tổng |
| ERM | Sở hữu câu hỏi kinh doanh, logic rủi ro, phép tính lõi và kết luận điều hành |
| Data Engineering & Quality | Chuẩn bị, đối soát, kiểm soát chất lượng và lineage dữ liệu |
| Data Science & Model Validation | Xây dựng/hiệu chỉnh/kiểm định mô hình nâng cao theo INT-02 |
| Risk Control Process | Phân tích quy trình và control chi tiết khi cần |
| UI/UX Ultra | Design direction, layout, hierarchy và visual QA |
| Creative Diagram | Sơ đồ được hỗ trợ, giữ đúng semantics |
| Artifact tools | Tạo và kiểm tra Excel/Word/PowerPoint/PDF/dashboard thực tế |

Mô hình ERM tự xử lý và các nhóm chuyển DSMV có danh mục chuẩn tại CALC/INT trong
[Yêu cầu](YEU-CAU.md); không duy trì danh mục thứ hai ở file này.

Các nhận định sơ bộ từ phiên lập kế hoạch cần kiểm tra lại khi triển khai:

- Hai skill dữ liệu có route và helper liên quan; chưa đủ bằng chứng rằng mọi
  mô hình nâng cao đã có engine tái sử dụng và end-to-end validation.
- UI/UX Ultra không thay công cụ tính toán spreadsheet hoặc tạo native Office.
- Creative Diagram có giới hạn profile/renderer; không mặc định hỗ trợ native
  heatmap 5×5, bow-tie đầy đủ, waterfall và uncertainty fan.
- Skill phụ không khả dụng phải kích hoạt nhánh xử lý có giới hạn, không bịa kết quả.

## 4. Cấu trúc dự án dự kiến

Chỉ năm file tài liệu đầu tiên đã được tạo. Các thư mục còn lại chỉ được tạo khi
bước triển khai tương ứng có nhu cầu thật; không dựng trước thư mục rỗng.

```text
Thien-ERM/
├── CLAUDE.md
├── docs/
│   ├── MUC-TIEU.md
│   ├── YEU-CAU.md
│   ├── NGUYEN-TAC.md
│   └── KE-HOACH.md
├── skill/
│   └── thien-skill-enterprise-risk-management-intelligence/
│       ├── SKILL.md
│       ├── agents/             # metadata nếu nền tảng cần
│       ├── references/
│       ├── industry-packs/
│       ├── templates/
│       ├── schemas/
│       ├── scripts/
│       ├── assets/
│       ├── integration/
│       └── hồ sơ license
├── tests/
├── qa/                         # bằng chứng chính thức
├── build/                      # staging có thể tái tạo
└── dist/<version>/             # ba ZIP và integrity evidence
```

Tên và số thư mục trong skill là thiết kế logic, sẽ được rút gọn nếu tài nguyên
có thể gom hợp lý. `agents/` metadata không phải lớp cài đặt `.agents/skills/`.
Không thêm `canonical/`, `platforms/` hoặc các bản mirror đầy đủ của skill.

## 5. Các giai đoạn sau khi được phép triển khai

### G0 — Chốt thiết kế và điều kiện nghiệm thu

Chốt metadata, dashboard mặc định, version/naming, file budgets và chính sách
giữ release; xử lý các quyết định mở. Dùng mã yêu cầu để liên kết QA, tránh
tạo thêm tài liệu trùng với bộ định hướng.

Hoàn thành khi các quyết định cần cho bước tiếp theo có căn cứ/phê duyệt rõ.

### G1 — Kiểm chứng nguồn, skill và nền tảng

Kiểm tra template license, logo nguồn, capability/version của skill liên quan,
cơ chế nền tảng và các tiêu chuẩn/nghiên cứu hiện hành. Ưu tiên ISO 31000,
IEC 31010, COSO ERM/appetite, IIA/Three Lines và nguồn chuyên ngành có liên quan;
chỉ lưu metadata/tóm tắt cần thiết, kiểm tra tài liệu thay thế hoặc hết hiệu lực.

Hoàn thành khi có capability matrix, source register và giới hạn đã biết.

### G2 — Mô hình nghiệp vụ và dữ liệu

Thiết kế taxonomy, RiskInstance, assessment/appetite, controls/RCM/RCSA, KRI,
scenario, treatment và reporting contracts. Chốt quan hệ object, as-of/version,
currency/entity/horizon, state precedence và cách tổng hợp không double-count.

Hoàn thành khi các object và workflow liên kết nhất quán với ERM-01 đến ERM-13.

### G3 — Skill lõi

Viết `SKILL.md`, intake, routing, progressive disclosure và các nhánh thiếu dữ
liệu/skill. Không nhồi mọi nghiệp vụ vào một file hoặc tạo file cho mỗi thuật ngữ.

Hoàn thành khi luồng ERM lõi có thể được kiểm tra hành vi độc lập với thiết kế hình thức.

### G4 — Định lượng và integration contracts

Tạo calculator cần thiết theo CALC, hợp đồng DEQ/DSMV theo INT, validation gates
và cách nhận lại kết quả. Không triển khai thay các engine nâng cao thuộc dự án
DSMV khi chưa được phép nâng cấp skill đó.

Hoàn thành khi phép tính có kiểm chứng phù hợp và handoff phản ánh đúng capability.

### G5 — Ngành và đầu ra

Hoàn thiện sáu industry packs, phương pháp ngành khác, templates/schema dùng
chung và đường tạo Excel/Word/PowerPoint/dashboard. Kết hợp UI/UX Ultra,
Creative Diagram và artifact tools theo năng lực đã kiểm tra.

Hoàn thành khi có đầu ra mẫu synthetic được gắn nhãn, đối soát và kiểm tra trực quan.

### G6 — Thương hiệu và pháp lý

Dùng logo nguồn, chỉ sinh biến thể cần thiết. Áp dụng license template theo
LEGAL-01 đến LEGAL-03; hỏi các trường còn thiếu, không tự đổi quyền cấp phép.

Hoàn thành khi metadata, assets và hồ sơ pháp lý nhất quán trong nguồn và gói.

### G7 — QA và vệ sinh

Thực hiện matrix tại mục 6; sửa các lỗi ảnh hưởng yêu cầu hoặc kết quả. Chạy
hygiene gate, chỉ giữ bằng chứng chính thức và ngoại lệ có giải thích.

Hoàn thành khi không còn lỗi chặn, mọi NOT_RUN/giới hạn được ghi đúng bản chất.

### G8 — Build và đóng gói

Sinh Claude/ChatGPT/Universal ZIP từ canonical source vào dist theo PKG.
Kiểm tra manifest/checksum, license, tài nguyên, package mismatch và reproducibility.
Universal không có lớp `.agents/skills/`.

Hoàn thành khi có ba gói đúng cơ chế nền tảng đã xác minh; nếu cần wrapper khác
thì phải có quyết định người dùng trước khi tạo.

### G9 — Kiểm thử nền tảng và bàn giao

Thử cài/đọc/trigger/hành vi trên Claude Web, Claude Code, ChatGPT Web và ChatGPT
Desktop trong phạm vi truy cập được phép. Tách native test khỏi kiểm tra ZIP.
Lập release audit, hướng dẫn sử dụng/cài đặt tối thiểu cần thiết, các giới hạn
và bước tiếp theo; không thêm tài liệu phụ nếu không có consumer cụ thể.

Hoàn thành khi khả năng được công bố có bằng chứng, các phần chưa kiểm chứng
được nêu rõ và dự án đáp ứng mục tiêu tinh gọn/bảo trì.

## 6. QA dự kiến

- **Structure:** naming/frontmatter, link/import, schema, resource và package.
- **Domain:** toàn bộ 120 tình huống tham khảo, rubric theo quyết định/kết quả,
  không theo việc khớp nguyên văn một câu trả lời.
- **Quantitative:** kết quả trọng yếu, units/currency/sign, missingness,
  scenario transmission, threshold boundaries và reproducibility.
- **Integration:** capability detection, handoff round-trip, specialist missing,
  model limitation và return contract.
- **Artifacts:** cross-format reconciliation và visual checks có ý nghĩa.
- **Platform:** import/install/trigger/fresh-context behavior trên bề mặt thực tế.
- **Edge cases:** metric direction, source lifecycle, methodology change giữa
  kỳ, duplicate loss, aggregation/dependency và multinational/industry cases.
- **Hygiene:** orphan/duplicate/size/line/count/temp/path/manifest/build gates.

Mỗi kết quả ghi rõ test hiện tại, bằng chứng lịch sử hoặc NOT_RUN; không dùng
sự tồn tại của test case để chứng minh đã chạy. Kiểm thử hành vi bằng phiên
mới/subagent phải có bối cảnh phù hợp và ghi đúng mức độ độc lập.

## 7. Đóng gói và nguồn đầu vào đã được chỉ định

Ba gói Claude, ChatGPT và Universal cùng một nguồn; quy tắc tên ZIP/version còn
chờ chốt. Hướng dẫn cài đặt phải phản ánh khả năng thật, đặc biệt ChatGPT Web/Desktop.

Các đường dẫn dưới đây chỉ là nguồn cục bộ cho dự án; không đưa vào runtime package:

- Logo: `/Users/thiendeptrainhat/Documents/Logo TDTN.png`.
- License: `/Users/thiendeptrainhat/Documents/Thien's Skills Library/Thien-Skills-License-Template/Tran-Ngoc-Thiens-Skills-Commercial-Source-Available-License-2.0.md`.
- Tài liệu tham khảo ban đầu: `/Users/thiendeptrainhat/.codex/attachments/fb4f53a0-0c59-470c-aee2-0f151382c403/pasted-text.txt`.
- Skill creator: `/Users/thiendeptrainhat/.codex/skills/.system/skill-creator/SKILL.md`.

Tham khảo cấu trúc dist của Thien-Skill-Risk-Control-Process, nhưng không sao
chép máy móc phạm vi, nội dung hoặc toàn bộ cấu trúc của skill đó.

## 8. Sổ quyết định và các điểm còn mở

### Đã chốt

- Một skill ERM, phạm vi/đầu ra/ngành/ngôn ngữ tại Mục tiêu và Yêu cầu.
- Tên đang dùng trong baseline: **Thiện's Skill — Enterprise Risk Management Intelligence**.
- Đa quốc gia; cho phép nhà máy/site và sản phẩm trọng yếu có materiality phù hợp.
- ERM tự tính phần lõi; chuyển mô hình nâng cao sang DSMV theo capability thực tế.
- Ba ZIP; Universal bỏ `.agents/skills/`; một canonical source.
- Logo TDTN; license song ngữ, ưu tiên tiếng Việt, luật/tài phán Việt Nam, giữ mẫu.
- Bắt buộc tinh gọn, có hygiene gate và QA có bằng chứng.
- Phạm vi được phép hiện tại: lưu tài liệu định hướng và commit Git cục bộ.

### Cần người dùng quyết định trước phần việc liên quan

- **D01:** chốt slug và typography hiển thị trước tạo metadata; giữ nguyên tên
  đầy đủ đang dùng trong baseline, không tự đổi tên thương hiệu.
- **D02:** version phát hành đầu tiên, quy tắc đặt tên ZIP và chính sách giữ release cũ.
- **D03:** dashboard mặc định/phạm vi hỗ trợ: HTML độc lập, tương tác hoặc nền tảng khác.
- **D04:** ngân sách số file, dung lượng và số dòng theo loại; ngưỡng cảnh báo/chặn.
- **D05:** các thông tin hành chính của license còn trống sau khi đọc mẫu, nếu có.
- **D06:** có dùng wrapper/plugin nếu kiểm chứng cho thấy nền tảng cần cơ chế đó.

### Cần kiểm chứng, không phải dữ kiện đã chốt

- **V01:** cơ chế cài đặt native chính xác trên ChatGPT Web/Desktop và package adapter.
- **V02:** capability/version thực tế của các skill tích hợp sau các lần nâng cấp.
- **V03:** yêu cầu kích thước/định dạng icon của từng nền tảng.
- **V04:** phiên bản/hiệu lực/phạm vi của standards, nghiên cứu và benchmark lúc sử dụng.
- **V05:** availability/quyền truy cập cần thiết cho platform-native tests.

Không tự suy câu trả lời cho D01–D06. Kiểm chứng V01–V05 trong phạm vi được phép;
chỉ hỏi người dùng khi kết quả tạo ra lựa chọn hoặc thiếu quyền/truy cập cần thiết.

## 9. Bàn giao giữa các phiên

Khi có tiến triển, cập nhật ngay mục Trạng thái và các quyết định liên quan;
ghi giai đoạn đã hoàn thành cùng bằng chứng ngắn, phần còn lại và bước kế tiếp.
Không tạo nhật ký, bản kế hoạch mới hoặc file trạng thái riêng cho từng phiên.
