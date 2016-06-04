import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.animation as animation


fig, ax = plt.subplots()

img = mpimg.imread('C:/Users/zchen4/Desktop/data/Park Map.jpg')
imgplot = ax.imshow(img, extent=[0,100,0,100])


with open('C:/Users/zchen4/Desktop/data/id 941.csv') as f1:
    data1 = f1.read()

with open('C:/Users/zchen4/Desktop/data/id 2672.csv') as f2:
    data2 = f2.read()

with open('C:/Users/zchen4/Desktop/data/id 4343.csv') as f3:
    data3 = f3.read()

data1 = data1.split('\n')
x1 = [row.split(',')[0] for row in data1]
y1 = [row.split(',')[1] for row in data1]


data2 = data2.split('\n')
x2 = [row.split(',')[0] for row in data2]
y2 = [row.split(',')[1] for row in data2]

data3 = data3.split('\n')
x3 = [row.split(',')[0] for row in data3]
y3 = [row.split(',')[1] for row in data3]


l1 = len(x1)
l2 = len(x2)
l3 = len(x3)

# data = np.array([x, y], np.int32)


# print data
#
# def animate(i,j):
#
def animate(i):
    if i < l1:
        x1_sub = x1[0:i]
        y1_sub = y1[0:i]
        ax.plot(x1_sub,y1_sub, c='black',linewidth = 1)

    if i < l2:
        x2_sub = x2[0:i]
        y2_sub = y2[0:i]
        ax.plot(x2_sub,y2_sub, c='blue',linewidth = 1)

    if i < l3:
        x3_sub = x3[0:i]
        y3_sub = y3[0:i]
        ax.plot(x3_sub,y3_sub, c='purple', linewidth = 1)

    return ax


def init():
    return ax


ani = animation.FuncAnimation(fig, animate, init_func=init, blit=False,
   interval=10, repeat=True)

plt.show()