# Giải pháp và kế hoạch tổng thể

Cập nhật: 2026-09-04. Tài liệu chuẩn về kiến trúc, trình tự, trạng thái và quyết định.
Phạm vi: [Mục tiêu](MUC-TIEU.md). Năng lực/acceptance: [Yêu cầu](YEU-CAU.md).
Bất biến và hygiene gate: [Nguyên tắc](NGUYEN-TAC.md).

## 1. Trạng thái hiện tại

- **GitHub — đã push:** bộ 1.0.0, README, QA và lịch sử bản thử đã được lưu trên
  `thiendeptrainhat/Thien-Skill-Enterprise-Risk-Management-Intelligence`, nhánh
  `main`, repository Private. Commit triển khai `04cf12e` nối baseline `d2741d4`;
  remote ref đã xác minh khớp. Không tạo GitHub Release. Chi tiết mục 23.
- **Tag v1.0.0:** đã tạo annotated tag ở máy và push lên GitHub theo yêu cầu;
  trỏ đến commit bàn giao `d3199e5`, hash tag/commit hai bên khớp. Chi tiết mục 23.
- **DOCUMENTATION_BASELINE:** baseline `d2741d4` đã được đọc và giữ làm mốc.
- **IMPLEMENTATION:** G0–G8 đã triển khai trong working tree ngày 2026-09-04.
  Canonical source có 31 file, khoảng 1,36 MiB; không có `.agents/skills/`, mirror hoặc
  thư mục rỗng. D01–D06 áp dụng đúng bảng tại mục 8.
- **RELEASE cục bộ:** **1.0.0 — Release**, ba ZIP Claude/ChatGPT/Universal
  tại `dist/1.0.0/`; manifest, canonical bytes và reproducibility đã kiểm.
  Nghiệm thu có giới hạn công bố tại mục 21 và USAGE; chưa cài/native-test 1.0.0.
  Giữ nguyên các bản Testing 0.1.0–0.1.4 và bản cài Claude 0.1.3.
- **QA 0.1.4:** 45 tests PASS/0 skip; Word kiểm style/nội dung và xem đủ 3 trang.
  120 domain responses, Excel 16 sheets, PPT 8 slides, HTML và native 0.1.3 là
  evidence lịch sử; không chuyển thành PASS 0.1.4. Chi tiết `qa/RESULTS.json`.
- **G9 — đã được phép 2026-09-04:** người dùng cho phép cài 0.1.0 trên Claude
  Code và upload bản thử lên ChatGPT Web; chỉ dẫn sau đó cho phép sửa logo và
  kiểm tra lại bằng cách replace bản Testing. Quyền này không tự mở rộng sang
  cài Claude Web/Desktop, sửa skill khác, push hoặc xuất bản.
- **Claude Code 0.1.3:** đã cập nhật, 31/31 file khớp manifest; CLI 2.1.183
  discovery PASS; native core/report/R02, workflow DEQ đọc từ file và Office
  export/render/overflow **PASS_WITH_LIMITS**. Dịch vụ đã hoạt động trở lại;
  hai lượt 529 và lượt dừng do hiểu nhầm quyền lệnh giữ làm lịch sử, không còn là blocker.
- **ChatGPT Web 0.1.3:** thay bản thử thành công, phiên mới đọc đúng VERSION;
  30/31 file khớp, không thiếu, YAML chuẩn hóa và thêm icon.svg. Logo card đúng.
  Native core/R02 gate, workflow DEQ và Office export/render **PASS_WITH_LIMITS**;
  chi tiết/giới hạn tại mục 15 và `qa/G9-NATIVE.json` → `regression_0_1_3`.
- **READINESS AUDIT 0.1.2:** **NOT_READY_FOR_1.0.0**. Lượt rà soát bổ sung phát
  hiện bốn lỗi chặn R01–R04 tại mục 13; các PASS cũ không bao phủ những lỗi này.
  Nguồn chuẩn và release 0.1.2 được giữ nguyên trong lượt audit.
- **REMEDIATION 0.1.3:** đã sửa R01–R04; R01/R02/R04 kiểm thử PASS,
  R03 đóng trong phạm vi smoke bằng test dữ liệu/static và **USER_REPORTED_PASS**
  cho bốn mục dashboard 0.1.3. Chi tiết tại mục 14.
- **FINAL ACCEPTANCE 0.1.3:** **NOT_READY_FOR_1.0.0**. Native trả lời tự do
  phát hiện R05/R06; đối chiếu Word xác nhận R07. Tự chọn skill và handoff kỹ thuật
  có thêm bằng chứng đạt trong phạm vi giới hạn; chi tiết tại mục 16.
- **REMEDIATION 0.1.4:** đã sửa mã/hướng dẫn và kiểm hồi quy tập trung. R07 đóng
  trong phạm vi lỗi đã xác minh; R05 còn lỗi native xác nhận phép tính chưa chạy,
  R06 còn ca reverse stress chưa hoàn tất. **Người dùng đã dừng kiểm thêm Claude**;
  giữ kết quả thực tế, chưa chuyển thành nghiệm thu 1.0.0. Lịch sử ở mục 17;
  **điều kiện còn thiếu và phạm vi công bố đã đối chiếu tại mục 18**.
- **NGUỒN HIỆN TẠI:** **1.0.0**, nâng từ đúng nguồn 0.1.5 đã kiểm R05/R06;
  chỉ đổi VERSION, USAGE và dòng phiên bản sản phẩm trong LICENSE-APPLICATION.
  Mã/phương pháp/schema/ngành/assets giữ nguyên; hồi quy promotion 12/12 đạt.
  R05 chỉ đóng ở đường sinh calculator, không xác nhận mọi lời văn host. Chi tiết mục 21.
- **R06 nguồn 0.1.5:** **PASS_WITH_LIMITS**, 4/4 ca hành vi trên ChatGPT Web
  nạp ZIP nguồn trong phiên mới; không cài native, không chạy thêm Claude. Chi tiết mục 20.
- **Nghiệm thu cuối:** 54/54 mã yêu cầu được đối chiếu với evidence và giới hạn;
  không còn lỗi chặn trong phạm vi đã chốt. Bộ 1.0.0 hoàn tất tại máy.
  Native 1.0.0 chưa kiểm; Claude Web/Desktop vẫn NOT_RUN; HTML smoke là
  USER_REPORTED_PASS. Không tự cài, push hoặc phát hành bên ngoài. Chi tiết mục 21.

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

Cây dưới đây là thiết kế logic; trạng thái triển khai thực tế xem mục 1.
Chỉ tạo thư mục khi có tài nguyên sử dụng thực tế; không dựng trước thư mục rỗng.

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

Ba gói Claude, ChatGPT và Universal cùng một nguồn; tên ZIP/version theo D02. Hướng dẫn cài đặt phải phản ánh khả năng thật, đặc biệt ChatGPT Web/Desktop.

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
- Phạm vi triển khai hiện tại theo mục 1; quyền lưu/commit tài liệu baseline
  trước đây không mở rộng thành quyền cài đặt, push hoặc phát hành.

### D01–D06 — đã được người dùng quyết định

Chỉ dẫn mới nhất của người dùng trong phiên triển khai xác nhận:

| ID | Quyết định có hiệu lực |
| --- | --- |
| D01 | Giữ **Thiện's Skill — Enterprise Risk Management Intelligence**; dùng slug đã đề xuất `thien-skill-enterprise-risk-management-intelligence` |
| D02 | Bản thử `0.1.0 — Testing`; bản hoàn thiện `1.0.0`. Tên ZIP `<slug>-<version>-<platform>.zip`; giữ release đã bàn giao, không tự xóa |
| D03 | Dashboard HTML tương tác, mở offline, không backend/CDN |
| D04 | Dung lượng đề xuất được chấp thuận. Số file linh hoạt khi mở rộng; các mốc đếm chỉ để rà soát trách nhiệm, consumer và trùng lặp, không còn là trần cứng |
| D05 | Giữ nguyên mẫu license 2.0. Tuyên bố áp dụng mang tên “Tran Ngoc Thien's Skill”; ngày áp dụng là ngày tạo gói Testing đầu tiên; repository local-only cho đến khi có thay đổi thực tế |
| D06 | Ba ZIP từ một thư mục skill chuẩn, chưa dùng wrapper/plugin. Chỉ xem lại adapter khi native test có bằng chứng cần thay đổi |

Ngân sách và cổng bảo trì (MiB = 1.048.576 byte):

| Phạm vi | Cảnh báo/rà soát | Chặn |
| --- | ---: | ---: |
| Canonical, payload giải nén và một staging payload | 3 MiB | 5 MiB |
| Mỗi ZIP nén | 3 MiB | 5 MiB |
| QA chính thức mỗi lượt | 15 MiB | 25 MiB |
| Mỗi binary asset | 1,5 MiB | 2 MiB |
| Mỗi text file / HTML template | 100 KiB / 250 KiB | 200 KiB / 500 KiB |

Mốc đếm để rà soát: canonical 32/40 file, ZIP 34/42, source dự án 48/60,
QA mỗi lượt 15/20. Vượt mốc phải giải thích trong hygiene evidence về mục đích,
consumer, khả năng gom và chi phí bảo trì; không tự dừng chỉ vì số file khi phần
mở rộng vẫn trong phạm vi đã duyệt. Thay đổi phạm vi hoặc vượt trần dung lượng
vẫn cần quyết định người dùng. Không lách ngân sách bằng file một dòng khổng lồ.

Mốc review số dòng: SKILL 200/300; reference/pack 300/450; code/schema/test
500/800; tài liệu quản trị 600/800; metadata/hướng dẫn 150/250. Đây là mốc bảo
trì, không phải lý do cắt nội dung cần thiết. License nguồn giữ nguyên 901 dòng.
Một logo chuẩn; biến thể chỉ khi có consumer kỹ thuật. Không tạo file/thư mục
rỗng, mirror hay log trạng thái song song. Release gồm ba ZIP và integrity evidence.

### Cần kiểm chứng, không phải dữ kiện đã chốt

- **V01:** cơ chế cài đặt native chính xác trên ChatGPT Web/Desktop và package adapter.
- **V02:** capability/version thực tế của các skill tích hợp sau các lần nâng cấp.
- **V03:** yêu cầu kích thước/định dạng icon của từng nền tảng.
- **V04:** phiên bản/hiệu lực/phạm vi của standards, nghiên cứu và benchmark lúc sử dụng.
- **V05:** availability/quyền truy cập cần thiết cho platform-native tests.

D01–D06 đã chốt như bảng trên. Kiểm chứng V01–V05 trong phạm vi được phép;
chỉ hỏi người dùng khi kết quả tạo ra lựa chọn hoặc thiếu quyền/truy cập cần thiết.

## 9. Bàn giao giữa các phiên

Khi có tiến triển, cập nhật ngay mục Trạng thái và các quyết định liên quan;
ghi giai đoạn đã hoàn thành cùng bằng chứng ngắn, phần còn lại và bước kế tiếp.
Không tạo nhật ký, bản kế hoạch mới hoặc file trạng thái riêng cho từng phiên.

## 10. Bằng chứng G0/G1 — phiên triển khai 2026-09-03

Đây là sổ bằng chứng ngắn trong Kế hoạch, không phải chứng nhận release. Những
lần chạy dưới đây là kiểm tra tại host hiện tại, không phải native ERM test.

### V01/V05 — nền tảng và quyền truy cập

| Bề mặt | Điều đã xác minh | Điều chưa làm và giới hạn |
| --- | --- | --- |
| ChatGPT Web | Chrome đã đăng nhập; `Plugins → Skills → Create → Upload from your computer` mở hộp “Upload a skill”, ghi `.zip/.skill` hoặc `SKILL.md` | Không chọn/upload file. Root layout, resources, script execution, trigger và fresh-context behavior của ERM: **NOT_RUN** |
| ChatGPT Desktop | Tài liệu chính thức công bố standalone skills; inventory app có tên ChatGPT, bundle `com.openai.codex` | CUA từ chối truy cập bundle này vì quy tắc an toàn của công cụ. Không lách bằng công cụ khác. Không dùng thành công trong phiên Codex để suy ChatGPT Desktop đã test; native ERM: **NOT_RUN** |
| Claude Web | Chrome đã đăng nhập; mở Skills, thấy danh sách và Add skill. Tài liệu Anthropic quy định ZIP có thư mục skill cùng tên | Chưa upload/install, chưa xác minh runtime code execution của ERM; native ERM: **NOT_RUN** |
| Claude Code | `claude --version` chạy thành công: `2.1.183` | Chưa kiểm tra auth/quota/model run, chưa cài ERM; native ERM: **NOT_RUN** |

