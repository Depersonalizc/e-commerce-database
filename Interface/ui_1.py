from bokeh.io import show, curdoc
from bokeh.plotting import figure
from bokeh.layouts import widgetbox as wb, layout, row
from bokeh.models import widgets as wd, ColumnDataSource
from bokeh.core.properties import value
from functools import partial
import string
# import pymssql

# 链接数据库用，需要后端提供的服务器地址，名称，账号和密码
# def connectSQLServer():
#     """Connect to SQL server."""
#     attr = dict(
#         server = "10.20.213.10",
#         database = "csc1002",
#         user = "csc1002",
#         password = "csc1002",
#         port = 1433,
#         as_dict = True
#     )

#     try:
#         return pymssql.connect(**attr)
#     except Exception as e:
#         print(e)
#         quit()

# sqlConn = connectSQLServer()

# ------------------------------------Class info------------------------------------
#以下主要是生成展示用的column和label，后端不用看这部分
data = {}
#这个string要改成全部type的string，等总共的type做出来以后要重新写一个
btnGroupLetters = wd.RadioButtonGroup(labels=list(string.ascii_uppercase), active=-1)
btnGroupTitle = wd.RadioButtonGroup(labels = ["begins with...", "...contains...", "...ends with"], active = 0)
title_input = wd.TextInput(value = "", title = "Customer ID", placeholder = "contains...") 
btnGroupDept = wd.RadioButtonGroup(labels = ["begins with...", "...contains...", "...ends with"], active = 0)
dept_input = wd.TextInput(value = "", title = "Seller ID", placeholder = "contains...")
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

# def refresh_table(tsql):
#     """Refresh data table with search result.
#     Keyword arguments:
#     tsql -- SQL string stating how & what to search for.
#     """
#     with sqlConn.cursor(as_dict = True) as cursor:
#         cursor.execute(tsql)
#         rows = cursor.fetchall()
#         data["Order ID"] = [row["orderID"] for row in rows]
#         data["Customer Name"] = [row["cust_name"] for row in rows]
#         data["Seller Name"] = [row["sell_name"] for row in rows]
#         data["Addres"] = [row["address"] for row in rows]
#         data["Timestamp"] = [row["time"] for row in rows]
#         data["Status"] = [row["status"] for row in rows]
#     table.source.data = data
# ————————————————————————————— SQL Queries———————————————————————————————
#搜索用的query，需要后端根据自己的数据结构提供

#搜索购买了特定type的产品的全部订单
#写完了可以改一下函数名字
def fetch_letter(idx):
    """Returns a SQL string for selecting data."""
    tsql = f"SELECT course_id, title, dept_name, credits, instructor\
        FROM lgu.course WHERE title like '{list(string.ascii_uppercase)[idx]}%' ORDER by course_id"
    return tsql

#搜索特定买家 和 或 卖家的订单 包含三个自动调用的子函数
def fetch_command():
    """Returns a SQL string for selecting data.
    Functions course_search(), logic(), dept_search()
    will be called automatically when calling this fuction.
    """
    tsql = f"SELECT course_id, title, dept_name, credits, instructor\
        FROM lgu.course WHERE (title like '{course_search()}' {logic()} dept_name like '{dept_search()}')\
        GROUP BY course_id, title, dept_name, credits, instructor ORDER BY course_id"
        # If the three functions above return empty strings,
        # the out come would be all classes in data
        # when calling refresh_table(tsql) later on.
    return tsql

# 点击某个type按钮后自动刷新，自动调用搜索函数搜索含这个type产品的全部订单
def btnGroupClicked(idx):
    """Refresh data table when one of the button 
    in button group is clicked.

    Keyword arguments:
    idx -- Index of the clicked button.
    """
    refresh_table(fetch_letter(idx))

# 不需要的函数，之后可以删掉

