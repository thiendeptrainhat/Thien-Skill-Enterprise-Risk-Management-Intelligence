# Nông nghiệp

Intake: crop, geography/site, hectares planted/harvested, season, yield unit,
irrigation/water rights, soil, input regime, buyer/offtake, currency và insurance.
Không dùng calendar-year averages che exposure theo giai đoạn sinh trưởng.

| Driver / CEI | Dữ liệu và chỉ số | Logic kiểm tra / treatment |
| --- | --- | --- |
| Heat/drought/flood ở giai đoạn nhạy cảm → giảm yield/quality → shortfall giao hàng | Rain/temperature theo site và stage, soil moisture, irrigation uptime | Area × harvested yield × grade-adjusted net price; adaptation/calendar/irrigation cần cost/lead time |
| Water/land availability → mất diện tích hữu dụng → giảm output | Quyền sử dụng, seasonal restrictions, measured water balance | Không giả định giấy tờ pháp lý hợp lệ; legal handoff khi cần |
| Input shortage/price → bỏ/giảm đầu tư → giảm yield hoặc margin | Seed/fertilizer lead time, actual application, input cost | Stress đồng thời input cost và yield, không giữ yield cố định nếu cơ chế có thay đổi |
| Pest/disease → loss hoặc market-access restriction | Surveillance scope, disease confirmation, treatment records | Chuyên gia nông học/xét nghiệm; observation không tự là chẩn đoán |
| Harvest/storage/cold chain → spoilage → grade downgrade/cash loss | Harvest capacity, moisture, temperature excursion, loss denominator | Capacity, inventory và timing cash; diversification có common-weather dependency |
| Commodity/FX/offtake → giá thực nhận giảm hoặc counterparty default | Contracts, basis, hedge volumes, receivables | Price/basis risk, credit; hedge không tự xóa volume risk |

Ví dụ: thiếu nước trong giai đoạn ra hoa → yield giảm → thiếu sản lượng theo hợp
đồng, phát sinh mua bù và phạt. Tách lost own contribution với buy-in incremental
cost và settlement để không tính trùng. Cash waterfall theo mùa phải phản ánh
chi đầu vào trước thu hoạch và khoản thanh toán trễ.

Weather scenario là giả định khi chưa có mô hình site/crop đã hiệu chỉnh; route
DSMV nếu cần forecasting/uncertainty. Tương quan giữa vùng có cùng drought phải
được nhận diện trước aggregation. Insurance có basis/exclusion/deductible và
delay; không coi payout là tiền chắc chắn. Tra S06 tại
[nguồn](../references/sources.md), không biến global disaster loss thành local
probability. Ngưỡng do mùa vụ, capacity và evidence doanh nghiệp quyết định.
