# Nguyên tắc thực hiện và bảo trì

Cập nhật: 2026-09-03. Tài liệu chuẩn về cách ra quyết định và các bất biến của dự án.
Yêu cầu sản phẩm: [Yêu cầu](YEU-CAU.md). Trạng thái: [Kế hoạch](KE-HOACH.md).

## 1. Phạm vi, quyền quyết định và sự thật

- Yêu cầu trực tiếp của người dùng được ưu tiên; tài liệu đính kèm chỉ tham khảo.
- Chỉ làm phần việc được phép. Không suy phê duyệt lưu tài liệu thành phê duyệt
  triển khai, cài đặt, xuất bản hoặc sửa các skill khác.
- Không tự giả định dữ kiện quan trọng. Ghi `Unknown`/`Not Provided` và hỏi khi
  thông tin đó ảnh hưởng phương pháp hoặc quyết định.
- Phân biệt fact, estimate, model output, scenario assumption và recommendation.
- Giả định/kịch bản đề xuất phải được ghi rõ là đề xuất, không được biến thành
  thông tin có thật của doanh nghiệp. Synthetic data phải có nhãn.
- Người có thẩm quyền phê duyệt appetite, limits, risk acceptance và báo cáo
  chính thức. Dự thảo và khuyến nghị không tự có giá trị phê duyệt.
- Không gọi một tác vụ mô hình là kiểm định độc lập nếu việc tổ chức đánh giá
  hoặc bằng chứng không đáp ứng tính độc lập thực tế.

## 2. Phương pháp ERM

- Tách RiskTaxonomy khỏi RiskInstance/Risk Register. Metadata chung giữ gọn;
  trường chuyên biệt thuộc đúng loại đối tượng, không ép owner/rating lên mọi node.
- Dùng materiality để quyết định đi sâu đến nhà máy/site/sản phẩm/dự án; không
  gom mọi lỗi tác nghiệp nhỏ vào enterprise risk universe.
- Risk statement phải nối nguyên nhân, sự kiện và tác động đến mục tiêu.
- Impact/Likelihood 1–5 là ordinal. Ma trận là công cụ phân loại, không phải mô
  hình xác suất/tổn thất; không cộng hoặc lấy trung bình máy móc các điểm ordinal.
- Xác định horizon và điều kiện trước khi so sánh rating hoặc xác suất.
- Không lấy tỷ lệ hiệu quả control tùy ý để suy residual risk.
- Control được mô tả hoặc có SOP không tự chứng minh operating effectiveness;
  đánh giá dựa trên evidence và phạm vi kiểm tra.
- Xác lập appetite methodology trước appetite status: metric, đơn vị, chiều
  tốt/xấu, entity, horizon, threshold, tolerance và thứ tự ưu tiên trạng thái.
- Không tự tạo một bộ ngưỡng appetite dùng chung cho mọi doanh nghiệp.
- Scenario không phải forecast; không gán xác suất nếu chưa có căn cứ mô hình.
- Dự báo driver/exposure rồi ánh xạ rating; không ngoại suy điểm 1–5 như biến liên tục.
- Aggregation phải xử lý double-counting, exposure chung, intercompany khi liên
  quan, concentration, dependency, common-mode và cascade.
- Treatment phải so với no-action case, xét chi phí, lead time, khả thi, rủi ro
  thứ cấp, tính đảo ngược, năng lực thực thi và chiến lược.

## 3. Dữ liệu, mô hình và nguồn

- Lưu provenance, as-of, version, entity, đơn vị, tiền tệ và horizon có ý nghĩa.
- Kiểm tra data quality, reconciliation, leakage và tính phù hợp của dữ liệu
  trước khi dựa vào kết quả mô hình.
- Mức kiểm định tương xứng với mục đích sử dụng: baseline, calibration, backtest,
  interval coverage, sensitivity, temporal/segment/stress stability khi liên quan.
- Phân biệt uncertainty do dữ liệu, tham số, mô hình và kịch bản; không tạo độ
  chính xác giả bằng các con số nhiều chữ số nhưng thiếu căn cứ.
- Tái lập phép tính bằng cấu hình, input version và seed khi phù hợp; có model
  card/giới hạn sử dụng và monitoring cho mô hình cần quản lý theo thời gian.
- Kiểm tra capability thực tế của skill/công cụ trước handoff. Có mode hoặc
  tài liệu hướng dẫn không có nghĩa đã có engine được kiểm thử.
- Ưu tiên nguồn chính thức và sơ cấp. Kiểm tra hiệu lực, phiên bản, phạm vi áp
  dụng, tài liệu thay thế/thu hồi và ngày kiểm tra; không đóng cứng nguồn lỗi thời.
- Không biến benchmark thành ngưỡng bắt buộc hoặc research population thành
  xác suất của doanh nghiệp cụ thể nếu thiếu bước hiệu chỉnh hợp lệ.
- Không sao chép nguyên bộ tiêu chuẩn/manual/nghiên cứu vào dự án. Lưu tóm tắt
  có mục đích, metadata và liên kết nguồn cần thiết.

## 4. Tích hợp và đầu ra

- ERM giữ business semantics và kết luận; skill chuyên môn chịu phần việc được giao.
- Handoff có input/output contract và tiêu chí chấp nhận; nhận lại kết quả phải
  kiểm tra phù hợp câu hỏi ban đầu trước khi đưa vào báo cáo.
