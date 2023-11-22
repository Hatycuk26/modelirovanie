import matplotlib.pyplot as plt
import numpy as np
import math as m
import xml.etree.ElementTree as et
import os.path


def func(x):
    a = 1
    function = 100 * m.sqrt(abs(a - 0.01 * x ** 2)) + 0.01 * abs(x + 10)
    return function


xmin = -15
xmax = 5
count = 1000

xlist = np.linspace(xmin, xmax, count)
ylist = []

for i in range(len(xlist)):
    y = func(xlist[i])
    ylist.append(y)

if(os.path.exists('results') == False):
    os.mkdir('results')



data = et.Element('data')
item_xdata = et.SubElement(data, 'xdata')
item_ydata = et.SubElement(data, 'ydata')
for i in range(len(xlist)):
    item_x = et.SubElement(item_xdata, 'x')
    item_y = et.SubElement(item_ydata, 'y')
    item_x.text = str(xlist[i])
    item_y.text = str(ylist[i])

ffile = et.ElementTree(data)
et.indent(ffile, space="\t", level=0)
ffile.write("results/results_1.xml", encoding="utf-8", xml_declaration=True)

plt.plot(xlist, ylist)
plt.show()