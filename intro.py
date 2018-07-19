import matplotlib.pyplot as plt

### Line Chart
x = [1,2,3]
y = [5,7,4]

x2 = [1,2,3]
y2 = [10,14,12]

plt.plot(x,y, label='first')
plt.plot(x2,y2, label='second')
plt.xlabel('Plot Number')
plt.ylabel('Important var')
plt.title('Int Graph\nCheck it out')
plt.legend()
plt.show()


### Bar Charts

# import matplotlib.pyplot as plt
plt.bar([1,3,5,7,9],[5,2,7,8,2], label="Example one")

plt.bar([2,4,6,8,10],[8,6,2,5,6], label="Example two", color='g')
plt.legend()
plt.xlabel('bar number')
plt.ylabel('bar height')

plt.title('Epic Graph\nAnother Line! Whoa')

plt.show()


### Histograms

# import matplotlib.pyplot as plt

population_ages = [22,55,62,45,21,22,34,42,42,4,99,102,110,120,121,122,130,111,115,112,80,75,65,54,44,43,42,48]

bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]

plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.show()


### Scatter Plots


x = [1,2,3,4,5,6,7,8]
y = [5,2,4,2,1,4,5,2]

plt.scatter(x,y, label='skitscat', color='k', s=250, marker="x")

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()


### Stack plots

# import matplotlib.pyplot as plt

days = [1,2,3,4,5]

sleeping = [7,8,6,11,7]
eating = [2,3,4,3,2]
working = [7,8,7,2,2]
playing = [8,5,7,8,13]

plt.plot([],[],color='m', label='Sleeping', linewidth=5)
plt.plot([],[],color='c', label='Eating', linewidth=5)
plt.plot([],[],color='r', label='Working', linewidth=5)
plt.plot([],[],color='k', label='Playing', linewidth=5)

plt.stackplot(days, sleeping,eating,working,playing, colors=['m','c','r','k'])

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()


### Pie Charts

# import matplotlib.pyplot as plt

slices = [7,2,2,13]
activities = ['sleeping','eating','working','playing']
cols = ['c','m','r','b']

plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90,
        shadow= True,
        explode=(0.1,0.1,0,0),
        autopct='%1.1f%%')

plt.title('Interesting Graph\nCheck it out')
plt.show()


### Loading Data from files
### ver_1
# import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('example.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x,y, label='Loaded from file!')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()


### ver_2 (Faster, cleaner, better)
# import matplotlib.pyplot as plt
import numpy as np

x, y = np.loadtxt('example.txt', delimiter=',', unpack=True)
plt.plot(x,y, label='Loaded from file!')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()

### Data from Internet

# import matplotlib.pyplot as plt
import numpy as np
import urllib
import matplotlib.dates as mdates


def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter


def graph_data(stock):
    # Unfortunately, Yahoo's API is no longer available
    # feel free to adapt the code to another source, or use this drop-in replacement.
    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'

    source_code = urllib.request.urlopen(stock_price_url).read().decode()

    stock_data = []
    split_source = source_code.split('\n')

    for line in split_source[1:]:
        split_line = line.split(',')
        if len(split_line) == 7:
            if 'values' not in line and 'labels' not in line:
                stock_data.append(line)

    date, closep, highp, lowp, openp, adj_closep, volume = np.loadtxt(stock_data,
                                                                      delimiter=',',
                                                                      unpack=True,
                                                                      # %Y = full year. 2015
                                                                      #  %y = partial year 15
                                                                      #  %m = number month
                                                                      #  %d = number day
                                                                      #  %H = hours
                                                                      #  %M = minutes
                                                                      #  %S = seconds
                                                                      #  12-06-2014
                                                                      #  %m-%d-%Y
                                                                      converters={0: bytespdate2num('%Y-%m-%d')})
    plt.plot_date(date, closep, '-', label='Price')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Int Graph\nCheck it out')
    plt.legend()
    plt.show()


graph_data('TSLA')


### Basic Customization

def graph_data(stock):
    fig = plt.figure()
    ax1 = plt.subplot2grid((1,1), (0,0),)
    # Unfortunately, Yahoo's API is no longer available
    # feel free to adapt the code to another source, or use this drop-in replacement.
    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'

    source_code = urllib.request.urlopen(stock_price_url).read().decode()

    stock_data = []
    split_source = source_code.split('\n')

    for line in split_source[1:]:
        split_line = line.split(',')
        if len(split_line) == 7:
            if 'values' not in line and 'labels' not in line:
                stock_data.append(line)

    date, closep, highp, lowp, openp, adj_closep, volume = np.loadtxt(stock_data,
                                                                      delimiter=',',
                                                                      unpack=True,
                                                                      # %Y = full year. 2015
                                                                      #  %y = partial year 15
                                                                      #  %m = number month
                                                                      #  %d = number day
                                                                      #  %H = hours
                                                                      #  %M = minutes
                                                                      #  %S = seconds
                                                                      #  12-06-2014
                                                                      #  %m-%d-%Y
                                                                      converters={0: bytespdate2num('%Y-%m-%d')})
    ax1.plot_date(date, closep, '-', label='Price')
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    ax1.grid(True, color='g', linestyle='-', linewidth=0.5)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Int Graph\nCheck it out')
    plt.legend()
    plt.subplots_adjust(left=0.1, bottom=0.20,right=0.94, top=0.90,wspace=0.2, hspace=0)
    plt.show()


graph_data('TSLA')


### Unix Time

import datetime
timestamp = 1339521878.04
value = datetime.datetime.fromtimestamp(timestamp)
print(value.strftime('%Y-%m-%d %H:%M:%S'))


### Colors & Fills


def graph_data(stock):
    fig = plt.figure()
    ax1 = plt.subplot2grid((1,1), (0,0),)
    # Unfortunately, Yahoo's API is no longer available
    # feel free to adapt the code to another source, or use this drop-in replacement.
    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'

    source_code = urllib.request.urlopen(stock_price_url).read().decode()

    stock_data = []
    split_source = source_code.split('\n')

    for line in split_source[1:]:
        split_line = line.split(',')
        if len(split_line) == 7:
            if 'values' not in line and 'labels' not in line:
                stock_data.append(line)

    date, closep, highp, lowp, openp, adj_closep, volume = np.loadtxt(stock_data,
                                                                      delimiter=',',
                                                                      unpack=True,
                                                                      converters={0: bytespdate2num('%Y-%m-%d')})
    ax1.plot_date(date, closep, '-', label='Price')

    ax1.plot([],[], linewidth=5, label='Loss', color='r', alpha=0.5)
    ax1.plot([],[], linewidth=5, label='Gain', color='g', alpha=0.5)

    ax1.fill_between(date, closep, closep[0],where=(closep > closep[0]),facecolors='g', alpha=0.3)
    ax1.fill_between(date, closep, closep[0],where=(closep < closep[0]),facecolors='r', alpha=0.3)

    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    ax1.grid(True, color='g', linestyle='-', linewidth=0.5)
    ax1.xaxis.label.set_color('c')
    ax1.yaxis.label.set_color('r')
    # ax1.set_yticks([0,25,50,75])


    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('EBAY Stocks')
    plt.legend()
    plt.subplots_adjust(left=0.1, bottom=0.20,right=0.94, top=0.90,wspace=0.2, hspace=0)
    plt.show()


graph_data('TWTR')


### Spine & Horizontal Lines
































