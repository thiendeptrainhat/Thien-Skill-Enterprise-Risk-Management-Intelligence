# Thiện's Skill — Enterprise Risk Management Intelligence

<p>
  <img src="skill/thien-skill-enterprise-risk-management-intelligence/assets/logo.png" alt="Logo TDTN — Thiện's Skill" width="160">
</p>

[Giấy phép / License](LICENSE.md)

Skill hỗ trợ **quản trị rủi ro doanh nghiệp (Enterprise Risk Management — ERM)**,
từ hiểu bối cảnh kinh doanh, nhận diện và đánh giá rủi ro đến lựa chọn ứng phó,
theo dõi và báo cáo cho ban điều hành/HĐQT.

Skill giúp trả lời: **mục tiêu nào bị ảnh
hưởng, rủi ro xảy ra qua cơ chế nào, bằng chứng đến đâu và cần quyết định gì?**

Chuyên sâu **FMCG, nông nghiệp, chăn nuôi, logistics, retail và IT/gia công phần
mềm**; có thể thích ứng với ngành khác theo mô hình kinh doanh và nguồn phù hợp.
Phạm vi từ tập đoàn, pháp nhân, đơn vị kinh doanh đến site hoặc dự án trọng yếu,
đa quốc gia. Mặc định trả lời bằng tiếng Việt, theo ngôn ngữ người dùng khi cần.

## Lợi ích và vai trò

| Nhu cầu | Skill hỗ trợ |
| --- | --- |
| Xây dựng hồ sơ rủi ro | Tách danh mục phân loại khỏi rủi ro cụ thể; nối nguyên nhân → sự kiện → tác động → mục tiêu, cùng owner và bằng chứng |
| Đánh giá và ưu tiên | Phân tích rủi ro trước kiểm soát, hiện tại và mục tiêu; thiết kế thang đánh giá theo bối cảnh và mức dữ liệu sẵn có |
| Quản lý khẩu vị rủi ro | Phân biệt sức chịu đựng, khẩu vị, mức dung sai và giới hạn; liên kết chỉ báo rủi ro (KRI), cảnh báo và hành động khi vượt ngưỡng |
| Hiểu tác động kinh doanh | Tính giá–lượng–chi phí–lợi nhuận, vốn lưu động, thanh khoản, mức tập trung; phân tích độ nhạy, kịch bản và stress trong năng lực thực tế |
| Lựa chọn ứng phó | So sánh phương án với trường hợp không hành động, xét chi phí/lợi ích, nguồn lực, thời gian và rủi ro còn lại |
| Báo cáo để ra quyết định | Tổng hợp risk profile, các điểm vượt ngưỡng, thông tin còn thiếu, phương án và quyết định cần xử lý; hỗ trợ Excel, Word, PowerPoint và HTML tương tác |

Skill phù hợp cho risk owner, bộ phận ERM, ban điều hành và HĐQT. Đầu ra Office
phụ thuộc công cụ/runtime của môi trường; dashboard HTML được thiết kế để mở
offline. Các định dạng dùng cùng dữ liệu báo cáo để đối soát.

**ERM giữ câu hỏi kinh doanh, logic rủi ro và kết luận điều hành.** Khi cần, skill
kiểm tra năng lực thực tế rồi chuyển phần việc chuyên sâu cho Data Engineering
& Quality, Data Science & Model Validation, Risk Control Process hoặc công cụ
thiết kế/tạo tài liệu. Skill không thay Master Orchestrator trong điều phối đa
lĩnh vực, cũng không thay kết luận kiểm toán độc lập, điều tra hoặc pháp lý.

Appetite, limits, chấp nhận rủi ro và báo cáo chính thức vẫn do người có thẩm
quyền phê duyệt. Thiếu dữ liệu được nêu rõ; kịch bản không tự trở thành dự báo,
và tiết kiệm effort không tự đồng nghĩa với tăng lợi nhuận.

## Hướng dẫn sử dụng

### Bắt đầu một yêu cầu

Sau khi cài, nêu tên skill và điều bạn cần giải quyết. Cung cấp những thông tin
đã có; skill sẽ hỏi phần thiếu ảnh hưởng đến kết luận:

- **Quyết định và đầu ra:** cần tư vấn việc gì, ai sử dụng, muốn trả lời trong
  chat hay cần báo cáo/file.