# 点击type按钮后自动更换下方输入栏里的placeholder，我们的project里
# 上方搜索的内容（type）和下方搜索的内容（客户ID）没有关联，所以不需要
def change_placeholder(idx, Name = None):
    """Change the appearence of place holder
    accoring to user's choice.

    Keyword arguments:
    idx -- Index of the clicked button.
    Name – Indicating which function calls this function. 
    """
    exec(f"{Name}_input.placeholder = btnGroupTitle.labels[idx]")
    #{Name} makes it applicable for both title & dept button group. 

# 将输入的客户ID转换成string，如果需要换成int的话这里需要改
def course_search():
    """Return a string formed key word.
    Used in searching course titles.
    """
    if btnGroupTitle.active == 0:
        return title_input.value + "%"
    if btnGroupTitle.active == 1:
        return "%" + title_input.value + "%"
    if btnGroupTitle.active == 2:
        return "%" + title_input.value

# 获得客户ID和商家ID之间的搜索逻辑，
# “或” 或者 “和”
def logic():
    """Return a string form logic word."""
    if optionGroup.active == 0:
        return "and"
    if optionGroup.active == 1:
        return "or"

# 将输入的卖家ID转换成string，如果需要换成int的话这里需要改
def dept_search():
    """Return a string formed key word.
    Used in searching departments.
    """
    if btnGroupDept.active == 0:
        return dept_input.value + "%"
    if btnGroupDept.active == 1:
        return "%" + dept_input.value + "%"
    if btnGroupDept.active == 2:
        return "%" + dept_input.value

# 点击刷新按钮后刷新界面
def refresh_clicked():
    """Refresh data table after clicking
    'refresh' button.
    """
    refresh_table(fetch_command())

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
    """Returns a list of selections."""
    tsql = "SELECT dept_name FROM lgu.student GROUP BY dept_name order by dept_name"
    with sqlConn.cursor(as_dict = True) as cursor:
        cursor.execute(tsql)
        dic_list = cursor.fetchall()
        option_list = []
        for dic in dic_list:
            option_list.append(dic["dept_name"]) 
        return option_list

# 更换图表中表示的商品type的函数
# 更换后需要重新选出该type下每个卖家收到的不同等级的评价数量（count）
def change_dept(attr, old, new):
    """Change data of chart after a selection 
    of department is made.
    
    Key arguements:
    attr -- The attribute of change. preset when called.
    old -- The value before change.
    new -- The value after change.
    """
    tsql = f"SELECT year, gpa, count(*) as counts\
        FROM lgu.student WHERE dept_name = '{new}' \
        GROUP BY year, gpa ORDER by year, gpa"
    with sqlConn.cursor(as_dict = True) as cursor:
        cursor.execute(tsql)
        rows = cursor.fetchall()
        for rating in Rating:
            for __row in rows:
                if __row["rating"] == rating:
                    data_rating[__row["Seller"]][Rating.index(rating)] = __row["counts"]
    source_plot.data = data_rating

#生成网页一开始的初始表单
dept_select = wd.Select(title = "Item Type", value = "Type A",
                     options = select_options() )
change_dept(None, None, "Type A")  # Set default value for chart.
#选择的type发生变化时自动调用change_dept函数，刷新图表。
dept_select.on_change("value", change_dept)

#以下是网页布局，后端不用关注
# ------------------------------------Layouts------------------------------------
cInfo = layout(
    [
        [wb(btnGroupLetters, width = 1000)],
        [wb(btnGroupTitle),wb(btnGroupDept)],
        [wb(title_input), wb(paragraph, optionGroup, width = 100), wb(dept_input)],
        [wb(refresh,width = 100)],
        [table]
    ]
)
sta = layout(row(dept_select, p))

page1 = wd.Panel(child = cInfo, title = "Order Info")
page2 = wd.Panel(child = sta, title = "Rating Statistics")

tabs = wd.Tabs(tabs = [page1, page2])
curdoc().add_root(tabs)