# Retail

Intake: store/e-commerce/omnichannel, category/cohort/site, same-store baseline,
gross-to-net sales, margin, stock ownership, fulfillment, payment scope và cash.
Reconcile units/revenue qua return, cancellations, discounts và channel transfers.

| Driver / CEI | Evidence / KRI | Kiểm tra / ứng phó |
| --- | --- | --- |
| Demand/mix/promotion lệch → margin thấp hoặc stock imbalance | Conversion, basket, returns, sell-through, forecast bias | Price–volume–mix; không cộng channel transfer thành incremental sales |
| Shrinkage/count failure → inventory không tồn tại → cash loss/stockout | Perpetual vs physical counts, reason codes, shrink denominator | Variance không tự là fraud; cần investigation khi có căn cứ |
| Aging/obsolescence → markdown/write-off → margin/cash erosion | Aging, shelf life, usable units, markdown buckets | Inventory model disjoint buckets, expected recovery value, collateral effects |
| Supplier/platform/channel concentration → disruption → mất service | On-time supplier delivery, dependence, substitution lead time | Concentration common upstream; alternative source cần onboarding feasibility |
| Checkout/payment/cyber outage → transaction failure → lost contribution | Declines vs customer abandonment, outage windows, recovery evidence | Payment scope xác định trước áp PCI; distinguish fraud loss/chargebacks/fees |
| Expansion/lease/fulfillment commitments → fixed cost cao → liquidity breach | Store cohort contribution, lease timing, cash runway | Break-even và demand stress, exit obligations; không suy site lỗ là cả chain lỗ |

Stockout loss cần lost sales thật sau substitution/backorder; shelf empty không
đồng nghĩa toàn demand bị mất. Avoid double count write-off với shrinkage của
cùng stock IDs. Net markdown discount khác toàn cost của markdown inventory.
Online fraud cảnh báo không là kết luận; route audit/investigation theo scope.

Store closure, pricing, assortment, staffing, inventory controls và backup
payments có trade-offs về service, safety, privacy và resources. Tra S09/S10
tại [nguồn](../references/sources.md); security/legal kiểm tra nghĩa vụ thực.
Ngưỡng shrink/stockout/KRI cần method doanh nghiệp, không tự gán “chuẩn retail”.
