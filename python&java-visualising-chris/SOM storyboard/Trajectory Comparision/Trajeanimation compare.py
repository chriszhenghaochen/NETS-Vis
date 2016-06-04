import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.animation as animation
import data
import math
from matplotlib import gridspec

fig = plt.figure(figsize=(8, 6))
gs = gridspec.GridSpec(2, 1,
                       height_ratios=[4,1]
                       )
ax = []
ax.append(plt.subplot(gs[0]))
ax.append(plt.subplot(gs[1]))

#####################################1 start#####################################
####read data######
with open('C:/Users/zchen4/Desktop/data/outputlab1.csv') as f1:
    data1 = f1.read()

data1 = data1.split('\n')
x = [row for row in data1]

tra = int(x[0])

print(x[:len(x)-1])

################find data-- tragetory##############

df = data.read_data('Fri')

tradata = df[df['id'] == tra]
# print(tradata)

travalue = tradata.ix[:,3:5].values
# print(travalue)

x1 = travalue[:,0]
y1 = travalue[:,1]

# print(x)
# print(y)

timevale = tradata.ix[:,0].values
# print(timevale)

###############find data-- speed change########
speeds1 = []
length = len(travalue)

times = np.diff(timevale)/np.timedelta64(1, 's')
# print(times)

f = open('C:/Users/zchen4/workspace/DTW/trace0.csv','w')
for i in range(length-1):
    # print(i)
    #distance

    x11 = float(x1[i])
    y11 = float(y1[i])
    x21 = float(x1[i+1])
    y21 = float(y1[i+1])
    distance = math.sqrt(math.pow(x11-x21,2) + math.pow(y11-y21,2))
    speed = distance/times[i]
    speeds1.append(speed)
    f.write(str(speed) + "\n")

f.close()

############################################1 done!!!##################################


############################################2 start####################################
####read data######
with open('C:/Users/zchen4/Desktop/data/outputlab2.csv') as f1:
    data1 = f1.read()

data1 = data1.split('\n')
x = [row for row in data1]

tra = int(x[0])

print(x[:len(x)-1])
################find data-- tragetory##############

df = data.read_data('Fri')

tradata = df[df['id'] == tra]
# print(tradata)

travalue = tradata.ix[:,3:5].values
# print(travalue)

x2 = travalue[:,0]
y2 = travalue[:,1]

# print(x)
# print(y)

timevale = tradata.ix[:,0].values
# print(timevale)

###############find data-- speed change########
speeds2 = []
length = len(travalue)

times = np.diff(timevale)/np.timedelta64(1, 's')
# print(times)

f = open('C:/Users/zchen4/workspace/DTW/trace1.csv','w')
for i in range(length-1):
    # print(i)
    #distance
    x11 = float(x2[i])
    y11 = float(y2[i])
    x21 = float(x2[i+1])
    y21 = float(y2[i+1])
    distance = math.sqrt(math.pow(x11-x21,2) + math.pow(y11-y21,2))
    speed = distance/times[i]
    speeds2.append(speed)
    f.write(str(speed) + "\n")

f.close()
############################################2 done!!!#################################


####################animation################

img = mpimg.imread('C:/Users/zchen4/Desktop/data/Park Map.jpg')
imgplot = ax[0].imshow(img, extent=[0,100,0,100])

l1 = len(x1)
l2 = len(x2)

def animate(i):
    if i < l1 and i > 1:
        x1_sub = x1[i-2:i]
        y1_sub = y1[i-2:i]
        speedval1 = math.pow(float(speeds1[i]),2)

        #thickness
        ax[0].plot(x1_sub, y1_sub, c='black', linewidth = speedval1 * 100)

        # #color
        # ax.plot(x1_sub, y1_sub, c = (1 - speedval1*10, 1-speedval1*10,1 -speedval1*10), linewidth = 2)

        #speed plotting
        x3_sub = speeds1[0:i]
        ax[1].plot(x3_sub, c='black')

    if i < l2 and i > 1:
        x2_sub = x2[i-2:i]
        y2_sub = y2[i-2:i]
        speedval2 = math.pow(float(speeds2[i]),2)

        #thickness
        ax[0].plot(x2_sub, y2_sub, c='blue', linewidth = speedval2 * 100)

        # #color
        # ax.plot(x2_sub, y2_sub, c = (1 - speedval2*10, 1-speedval2*10,1 -speedval2*10), linewidth = 2)


        #speed
        x4_sub = speeds2[0:i]
        ax[1].plot(x4_sub, c='blue')

    return ax


def init():
    return ax


ani = animation.FuncAnimation(fig, animate, init_func=init, blit=False,
   interval=10, repeat=True)

plt.show()