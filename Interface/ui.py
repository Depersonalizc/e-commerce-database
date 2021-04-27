from bokeh.io import show, curdoc
from bokeh.plotting import figure
from bokeh.layouts import widgetbox as wb, layout, row
from bokeh.models import widgets as wd, ColumnDataSource
from bokeh.models import Div
from bokeh.core.properties import value
from functools import partial
from queries import SellerAnalytics
from queries import get_cnx
import string

cfg = {
        'user': 'root',
        'password': '235whoisra',
        'database': 'csc3170'
    }

cnx = get_cnx(cfg)

ana = SellerAnalytics(cnx, seller_id=1)

# ------------------------------------Class info------------------------------------
data = {}

seller_login = wd.Select(title = "Seller Login", value = "1",
                     options = ["1","2","3","4","5","6","7","8","9","10"] )
order_options = wd.Select(title = "Order by", value = "Stock",
                     options = ["Stock","Sales Volume","Average Rating"] )
acsd_opt = wd.RadioButtonGroup(labels = ["Descending:↓", "Ascending:↑", ], active = 0, height = 50)
columns_item =[
    wd.TableColumn(field = "Item ID", title = "Item ID"),
    wd.TableColumn(field = "Item Type", title = "Item Type"),
    wd.TableColumn(field = "Stock", title = "Stock"),
    wd.TableColumn(field = "Sales Volume", title = "Sales Volume"),
    wd.TableColumn(field = "Average Rating", title = "Average Rating"),
    wd.TableColumn(field = "Description", title = "Description")
]

table_item = wd.DataTable(source = ColumnDataSource(data = data),
    columns = columns_item, width = 800, height = 200) 

labels1 = [
    "Toiletries",
    "Imported goods", 
    "Women’s wear", 
    "Men’s wear",
    "Food",
    "Shoes",
    "Phone",
    "Bags and suitcases",
    "Sporting goods",
    "Jewelry",
    "Electric appliance",
    "Car"
]
labels2 = [
    "Health care products",
    "Medicine",
    "Car accessories",
    "Articles of luxury",
    "Packaging",
    "Digital appliance",
    "Home improvement products",
    "Underwear",
    "Mother and baby products"
]
btnGroupLetters1 = wd.RadioButtonGroup(labels=labels1, active=-1)

btnGroupLetters2 = wd.RadioButtonGroup(labels=labels2, active=-1)

cust_input = wd.TextInput(value = "", title = "Customer ID", placeholder = "contains...") 
paragraph = wd.Paragraph(text = "option", width = 100)
refresh = wd.Button(label="Refresh")

columns =[
    wd.TableColumn(field = "Order ID", title = "Order ID"),
    wd.TableColumn(field = "Customer Name", title = "Customer ID"),
    wd.TableColumn(field = "Addres", title = "Addres"),
    wd.TableColumn(field = "Timestamp", title = "Timestamp"),
    wd.TableColumn(field = "Status", title = "Status"),
]

table = wd.DataTable(source = ColumnDataSource(data = data),
    columns = columns, width = 800, height = 200) 

def btnGroup1Clicked(idx):
    label = labels1[idx]
    # data = 查找该卖家旗下全部含有该品种商品的订单的query

def btnGroup2Clicked(idx):
    label = labels2[idx]
    # data = 查找该卖家旗下全部含有该品种商品的订单的query

def refresh_table():    
    data = data
    #data = 上方各种条件下集和的query, 搜索条件是"%" + title_input.value + "%"

btnGroupLetters1.on_click(btnGroup1Clicked)
btnGroupLetters2.on_click(btnGroup2Clicked)
refresh.on_click(refresh_table)
# ————————————————————————————— SQL Queries———————————————————————————————

# 没有连上数据库的话生成网页展示的初始数据时会报错，所以我先给标注上了
# 前面的函数改了名字的话下面这里也要跟着改一下

#refresh_table(fetch_command())
#btnGroupLetters.on_click(btnGroupClicked)
#btnGroupTitle.on_click(partial(change_placeholder, Name = "title"))
#btnGroupDept.on_click(partial(change_placeholder, Name = "dept"))
#refresh.on_click(refresh_clicked)

# ------------------------------------Statistics------------------------------------
Rating = ["5★", "4.5★", "4★", "3.5★", "3★", "2.5★", "2★", "1.5★", "1★"]
Sellers = ["SellerA", "SellerB", "SellerC"]
colors = ["#c9d9d3", "#718bdf", "#e84d60"]
data_rating = {
    "Rating": Rating,
    "SellerA": [0]*9,
    "SellerB": [0]*9,
    "SellerC": [0]*9,
}