- **Bối cảnh:** ngành, mô hình kinh doanh, mục tiêu, phạm vi tổ chức và quốc gia.
- **Thời gian và đơn vị:** ngày chốt dữ liệu, kỳ đánh giá, tiền tệ và đơn vị đo.
- **Dữ liệu và phương pháp:** tài liệu nguồn, sự cố, kiểm soát, chỉ báo, ngưỡng
  hoặc phương pháp đã được duyệt; nêu rõ phần chưa có.

Câu hỏi hẹp có thể xử lý ngay trong chat, không cần lập bộ hồ sơ đầy đủ.

**Ví dụ — xây dựng risk profile:**

```text
Dùng Thiện's Skill — Enterprise Risk Management Intelligence để xây dựng
risk profile cho doanh nghiệp retail tại Việt Nam, phục vụ cuộc họp HĐQT.
Phạm vi: toàn doanh nghiệp; kỳ đánh giá: Q4/2026; đơn vị tiền: tỷ VND.
Tôi sẽ gửi kế hoạch kinh doanh, báo cáo vận hành và danh sách sự cố.
Chưa có appetite được phê duyệt. Hãy hỏi thông tin còn thiếu, nhận diện
rủi ro trọng yếu có căn cứ và đề xuất bước tiếp theo. Trước hết trả lời trong chat.
```

**Ví dụ — phân tích kịch bản:**

```text
Dùng skill ERM phân tích tác động giá nguyên liệu tăng đến lợi nhuận và
dòng tiền theo dữ liệu đính kèm. Làm rõ baseline, đơn vị và giả định trước
khi tính. So sánh các phương án chuyển chi phí vào giá bán; phân biệt
kịch bản giả định với dự báo. Chỉ rõ thông tin còn thiếu để làm reverse stress.
```

**Ví dụ — báo cáo và theo dõi:**

```text
Từ risk register và phương pháp đã duyệt đính kèm, dùng skill ERM lập
báo cáo điều hành và dashboard HTML offline. Giữ Risk ID, nêu KRI vượt
ngưỡng, dữ liệu chưa đủ, tiến độ ứng phó và quyết định cần phê duyệt.
Đối soát số liệu giữa báo cáo và dashboard trước khi bàn giao.
```

Với Claude Code, có thể gọi trực tiếp
`/thien-skill-enterprise-risk-management-intelligence` rồi viết yêu cầu.
Trên ChatGPT, chọn skill trong giao diện nếu có hoặc nêu rõ tên trong yêu cầu;
việc nêu tên không thay cho xác nhận skill đã được nạp.

### Dùng các công cụ đi kèm

Nếu cần chạy validator, calculator hoặc tạo báo cáo bằng lệnh, xem
[USAGE — cách dùng và runtime](skill/thien-skill-enterprise-risk-management-intelligence/USAGE.md).
Phép tính có kiểm chứng dùng engine thực chạy; phần diễn giải do nền tảng viết
thêm không tự thừa hưởng trạng thái kiểm chứng. Người dùng vẫn cần kiểm tra
nguồn dữ liệu và giả định trước khi sử dụng kết quả cho quyết định.

## Hướng dẫn cài đặt

### Chọn gói

Bộ **v1.0.0** gồm ba gói từ cùng một nguồn skill:

| Gói | Tệp tải về |
| --- | --- |
| Claude | [Tải ZIP Claude](dist/1.0.0/thien-skill-enterprise-risk-management-intelligence-1.0.0-claude.zip) |
| ChatGPT | [Tải ZIP ChatGPT](dist/1.0.0/thien-skill-enterprise-risk-management-intelligence-1.0.0-chatgpt.zip) |
| Universal | [Tải ZIP Universal](dist/1.0.0/thien-skill-enterprise-risk-management-intelligence-1.0.0-universal.zip) |

Đối chiếu tệp tải về với [SHA256SUMS](dist/1.0.0/SHA256SUMS) khi cần xác nhận
tính toàn vẹn. Mỗi ZIP chứa trực tiếp thư mục
`thien-skill-enterprise-risk-management-intelligence/`, trong đó có `SKILL.md`
và các tài nguyên. Giữ nguyên thư mục; không chỉ lấy riêng `SKILL.md`.
Universal không chứa lớp `.agents/skills/`.

**Phân biệt hướng dẫn cài với bằng chứng kiểm thử:** bộ v1.0.0 đã đóng gói và
kiểm tính toàn vẹn tại máy, chưa được cài/kiểm native trên các nền tảng đích.
Mức kiểm chứng từng phiên bản được công bố tại
[USAGE](skill/thien-skill-enterprise-risk-management-intelligence/USAGE.md).

