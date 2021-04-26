from bokeh.io import show, curdoc
from bokeh.plotting import figure
from bokeh.layouts import widgetbox as wb, layout, row
from bokeh.models import widgets as wd, ColumnDataSource
from bokeh.core.properties import value
from functools import partial
import string
import pymssql


# ------------------------------------Class info------------------------------------
data = {}

seller_login = wd.Select(title = "Seller Login", value = "Seller A",
                     options = ["Seller A","Seller B", "Seller C"] )

columns_item_sold =[
    wd.TableColumn(field = "Item ID", title = "Item ID"),
    wd.TableColumn(field = "Item Type", title = "Item Type"),
    wd.TableColumn(field = "Sales Volume", title = "Sales Volume"),
]

table_item_sold = wd.DataTable(source = ColumnDataSource(data = data),
    columns = columns_item_sold, width = 800, height = 280) 

# 为了保证页面美观性将所有的type拆分城了两个button Group
# 在它们上面用的的function都一样
btnGroupLetters1 = wd.RadioButtonGroup(labels=[
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
], active=-1)

btnGroupLetters2 = wd.RadioButtonGroup(labels=[
    "Health care products",
    "Medicine",
    "Car accessories",
    "Articles of luxury",
    "Packaging",
    "Digital appliance",
    "Home improvement products",
    "Underwear",
    "Mother and baby products"
], active=-1)

cust_input = wd.TextInput(value = "", title = "Customer ID", placeholder = "contains...") 
paragraph = wd.Paragraph(text = "option", width = 100)
optionGroup = wd.RadioGroup(labels = ["and", "or"], active = 0, width = 100, inline = True)
refresh = wd.Button(label="Refresh")

columns =[
    wd.TableColumn(field = "Order ID", title = "Order ID"),
    wd.TableColumn(field = "Customer Name", title = "Customer ID"),
    wd.TableColumn(field = "Seller Name", title = "Seller ID"),
    wd.TableColumn(field = "Addres", title = "Addres"),
    wd.TableColumn(field = "Timestamp", title = "Timestamp"),
    wd.TableColumn(field = "Status", title = "Status"),
]

table = wd.DataTable(source = ColumnDataSource(data = data),
    columns = columns, width = 800, height = 280) 

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

# 选择出全部的商品type（需要SQL语句），用作展示下拉列表里面的各个选项
def select_options():
        return ["Type A", "B", "C"]

# 更换图表中表示的商品type的函数
# 更换后需要重新选出该type下每个卖家收到的不同等级的评价数量（count）
#生成网页一开始的初始表单
dept_select = wd.Select(title = "Item Type", value = "Type A",
                     options = ["A","B"] )

#以下是网页布局，后端不用关注
# ------------------------------------Layouts------------------------------------
sInfo = layout(
        [seller_login],
        [table_item_sold]
)

cInfo = layout(
    [
        [seller_login],
        [wb(btnGroupLetters1, width = 1000)],
        [wb(btnGroupLetters2, width = 1000)],
        [wb(cust_input)],
        [wb(refresh, width = 100)],
        [table]
    ]
)


sta = layout(dept_select)

page1 = wd.Panel(child = sInfo, title = "Items Sold")
page2 = wd.Panel(child = cInfo, title = "Order Info")
page3 = wd.Panel(child = sta, title = "Rating Statistics")

tabs = wd.Tabs(tabs = [page1, page2, page3])
curdoc().add_root(tabs)


