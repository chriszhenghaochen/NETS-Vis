import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.animation as animation
import math
from matplotlib import gridspec

fig = plt.figure(figsize=(8, 6))
gs = gridspec.GridSpec(2, 2,
                       width_ratios=[1,1],
                       height_ratios=[4,1]
                       )
ax = []
ax.append(plt.subplot(gs[0]))
ax.append(plt.subplot(gs[1]))
ax.append(plt.subplot(gs[2]))
ax.append(plt.subplot(gs[3]))


img1 = mpimg.imread('C:/Users/zchen4/Desktop/data/Park Map.jpg')
img2 = mpimg.imread('C:/Users/zchen4/Desktop/data/SOM frequence fri.png')
ax[0].imshow(img1, extent=[0,100,0,100])
ax[1].imshow(img2, extent=[0,100,0,100])

with open('C:/Users/zchen4/Desktop/data/dataout/id = 941.csv') as f1:
    data1 = f1.read()

with open('C:/Users/zchen4/Desktop/data/dataout/id = 2672.csv') as f2:
    data2 = f2.read()

with open('C:/Users/zchen4/workspace/DTW/trace0.csv') as f3:
    data3 = f3.read()

with open('C:/Users/zchen4/workspace/DTW/trace1.csv') as f4:
    data4 = f4.read()

with open("output.txt") as f5:
    data5 = f5.read()



data1 = data1.split('\n')
x1 = [row.split(',')[0] for row in data1]
y1 = [row.split(',')[1] for row in data1]

data2 = data2.split('\n')
x2 = [row.split(',')[0] for row in data2]
y2 = [row.split(',')[1] for row in data2]

data3 = data3.split('\n')
x3 = [row.split(',')[0] for row in data3]

data4 = data4.split('\n')
x4 = [row.split(',')[0] for row in data4]


data5 = data5.split('\n')
x5 = [row.split(',')[0] for row in data5]
y5 = [row.split(',')[1] for row in data5]
# print x2

l1 = len(x1)
l2 = len(x2)
l3 = len(x3)
l4 = len(x4)

if l1 != l3 or l2 != l4:
    print "no equal"

max_len =max(l1,l2)

# ax[1].imshow(extent=[0,l2,0,m2])

# data = np.array([x, y], np.int32)


# print data
#
# def animate(i,j):
#
def animate(i):
    if i > 1:
        if i < l1:
            x1_sub = x1[i-2:i]
            y1_sub = y1[i-2:i]
            speed1 = math.pow(float(x3[i]),2)
            ax[0].plot(x1_sub, y1_sub, c = (1-speed1*10, 1-speed1*10, 1-speed1*10), linewidth = 2)

        if i < l2:
            x2_sub = x2[i-2:i]
            y2_sub = y2[i-2:i]
            speed2 = math.pow(float(x4[i]),2)
            ax[0].plot(x2_sub, y2_sub, c = (1 - speed2*10, 1-speed2*10,1 -speed2*10), linewidth = 2)

    if i < l3:
        x3_sub = x3[0:i]
        ax[2].plot(x3_sub, c='b')

    if i < l4:
        x4_sub = x4[0:i]
        ax[2].plot(x4_sub, c='r')

    if i < max_len:
        x5_sub = x5[0:i]
        y5_sub = y5[0:i]
        ax[3].plot(x5_sub, y5_sub, c = 'g', linewidth = 2)


    return ax


def init():
    return ax


ani = animation.FuncAnimation(fig, animate, init_func=init, blit=False,
   interval=10, repeat=True)

plt.show()