### Claude Code

1. Tải và giải nén ZIP Claude.
2. Đặt **toàn bộ thư mục skill đã giải nén** vào một trong hai vị trí:
   - Cá nhân, dùng cho các dự án: `~/.claude/skills/`.
   - Chỉ một dự án: `.claude/skills/` bên trong dự án đó.
3. Kiểm tra cấu trúc đích, ví dụ:
   `~/.claude/skills/thien-skill-enterprise-risk-management-intelligence/SKILL.md`.
4. Mở phiên Claude Code mới và gọi lệnh skill ở phần sử dụng phía trên.
   Nếu đã có bản cũ cùng tên, lưu bản cũ ra ngoài thư mục được quét trước khi
   thay thế cả thư mục; tránh trộn file giữa hai phiên bản.

Đường dẫn và cách gọi dựa trên
[tài liệu Claude Code về skills](https://code.claude.com/docs/en/skills).

### ChatGPT Web

Quy trình dưới đây đã được quan sát và dùng cho bản thử trên tài khoản kiểm
thử của dự án. Chỉ áp dụng nếu tài khoản của bạn có các mục tương ứng:

1. Mở **Plugins → Skills → Create → Upload**.
2. Chọn ZIP ChatGPT; kiểm tra tên **Thiện's Skill — Enterprise Risk Management
   Intelligence** và hoàn tất thao tác thêm skill theo giao diện.
3. Mở cuộc trò chuyện mới, chọn/gọi skill và yêu cầu đọc `VERSION` của nguồn
   được nạp để xác nhận đang dùng bản mong muốn.

Nếu không thấy mục upload skill, chưa thể áp dụng quy trình này cho tài khoản
đó. Tài liệu công khai mô tả skills và cách phân phối qua plugin; dự án này
không có plugin wrapper. Xem [Build skills — OpenAI](https://learn.chatgpt.com/docs/build-skills).
Đính kèm ZIP vào một cuộc trò chuyện để đọc thử là **nạp nguồn cho phiên đó**,
không phải cài skill dùng lâu dài.

### Claude Web

1. Tải ZIP Claude, giữ nguyên cấu trúc thư mục bên trong.
2. Mở **Customize → Skills**, tìm tùy chọn thêm/tải skill và chọn ZIP.
3. Bật skill sau khi thêm, rồi mở cuộc trò chuyện mới để kiểm tra nhận diện
   tên, đọc phiên bản và xử lý một yêu cầu phù hợp.

Đây là hướng dẫn theo [tài liệu Anthropic](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills),
**chưa phải quy trình cài ERM đã kiểm chứng trên Claude Web**. Tên menu và quyền
sử dụng tùy giao diện/tài khoản; nếu thiếu tùy chọn, kiểm tra hướng dẫn của nền tảng.

### ChatGPT Desktop và gói Universal

ChatGPT Desktop là nền tảng đích nhưng dự án **chưa xác minh quy trình cài và
chạy ERM trực tiếp** trên ứng dụng này. Tham khảo mục Skills theo
[hướng dẫn OpenAI](https://learn.chatgpt.com/docs/build-skills); không dùng kết
quả trong Codex để suy rằng ChatGPT Desktop đã được kiểm thử.

Gói Universal cung cấp thư mục skill chuẩn cho môi trường hỗ trợ định dạng
này. Giải nén và dùng cơ chế import/copy được chính môi trường đó công bố;
không coi gói Universal là trình cài tự động cho mọi ứng dụng.

## Tài liệu và giấy phép

- [USAGE](skill/thien-skill-enterprise-risk-management-intelligence/USAGE.md):
  công cụ đi kèm, điều kiện runtime và giới hạn kiểm chứng.
- [SKILL.md](skill/thien-skill-enterprise-risk-management-intelligence/SKILL.md):
  điểm vào nghiệp vụ và các tài nguyên theo nhu cầu.
- [Kế hoạch](docs/KE-HOACH.md): nguồn chuẩn về tiến độ, quyết định và nghiệm thu.
- [LICENSE](skill/thien-skill-enterprise-risk-management-intelligence/LICENSE)
  và [tuyên bố áp dụng](skill/thien-skill-enterprise-risk-management-intelligence/LICENSE-APPLICATION.md):
  điều khoản **Tran Ngoc Thien's Skill**, dựa trên Commercial Source Available
  License 2.0; có mã nguồn không tự cấp quyền sử dụng hoặc phân phối không giới hạn.
