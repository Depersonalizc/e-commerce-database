from math import pi

import pandas as pd

from bokeh.io import show, curdoc
from bokeh.palettes import Category20c
from bokeh.plotting import figure
from bokeh.transform import cumsum
from bokeh.layouts import widgetbox as wb, layout, row
from bokeh.models import widgets as wd, ColumnDataSource
from bokeh.models import Div
from bokeh.core.properties import value
from functools import partial
from queries import SellerAnalytics, CustomerAnalytics
from queries import get_cnx
import string

from bokeh.io import output_file, show
from collections import Counter

cfg = {
        'user': 'root',
        'password': 'aaaaa',
        'database': 'csc3170_2'
    }

cnx = get_cnx(cfg)
customer = CustomerAnalytics(cnx, cust_id=7)

ana = SellerAnalytics(cnx, seller_id=7)

# ------------------------------------TAB 1------------------------------------
data = {}

seller_login = wd.Select(title = "Seller Login", value = "1",
                     options = ["1","2","3","4","5","6","7","8","9","10"], height=120)
order_options = wd.Select(title = "Order by", value = "Stock",
                     options = ["Stock","Sales Volume","Average Rating"] )
acsd_opt = wd.RadioButtonGroup(labels = ["Descending:↓", "Ascending:↑", ], active = 0, height = 50)
item_search_input = wd.TextInput(value = "", title = "Item Description", placeholder = "Search item...") 
item_search_button = wd.Button(label="Search", height = 50)

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
        rawdata6 = ana.my_selling_items(order_by='stock', asc=bool(acsd_opt.active))
    if order_options.value == "Sales Volume": 
        rawdata6 = ana.my_selling_items(order_by='SUM(quantity)', asc=bool(acsd_opt.active))
    if order_options.value == "Average Rating":
        rawdata6 = ana.my_selling_items(order_by='AVG(rating)', asc=bool(acsd_opt.active))
    refresh_table_item(rawdata6)
    if order_options_order.value == "Seller ID":
        rawdata4 = ana.my_orders(order_by='sellerID', asc=bool(acsd_opt.active))
    if order_options_order.value == "Order ID": 
        rawdata4 = ana.my_orders(order_by='orderID', asc=bool(acsd_opt.active))
    if order_options_order.value == "Time":
        rawdata4= ana.my_orders(order_by='time', asc=bool(acsd_opt.active))
    if order_options_order.value == "Status":
        rawdata4 = ana.my_orders(order_by='status', asc=bool(acsd_opt.active))
    refresh_table_order(rawdata4)

def change_order(attr,old,new):
    if new == "Stock":
        rawdata = ana.my_selling_items(order_by='stock', asc=bool(acsd_opt.active))
    if new == "Sales Volume": 
        rawdata = ana.my_selling_items(order_by='SUM(quantity)', asc=bool(acsd_opt.active))
    if new == "Average Rating":
        rawdata = ana.my_selling_items(order_by='AVG(rating)', asc=bool(acsd_opt.active))
    refresh_table_item(rawdata)

def change_acdc(idx):
    acsd_opt.active = idx
    if order_options.value == "Stock":
        rawdata5 = ana.my_selling_items(order_by='stock', asc=bool(idx))
    if order_options.value == "Sales Volume": 
        rawdata5 = ana.my_selling_items(order_by='SUM(quantity)', asc=bool(idx))
    if order_options.value == "Average Rating":
        rawdata5 = ana.my_selling_items(order_by='AVG(rating)', asc=bool(idx))
    refresh_table_item(rawdata5)
    if order_options_order.value == "Seller ID":
        rawdata3 = ana.my_orders(order_by='sellerID', asc=bool(idx))
    if order_options_order.value == "Order ID": 
        rawdata3 = ana.my_orders(order_by='orderID', asc=bool(idx))
    if order_options_order.value == "Time":
       rawdata3 = ana.my_orders(order_by='time', asc=bool(idx))
    if order_options_order.value == "Status":
       rawdata3= ana.my_orders(order_by='status', asc=bool(idx))
    refresh_table_order(rawdata3)

def search_item():
    refresh_table_item(rawdata)
    
Title1 = Div(text = "<b>Item(s) in Stock<b>", style={'font-size': '220%'},default_size = 1200, width=500, height=100)

columns_order =[
    wd.TableColumn(field = "Order ID", title = "Order ID"),
    wd.TableColumn(field = "Item ID", title = "Item ID"),
    #wd.TableColumn(field = "Description", title = "Description"),
    wd.TableColumn(field = "Quantity", title = "Quantity"),
    wd.TableColumn(field = "Customer ID", title = "Customer ID"),
    wd.TableColumn(field = "Time", title = "Time"),
    wd.TableColumn(field = "Address", title = "Address"),
    wd.TableColumn(field = "Status", title = "Status")
]

