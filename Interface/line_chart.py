from bokeh.plotting import figure, output_file, show
import datetime
import numpy as np
np.set_printoptions(suppress=True,formatter={'float_kind':'{:.1f}'.format})

ana = [{'time':datetime.datetime(2010,4,26,0,0),'COUNT(orderID)':2},{'time':datetime.datetime(2012,5,26,0,0),'COUNT(orderID)':3},
        {'time':datetime.datetime(2014,6,26,0,0),'COUNT(orderID)':4},{'time':datetime.datetime(2016,7,26,0,0),'COUNT(orderID)':5},
        {'time':datetime.datetime(2017,8,26,0,0),'COUNT(orderID)':2},{'time':datetime.datetime(2018,9,26,0,0),'COUNT(orderID)':3},
        {'time':datetime.datetime(2019,10,26,0,0),'COUNT(orderID)':2},{'time':datetime.datetime(2020,11,26,0,0),'COUNT(orderID)':3},
        {'time':datetime.datetime(2021,12,26,0,0),'COUNT(orderID)':2},{'time':datetime.datetime(2022,1,26,0,0),'COUNT(orderID)':3},]

x = []
y = []

for i in range(len(ana)):
    tempDict = ana[i]
    dt_time = tempDict['time']
    x.append(dt_time.year)
    dt_count = tempDict['COUNT(orderID)']
    y.append(dt_count)

'''
for i in range(len(ana)):
    tempDict = ana[i]
    dt_time = tempDict['time']
    x.append(dt_time.month)
    dt_count = tempDict['COUNT(orderID)']
    y.append(dt_count)
'''


output_file("multiple.html")

p = figure(plot_width=400, plot_height=400)
p.line(x, y, line_width=2)

p.circle(x, y, fill_color="white", size=8)

show(p)