p = figure(x_range = Rating, y_range = (0, 40),
            plot_height = 250,
            title = "Rating counts for similar types of product of different sellers",
            toolbar_location = None, tools ="")

source_plot = ColumnDataSource(data = {})

p.vbar_stack(Sellers, x = "Rating", width = 0.9, 
            color = colors, source = source_plot, 
            legend = [value(x) for x in Sellers])


def refresh_table_item(rawdata):
    data["Item ID"] = [row["itemID"] for row  in rawdata]
    data["Item Type"] = [row["type"] for row  in rawdata]
    data["Stock"] = [row["stock"] for row in rawdata]
    data["Sales Volume"] = [row["SUM(quantity)"] for row in rawdata]
    data["Average Rating"] = [row["AVG(rating)"] for row in rawdata]
    data["Description"] = [row["description"] for row in rawdata]
    
    table_item.source.data = data  

def change_seller(attr,old,new):
    ana.login(new)
    if order_options.value == "Stock":
        rawdata = ana.my_selling_items(order_by='stock', asc=bool(acsd_opt.active))
    if order_options.value == "Sales Volume": 
        rawdata = ana.my_selling_items(order_by='SUM(quantity)', asc=bool(acsd_opt.active))
    if order_options.value == "Average Rating":
        rawdata = ana.my_selling_items(order_by='AVG(rating)', asc=bool(acsd_opt.active))
    refresh_table_item(rawdata)

def change_order(attr,old,new):
    if new == "Stock":
        rawdata = ana.my_selling_items(order_by='stock', asc=bool(acsd_opt.active))
    if new == "Sales Volume": 
        rawdata = ana.my_selling_items(order_by='SUM(quantity)', asc=bool(acsd_opt.active))
    if new == "Average Rating":
        rawdata = ana.my_selling_items(order_by='AVG(rating)', asc=bool(acsd_opt.active))
    refresh_table_item(rawdata)

def change_acdc(idx):
    print(idx)
    acsd_opt.active = idx
    if order_options.value == "Stock":
        rawdata = ana.my_selling_items(order_by='stock', asc=bool(idx))
    if order_options.value == "Sales Volume": 
        rawdata = ana.my_selling_items(order_by='SUM(quantity)', asc=bool(idx))
    if order_options.value == "Average Rating":
        rawdata = ana.my_selling_items(order_by='AVG(rating)', asc=bool(idx))
    refresh_table_item(rawdata)
    

Title1 = Div(text = "<b>Item(s) in Stock<b>", default_size = 1200, width=200, height=100)

rawdata = rawdata = ana.my_selling_items(order_by='stock', asc=bool(acsd_opt.active))
refresh_table_item(rawdata)
seller_login.on_change('value', change_seller)
order_options.on_change('value', change_order)
acsd_opt.on_click(change_acdc)



# 更换图表中表示的商品type的函数
# 更换后需要重新选出该type下每个卖家收到的不同等级的评价数量（count）
#生成网页一开始的初始表单
dept_select = wd.Select(title = "Item Type", value = "Toiletries",
                     options = [
    "Toiletries",
    "Imported goods", 
    "Women’s wear", 
    "Men’s wear",
    "Food",
    "Shoes",
    "Phone",
    "Bags and suitcases",
    "Sporting goods",
    "Jewelry",
    "Electric appliance",
    "Car",
    "Health care products",
    "Medicine",
    "Car accessories",
    "Articles of luxury",
    "Packaging",
    "Digital appliance",
    "Home improvement products",
    "Underwear",
    "Mother and baby products"
    ] )

# ------------------------------------Layouts------------------------------------
sInfo = layout(
        [seller_login, order_options, acsd_opt],
        [Title1],
        [table_item]
)

cInfo = layout(
    [
        [wb(btnGroupLetters1, width = 1000)],
        [wb(btnGroupLetters2, width = 1000)],
        [wb(cust_input)],
        [wb(refresh, width = 100)],
        [table]
    ]
)


sta = layout(
    [dept_select]
    )

page1 = wd.Panel(child = sInfo, title = "Seller Shop Info")
page2 = wd.Panel(child = cInfo, title = "BuyerAnalytics")
page3 = wd.Panel(child = sta, title = "Seller Analytics")

tabs = wd.Tabs(tabs = [page1, page2, page3])
curdoc().add_root(tabs)