table_order= wd.DataTable(source = ColumnDataSource(data = data),
    columns = columns_order, width = 1200, height = 280) 

def refresh_table_order(rawdata):
    data["Order ID"] = [row["orderID"] for row  in rawdata]
    data["Item ID"] = [row["itemID"] for row  in rawdata]
    #data["Description"] = [row["description"] for row in rawdata]
    data["Quantity"] = [row["quantity"] for row in rawdata]
    data["Customer ID"] = [row["custID"] for row in rawdata]
    data["Time"] = [row["time"] for row in rawdata]
    data["Address"] = [row["address"] for row in rawdata]
    data["Status"] = [row["status"] for row in rawdata]
    
    table_order.source.data = data  

rawdata = ana.my_selling_items(order_by='stock', asc=bool(acsd_opt.active))
refresh_table_item(rawdata)
rawdata2 = ana.my_orders(order_by = 'time')
refresh_table_order(rawdata2)

Title2 = Div(text = "<b>My Orders<b>", default_size = 1200, style={'font-size': '220%'}, width=500, height=100)
order_options_order = wd.Select(title = "Order by", value = "Time",
                     options = ["Order ID", "Seller ID", "Time", "Status"] )

def change_order_order(attr,old,new):
    if new == "Order ID":
        rawdata2 = ana.my_orders(order_by='sellerID', asc=bool(acsd_opt.active))
    if new == "Seller ID": 
        rawdata2 = ana.my_orders(order_by='orderID', asc=bool(acsd_opt.active))
    if new == "Time":
       rawdata2 = ana.my_orders(order_by='time', asc=bool(acsd_opt.active))
    if new == "Status":
       rawdata2 = ana.my_orders(order_by='status', asc=bool(acsd_opt.active))
    refresh_table_order(rawdata2)

seller_login.on_change('value', change_seller)
order_options.on_change('value', change_order)
order_options_order.on_change('value', change_order_order)
acsd_opt.on_click(change_acdc)
item_search_button.on_click(search_item)

# ------------------------------------TAB 2------------------------------------

labels1 = [
    "Wear",
    "Food",
    "Phone",
    "Jewelry",
    "Medicine",
    "Car",
    "Articles of luxury",
    "Packaging",
    "Digital appliance",
    "Home improvement products",
    "Mother and baby products"
]

btnGroupLetters1 = wd.RadioButtonGroup(labels = labels1, active=-1)

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


def refresh_table():    
    data = data
    #data = 上方各种条件下集和的query, 搜索条件是"%" + title_input.value + "%"

btnGroupLetters1.on_click(btnGroup1Clicked)
refresh.on_click(refresh_table)
# ————————————————————————————— SQL Queries———————————————————————————————

# 没有连上数据库的话生成网页展示的初始数据时会报错，所以我先给标注上了
# 前面的函数改了名字的话下面这里也要跟着改一下

#refresh_table(fetch_command())
#btnGroupLetters.on_click(btnGroupClicked)
#btnGroupTitle.on_click(partial(change_placeholder, Name = "title"))
#btnGroupDept.on_click(partial(change_placeholder, Name = "dept"))
#refresh.on_click(refresh_clicked)

# ------------------------------------TAB 3------------------------------------

# ------------------------------------Statistics------------------------------------

# ----------------------------------PIE CHART: Rating Distribution-----------------------------------
Rating = ["10★", "8★", "7★", "6★", "5★", "4★", "2★", "1★"]
rawdata2 = ana.rating_counts(asc=False)
data_pie = {}
for i in range(8):
    data_pie[Rating[i]] = rawdata2[i]['COUNT(rating)']

x = Counter(data_pie)

data_pie_2 = pd.DataFrame.from_dict(dict(x), orient='index').reset_index()
data_pie_2 = data_pie_2.rename(index=str, columns={0:'value', 'index':'country'})
data_pie_2['angle'] = data_pie_2['value']/sum(x.values()) * 2*pi
data_pie_2['color'] = Category20c[len(x)]

p = figure(plot_height=350, title="Rating Distribution", toolbar_location=None,
           tools="hover", tooltips=[("Country", "@country"),("Value", "@value")])

