import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.animation as animation
import math
from matplotlib import gridspec

fig = plt.figure(figsize=(8, 6))
gs = gridspec.GridSpec(2, 1,
                       height_ratios=[4,1]
                       )
ax = []
ax.append(plt.subplot(gs[0]))
# ax.append(plt.subplot(gs[1]))


####read data######
with open('outputlab.csv') as f1:
    data1 = f1.read()

FMT = '%H:%M:%S'

data1 = data1.split('\n')
x1 = [row for row in data1]

tra = x1[0]
print(tra)


################find data-- tragetory##############

df = pd.read_csv('out.csv')

tradata = df[df['id'] == tra]
# print(tradata)

travalue = tradata.ix[:,4:6].values.astype('timedelta64')
# print(travalue)

x = travalue[:,0]
y = travalue[:,1]

# print(x)
# print(y)

# timevale = tradata.ix[:,0].values
# print(timevale)

###############find data-- speed change########
speeds = []
length = len(travalue)

# times = np.diff(timevale)/np.timedelta64(1, 's')
# # print(times)
#
# for i in range(length-1):
#     # print(i)
#     #distance
#     x1 = float(x[i])
#     y1 = float(y[i])
#     x2 = float(x[i+1])
#     y2 = float(y[i+1])
#     distance = math.sqrt(math.pow(x1-x2,2) + math.pow(y1-y2,2))
#     speed = distance/times[i]
#     speeds.append(speed)

####################animation################

img = mpimg.imread('map.jpg')
imgplot = ax[0].imshow(img, extent=[0,100,0,100])

l1 = len(travalue)



def animate(i):
    if i < l1-1 and i >= 0:
        x1_sub = x[i:i+2]
        y1_sub = y[i:i+2]
        # speedval = math.pow(float(speeds[i]),2)

        #thickness
        ax[0].plot(x1_sub, y1_sub, c='red')

        # #color
        # ax[0].plot(x1_sub, y1_sub, c = (1 - speedval*10, 1-speedval*10,1 -speedval*10), linewidth = 2)

        #speed
        # x4_sub = speeds[0:i]
        # ax[1].plot(x4_sub, c='black')


    return ax


def init():
    return ax


ani = animation.FuncAnimation(fig, animate, init_func=init, blit=False,
   interval=10, repeat=True)

plt.show()