V01: xác minh được định dạng UI chấp nhận trên Web, **chưa chứng minh một gói
import thành công**. V05: quyền kiểm tra read-only đã dùng; cài đặt/upload vẫn
chưa được người dùng cho phép. Desktop có blocker công cụ cụ thể, cần user-run
hoặc bề mặt được phép khi đến G9. Chưa cần xin quyền đó trước khi có gói reviewable.

[OpenAI Build skills](https://learn.chatgpt.com/docs/build-skills) nêu standalone
trên Desktop và plugin xuyên các bề mặt; trang này chưa mô tả đường upload Web
đã quan sát. Dùng bằng chứng UI theo đúng tài khoản và ngày kiểm tra, không suy
ra mọi tài khoản đều có. [Anthropic custom skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)
và [Claude Code skills](https://code.claude.com/docs/en/skills) là nguồn cấu trúc
Claude; không dùng cơ chế API làm bằng chứng native Web/Desktop.

### V02 — capability matrix tại host

Identity được đọc từ manifest/VERSION/license application, không suy version
skill từ LICENSE-VERSION. SHA-256 dưới đây là của SKILL.md thực tế đang đọc;
phải kiểm tra lại tại thời điểm handoff, không đóng cứng máy người dùng vào package.

| Skill | Identity | Đã xem/chạy | Giới hạn sử dụng cho ERM |
| --- | --- | --- | --- |
| DEQ | `1.1.1`, PACKAGE-MANIFEST | `profile_tabular.py`, `reconcile_tabular.py` chạy synthetic CSV, kết quả bên dưới | CSV/TSV helper hoạt động; chưa chứng minh ETL mọi định dạng hoặc Power BI end-to-end |
| DSMV | `1.2.0`, PACKAGE-MANIFEST và TOOL_VERSION | doctor, classification, invalid probability chạy; đọc command surface regression/forecast/temporal-check/drift/manifest | Có metrics/validation helpers, không phải fitted forecasting/EVT/copula/solver engine. Những engine INT-02 chưa chạy: **NOT_RUN** |
| UI/UX Ultra | `2.0.1`, VERSION và BUILD-INFO | `route.py` với native Excel trả “outside this release scope” | Không chuyển spreadsheet calculation/native Office cho skill này; chỉ dùng design theo surface hỗ trợ |
| Creative Diagram | `2.5.0`, SOURCE_MANIFEST.project | `output_pipeline.py --print-job-contract` chạy, khai báo 45 profiles; output SVG + ledger | Không có profile riêng heatmap 5×5/bow-tie/waterfall/uncertainty fan. Chưa render test mới; không coi quadrant/fishbone là thay thế tương đương |
| Risk Control Process | `1.1.1`, LICENSE-APPLICATION | Đã đọc route và phạm vi quy trình/RCM/SoD/SPOF | Handoff nghiệp vụ chuyên sâu; hành vi runtime mới chưa test |
| Master Orchestrator | `1.2.1`, VERSION | Đã đọc routing/capability/authority contract | Chỉ chuyển yêu cầu đa lĩnh vực vượt ERM, không thay ERM owner; chưa test delegation |

| Skill | SHA-256 SKILL.md |
| --- | --- |
| DEQ | `bdfa41fd1253e3aeae2526b8d66cdaab13a651e86df62bb96d1a84dc532e7f12` |
| DSMV | `25baeea5541e15328e89725e3a118bfcf4f5809e2ec7f74ec963b266b6bd0a8e` |
| UI/UX Ultra | `d016a43b99173b5736f0e0f5e050841e9b748d115f23583c79cb068d709084d4` |
| Creative Diagram | `70ec9f968edb7a423bd42207a12642b9cd82c52d4a9308ee5ef2e0185829a534` |
| Risk Control Process | `12ffe085521c62df2c3a4545c53118e30384a6ed769ecbcf0475b61894d384d9` |
| Master Orchestrator | `c53cd06940f3de7e21fb6f77619b4257b269ac982757d841b17d4890bf74f400` |

Bundled runtime `26.826.12353`, Python `3.12.13`: kiểm tra metadata thấy
openpyxl 3.1.5, python-docx 1.2.0, python-pptx 1.0.2, Pillow 12.3.0,
numpy 2.3.5, pandas 2.2.3. PyYAML/jsonschema/sklearn/nbformat/nbclient không
được phát hiện trong runtime này. Đây là availability, **chưa phải** export,
recalculation, render hoặc cross-format QA. Chưa cài dependency nào.

### Bằng chứng chạy helper

Thực hiện bằng bundled Python với `-B`/`PYTHONDONTWRITEBYTECODE=1`; toàn bộ fixture
trong `TemporaryDirectory` và đã dọn sau khi chạy; không ghi vào skill tích hợp.
Fixture gốc CSV: header `id,amount,target,score`, hai dòng `a,10,0,0.1` và
`b,20,1,0.9` (synthetic). Không có dữ liệu doanh nghiệp thật.

| Check | Lệnh/biến thể đủ tái hiện | Actual và đánh giá |
| --- | --- | --- |
| G1-PROFILE | `profile_tabular.py a.csv` | Exit 0; 4 cột, amount min=10 max=20; assertion **PASS** |
| G1-RECON-EQUAL | `reconcile_tabular.py a.csv b.csv --key id --amount amount`; b bằng a nhưng file khác | Exit 0; amount source=target=30, difference=0; smoke thành công, không phải đối soát data thực |
| G1-RECON | Lệnh trên; đổi amount của a/b trong b.csv thành 20/10 | Exit 1, amount status CONDITIONAL; difference tổng=0 nhưng mismatch theo key=2; assertion phát hiện sai lệch **PASS** (không đổi CONDITIONAL thành PASS của dataset) |
| G1-CLASS | `model_validation.py classification --input a.csv --target-col target --score-col score --output c.json` | Exit 0; Brier≈0.01, ROC AUC=1; assertion **PASS** trên 2 dòng synthetic, không chứng minh calibration/external validity |
| G1-INVALID | Lệnh classification với `target,score`: `0,1.2` và `1,0.9` | Exit 2, “Probability outside [0,1]”; không có report file; assertion **PASS** |
| G1-DOCTOR | `model_validation.py doctor` | Exit 0; core_supported=true; optional modules chỉ là detection |
| G1-DIAGRAM-CONTRACT | `output_pipeline.py --print-job-contract` | Exit 0; 45 public profiles, fixed output SVG/ledger; discovery thành công, rendering **NOT_RUN** |
| G1-OFFICE-ROUTE | `route.py 'Create native Excel workbook with risk formulas' --format text` | Exit 0; từ chối route Office đúng giới hạn đã công bố; Office artifact **NOT_RUN** |

### Nguồn đầu vào cục bộ

- Logo mục 7 đọc được và đã xem trực quan: PNG 1100×1100, 948.765 byte,
  SHA-256 `020a47a3c831664c700c9e4491c7ae00cf5a8f330e6c3c57422ee246df56d69e`.
  Chưa tạo bản sao hay biến thể.
- License mục 7: 901 dòng, 51.373 byte,
  SHA-256 `ced33214d371fabe382d3ca303042af7219ad96fb98acdd1b858d0d89478d4b5`.
  Header đã có owner Tran Ngoc Thien, email, địa chỉ Ho Chi Minh, Vietnam và
  effective date 03 August 2026; áp dụng ERM phụ thuộc D05, không sửa template.
- Tài liệu gốc mục 7: SHA-256
  `f364f012ec2e3dc0f9c09cb35aae3516b1348c96c1540f7c07aa4e614d8899e2`.
  Đã xác định danh sách 120 case tại dòng 3760–3912; chưa chạy các case ERM.
  Dòng “ít nhất 60” trong tài liệu tham khảo không hạ yêu cầu baseline QA-01=120.

### V03 — icon và adapter

- Logo nguồn đã đáp ứng định dạng PNG, hình vuông; chưa có bằng chứng cần resize.
- `skill-creator/references/openai_yaml.md` và phần Optional metadata của
  [OpenAI Build skills](https://learn.chatgpt.com/docs/build-skills) hỗ trợ
  `icon_small`/`icon_large` bằng đường dẫn tương đối, có ví dụ SVG/PNG; không
  đưa ra kích thước pixel bắt buộc trong nguồn đã đọc. Đề xuất cùng trỏ một logo.
- Tài liệu cấu trúc Claude đã đọc không yêu cầu icon riêng để import skill.
  Không biến ví dụ logo trong tài liệu thành yêu cầu hệ thống.
- Kích thước/hiển thị thực tế trên từng UI: **NOT_RUN**; không tự tạo icon
  32/128/512px theo suy đoán. Chỉ tạo biến thể khi native test cho thấy consumer.
- [Plugin manifest](https://developers.openai.com/plugins/build/plugins) có
  `composerIcon`/`logo`, nhưng chỉ áp dụng nếu D06 sau này cần wrapper; không
  dùng schema plugin để suy standalone skill cần plugin hoặc một bộ icon mới.

Các dòng trên ghi kết quả G1 trước khi import. G9 sau đó cung cấp consumer thực:
ảnh master 1100×1100 bị ChatGPT thay bằng icon mặc định, còn PNG 128×128 và
512×512 làm UI sinh đúng logo TDTN. Đây là bằng chứng target-specific; nguồn
OpenAI công khai đã tìm chỉ xác nhận upload ZIP, không nêu fallback threshold.

### V04 — source register ban đầu

Ngày kiểm tra toàn bảng: **2026-09-03**. `PUBLIC_METADATA` nghĩa là đã mở trang
chính thức và đọc metadata/phạm vi, không phải đọc toàn văn có bản quyền.
Nguồn phương pháp không tự là quy định pháp lý tại mọi quốc gia hoặc ngưỡng
appetite. Không sao chép toàn bộ tiêu chuẩn hay bảng/ảnh vào gói thương mại.

| ID / nguồn chính thức | Phiên bản và trạng thái thấy được | Phạm vi dùng / giới hạn đọc |
| --- | --- | --- |
| S01 — [ISO 31000](https://www.iso.org/standard/65694.html) | 2018, edition 2; trang ghi confirmed 2023/current và có ISO/CD 31000 đang phát triển | PUBLIC_METADATA; khung ERM mọi ngành. Bản dự thảo không thay thế bản published |
| S02 — [IEC 31010](https://www.iso.org/standard/72140.html) | 2019, edition 2, published; thay edition 2009 | PUBLIC_METADATA; chọn kỹ thuật assessment, không coi là chuẩn bắt buộc dùng 5×5 |
| S03 — [COSO ERM](https://www.coso.org/guidance-erm) | Trang tiếp tục dẫn framework 2017, Risk Appetite—Critical to Success 2020; có Practical ERM 2026 | PUBLIC_METADATA/index; strategy/performance và appetite. Chưa đọc đầy đủ publication 2026 hoặc nội dung trả phí |
| S04 — [IIA Statements of Position](https://www.theiia.org/en/resources/statements-of-position) | Three Lines Model và Role of Internal Audit in ERM mới, công bố 08/07/2026, thay position papers cũ | PUBLIC_METADATA và tóm tắt chính thức; quản trị/ranh giới ERM–IA. Bản 2020/update 2024 chỉ là lịch sử |
| S05 — [Codex CXC 1-1969](https://doi.org/10.4060/cc6125en) | PDF FAO đã mở: revised 2022; ấn phẩm Rome 2023 | Đọc metadata/trang đầu, chưa đọc toàn văn 60 trang. FMCG thực phẩm, chất lượng/HACCP; không phủ FMCG phi thực phẩm. Không nhúng tài liệu CC BY-NC-SA vào package thương mại |
| S06 — [FAO Disasters and Agriculture](https://www.fao.org/publications/fao-flagship-publications/the-impact-of-disasters-on-agriculture-and-food-security/) | Báo cáo 2025, edition 2; trang phân biệt các bản 2023/2021 | PUBLIC_METADATA; nông nghiệp, shock/cascade và exposure. Không chuyển tỷ lệ thiệt hại tổng hợp thành xác suất doanh nghiệp |
| S07 — [WOAH Codes and Manuals](https://www.woah.org/en/what-we-do/standards/codes-and-manuals/) | Trang xác nhận phạm vi health/welfare/trade; edition hiện hành cụ thể chưa hiện trong nội dung lấy được | PUBLIC_METADATA; chăn nuôi. **OPEN**: chọn đúng edition/chapter/species/jurisdiction trước dẫn yêu cầu cụ thể |
| S08 — [UNCTAD RMT 2025](https://unctad.org/publication/review-maritime-transport-2025) | Search metadata có RMT 2025; mở publication/index/press release đều bị HTTP 403 | **ACCESS_LIMITED**, chưa đọc nội dung; ứng viên cho logistics biển, không suy toàn bộ logistics hay dùng số liệu chưa đọc |
| S09 — [PCI SSC Document Library](https://www.pcisecuritystandards.org/document_library/) | Danh mục hiện có PCI DSS v4.0.1 | PUBLIC_METADATA/index; retail có thanh toán thẻ, không suy mọi retailer cùng phạm vi PCI. Chưa xác định obligation theo hệ thống/hợp đồng cụ thể |
| S10 — [NIST CSF](https://www.nist.gov/cyberframework) | CSF 2.0; CSF 1.1 ở archive; SP 1353 ipd là draft đang lấy ý kiến | PUBLIC_METADATA; IT/outsourcing và cyber mọi ngành. Không đổi draft thành requirement chính thức |
| S11 — [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) | AI RMF 1.0 đang revision; GenAI Profile NIST AI 600-1 ngày 26/07/2024; critical infrastructure 2026 mới concept note | PUBLIC_METADATA; AI governance, không cung cấp tỷ lệ effort saving hay xác suất thương mại cho IT outsourcing |

V04 đã xác minh nguồn nền tảng/phạm vi và phát hiện thay thế quan trọng tại S04.
Các khoảng trống S03/S05–S09 được giữ rõ; kiểm tra nguồn chi tiết khi viết pack
và trước dùng benchmark. Dữ liệu thị trường, pháp luật, disease status, FX và
ngưỡng doanh nghiệp phải được kiểm tra theo nhiệm vụ, không đóng cứng tại G1.

### Tham khảo packaging và mức kiểm chứng

Đã mở ba ZIP `1.2.1` trong dist dự án cục bộ `Thien-Risk-Process-Control`:
Claude 48 file; ChatGPT 49; Universal 49. Có đủ năm file pháp lý theo LEGAL-03.
Universal tham khảo chứa `.agents/skills/`; **không áp dụng** cấu trúc này cho ERM.
Runtime skill RCP đang đọc vẫn là `1.1.1`. Chưa cài hay chuyển sang dist `1.2.1`.
Việc đọc ZIP chỉ là structure inspection, không chứng minh native install.

### G2–G8 đã triển khai

Thiết kế object/quan hệ đã chuyển vào nguồn chuẩn, không giữ bản mô tả song song:
[Data model](../skill/thien-skill-enterprise-risk-management-intelligence/references/data-model.md),
[Schema](../skill/thien-skill-enterprise-risk-management-intelligence/schemas/engagement.schema.json)
và [Assessment/appetite](../skill/thien-skill-enterprise-risk-management-intelligence/references/assessment-appetite.md).
Source register vận hành nằm tại [sources.md](../skill/thien-skill-enterprise-risk-management-intelligence/references/sources.md);
mục V04 ở trên là bằng chứng xác minh lịch sử.

## 11. Bằng chứng triển khai G2–G8 — 2026-09-04

| Gate | Actual / trạng thái |
| --- | --- |
| G2 data model/schema | PASS: validator standard-library kiểm structure, unique/referential IDs, taxonomy levels, source replacement cycle, method/horizon, metric unit/currency/scope, future/stale observation và authority fields |
| G3 core skill | PASS: skill-creator progressive disclosure; 120 prompts synthetic được 3 fresh agents chạy, mỗi batch review bởi agent khác; 120 PASS cho response behavior, không suy native/external behavior |
| G4 quantitative | PASS: 27 tests; margin/pass-through, working capital/cash, credit/concentration, disruption/quality/inventory, project EAC, headroom, treatment NPV, deterministic simulation, threshold/missing/source/method/dedup/injection edge cases |
| G4 integration | Contract và capability gates đã viết; helper smokes G1 PASS_WITH_LIMITS. Specialist handoff thật **NOT_RUN** |
| G5 industries | Sáu pack FMCG, agriculture, livestock, logistics, retail và IT/outsourcing có driver–CEI–KRI–scenario–treatment và industry boundaries; tests 1–120 bao phủ route/context synthetic |
| G5 artifacts | Từ một snapshot SHA-256 `c19b9fee55c6dc41ee667411e8b7d658ed8dc98ef5e151f4e2adda331f3ff8ac`: Excel/Word/PPT/HTML đều chứa R1–R3, K1–K3, SC1, TR1. Excel formula counts 3/2/1 và KRI statuses khớp engine |
| Visual QA | Excel 15 sheets PASS, Word 2 trang PASS, PPT 6 slides PASS và no-overflow; HTML structure/JS syntax/offline CSP PASS. Lượt kiểm lại 2026-09-04 đạt 15/15 static checks cho responsive breakpoint, focus, native controls, `aria-live`, event wiring, escaping và ID/data contract; interaction/visual vẫn **NOT_RUN** vì Browser Use chặn agent tự mở `file://` |
| G6 legal/brand | Logo nguồn dùng một PNG; LICENSE copy byte-for-byte template; application date 2026-09-04; đủ LICENSE-APPLICATION, LICENSE-VERSION, NOTICE, THIRD-PARTY-NOTICES và OpenAI metadata |
| G7 hygiene | PASS: 29 canonical files/1,1 MiB, mỗi ZIP ~1,03 MB, QA 3,4 MiB/10 file trước evidence; không empty/temp/cache/machine path/broken relative link; license 901 dòng là ngoại lệ bắt buộc vì giữ nguyên mẫu |
| G8 packaging | PASS: ba ZIP, 30 entries/gói gồm direct skill folder + generated PACKAGE-MANIFEST; internal hashes re-read; deterministic timestamp; Universal không có `.agents/skills/` |

Domain evidence nằm trong ba batch `qa/domain-*.json`: response, tool dùng,
limitations và reason review trên từng case. `qa/RESULTS.json` là summary chính;
không phải tài liệu trạng thái thứ hai. Sample artifacts trong `qa/sample/` dùng
hoàn toàn dữ liệu synthetic, không chứng minh phương pháp hoặc dữ liệu doanh
nghiệp thực. `dist/0.1.0/RELEASE-MANIFEST.json` và `SHA256SUMS` là integrity
metadata, không phải tuyên bố cài đặt thành công.

### Các giới hạn giữ lại cho G9/1.0.0

- Claude Code và ChatGPT Web đã cài/upload và chạy native smoke; blocker xác thực
  và file chooser khi upload đã được người dùng xử lý. Claude Web chưa được cấp
  quyền cài; ChatGPT Desktop vẫn bị giới hạn truy cập CUA. Không suy kết quả giữa
  các bề mặt.
- HTML interaction/visual vẫn **NOT_RUN**: ngày 2026-09-04 Browser Use URL policy
  chặn cả điều hướng lẫn lấy tab Chrome sau khi người dùng tự mở dashboard.
  Quyền file URL của tiện ích không gỡ được giới hạn này; không thử đường vòng.
  Sau checklist tìm kiếm/filter/reset/keyboard, người dùng xác nhận “okie rồi đó”:
  ghi **USER_REPORTED_OK** trong `qa/RESULTS.json`. Chưa có kết quả từng ca, ảnh
  hoặc kích thước viewport; không suy thành coverage đầy đủ hay agent-tested PASS.
- Capability của skill liên quan phải khám phá lại tại mỗi handoff; không nâng
  version khác hoặc giả định có engine chưa test.
- Version chỉ lên 1.0.0 sau khi các blocker nghiệm thu được giải quyết hoặc người
  dùng chấp nhận rõ các NOT_RUN còn lại; không đổi version chỉ vì đã có ZIP.
- Không push hoặc phát hành công khai; cài/upload chỉ trong hai bề mặt đã được
  người dùng cho phép. Không sửa/nâng cấp skill khác.

## 12. G9 — bằng chứng native 2026-09-04

### Lần thử đầu — lịch sử, blocker đã được xử lý

- Claude package đã cài bằng `unzip -n`; target chưa tồn tại, không ghi đè skill
  khác. Hash 29 file đối chiếu lại với manifest: PASS. Init event của CLI có tên
  skill trong cả `skills` và `slash_commands`: chỉ ghi PASS discovery.
- `claude auth status` trong sandbox báo chưa đăng nhập; chạy ngoài sandbox xác
  nhận OAuth có trong Keychain. API call thực tế vẫn 401 token revoked, nên
  không dùng loggedIn=true làm bằng chứng phiên model chạy thành công.
- Direct installed-script smoke: pass-through baseline 30000, scenario 21500,
  delta -8500; validator synthetic VALID và giữ warning C1 thiếu evidence.
  Đây là kiểm tra resource/runtime, không phải Claude tự gọi tool thành công.
- ChatGPT upload dừng ở `fileChooser.setFiles`: code -32000, Not allowed;
  upload dialog còn mở, không có success. Công cụ hướng dẫn người dùng bật
  Allow access to file URLs. Chưa thay adapter hoặc rebuild vì chưa có lỗi package.
- `qa/G9-NATIVE.json` giữ bằng chứng gọn, không lưu token/credential hoặc toàn bộ
  profile metadata. Canonical source và cả ba ZIP không đổi; không push/publish.

### Sau xác nhận “đã xong” của người dùng

- Claude Code re-auth thành công. Lượt explicit đầu đọc VERSION 0.1.0 và các
  reference/pack qua Read. Lệnh ghép `cd`/pipe bị permission mode chặn; phản hồi
  đã nêu đúng calculator NOT_RUN ở lượt đó. Không dùng phép tính tay làm bằng chứng.
- Lượt mới cho phép đúng một lệnh calculator độc lập, không cd/pipe/redirect:
  Bash tool thực sự trả JSON baseline profit 30000, scenario 21500, delta -8500;
  exit thành công, không permission denial. Đây là PASS native calculator.
- Lượt implicit không đưa tên skill vào prompt: Claude tự gọi đúng ERM qua Skill,
  đọc bốn reference/pack FMCG và trả breach, UNKNOWN, SOP chưa chứng minh OE,
  dedup economic_loss_id L1. PASS cho một ca trigger/hành vi fresh-context; không
  suy thành độ chính xác routing trên mọi prompt hoặc 120 ca native.
- ChatGPT upload cùng ZIP bàn giao thành công, không rebuild; UI hiển thị đủ
  references, sáu pack, scripts, license và VERSION. Có thêm `assets/icon.svg`
  trên UI import. Hash runtime xác nhận 28/29 file khớp, không file thiếu; chỉ
  agents/openai.yaml bị service đổi. JSON calculator trả về khớp toàn bộ stdout
  Claude (parameters/context/formula reference và các Decimal strings).
- ChatGPT Web Work chạy explicit smoke trong phiên mới: pass-through khớp Claude;
  `evaluate_metric`/`headroom`/`portfolio_status` giữ breach và incomplete/UNKNOWN;
  T&M savings chưa là realized benefit, copula/EVT chưa verified là NOT_RUN.
  Tool activity được UI hiển thị; không tuyên bố có raw process trace từ Web.

### G9-UI01 — phát hiện trên 0.1.0, xử lý trên 0.1.2

- Quan sát trực tiếp YAML trong Skills detail: icon_small/icon_large đổi từ
  `./assets/logo.png` sang `assets/icon.svg`; service bỏ quote/wrap lại YAML và
  bổ sung `policy.products: [chatgpt, codex, api, atlas]`. Đây không phải bằng
  chứng đã thử các product đó. `allow_implicit_invocation: true` còn nguyên.
- Screenshot UI cho thấy SVG là icon biểu đồ cột mặc định, không phải logo nguồn.
  **Branding UI FAIL**; logo.png trong payload vẫn khớp SHA-256. Không sửa/cài
  bản khác hoặc lưu editor Web ở lượt kiểm tra này.
- 28 file giữ nguyên gồm SKILL.md, reference, sáu pack, scripts, license, VERSION
  và logo nguồn. Phần nghiệp vụ/core native smoke PASS_WITH_LIMITS không bị
  gộp với kiểm tra branding. Chưa chạy lại 120 ca trên từng nền tảng.
- Người dùng sau đó yêu cầu xử lý lỗi và kiểm tra lại. Từ logo master 1100×1100,
  sinh kỹ thuật hai PNG 128×128/512×512 bằng `sips`; SHA-256 lần lượt là
  `58695db...ee12` và `be8ef617...c220`, trùng byte với các biến thể TDTN đang
  hoạt động trên một skill ChatGPT khác. Skill kia chỉ được đọc, không bị sửa.
- Metadata canonical trỏ small/large vào hai PNG. Bản 0.1.1 replace thành công:
  card Installed và Created by me đều hiện đúng khi xem trực quan. Native
  regression đọc VERSION 0.1.1; 30/31 file manifest khớp, không file thiếu;
  chỉ `agents/openai.yaml` khác do service chuẩn hóa; không có extra không giải thích.
- Sửa tiếp wording hỗ trợ native đã cũ trong USAGE, đóng gói 0.1.2 và replace
  lần cuối. Logo 0.1.2 đã xem lại trực tiếp và vẫn đúng. Không đổi nghiệp vụ,
  calculator, schema hoặc sáu pack; 27 tests cũ chạy lại PASS trước build.
- Các phần nghiệm thu còn lại: Claude Web (chưa được phép cài), ChatGPT Desktop
  (CUA access blocked), HTML interaction/visual, handoff chuyên môn thật và
  native Office export. Không ghi PASS cho các mục này.
- Release 0.1.2 có 31 canonical files và 32 entries/ZIP; hygiene/YAML/internal
  manifest/checksum PASS. 0.1.0/0.1.1 được giữ theo version policy. Không
  commit/push/phát hành công khai hoặc cài thêm nền tảng.

## 13. Rà soát điều kiện v1.0.0 — đối tượng 0.1.2, ngày 2026-09-04

**Kết luận: chưa đủ điều kiện hoàn tất.** Đây là audit, chưa sửa canonical hoặc
đổi version. Bằng chứng/reproduction tại `qa/RESULTS.json` → `release_readiness_audit`.
Ba ZIP được dựng lại trong temp và khớp byte hoàn toàn; temp đã dọn. 27 unit tests
chạy lại PASS; 120 response/review lịch sử đủ ID và khớp hash, không chạy lại hành vi.

### Đối chiếu yêu cầu với bằng chứng

| Yêu cầu | Kết quả và giới hạn |
| --- | --- |
| ERM-01–08 | Core/reference/schema bao phủ context, taxonomy/CEI, assessment/appetite/control/KRI; 27 tests và domain evidence hỗ trợ trong phạm vi synthetic |
| ERM-09–11; CALC-01–02 | Phép tính minh bạch, scenario/aggregation và ranh giới validated model đã có; mô hình nâng cao không được coi là engine đã chạy |
| ERM-12–13 | Hướng dẫn treatment/reporting có; mapping target/no-action vào schema và bảo toàn caveat cần làm rõ khi sửa đầu ra |
| IND-01–07 | Sáu pack đúng ngành, gồm phân biệt backlog/pipeline và AI benefit trong IT; thích ứng ngành khác có hướng dẫn. Không suy thành sáu engagement doanh nghiệp thực đã kiểm thử |
| INT-01–06 | Discovery/contract/fallback có, helper G1 có bằng chứng; **R02 FAIL**, handoff round-trip chuyên môn thực chưa chạy |
| OUT-01–03 | Sample Office cũ đã render/review; **R01 FAIL** với input số dạng chuỗi hợp lệ. Không đồng nhất sample PASS với exporter hỗ trợ mọi input schema |
| OUT-04–07 | JSON/HTML sample tái tạo khớp; IDs/tổng chọn lọc đã đối soát. **R03 FAIL**; HTML USER_REPORTED_OK, agent interaction/visual NOT_RUN; chưa đủ bằng chứng narrative parity toàn bộ |
| BRAND-01–02; LEGAL-01–03 | Ngôn ngữ/brand đúng nguồn; LICENSE và master logo khớp byte nguồn chỉ định; đủ hồ sơ pháp lý. Logo card ChatGPT đã PASS, không suy mọi artifact đều có logo |
| PKG-01–03,06 | 31 nguồn/32 entries mỗi ZIP, root đúng, không `.agents/skills/`; CRC/hash/source equality và reproducibility PASS; **R04 FAIL** ở chính sách gate |
| PKG-04–05 | Claude Code smoke trên 0.1.0; ChatGPT Web regression trên 0.1.2. Diff 0.1.0→0.1.2 chỉ VERSION/USAGE/UI YAML và hai icon; không tuyên bố toàn bộ nền tảng đã được test |
| QA-01–08 | Có mapping, 120 responses/reviews, unit và artifact evidence; audit bổ sung tìm lỗi ngoài suite cũ. Các FAIL/NOT_RUN giữ riêng, chưa đạt cổng hoàn tất |

### Bốn lỗi chặn phải sửa và kiểm lại

| ID | Bằng chứng 0.1.2 | Điều kiện đóng |
| --- | --- | --- |
| R01 — Office numeric strings | Chuyển value/threshold của fixture sang chuỗi: `prepare()` VALID, nhưng exporter thực chạy exit 1 `Excel KRI formula reconciliation failed`, không sinh Office | Xử lý đúng số dạng chuỗi, số âm và precision; đối chiếu engine/Excel, không ép số lớn sang float im lặng |
| R02 — handoff acceptance | H1 có `result_status=validated`, `validation_status=FAIL`, capability verified và method được validator trả VALID; schema không yêu cầu validation evidence | Contract/validator phải từ chối trạng thái mâu thuẫn hoặc thiếu evidence; chạy cả accepted/rejected return, không suy business approval |
| R03 — appetite utilization | K1 tính `utilization=1` (100%) trong JSON nhưng HTML renderer chỉ hiện limit/headroom/action | Hiển thị utilization phù hợp; floor/zero/signed case ghi không áp dụng; đối soát dữ liệu và bằng chứng hiển thị |
| R04 — hygiene/release gate | Temp source 41 file nhỏ có links vẫn bị chặn vì >40; gate còn áp cứng 800 dòng/200 KiB cho HTML, thiếu kiểm ZIP/QA budget và hardcode state Testing | Khớp D04: count/lines là review, size là hard gate theo loại; kiểm ZIP/QA và cấu hình release state; không sửa ZIP đã bàn giao |

Hai điểm bổ sung phải được xử lý trong lượt sửa đầu ra: `data-model.md` nói
treatment có target/no-action nhưng schema chưa có mapping rõ (thêm `target` bị
từ chối); cần một cách lưu/truy nguyên được kiểm thử. Warning C1 thiếu OE evidence
có trong JSON/HTML nhưng không ở text DOCX/PPTX: cần đối soát caveat trọng yếu hoặc
nêu căn cứ lựa chọn nội dung, không dùng ID presence thay chứng minh narrative parity.
HTML dùng tên thương hiệu bằng chữ, không có thẻ ảnh; đây là quan sát thiết kế,
không phải tái phát lỗi logo card ChatGPT G9-UI01.

### Các giới hạn cần quyết định sau khi sửa lỗi

| Mục | Khuyến nghị cho nghiệm thu 1.0.0 |
| --- | --- |
| Claude Web | Chạy native smoke nếu giữ tuyên bố hỗ trợ đã kiểm chứng; cần quyền upload riêng. Có thể giữ “chưa kiểm chứng” nếu người dùng chấp nhận rõ giới hạn |
| ChatGPT Desktop | CUA bị chặn; nhận user-run evidence hoặc giữ NOT_RUN được người dùng chấp nhận, không dùng Codex thay bằng chứng |
| HTML visual/keyboard/responsive | Giữ USER_REPORTED_OK hiện có; khuyến nghị kết quả từng ca và ảnh/viewport cho template sau sửa R03. Xác nhận chung không đủ coi toàn bộ ca đã PASS |
| Office trên native platforms | Có thể công bố exporter phụ thuộc runtime, với local export/QA đã kiểm lại sau R01; native export vẫn NOT_RUN cho tới khi chạy |
| Specialist round-trip | Sửa R02 trước; nên chạy một handoff synthetic qua capability thật. Không yêu cầu kiểm thử mọi engine DSMV ngoài phạm vi ERM |
| skill-creator quick_validate | Lần audit thử lại bị thiếu PyYAML trước khi chạy checks; Ruby Psych đã PASS. Khuyến nghị chấp nhận kiểm tra tương đương cho gate cấu trúc, không cài dependency chỉ để đổi nhãn |

Chưa cần xin quyết định giới hạn ngay khi lỗi nội bộ còn mở. Sửa trong phạm vi
đã được phép, thêm regression cho lỗi thật, tạo candidate Testing kế tiếp nếu
canonical thay đổi, rồi trình một bảng ngoại lệ cụ thể trước 1.0.0. Không tự cài,
upload, push hoặc phát hành. D01–D06 giữ nguyên; đây không phải phê duyệt bỏ gate.

Hygiene audit: canonical 1.399.413 byte/31 file; không binary trùng, empty dir
hoặc orphan không giải thích. Consumer đã truy từ entrypoint/USAGE/import/UI/legal.
LICENSE 901 dòng giữ mẫu là ngoại lệ đã duyệt. Kế hoạch vượt mốc review 600 dòng
do giữ evidence lịch sử và audit hiện tại cùng một nơi; đã rà soát trách nhiệm,
không tách thêm tài liệu trạng thái song song và vẫn dưới mốc 800 dòng.

## 14. Sửa lỗi và bản thử 0.1.3 — 2026-09-04

Người dùng đã cho phép “sửa bốn lỗi đã xác minh và tạo bản thử 0.1.3”.
Giữ tên, phạm vi ERM/sáu ngành, D01–D06 và một nguồn chuẩn. Không cài/upload,
sửa skill khác, push hoặc phát hành. Audit 0.1.2 tại mục 13 là lịch sử, không
đổi FAIL cũ thành PASS; evidence lượt sửa tại `qa/RESULTS.json` → `remediation_0_1_3`.

| Lỗi | Sửa và kết quả kiểm lại |
| --- | --- |
| R01 | Chuẩn hóa đúng cột số Excel; decimal strings/số âm/exponent khớp engine. Từ chối rõ precision vượt 15 chữ số có nghĩa hoặc round-trip không an toàn; không làm tròn im lặng. Test Office runtime PASS |
| R02 | `validated` yêu cầu capability verified, method, validation PASS/PASS_WITH_LIMITS và evidence hiện hành. FAIL/NOT_RUN/thiếu evidence bị từ chối; accepted/rejected round-trip PASS |
| R03 | Renderer thêm utilization theo phần trăm và “Không áp dụng”; test upper/floor/zero/signed/two-sided/opt-out PASS; K1 JSON=1 (100%). Syntax/static đã kiểm; **đóng R03 trong phạm vi smoke với USER_REPORTED_PASS 0.1.3** cho K1/K2, tìm/lọc/reset và thu hẹp cửa sổ. Agent visual/interaction vẫn NOT_RUN; xác nhận 0.1.2 giữ riêng |
| R04 | Count/lines chỉ kích hoạt review; hard byte budget đúng D04 cho text/HTML/binary/QA/payload/ZIP. Có cấu hình Testing/Release, chặn Release cho 0.x; test 41 file, HTML 300/500 KiB, QA/ZIP, no-overwrite/reproducibility PASS |

Bổ sung mapping `no_action_case`, `target`, `target_assessment_ids`; validator
kiểm basis/risk/reference, cảnh báo khi thiếu, không tự tạo target rating. Cảnh
báo C1 và hai narrative no-action/target được đối soát nguyên văn trong cả ba
Office outputs; HTML kiểm payload và renderer, chưa coi là bằng chứng hiển thị.

Đã chạy **42 tests, 0 skip** sau thay đổi cuối. Bộ mẫu cùng snapshot
`8ea35412e7940ab5f83839d7febaab665d84806d4dea36239686bb7b7952d99d`:
Excel 16 sheets/zero formula errors, counts 3/2/1 và KRI khớp; Word 2 trang
đã xem cả hai (hash chuyển xuống footer để tránh trang mồ côi); PPT 8 slides
đã xem, overflow test PASS. Thay bộ mẫu/ảnh tổng hợp hiện có, không tạo thêm
bộ trạng thái hoặc lưu toàn bộ preview tạm. 120 domain cases là lịch sử.

Ba gói 0.1.3 giữ **Testing** và native `NOT_RUN_FOR_THIS_BUILD`, root trực tiếp,
31 canonical files/32 entries mỗi ZIP. Bản 0.1.0–0.1.2 giữ nguyên. Kế hoạch
vượt mốc review 600 dòng do cần giữ audit/khắc phục trong cùng nguồn trạng thái;
đã rà trách nhiệm và không tách tài liệu song song. LICENSE 901 dòng giữ mẫu.
Bản 1.0.0 vẫn chưa hoàn tất: còn quyết định giới hạn G9/handoff ở mục 13.

Đóng gói đã kiểm: ba ZIP 0.1.3 dựng lại trong temp khớp SHA-256; CRC, manifest
và từng byte nguồn khớp. ZIP 0.1.0–0.1.2 vẫn khớp manifest gốc. Canonical
1.409.898 byte/31 file; QA khoảng 4 MiB/11 file; source dự án 41 file.

Nghiệm thu người dùng bổ sung ngày 2026-09-04: trả lời **“pass”** sau checklist
bốn mục của dashboard 0.1.3: K1=100%, K2=“Không áp dụng”, tìm/lọc/reset hoạt
động và nội dung đọc được khi thu hẹp cửa sổ. Ghi **USER_REPORTED_PASS** cho
checklist, đóng R03 trong phạm vi này. Đây là xác nhận chung, không có ảnh,
viewport hoặc log riêng từng ca; không suy thành agent PASS, keyboard PASS hay
responsive coverage toàn diện. Không đổi canonical/version/ZIP và không cài/upload.

## 15. G9 lại trên 0.1.3 — Claude Code và Web hoàn tất có giới hạn

Người dùng cho phép chạy lại G9 đúng 0.1.3 trên Claude Code và ChatGPT Web;
bao gồm cập nhật bản cài/bản upload thử trong hai bề mặt này. Không mở rộng
sang nền tảng khác, sửa skill khác, push hoặc phát hành công khai.

Kết quả ngày 2026-09-04 (giữ nguyên ZIP/canonical):

| Phần | Kết quả và bằng chứng |
| --- | --- |
| Claude Code install/discovery | PASS: target cũ 0.1.0 không có sửa/extra, cập nhật đúng ZIP 0.1.3; 31 file khớp; CLI 2.1.183 liệt kê skill/slash command |
| Claude native execution | PASS_WITH_LIMITS sau khi dịch vụ phục hồi: explicit ERM trigger, core/report/R02, DEQ file-loaded workflow và Office đã chạy thật; chi tiết lượt tiếp tục bên dưới. Hai lượt 529 đầu giữ riêng trong QA |
| Web install/integrity/brand | PASS_WITH_PLATFORM_NORMALIZATION: VERSION 0.1.3, 30/31 khớp, không missing; YAML chuẩn hóa và icon.svg là khác biệt. SKILL/VERSION/manifest/exporter hash đối chiếu ZIP local khớp; logo Installed card xem trực tiếp đúng |
| Web core/report/R02 | PASS: profit 30000→21500, delta -8500; decimal-string snapshot VALID, warning C1 giữ nguyên; counts 3/2/1, breach/capacity_breach/UNKNOWN; K1 utilization=1, K2=null; no-action/target giữ. Ba invalid handoff exit 2, valid synthetic contract exit 0 |
| Web DEQ round-trip | PASS_WITH_LIMITS cho workflow phát hiện/từ chối: DEQ 1.1.1, profiler 1.2.0/reconciler 1.1.0 chạy thật; L1 lặp, raw 24000/unique 13000. Reconciler CONDITIONAL/exit 1 vì self-comparison và thiếu policy evidence; return FAIL, ERM raw aggregation rejected; CSV unit UNKNOWN. Không gọi đây là validation độc lập hay accepted production return |
| Web native Office | PASS_WITH_LIMITS: dependency có sẵn, exporter cùng hash; XLSX 16 sheet, Word 2 trang, PPT 8 slide render/xem bởi Web agent; counts/statuses khớp, zero formula errors, PPT overflow PASS. Chưa có reviewer độc lập |

Phiên bằng chứng: [Kiểm thử ERM Enterprise](https://chatgpt.com/c/6a99ca90-01c4-83ec-88fe-f5cab28dc70d).
Đã mở `output_manifest.json` và `office_runtime_qa.json` qua UI; giữ selected
hashes trong G9 JSON, không chép 72 file scratch/render của Web vào repository.
Core dùng `--output` nên stdout rỗng đúng CLI; kết quả lấy từ JSON output, không
nhầm là chưa chạy. Snapshot string-input khác hash fixture numeric local là có chủ ý.

Giới hạn Office được ghi thêm: sheet Treatments/Handoffs rộng cần cuộn ngang;
Web báo OOXML chưa chứng minh strict `standard_business_brief` preset (Normal
style/heading spacing). Render sạch không thay chứng nhận preset; không sửa
exporter hoặc skill khác trong G9. Giữ ghi chú để review định dạng trước bản hoàn thiện.
Native implicit selection 0.1.3 và 120 ca native chưa chạy. Bản 1.0.0 chưa được
hoàn tất; native Claude đã chạy lại thành công có giới hạn, còn cần chốt ngoại lệ nghiệm thu. Quyền chạy
lại G9 hai bề mặt vẫn có hiệu lực, không cần xin lại cho cùng phạm vi.
Metadata trong gói là trạng thái tại lúc build; evidence G9 mới ghi ở kế hoạch/QA,
không ghi đè ZIP đã bàn giao hoặc thay VERSION chỉ để phản ánh lượt kiểm thử.

Lượt tiếp tục theo chỉ dẫn mới “quyền hiện có đã đủ; 0.1.3 — Testing”:

| Phần native Claude Code | Bằng chứng thực chạy và giới hạn |
| --- | --- |
| Trigger/core/report | ERM có trong discovery và được gọi explicit; Sonnet 4.6 đọc VERSION, chạy core: 30000→21500, delta -8500. Snapshot decimal-string VALID; counts 3/2/1, breach/capacity_breach/UNKNOWN; K1 utilization=1, K2=null; warning C1 và treatment target/no-action giữ nguyên |
| R02 gate | Validator thực trả exit 2/2/2/0 cho FAIL, NOT_RUN, PASS thiếu evidence và PASS + SYN1 current. Ca cuối là chấp nhận contract synthetic, không xác nhận validation chuyên môn độc lập |
| DEQ capability/workflow | DEQ không đăng ký trong Claude; đọc trực tiếp skill 1.1.1 và chạy profiler 1.2.0/reconciler 1.1.0 hiện có. Profile 3 dòng/5 cột, 2 loss IDs, L1 lặp; raw 24000/core dedup 13000. Reconciler exit 2 do chặn self-reconciliation, không tạo return JSON. ERM chỉ nhận profile evidence, không nhận raw total là validated; CSV unit UNKNOWN, scope Group do harness synthetic cấp |
| Office | Exporter khớp byte nguồn cài; check/export exit 0; XLSX 16 sheets, 6 công thức, 0 ô lỗi; counts/statuses khớp report. DOCX 2 trang, PPT 8 slides; warning C1 và target/no-action khớp text cả hai. Native đọc ảnh 2 trang Word, đủ 8 slides và 4 sheets Summary/KRI/Treatments/Handoffs; 12 sheets khác chỉ render, chưa visual-review ở Claude |
| PPT overflow | Lượt đầu NOT_RUN do harness thiếu RUNTIME_NODE; bổ sung đường dẫn runtime có sẵn ở môi trường gọi, không sửa renderer/skill. Lượt native sau exit 0: “Test passed. No overflow detected.” |

Harness tạm do Codex chuẩn bị; **Claude Code thực thi** script đã cài và runtime
có sẵn. Đây là explicit scripted regression, không phải implicit selection hay
review nghiệp vụ độc lập. Một lượt rộng đã dừng vì Claude hiểu nhầm lệnh `ls`
bị từ chối thành toàn bộ Bash bị chặn; lượt đúng lệnh Python được cấp quyền chạy
thành công, không có permission denial. Không xin/cấp quyền mới hoặc lách chặn.
Cách diễn giải “0 formulas” của native report đầu đã được sửa bằng đếm OOXML:
6 công thức, 0 ô lỗi; không dùng lỗi diễn giải đó làm kết luận về exporter.

**Kết luận phạm vi này: PASS_WITH_LIMITS trên Claude Code và ChatGPT Web.**
Còn NOT_RUN: implicit selection/native 120 ca, DEQ registered invocation ở Claude,
independent reconciliation/accepted production return, reviewer độc lập và các
bề mặt chưa được phép. Word strict preset vẫn chưa chứng nhận; HTML giữ đúng
USER_REPORTED_PASS trước đó. Không tự chuyển các giới hạn này thành PASS.

Đã đối chiếu sau chạy: 31/31 file cài Claude không đổi; SHA-256 của cả 12 ZIP
đã bàn giao giữ nguyên. Evidence chọn lọc, command exits, artifact/trace hashes
lưu trong `qa/G9-NATIVE.json` → `regression_0_1_3.claude_code`; `qa/RESULTS.json`
trỏ cùng lượt. Không chép cây output/render tạm vào dự án; không tạo lịch tự chạy
vì dịch vụ đã phục hồi và lượt native được yêu cầu đã hoàn tất.

## 16. Nghiệm thu cuối 0.1.3 — 2026-09-04

Người dùng yêu cầu rà soát để xác định phần còn thiếu trước 1.0.0. Kết luận:
**NOT_READY_FOR_1.0.0**; giữ **0.1.3 — Testing**. Chỉ cập nhật kế hoạch và hai
file QA hiện có. Nguồn chuẩn, bản cài, VERSION và ZIP không đổi. Mapping yêu cầu
và ngoại lệ tại `qa/RESULTS.json` → `final_acceptance_0_1_3`; bằng chứng thực chạy,
câu trả lời cuối và trace hashes tại `qa/G9-NATIVE.json` → `acceptance_0_1_3`.

| Kiểm bổ sung | Kết quả và giới hạn |
| --- | --- |
| Claude Code tự chọn skill | Ba phiên mới: FMCG/IT tự gọi ERM; yêu cầu đảo chuỗi không gọi ERM. Selection PASS cho ba ca; nội dung FMCG/IT FAIL R05/R06. Sonnet 4.6 thực chạy, exit 0, không còn 529; không suy thành coverage toàn bộ ngành |
| ChatGPT Web tự chọn skill | Một ca FMCG PASS_WITH_LIMITS: tự chọn ERM, lợi nhuận 30000→21500; bridge +4500−9000−4000=−8500. Activity UI và câu trả lời hoàn tất ghi nhận chạy core; follow-up đọc VERSION 0.1.3/SKILL hash khớp local. Không có raw backend trace, không dùng PASS này xóa lỗi Claude |
| DEQ → ERM, chiều nhận hợp lệ | Helper DEQ hiện có thực đối soát hai CSV synthetic khác file: 2 loss IDs, tổng 13000 triệu VND, Group/Q4-2026/as-of đầy đủ; key/per-key/schema/hash PASS. Return và snapshot/report ERM được nhận; ca sai đơn vị bị từ chối. PASS_WITH_LIMITS là kiểm kỹ thuật local do Codex thực hiện, không phải lượt native mới, kiểm định độc lập hay phê duyệt dữ liệu production |
| Word preset | Đối chiếu nguồn/preset/OOXML xác nhận R07; render sạch trước đây vẫn có giá trị về khả năng đọc và dữ liệu, không chứng nhận đúng preset |
| Cấu trúc và toàn vẹn | Lệnh quick_validate dừng trước kiểm vì thiếu yaml: NOT_RUN. Ruby Psych + kiểm tương đương các quy tắc frontmatter/name/description/scaffold PASS; không cài dependency. 31/31 file canonical và bản cài Claude khớp manifest; 12 ZIP giữ nguyên hash |

Phiên Web: [Tính tác động lợi nhuận](https://chatgpt.com/c/6a99d6ed-f27c-83ec-8bae-b9765d96b2e9).
Không chạy lại 42 tests, 120 domain responses hoặc render Office khi nguồn không
đổi; giữ đúng phạm vi bằng chứng cũ. Native implicit trước đây NOT_RUN ở mục 15
nay đã được bổ sung các ca giới hạn trên, chưa bao phủ 120 ca native.

| Việc còn mở | Bằng chứng xác minh | Cách xử lý và điều kiện đóng |
| --- | --- | --- |
| **R05 — cao, chặn nghiệm thu** | Claude I01 cho tổng lợi nhuận đúng nhưng viết −4500 = 35×(−100), thực tế −3500; viết 4000 = 100×100−5×900, thực tế 5500. Không gọi calculator trong ca này | Buộc diễn giải định lượng dựa trên phép tính đã chạy, đối soát từng thành phần và tổng bridge. Kiểm lại câu trả lời native trong phiên mới, bao gồm bảng và căn cứ phép tính; đây là lỗi hành vi trả lời, chưa phải lỗi engine |
| **R06 — cao, chặn nghiệm thu** | I02 tự dùng top 3 khách hàng >50% backlog làm quy tắc trọng yếu dù người dùng cấm tự đặt ngưỡng; I01 gọi cú sốc forward là reverse stress khi chưa có điều kiện thất bại, và diễn giải tỷ lệ kịch bản như elasticity có căn cứ ngành | Giữ ngưỡng thiếu là chưa biết, phân biệt đề xuất minh họa; reverse stress phải bắt đầu từ điều kiện thất bại. Kiểm hồi quy thiếu appetite/horizon, ranh giới reverse stress và diễn giải kịch bản trong phiên native mới |
| **R07 — trung bình, cần xử lý trước bản hoàn thiện** | Exporter khai báo standard_business_brief nhưng Word thiếu Normal; body after 8pt thay 6pt; H1 hiệu lực before/after 18/6pt thay 16/8pt; H2 before 14pt thay 12pt | Khớp style/paragraph overrides với preset đã khai báo, render/xem mọi trang và đối soát nội dung. Baseline sản phẩm không bắt buộc tên preset này; nếu chọn thiết kế riêng thì cần quyết định rõ, không tự đổi nhãn để bỏ qua sai lệch |

Sau khi sửa và kiểm lại, cần chốt phạm vi nghiệm thu còn thiếu:

| Ngoại lệ | Khuyến nghị có căn cứ | Trạng thái |
| --- | --- | --- |
| E01 — bề mặt chưa thử | Giữ Claude Web/ChatGPT Desktop NOT_RUN và chỉ công bố phạm vi đã kiểm; nếu cần native coverage thêm thì xin đúng quyền còn thiếu. Không tự bỏ mục tiêu đa nền tảng | OPEN cho bản hoàn thiện |
| E02 — HTML/visual coverage | Giữ bốn mục smoke USER_REPORTED_PASS; agent keyboard/responsive và visual toàn diện chưa kiểm. Không hỏi lại xác nhận PASS đã có | OPEN về phạm vi nghiệm thu |
| E03 — độc lập/production | Chấp nhận bằng chứng tích hợp kỹ thuật synthetic với giới hạn rõ; không chứng nhận tính đúng của nguồn doanh nghiệp hay reviewer độc lập | DISCLOSE_SCOPE |
| E04 — quick_validate | Đề xuất nhận bộ kiểm cấu trúc tương đương đã chạy; lệnh gốc vẫn NOT_RUN vì thiếu PyYAML | OPEN cho bản hoàn thiện |

Các lỗi R05/R06 cần sửa, không đề xuất miễn trừ. R07 cần khớp preset hoặc quyết
định thiết kế rõ. Khi đủ điều kiện, cập nhật VERSION/USAGE/bảng hỗ trợ và metadata
cho gói tương lai; trạng thái trong ZIP 0.1.3 là tại lúc build, không ghi đè để
hợp thức hóa evidence mới. Lượt audit không nâng phiên bản hoặc phát hành.

Cổng vệ sinh sau audit: `tools/build_release.py --check` exit 0; canonical 31
file/1.409.898 byte, source dự án 41 file, QA 11 file/~4,04 MiB. Đã review kế
hoạch vượt mốc 600 dòng để giữ một nguồn trạng thái; không thêm tài liệu song song.

## 17. Sửa R05–R07 và hồi quy 0.1.4

Người dùng cho phép sửa ba điểm và kiểm thử trên bản thử kế tiếp. Đã tạo
**0.1.4 — Testing** từ nguồn chuẩn; giữ nguyên toàn bộ 12 ZIP cũ và bản cài Claude 0.1.3. Không cài/nâng skill khác, push hoặc phát hành.

| Điểm | Thay đổi và bằng chứng thực chạy | Kết luận |
| --- | --- | --- |
| R05 — lời giải định lượng | `pass_through` trả profit bridge với factors/formula/amount và reconciliation; kiểm units/từng tích/tổng, yêu cầu runtime hoặc UNCHECKED. Bốn ca bridge có expected độc lập đều đạt. Native I01 đã thực chạy core: 30000→21500, +4500−9000−4000=−8500 | Mã và ca I01 đạt trong phạm vi đó. **Chưa đóng hành vi:** I02 trên nguồn cuối vẫn ghi “đã kiểm” 80−20 mà chỉ gọi Read, không chạy calculator/không nhãn UNCHECKED |
| R06 — phương pháp/ngưỡng | Siết ngưỡng thiếu kể cả câu hỏi/Insight; reverse stress bắt đầu từ failure condition; ceteris paribus không suy elasticity=0. IT dùng input của nhiệm vụ và Δprofit theo revenue/cost tăng thêm, không tự dùng effort×wage. I02 cuối bỏ ngưỡng tự đặt, giữ horizon/appetite chưa biết, diễn giải AI đúng các điểm đang sửa | **Còn mở:** ca reverse stress trên nguồn cuối bị dừng do hạn mức. Các lượt trước cho ranh giới số đúng nhưng còn ngưỡng ví dụ/Insight không có căn cứ; không chuyển thành PASS toàn R06 |
| R07 — Word preset | Khai báo Normal mặc định; một định nghĩa mỗi heading; body after 6pt, H1 16/8pt, H2 12/6pt; bỏ override sai. Export thực exit 0; OOXML và nội dung IDs/C1/no-action/target khớp; xem riêng đủ 3 trang và render lại bản byte-identical cho ảnh pixel-identical | **Đóng lỗi đã xác minh.** Preset bundle cũ không còn ở môi trường; dùng tokens đã ghi trong audit, không tuyên bố chứng nhận toàn bộ thư viện preset cũ |

Hồi quy mã trên nguồn cuối: **45 tests, 0 skip, PASS** (42 ca cũ + bridge,
context object và Word). Lỗi CLI context sai kiểu trả InputError; help nêu rõ
JSON file và tên tham số. Exporter thực chạy khác nguồn cuối duy nhất comment;
không khác code. Word sample/contact sheet hiện tại thuộc 0.1.4; XLSX/PPTX/HTML
sample giữ 0.1.3, không gán nhầm version. Bằng chứng trong `qa/RESULTS.json` →
`remediation_0_1_4` và `qa/G9-NATIVE.json` → `regression_0_1_4`.

Native dùng bản sao tạm file-loaded, không phải implicit discovery hoặc bản ZIP
đã cài. Các lượt đọc nhầm global 0.1.3 bị loại; lượt sandbox không thấy login là
NOT_RUN, auth ở môi trường được phép đã xác minh. Một số lệnh bị Claude dontAsk
chặn; ca không tính được giữ NOT_RUN/UNCHECKED, không mở rộng quyền để lách chặn.
Lượt cuối reverse stress trả **session limit — resets 2:30pm (Asia/Saigon)**,
ngày 2026-09-04; I02 kết thúc và được review riêng. Giữ cả thất bại và giới hạn,
không lấy một ca PASS để xóa kết quả trái chiều. Không có reviewer độc lập mới.

**Chỉ dẫn mới nhất:** “kiểm vậy trên claude là đủ rồi, không cần tiếp tục kiểm
thêm”. Đã kết thúc lượt kiểm Claude theo yêu cầu; không chạy lại khi hạn mức
đặt lại, không lên lịch tự chạy. Quyết định dừng kiểm không đổi các ca FAIL hoặc
chưa hoàn tất thành PASS. R05 còn vấn đề xác nhận số học chưa chạy; R06 có
bằng chứng đạt từng phần và ca reverse stress cuối chưa hoàn tất.

Bản thử 0.1.4 đã đóng gói để bàn giao cùng giới hạn trên. Chưa có native ZIP
0.1.4 đã cài hoặc ChatGPT Web 0.1.4; không kế thừa PASS của 0.1.3. E01/E02/E04
ở mục 16 vẫn là phạm vi cần chốt trước 1.0.0; E03 giữ giới hạn synthetic,
không độc lập/production. Không tự nâng lên 1.0.0 từ việc người dùng dừng kiểm.

Cổng vệ sinh/đóng gói: 31 file canonical, 41 file source dự án, 11 file QA;
không thêm file trách nhiệm trùng, thư mục rỗng hoặc tài liệu trạng thái song song.
Ba ZIP folder-root có 32 entries/gói (31 nguồn + manifest), không `.agents/skills/`;
đối chiếu bytes/hash, CRC và rebuild trùng hash. Ngân sách byte trong giới hạn.
Kế hoạch vượt mốc review 800 dòng: giữ lịch sử quyết định/bằng chứng ở một nơi,
không tách thành status file. Chỉ giữ evidence chọn lọc, không giữ reasoning/raw
trace tạm; QA JSON lớn được review để không nhân bản toàn bộ tài nguyên đã đọc.

## 18. Chốt điều kiện còn thiếu trước 1.0.0 — dựa trên bằng chứng hiện có

Phạm vi lượt này: đối chiếu yêu cầu, source và QA đã lưu; không chạy thêm Claude,
không chạy lại bộ test hoặc sinh artifact mới. 31 file canonical khớp hash của
nguồn 0.1.4 đã ghi trong QA. Không thay VERSION, source, ZIP, baseline yêu cầu
hoặc bằng chứng native. Kết luận hiện tại vẫn **NOT_READY_FOR_1.0.0**.

### Hai điều kiện kỹ thuật còn thiếu

| Điểm / yêu cầu | Kết luận từ bằng chứng | Điều kiện để đóng, không yêu cầu thêm Claude |
| --- | --- | --- |
| **R05 — lỗi xác nhận mức kiểm chứng**; CALC-01, OUT-06, QA-04/06/08 | Engine/bridge đã có kết quả đạt; ca I02 cuối không chứng minh lỗi số học mới: 80−20=60 đúng, nhưng câu “đã kiểm” không có lượt thực thi tương ứng. `calculate()` trả input/context/output; hiện chưa có cổng đối soát trạng thái kiểm chứng của lời giải tự do | Cơ chế xuất kết quả phải gắn từng kết luận định lượng được xác nhận với input/đơn vị/kỳ và output thực chạy; thiếu, lệch hoặc không có execution evidence thì chưa kiểm, không tự xác nhận bằng một trường status. Kiểm cổng này ngoài Claude với bằng chứng hợp lệ và ca thiếu/sai evidence; đối soát từng thành phần bridge. Thêm lời nhắc đơn thuần hoặc sửa câu trả lời QA bằng tay không đủ đóng lỗi |
| **R06 — khoảng trống bằng chứng hành vi trên nguồn cuối**; ERM-01/05/09, IND-06, QA-02/04/08 | I02 cuối đạt các điểm ngưỡng/AI đang sửa. Lỗi reverse stress/elasticity/ngưỡng ví dụ nằm ở các lượt trước; lượt nguồn cuối bị session limit nên không thể kết luận FAIL mới hoặc PASS toàn R06 | Cần đánh giá tập trung ngoài Claude trên nguồn sẽ bàn giao: thiếu failure condition thì hỏi, không tự chèn ngưỡng; khi có điều kiện thì giải đúng ranh giới/equality và hai phía; không suy elasticity/benchmark từ scenario, không quy effort saving thành profit saving. Ghi rõ phương thức đánh giá; review source hay test số học không thay PASS hành vi end-to-end |

R05: hướng xử lý phù hợp là tận dụng calculator/report hiện có để sinh phần số
liệu và nhãn kiểm chứng có căn cứ, tránh thêm lớp skill hoặc một validator chỉ
so từ khóa “đã kiểm”. Skill dạng file không tự chặn mọi câu chữ của ứng dụng chủ;
biện pháp trong pipeline chỉ bảo vệ phần đi qua pipeline đó. Điều kiện nghiệm
thu là bằng chứng khắc phục ca lỗi trong phạm vi công bố, không phải cam kết mô
hình không bao giờ sai. Nếu kết quả ngoài Claude không đủ khép lỗi thì tiếp tục
Testing; không lấy việc dừng Claude làm miễn trừ. Lượt này chỉ chốt tiêu chí,
chưa triển khai cơ chế mới hoặc chạy đánh giá thay thế.

### Giới hạn đã có căn cứ trong baseline, không tạo thêm cổng phê duyệt

| Mục cũ | Cách xử lý cho hồ sơ nghiệm thu |
| --- | --- |
| **E01 — nền tảng** | PKG-04 giữ mục tiêu bốn bề mặt; PKG-05 và G9 yêu cầu chỉ công bố đúng khả năng đã kiểm. Giữ Claude Web/ChatGPT Desktop NOT_RUN; Universal chỉ có bằng chứng cấu trúc gói. Không coi thiếu bằng chứng là không tương thích, cũng không quảng bá hỗ trợ native đầy đủ. Đây là giới hạn phải công bố, không tự buộc cài/thử thêm ngoài quyền hoặc trái lệnh dừng Claude |
| **E02 — HTML/visual** | Giữ USER_REPORTED_PASS cho đúng bốn mục smoke dashboard 0.1.3; không hỏi lại. Keyboard và coverage responsive/visual rộng hơn chưa kiểm; không tự thêm yêu cầu phủ mọi thiết bị/viewport. Khi thay renderer có ảnh hưởng thì mới xác định hồi quy tương ứng |
| **E03 — độc lập/production** | Bằng chứng synthetic/handoff kỹ thuật đáp ứng đúng phạm vi đã chạy; không biến thành xác minh dữ liệu doanh nghiệp, reviewer độc lập hoặc production approval. QA-05 không bắt dự án này xây toàn bộ engine/chứng nhận của skill phụ |
| **E04 — validator gốc** | Chấp nhận Ruby Psych + kiểm tương đương frontmatter/name/description/scaffold làm bằng chứng cấu trúc theo QA-02. Lệnh quick_validate gốc vẫn NOT_RUN do thiếu PyYAML ở lượt đã ghi; không đổi thành PASS, không cài dependency. Không có yêu cầu sản phẩm buộc chỉ một chương trình validator mới được chứng minh cấu trúc |

Bảng công bố phải tách phiên bản và loại bằng chứng:

- Claude Code: native 0.1.3 có giới hạn; 0.1.4 chỉ file-loaded candidate, còn R05
  và thiếu xác minh R06. Không có bằng chứng bản ZIP 0.1.4 đã cài.
- ChatGPT Web: native 0.1.3 có giới hạn; bản 0.1.4 chưa upload/native-test.
- Claude Web/ChatGPT Desktop: NOT_RUN. Universal: folder-root, không lớp
  `.agents/skills/`; cấu trúc di động không chứng minh native support.
- 45 tests/Word ba trang thuộc 0.1.4; 120 domain responses và mẫu XLSX/PPTX/HTML
  là lịch sử theo QA, không nhận diện chúng là lượt kiểm mới trên 1.0.0.

### Sau khi hai điều kiện kỹ thuật được giải quyết

Đối chiếu requirement–evidence theo phạm vi thay đổi; chỉ hồi quy phần chịu ảnh
hưởng ngoài Claude, không mặc định chạy lại toàn bộ 120 ca. Khi không còn lỗi
chặn mới cập nhật VERSION/USAGE/bảng hỗ trợ và metadata cho **1.0.0**, rồi chạy
cổng vệ sinh, build ba gói, kiểm source/manifest/hash/reproducibility trên đúng
nguồn cuối. Không ghi đè 0.1.4, không tự cài/push/phát hành bên ngoài.

Không có câu hỏi quyết định mới cần người dùng trả lời trong lượt này: D01–D06,
PASS dashboard và lệnh dừng Claude đã rõ; các giới hạn trên áp dụng trực tiếp
PKG-05, QA-04/05/08 và G9, không sửa phạm vi sản phẩm. **Việc nên làm kế tiếp là
xử lý R05 ở đường sinh kết quả có kiểm chứng**, sau đó đánh giá tập trung R05/R06
ngoài Claude. Bằng chứng gốc vẫn ở hai JSON QA hiện có; mục này là nơi chuẩn cho
điều kiện đóng, không tạo tài liệu trạng thái mới.

## 19. R05 — cơ chế sinh kết quả có kiểm chứng, nguồn 0.1.5

Người dùng yêu cầu xử lý R05 ở cơ chế sinh kết quả. Đã sửa trong calculator hiện
có; không thêm file/module/skill, không chạy thêm Claude. Nguồn mang VERSION
**0.1.5 — Testing** để phân biệt với gói 0.1.4 bất biến; chưa build/cài/upload.

- `--checked`: luôn thực thi từ snapshot input mới, rồi sinh calculation,
  verification và text cố định. Nhãn EXECUTED chỉ mô tả phép tính trong khối đó.
- `--compare`: đối soát toàn bộ kết quả calculator gốc với lần chạy mới, gồm
  parameters, context, source_refs và output. PASS tự khai, null, thiếu file,
  sai kết quả/đơn vị/kỳ hoặc envelope thay raw result đều không được nhận.
  Không truyền comparison thì ghi NOT_REQUESTED, không tự nhận đã đối soát.
- `--text`: lấy lời giải engine sinh cho chat. Thành phần profit bridge được
  kiểm tích/tổng/delta trước khi xuất; lỗi trả exit 2/UNCHECKED, không tạo output
  được xác nhận. Lệnh JSON cũ giữ nguyên và vẫn không ghi đè file.
- Operation `arithmetic` xử lý phép tính hẹp hai toán hạng (+, −, ×, ÷), như
  backlog 80−20 và weighted pipeline 120×0,4, không cần ép thành engagement.
- Input/calculation/engine hash và VERSION gắn với kết quả; đây là dấu vết nội
  dung, không phải chữ ký hoặc chứng minh một lần chạy lịch sử. Nguồn, đơn vị,
  giả định và phê duyệt kinh doanh vẫn phải được đánh giá riêng.

**Kết quả thực chạy ngoài Claude:** 43 tests core/report PASS, 0 skip (36 ca cũ
+ 7 ca kiểm cơ chế mới). Sáu ca CLI: backlog=60, weighted pipeline=48 và bridge
+4500−9000−4000=−8500/profit=21500; raw result khớp trả MATCH; thành phần bridge
sai và chỉ có status PASS đều bị từ chối exit 2, stdout rỗng. Tests còn bao phủ
lỗi runtime, context thiếu/sai, comparison null, chia 0, nhãn tự khai, giữ input
snapshot và không ghi đè. Lượt collector ban đầu dừng vì so chuỗi khác scale
Decimal; đã sửa kỳ vọng số của collector, không coi đó là lỗi calculator hoặc
đổi lượt dừng thành PASS. Evidence trong `qa/RESULTS.json` →
`r05_checked_generation_0_1_5`; không thêm file bằng chứng riêng.

**Kết luận R05: đã xử lý và kiểm chứng trong đường sinh calculator.** Không
khẳng định đã sửa hành vi mọi câu trả lời tự do: host có thể bỏ qua đường này
hoặc viết thêm lời giải; phần đó không thừa hưởng nhãn EXECUTED. Dấu vết/status
không được nhận từ người dùng để thay thế phép chạy mới. Lỗi Claude cũ giữ
nguyên trong G9 JSON, không kiểm lại theo lệnh dừng. R06 vẫn cần đánh giá tập
trung ngoài Claude trước khi nghiệm thu 1.0.0; không lấy PASS cơ chế R05 thay
PASS phương pháp/hành vi của R06.

Chỉ thay core, hướng dẫn dùng, VERSION, test và trạng thái/QA liên quan; không
sửa schema/Office/dashboard/ngành/skill khác hoặc hồ sơ pháp lý. Giữ 31 file
canonical; các ZIP đã bàn giao và mẫu artifact cũ không đổi. Cổng vệ sinh được
kiểm trên nguồn đang phát triển, không tuyên bố đã có gói 0.1.5. Kế hoạch vẫn
là nguồn trạng thái duy nhất; phần vượt mốc dòng được giữ để nối bằng chứng và
quyết định, không tách nhật ký song song.

## 20. R06 — đánh giá tập trung ngoài Claude trên nguồn 0.1.5

**Kết luận: PASS_WITH_LIMITS, 4/4 ca đạt, 0 FAIL, 0 NOT_RUN.** R06 được đóng
trong phạm vi bốn ca hành vi xác định tại mục 18 trên nguồn **0.1.5 — Testing**.
Không thay nguồn skill, không chạy thêm Claude và chưa nâng lên 1.0.0.

Phương thức: bốn phiên ChatGPT Web Work mới, bộ chọn **GPT-5.6 Sol Extra High**,
nạp cùng ZIP nguồn 0.1.5 qua tệp đính kèm. Hai ca đầu upload từ máy, hai ca sau
chọn lại chính tệp đầu từ Library. Không cài hoặc thay native skill 0.1.3.
Prompt chỉ chứa nhận diện nguồn và bài toán; không cung cấp rubric/đáp án, không
nhờ phiên thử tự chấm. Đánh giá do agent triển khai đọc câu trả lời đầu tiên,
không tuyên bố reviewer độc lập hoặc kiểm đủ mọi hành vi/nền tảng.

| Ca | Kết quả quan sát | Kết luận |
| --- | --- | --- |
| IT thiếu horizon/ngưỡng, AI effort–profit | Giữ horizon/materiality/appetite chưa xác định; không tự thêm ngưỡng trong kết luận hoặc câu hỏi. Backlog 60 và weighted pipeline 48 không bị coi là doanh thu bảo đảm. Phân biệt effort, capacity, doanh thu thực hiện, chi phí tránh được và chi phí AI/review/rework | PASS |
| Reverse stress thiếu failure condition | Hỏi chỉ tiêu/ngưỡng/equality/thẩm quyền; baseline 30.000 và công thức Profit(d)=30.000−40.000d, d*=(30.000−L)/40.000 chỉ có điều kiện. Không tự chọn L hoặc nhận đã hoàn tất reverse stress | PASS |
| Reverse stress có failure condition | Q=750 cho profit=20.000 chưa thất bại; Q=749 cho 19.960 thất bại; Q=751 cho 20.040 chưa thất bại. Phân biệt mức giảm biên 25% với mức nguyên đầu tiên thất bại 25,1%; điều kiện bài tập không phải appetite; giữ giá không có nghĩa elasticity=0 | PASS |
| Scenario–elasticity | Profit 30.000→21.500; bridge +4.500−9.000−4.000=−8.500. Không suy quan hệ cầu–giá nhân quả/benchmark ngành từ giả định; nhận diện forward scenario, chưa reverse stress và chưa kết luận trong/ngoài appetite | PASS |

**Nhận diện nguồn và mức bằng chứng:** SHA-256 của 31 file canonical và ZIP
vận chuyển được kiểm tại máy trước/sau lượt đánh giá; nguồn không đổi. Cả bốn
câu trả lời ghi VERSION 0.1.5 và bốn hash khớp của SKILL.md, scenarios-portfolio,
it-outsourcing và erm_core.py. UI có dấu vết đọc tài nguyên và chạy lệnh. Ba
phiên hiển thị patched/edited files được hỏi bổ sung chỉ về kỹ thuật: đều báo
chỉ tạo JSON đầu vào ngoài bundle, 31/31 file nguồn khớp manifest sau thực thi,
0 thiếu/lệch; bốn hash tính lại vẫn khớp. Không gửi gợi ý sửa đáp án nghiệp vụ.
UI chỉ cung cấp tóm tắt hoạt động công cụ và phản hồi, không lưu được raw
stdout độc lập; ghi đúng giới hạn đó, không coi hash tự thân là chữ ký thực thi.

Ca ranh giới tự phát hiện nhãn đơn vị trung gian chưa đúng, chạy lại riêng phần
đó và nói rõ không dùng lượt trước làm kết luận; câu trả lời cuối đạt tiêu chí.
R05 vẫn chỉ đóng ở đường sinh calculator đã kiểm tại mục 19, không mở rộng thành
cam kết mọi lời văn host được bảo vệ. Đây là dữ liệu synthetic và kiểm hành vi
nạp từ file, không thay các giới hạn nền tảng/visual/production trong mục 18.

Prompt, rubric, trích đoạn phản hồi, liên kết đủ bốn phiên, hash và kết luận
nằm tại `qa/RESULTS.json` → `r06_focused_review_0_1_5`. Giữ evidence native cũ
trong `qa/G9-NATIVE.json` theo đúng phiên bản. Lần chuẩn bị trước bị khóa Mac,
chưa gửi prompt, đã được tiếp tục sau khi người dùng mở khóa; không còn blocker.
ZIP vận chuyển tạm được dọn sau khi dùng; không thêm file QA/trạng thái song
song hoặc `dist/0.1.5`, không sửa các bản bàn giao.

**Bước kế tiếp:** đối chiếu requirement–evidence cuối theo giới hạn đã chốt ở
mục 18, cập nhật VERSION/USAGE/metadata và bảng công bố khi chuyển sang 1.0.0,
rồi cổng vệ sinh/build/manifest/hash/reproducibility trên đúng nguồn cuối.
Không có quyết định mới cần hỏi trong phạm vi R06; không cần thêm Claude hoặc
chạy lại toàn bộ 120 ca khi chưa có thay đổi tạo rủi ro tương ứng.

## 21. Nghiệm thu nguồn 0.1.5 và bộ 1.0.0 cục bộ

**Kết luận: ACCEPTED_FOR_LOCAL_1_0_0_WITH_DISCLOSED_LIMITS.** Người dùng yêu
cầu đối chiếu nghiệm thu cuối nguồn 0.1.5 để chốt điều kiện lên 1.0.0; phạm vi
triển khai/hoàn thiện và đóng gói cục bộ đã được phép. Không có quyết định kinh
doanh mới cần hỏi; E01–E04 áp dụng theo mục 18, không tạo thêm vòng phê duyệt.

Đã đọc lại bộ định hướng, dùng skill-creator, kiểm Git và source/evidence. Nguồn
0.1.5 khớp 31/31 hash của cả R05 và R06. So 0.1.4 chỉ khác năm file đã được xử
lý tại R05; schema, validator, report/Office/HTML, logo và sáu pack không đổi.
120 case ID/response/cross-review và hash của ba batch vẫn khớp; đây là kiểm
tính toàn vẹn lịch sử, không phải chạy lại 120 ca. Năm sample artifact và toàn
bộ file của năm release Testing còn nguyên hash.

**Đối chiếu đủ 54 mã yêu cầu**, không thiếu hoặc lặp mã trong mapping tại
`qa/RESULTS.json` → `final_acceptance_0_1_5.requirements_mapping`:

- ERM-01–08: context, taxonomy, assessment, controls, appetite/KRI có source,
  schema và bằng chứng domain/semantic; R06 bổ sung xử lý thiếu ngưỡng đúng.
- ERM-09–11/CALC: giữ engine có kiểm chứng, simulation có điều kiện và ranh giới
  mô hình nâng cao; R05 chỉ bảo vệ khối calculator; R06 đạt bốn ca Web nguồn 0.1.5.
- ERM-12–13/OUT: treatment/target/warning được ánh xạ; giữ evidence Word 0.1.4,
  XLSX/PPTX và HTML 0.1.3 theo phạm vi. HTML keyboard/visual rộng hơn chưa kiểm.
- IND/INT: sáu pack và thích ứng ngành khác, capability-first/handoff gate còn
  nguyên; không công bố mọi DSMV engine, independent validation hoặc production.
- BRAND/LEGAL: giữ thương hiệu, ảnh gốc và điều khoản license; chỉ cập nhật dòng
  phiên bản sản phẩm, không đổi ngày áp dụng, quyền, owner hoặc phân phối.
- PKG/QA: một canonical, ba gói, evidence phân loại theo phiên bản; cơ chế native
  chưa kiểm trên 1.0.0 vẫn NOT_RUN. R01–R07 đóng đúng phạm vi tại JSON, không
  chuyển các lỗi native lịch sử thành PASS hay cam kết host không bao giờ sai.

### Phần thay đổi và kiểm trên bản cuối

Đổi đúng ba file: VERSION=1.0.0, USAGE (mức hỗ trợ/giới hạn hiện tại và cách dùng)
và dòng phiên bản trong LICENSE-APPLICATION. 28/31 file khác giữ nguyên từng
byte; không sửa code, schema, phương pháp, ngành, assets hoặc skill bên ngoài.
USAGE gom hướng dẫn hiện tại, bỏ các mục diễn tiến bản thử đã hết vai trò;
không thêm README/changelog/tài liệu trạng thái mới.

- **12/12 tests PASS, 0 skip:** 7 checked-generation, 1 snapshot/report và 4
  release gates trên nguồn promotion. Không chạy Office/native/Claude mới.
- **CLI version PASS:** lệnh checked thực chạy trả skill_version=1.0.0 và
  backlog=60; không dùng version string tự khai thay thực thi.
- **Structure PASS_EQUIVALENT:** Ruby Psych cùng checks field/name/scaffold,
  implicit invocation và icon resource. Validator gốc giữ NOT_RUN lịch sử do
  thiếu PyYAML; không cài dependency hoặc gọi đó là PASS của validator gốc.
- **Hygiene PASS:** 31 canonical file, 1.426.573 byte; 41 project source file,
  11 QA file. Consumer được giải thích cho cả 31 file; không orphan không rõ
  lý do, binary/text trùng hoàn toàn, near-duplicate trên ngưỡng rà soát 0,8,
  broken link, cache/temp, đường dẫn cá nhân trong package hoặc thư mục rỗng.
  Logo lớn nhất 948.765 byte; LICENSE dài nhất 901 dòng giữ nguyên theo D05.
  KE-HOACH vượt mốc dòng nhưng giữ vai trò lịch sử quyết định/evidence duy nhất.
  JSON QA lớn được giữ vì chứa evidence thực chạy, vẫn dưới trần 200 KiB/file;
  không chia thêm file để lách ngân sách. Chi tiết inventory/consumer tại JSON.

### Gói bàn giao và giới hạn

`dist/1.0.0/` chứa ba ZIP, RELEASE-MANIFEST.json và SHA256SUMS. Mỗi ZIP có
31 file canonical và một PACKAGE-MANIFEST, folder-root, không `.agents/skills/`.
Đã đọc lại CRC/path/bytes/hash/version/state/target; build lần hai trong thư mục
tạm cho SHA-256 giống nhau ở cả ba gói. ZIP khoảng 1,24 MiB/gói, dưới trần 5 MiB.
Staging/rebuild tạm được dọn; các bản Testing và QA cũ giữ nguyên.

| Gói | Byte | SHA-256 |
| --- | ---: | --- |
| Claude | 1.299.613 | `e22fce9b24c2d5027deffe55b9f165bbc5b8e22ea3bfb1640139fb7e148481e7` |
| ChatGPT | 1.299.615 | `9e7e3112e145f670900e327be884f6d0add5209cd937a3b9a757904eb7dc059e` |
| Universal | 1.299.615 | `e9162644030a35283ddaaafdac10c412f14ffe59bf255c6a79f31df37cc16133` |

**Hoàn tất tại máy, chưa cài/push/phát hành bên ngoài.** RELEASE không phải
chứng nhận native: manifest ghi NOT_RUN_FOR_THIS_BUILD; Claude Web và ChatGPT
Desktop chưa kiểm, Universal chỉ được kiểm cấu trúc. R05 giới hạn đường sinh;
R06 file-loaded Web bốn ca, synthetic và author-reviewed; HTML chỉ smoke do
người dùng báo đạt. Bảng hỗ trợ này được đưa vào USAGE của cả ba gói.

Bước tiếp theo khi người dùng cần sử dụng là chọn nơi cài hoặc phân phối bộ
1.0.0 và cấp quyền riêng cho hành động đó; không tự đặt thêm kiểm Claude hay
mở rộng nghiệm thu. Không có phần triển khai/đóng gói cục bộ bắt buộc còn dở.

## 22. README cho người sử dụng repository

Theo yêu cầu người dùng, tạo `README.md` tại gốc: giới thiệu skill, lợi ích/vai
trò, hướng dẫn sử dụng với ba ví dụ và hướng dẫn cài đặt theo nền tảng. README
là điểm vào cho người đọc repository/GitHub; liên kết đến USAGE và Kế hoạch,
không làm nguồn trạng thái thứ hai hoặc chép toàn bộ acceptance matrix.

Cách cài Claude Code/Claude Web đối chiếu tài liệu Anthropic; phần ChatGPT
đối chiếu OpenAI Docs và evidence UI đã có. Menu upload Web được ghi theo tài
khoản thử, không suy mọi tài khoản đều có. ChatGPT Desktop và cài ERM trên
Claude Web vẫn chưa kiểm chứng; nạp ZIP vào chat được phân biệt với cài native.
Không thực hiện cài đặt hoặc chạy thêm Claude trong lượt viết tài liệu này.

Đã kiểm liên kết cục bộ của README, các tệp tải và cấu trúc Markdown; không có
liên kết cục bộ thiếu. 31/31 canonical file và ba ZIP 1.0.0 giữ nguyên hash.
Chỉ thêm README và cập nhật mục này; source dự án tăng từ 41 lên 42 file,
trong mốc rà soát D04. Không rebuild gói, sửa QA lịch sử, commit hoặc push.
README không nằm trong payload skill, nên manifest/hygiene của gói bàn giao
vẫn mô tả đúng bản đã build. Việc cài/push/phân phối cần quyền riêng đã nêu.

## 23. Commit và push repository GitHub

Người dùng xác nhận URL đích sau đề nghị commit/push bộ 1.0.0:
https://github.com/thiendeptrainhat/Thien-Skill-Enterprise-Risk-Management-Intelligence.
Phạm vi là lưu toàn bộ dự án đã hoàn thiện lên repository này, giữ nhánh `main`
và commit baseline `d2741d4`; không thay quyền truy cập, tạo GitHub Release hoặc
cài bản 1.0.0 lên nền tảng.

Trước commit: GitHub API trả `PRIVATE`, `isEmpty=true`, `viewerPermission=ADMIN`;
`git ls-remote` không có ref. Dự án có 83 file ngoài `.git`, 27.917.463 byte,
gồm nguồn, tài liệu, QA và sáu thư mục phiên bản dist được giữ theo chính sách.
Không có file tên tạm/cache/key hoặc mẫu credential trong các file văn bản đã
quét; đây là kiểm tra mẫu hẹp trước commit, không phải kiểm toán bảo mật.
31/31 hash canonical và 3/3 checksum ZIP 1.0.0 khớp evidence bàn giao;
`git diff --check` sạch. Không chạy thêm Claude, không rebuild hoặc đổi gói.

**Kết quả thực tế:** commit `04cf12e63bcd5aee1e6d05e48894fe31741df251`
(`feat: complete ERM Intelligence v1.0.0 with verified release packages`) đã
push thành công bằng `git push -u origin main`. `git ls-remote origin
refs/heads/main` trả đúng SHA trên; upstream là `origin/main`. Commit giữ
baseline, gồm 82 file thêm/sửa; CLAUDE.md đã nằm trong baseline nên không đổi.
Nguồn và các gói vẫn nguyên hash; không chạy lại kiểm thử hoặc thay evidence
lịch sử. Mục này được cập nhật bằng commit tài liệu tiếp nối để lưu xác nhận
push thực tế; hồ sơ QA/build trước đây giữ đúng trạng thái tại thời điểm tạo.

**Tag theo yêu cầu tiếp theo của người dùng:** đã tạo annotated tag `v1.0.0`
tại commit bàn giao `d3199e51a6fbe4a55bc157738eb9460dde05058f` và push bằng
`git push origin refs/tags/v1.0.0`. Tag object là
`7aff67566fbd2f10b13ef19b0af99db6f3dc13d2`; `git ls-remote` xác nhận cả tag
object và peeled commit trên GitHub khớp cục bộ. Tag chưa tồn tại trước thao
tác; không thay/force tag, không tạo GitHub Release. Commit tài liệu ghi nhận
này tiếp nối trên `main`; tag giữ nguyên commit bàn giao, source/ZIP không đổi.

## 24. Hiển thị logo và giấy phép trên GitHub

Người dùng báo thiếu logo và tab license. Đã xác nhận trực tiếp trên trang
repository: README chưa có ảnh logo; chỉ có tab README, LICENSE nằm sâu trong
canonical nên chưa hiện ở phần điều hướng giấy phép cấp repository.

Sửa README để nhúng trực tiếp logo nguồn sẵn có, rộng 160 px, có alt text;
thêm LICENSE.md ở gốc làm điểm truy cập đến LICENSE và LICENSE-APPLICATION
chuẩn. Không sao chép toàn văn, không đổi điều khoản/phạm vi pháp lý và không
thêm asset. File mới có consumer là GitHub repository navigation và README;
không thuộc payload skill. Tag v1.0.0 và các ZIP giữ nguyên. Đây là sửa trình
bày repository trên main, không thay code hoặc mở lại kiểm thử Claude.

Tài liệu GitHub về licensing đặt file license ở gốc; nhận diện tên giấy phép
dựa vào bộ mẫu có sẵn nên không giả định tên giấy phép tùy chỉnh sẽ hiện đúng.
Nguồn: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository.
**Kết quả sau push commit `937b5a0`:** mở trang GitHub mới trên Chrome;
ảnh chụp giao diện xác nhận logo TDTN hiển thị đúng trong README và tab License
nằm cạnh README. Bấm tab License mở `?tab=License-1-ov-file`, hiển thị tiêu đề
Tran Ngoc Thien's Skill — License, nội dung song ngữ và liên kết toàn văn/tuyên
bố áp dụng. Sidebar Resources cũng có License. Kiểm liên kết cục bộ của hai
file đều đạt; `git diff v1.0.0 -- skill dist` rỗng. Không nhận đây là GitHub
chứng nhận hay phân loại giấy phép nguồn mở. Không thêm file QA/screenshot;
bằng chứng quan sát được ghi ngay tại mục này.

**Điều chỉnh theo yêu cầu trực tiếp tiếp theo:** người dùng yêu cầu toàn văn
ngay trong tab License, không dùng trang dẫn nguồn. LICENSE.md ở gốc được
thay bằng toàn bộ 901 dòng / 51.373 byte của LICENSE chuẩn, giữ nguyên từng
byte tiếng Việt và tiếng Anh. Bản ở gốc là bản sao phục vụ hiển thị GitHub
được người dùng yêu cầu; consumer là tab License. LICENSE trong canonical
vẫn là nguồn chuẩn duy nhất để sửa điều khoản và đóng gói; khi giấy phép thay
đổi, phải đồng bộ bản hiển thị và đối chiếu byte/hash trước push. Đây là ngoại
lệ nhân bản có mục đích theo chỉ dẫn mới, không duy trì hai bản soạn độc lập.
Đã đối chiếu byte/hash khớp; source, ZIP và tag v1.0.0 giữ nguyên.
Sau push commit `1271c4c`, mở trực tiếp tab License trên GitHub và xác nhận
giao diện chứa toàn văn cả Phần I tiếng Việt và Part II tiếng Anh, đủ mục
1–18 mỗi phần và liên hệ cuối văn bản; không còn trang dẫn nguồn trước đây.
SHA-256 của bản hiển thị và LICENSE chuẩn cùng là
`ced33214d371fabe382d3ca303042af7219ad96fb98acdd1b858d0d89478d4b5`.
