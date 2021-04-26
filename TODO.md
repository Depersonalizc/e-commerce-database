# Seller-end `(SellerAnalytics)`

## TAB 1： 商品展示

- [x] 能够选择不同sellerID的一个下拉选择框 -- `login()`
- [x] 能够展示出被选中的sellerID旗下售出的所有商品，它们的id，type和总销量。
  排序顺序要按照总销量的数量从多到少排序。-- `my_selling_items()`

## TAB 2：商品品种分类总览



## TAB 3：商品评价分析和其他图表
- [ ] 一个能够选择不同type的下拉框
- [ ] 一个图表，它能展示三个seller旗下的这个type的商品的1~5星评价的数量
  （按照星级逐一计数，以柱状图的形式呈现），意在用这个图表让商家
  了解自己的哪个产品相对于其他竞争商家更有优势。
- [ ] 一个能够选择不同SellerID的下拉框
- [x] 一个表格，它展示了该seller销量最高的三个商品名字和相应的数量 `my_selling_items()`
- [x] 一个表格，它展示了该seller五星好评最高的三个商品名字和相应的数量 `my_selling_items()`
- [x] A line graph showing the sale trends of the buyer's shop -- `sales_trend()`



# User-end `(BuyerAnalytics)`

- [ ] 全部商品品种（type）为一个按钮组，点击后下方表格里会呈现所有
  购买了该品种的商品的订单，它们的orderID，CustID，SellerID，Address，Timestamp 和 status
- [ ] 能够选择不同CustID的下拉选择框 **`Probably don't need this`**
- [ ] 一个刷新按钮，点击后会显示所有”被选中的type（如果没有按下任何type按钮就是all）“下
  该客户（被选中的custID）的全部订单，它们的orderID，CustID，SellerID，Address，Timestamp和status