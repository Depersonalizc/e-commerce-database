from bokeh.io import show, curdoc
from bokeh.plotting import figure
from bokeh.layouts import widgetbox as wb, layout, row
from bokeh.models import widgets as wd, ColumnDataSource
from bokeh.core.properties import value
from functools import partial
import string
import pymssql

def connectSQLServer():
    """Connect to SQL server."""
    attr = dict(
        server = "10.20.213.10",
        database = "csc1002",
        user = "csc1002",
        password = "csc1002",
        port = 1433,
        as_dict = True
    )

    try:
        return pymssql.connect(**attr)
    except Exception as e:
        print(e)
        quit()

sqlConn = connectSQLServer()

# ------------------------------------Class info------------------------------------
data = {}
btnGroupLetters = wd.RadioButtonGroup(labels=list(string.ascii_uppercase), active=-1)
btnGroupTitle = wd.RadioButtonGroup(labels = ["begins with...", "...contains...", "...ends with"], active = 0)
title_input = wd.TextInput(value = "", title = "Title:", placeholder = "contains...") 
btnGroupDept = wd.RadioButtonGroup(labels = ["begins with...", "...contains...", "...ends with"], active = 0)
dept_input = wd.TextInput(value = "", title = "Department:", placeholder = "contains...")
paragraph = wd.Paragraph(text = "option", width = 100)
optionGroup = wd.RadioGroup(labels = ["and", "or"], active = 0, width = 100, inline = True)
refresh = wd.Button(label="Refresh")

columns =[
    wd.TableColumn(field = "Course ID", title = "Course ID"),
    wd.TableColumn(field = "Title", title = "Title"),
    wd.TableColumn(field = "Department", title = "Department"),
    wd.TableColumn(field = "Credit", title = "Credit"),
    wd.TableColumn(field = "Instructor", title = "Instructor"),
]

table = wd.DataTable(source = ColumnDataSource(data = data),
    columns = columns, width = 800, height = 280) 

def refresh_table(tsql):
    """Refresh data table with search result.
    Keyword arguments:
    tsql -- SQL string stating how & what to search for.
    """
    with sqlConn.cursor(as_dict = True) as cursor:
        cursor.execute(tsql)
        rows = cursor.fetchall()
        data["Course ID"] = [row["course_id"] for row in rows]
        data["Title"] = [row["title"] for row in rows]
        data["Department"] = [row["dept_name"] for row in rows]
        data["Credit"] = [row["credits"] for row in rows]
        data["Instructor"] = [row["instructor"] for row in rows]
    table.source.data = data


def fetch_letter(idx):
    """Returns a SQL string for selecting data."""
    tsql = f"SELECT course_id, title, dept_name, credits, instructor\
        FROM lgu.course WHERE title like '{list(string.ascii_uppercase)[idx]}%' ORDER by course_id"
    return tsql


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


def btnGroupClicked(idx):
    """Refresh data table when one of the button 
    in button group is clicked.

    Keyword arguments:
    idx -- Index of the clicked button.
    """
    refresh_table(fetch_letter(idx))


def change_placeholder(idx, Name = None):
    """Change the appearence of place holder
    accoring to user's choice.

    Keyword arguments:
    idx -- Index of the clicked button.
    Name – Indicating which function calls this function. 
    """
    exec(f"{Name}_input.placeholder = btnGroupTitle.labels[idx]")
    #{Name} makes it applicable for both title & dept button group. 


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


def logic():
    """Return a string form logic word."""
    if optionGroup.active == 0:
        return "and"
    if optionGroup.active == 1:
        return "or"


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


def refresh_clicked():
    """Refresh data table after clicking
    'refresh' button.
    """
    refresh_table(fetch_command())


refresh_table(fetch_command())
btnGroupLetters.on_click(btnGroupClicked)
btnGroupTitle.on_click(partial(change_placeholder, Name = "title"))
btnGroupDept.on_click(partial(change_placeholder, Name = "dept"))
refresh.on_click(refresh_clicked)

# ------------------------------------Statistics------------------------------------
GPA = ["A+", "A", "B+", "B", "C+", "C", "D+", "D", "F"]
years = ["2015", "2016", "2017"]
colors = ["#c9d9d3", "#718bdf", "#e84d60"]
data_gpa = {
    "GPA": GPA,
    "2015": [0]*9,
    "2016": [0]*9,
    "2017": [0]*9,
}

p = figure(x_range = GPA, y_range = (0, 40),
            plot_height = 250,
            title = "GPA Counts by Year",
            toolbar_location = None, tools ="")

source_plot = ColumnDataSource(data = {})

p.vbar_stack(years, x = "GPA", width = 0.9, 
            color = colors, source = source_plot, 
            legend = [value(x) for x in years])

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
        for gpa in GPA:
            for __row in rows:
                if __row["gpa"] == gpa:
                    data_gpa[__row["year"]][GPA.index(gpa)] = __row["counts"]
    source_plot.data = data_gpa

dept_select = wd.Select(title = "Department", value = "Accounting",
                     options = select_options() )
change_dept(None, None, "Accounting")  # Set default value for chart.
dept_select.on_change("value", change_dept)

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

page1 = wd.Panel(child = cInfo, title = "Course Info")
page2 = wd.Panel(child = sta, title = "Statistics")

tabs = wd.Tabs(tabs = [page1, page2])
curdoc().add_root(tabs)