- Nếu skill phụ thiếu hoặc không khả dụng, tiếp tục phần ERM có thể thực hiện
  và nêu chính xác phần chưa xử lý, không bịa kết quả hoặc công bố năng lực chưa có.
- Logic, dữ liệu và trạng thái có một nguồn chuẩn; Office/dashboard chỉ là các
  biểu diễn được đối soát, không trở thành nhiều hệ số liệu độc lập.
- UI/UX Ultra hỗ trợ thiết kế; Creative Diagram hỗ trợ hình phù hợp năng lực;
  dùng renderer/artifact tool phù hợp cho đầu ra thực tế.
- Kiểm tra nội dung và hình thức; không mô tả ảnh nhúng là native editable object.
- Không tự nâng cấp skill khác, tạo plugin hoặc mở rộng nền tảng ngoài phạm vi
  đã được người dùng cho phép.

## 5. Điều kiện để tạo một file

Chỉ tạo file khi có trách nhiệm rõ và ít nhất một bên sử dụng cụ thể: được đọc
qua liên kết, import, build/packaging, yêu cầu pháp lý, tài sản đầu ra hoặc QA.
Không tạo placeholder, thư mục rỗng, bản mẫu hay tài liệu phụ chỉ để đủ cây thư mục.

- Một nội dung có một nơi chuẩn; dùng liên kết khi nơi khác cần tham chiếu.
- Không tạo một file cho từng thuật ngữ, risk, template nhỏ hoặc test case.
- Gom nội dung cùng trách nhiệm; chia khi nội dung có mục đích, vòng đời hoặc
  cách sử dụng khác nhau. Không chia máy móc chỉ vì số dòng.
- `SKILL.md` giữ mục tiêu, tuyến xử lý, điều kiện chọn và bất biến thiết yếu.
  Chi tiết có điều kiện được tải từ supporting resources theo nhu cầu.
- Không duy trì toàn bộ bản sao theo Claude/ChatGPT/Universal. Khác biệt nền tảng
  chỉ nằm ở metadata, adapter hoặc quy tắc build thật sự cần thiết.
- Dùng tên file ổn định, đường dẫn tương đối trong nguồn di động, schema/template
  có mục đích rõ. Không nhúng đường dẫn máy cá nhân vào gói phát hành.

## 6. Kích thước, vòng đời và tài sản

- Ngân sách đã chốt tại D04 trong Kế hoạch: số file linh hoạt khi mở rộng;
  dùng mốc đếm/số dòng để rà soát, giữ trần dung lượng và trách nhiệm từng file.
- Phân biệt mức cảnh báo và mức chặn. Ngoại lệ phải có lý do, người chịu trách
  nhiệm, consumer và thời điểm xem xét lại; không bỏ qua giới hạn một cách ngầm định.
- Tách source, staging/build, file tạm và dist. Build output phải có thể tái tạo.
- Chỉ đưa artifact đã kiểm tra vào dist. Không đóng gói source tạm hoặc toàn bộ
  môi trường chạy, dependency cache, log, screenshot thử và intermediate render.
- Giữ fixture tái sử dụng, bằng chứng QA chính thức, manifest/checksum cần thiết.
  Chính sách giữ/xóa release cũ phải được chốt; không tự xóa lịch sử của người dùng.
- Giữ một ảnh logo nguồn chuẩn. Biến thể chỉ tồn tại khi có consumer/yêu cầu nền
  tảng thật; ghi nhận nguồn gốc và tránh binary trùng nhau.
- Không thêm thư viện/runtime nặng khi bài toán có thể xử lý bằng cơ chế đã có.
  Mọi dependency mới phải có lý do và cách kiểm chứng trên nền tảng đích.

## 7. Cổng vệ sinh và nghiệm thu

Trước khi đóng gói phải kiểm tra:

1. Orphan: file không có consumer hợp lệ hoặc không được manifest giải thích.
2. Broken links/imports và resource bị thiếu.
3. Duplicate/near-duplicate nội dung, binary giống nhau và bản sao theo nền tảng.
4. File quá lớn, quá dài hoặc số file vượt ngân sách.
5. Cache, temp, backup, scratch, intermediate và thư mục rỗng không cần thiết.
6. Đường dẫn cá nhân, source/package mismatch và manifest/checksum mismatch.
7. Tính tái lập của quá trình build.

Báo cáo vệ sinh cuối cùng nêu số file theo loại, file lớn/dài nhất, orphan,
duplicate, source/generated, ngoại lệ và sai lệch gói. Kiểm tra chưa chạy phải
ghi NOT_RUN; không tạo PASS chỉ từ việc file có tồn tại.

## 8. Cập nhật mà không đi chệch hướng

- Cập nhật đúng tài liệu chuẩn theo [CLAUDE.md](../CLAUDE.md), không tạo nhiều bản
  kế hoạch song song hoặc file nhật ký mỗi phiên.
- Ghi trạng thái ngắn, bằng chứng hoàn thành và quyết định còn mở vào Kế hoạch.
- Nếu yêu cầu mới mâu thuẫn baseline, chỉ sửa phần được người dùng quyết định;
  nêu tác động đến phạm vi, phụ thuộc, QA và bảo trì trước thay đổi liên quan.
- Không coi bản phác thảo, benchmark hoặc đề xuất của agent là quyết định đã duyệt.