p.wedge(x=0, y=1, radius=0.4, 
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', legend='country', source=data_pie_2)

p.axis.axis_label=None
p.axis.visible=False
p.grid.grid_line_color = None

# --------------------------------LINE CHART--------------------------------------
btnGroupTime = wd.RadioButtonGroup(labels = ["Yearly", "Monthly"], active = 0)
def get_data_line():
    line_source  = {}
    line_source['x'] = x_line
    line_source['y'] = y_line
    return line_source


def btnGroupTimeClicked(idx):
    btnGroupTime.active = idx
    rawdata_line = ana.sales_trend(timespan='yearly')
    if idx == 0:
        rawdata_line = ana.sales_trend(timespan='yearly')
        for i in range(len(rawdata_line)):
            tempDict = rawdata_line[i]
            dt_time = tempDict['time']
            x_line.append(dt_time.year)
            dt_count = tempDict['COUNT(orderID)']
            y_line.append(dt_count)

    if idx == 1:
        rawdata_line = ana.sales_trend(timespan='monthly')
        
        for i in range(len(rawdata_line)):
            tempDict = rawdata_line[i]
            dt_time = tempDict['time']
            if dt_time.year == 2020:
                x_line.append(dt_time.month)
                dt_count = tempDict['COUNT(orderID)']
                y_line.append(dt_count)
    source_line.data = get_data_line()
    x_line.clear()
    y_line.clear()
            
btnGroupTime.on_click(btnGroupTimeClicked)

x_line = []
y_line = []

source_line = ColumnDataSource(data = get_data_line())
btnGroupTimeClicked(0)
p_line = figure(plot_width=400, plot_height=400)
p_line.line(x='x', y='y', source = source_line, line_width=2)
p_line.circle(x_line, y_line, fill_color="white", size=8)

# ----------------------------------PIE CHART: Gender Distribution-----------------------------------
Gender = ["Male", "Female"]
rawdata_gen = ana.customer_distribution(group_by='cust_gender')
data_pie_gen = {}
for i in range(2):
    data_pie_gen[Gender[i]] = rawdata_gen[i]['COUNT(DISTINCT custID)']
    
x = Counter(data_pie_gen)

data_pie_gen_2 = pd.DataFrame.from_dict(dict(x), orient='index').reset_index()
data_pie_gen_2 = data_pie_gen_2.rename(index=str, columns={0:'value', 'index':'country'})
data_pie_gen_2['angle'] = data_pie_gen_2['value']/sum(x.values()) * 2*pi
data_pie_gen_2['color'] = ["#c9d9d3", "#718bdf"]

p_gen = figure(plot_height=350, title="Gender Distribution of Customers", toolbar_location=None,
           tools="hover", tooltips=[("Country", "@country"),("Value", "@value")])

p_gen.wedge(x=0, y=1, radius=0.4, 
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', legend='country', source=data_pie_gen_2)

p_gen.axis.axis_label=None
p_gen.axis.visible=False
p_gen.grid.grid_line_color = None

# ----------------------------------PIE CHART: Location Distribution-----------------------------------
ADDR = ['Anhui', 'Beijing', 'Guangdong', 'Hebei', 'Henan', 'Jiangsu', 'Shanghai'] 
rawdata_addr = ana.customer_distribution(group_by='address')
data_pie_addr = {}
for i in range(7):
    data_pie_addr[ADDR[i]] = rawdata_addr[i]['COUNT(DISTINCT custID)']
    
x_addr = Counter(data_pie_addr)

data_pie_addr_2 = pd.DataFrame.from_dict(dict(x_addr), orient='index').reset_index()
data_pie_addr_2 = data_pie_addr_2.rename(index=str, columns={0:'value', 'index':'country'})
data_pie_addr_2['angle'] = data_pie_addr_2['value']/sum(x_addr.values()) * 2*pi
data_pie_addr_2['color'] = Category20c[7]

p_addr = figure(plot_height=350, title="Location Distribution of Customers", toolbar_location=None,
           tools="hover", tooltips=[("Country", "@country"),("Value", "@value")])

p_addr.wedge(x=0, y=1, radius=0.4, 
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', legend='country', source=data_pie_addr_2)

p_addr.axis.axis_label=None
p_addr.axis.visible=False
p_addr.grid.grid_line_color = None


# ------------------------------------Layouts------------------------------------
sInfo = layout(
        [seller_login],
        [Title1],
        [order_options, acsd_opt],
        [item_search_input, item_search_button],
        [table_item],
        [Title2],
        [order_options_order,acsd_opt],
        [table_order]
)


sta1 = layout(
    row(p_line, btnGroupTime)
    )

sta2 = layout(
    row(p)
    )

sta3 = layout(
    row(p_gen)
    )

sta4 = layout(
    row(p_addr)
    )
page1 = wd.Panel(child = sInfo, title = "Shop Info")
page2 = wd.Panel(child = sta1, title = "Sales Trend")
page3 = wd.Panel(child = sta2, title = "Rating Distribution")
page4 = wd.Panel(child = sta3, title = "Customers Distribution (Gender)")
page5 = wd.Panel(child = sta4, title = "Customers Distribution (Location)")

tabs = wd.Tabs(tabs = [page1, page2, page3, page4, page5])
curdoc().add_root(tabs)


