import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


fig, axes = plt.subplots(nrows=2, ncols=2)

file1 = pd.read_csv('C:/Users/zchen4/Desktop/data/dist_speed_4343.csv')

mean1 = file1.speed.mean()
stan1 = file1.speed.std()

file3 = file1[['speed']]
file3.to_csv('C:/Users/zchen4/workspace/DTW/trace0.csv', index = False, header = False)

file1 = file1.set_index(['Timestamp'])

file1.speed.plot(ax=axes[0,0])
axes[1,0].axhline(y=mean1, c="red")
axes[1,0].axhline(y=stan1, c="blue")

file2 = pd.read_csv('C:/Users/zchen4/Desktop/data/dist_speed_2672.csv')

file3 = file2[['speed']]
file3.to_csv('C:/Users/zchen4/workspace/DTW/trace1.csv', index = False, header= False)

mean2 = file2.speed.mean()
stan2 = file2.speed.std()

file2 = file2.set_index(['Timestamp'])

file2.speed.plot(ax=axes[0,1])
axes[1,0].axhline(y=mean2, c="red")
axes[1,0].axhline(y=stan2, c="blue")



with open('C:/Users/zchen4/Desktop/data/output.txt') as f:
    data = f.read()

data = data.split('\n')

x = []
y = []
for row in data:
    if row != '':
        x.append(row.split(',')[0])
        y.append(row.split(',')[1])

ax3 = fig.add_subplot(axes[1,1])
ax3.set_xlabel('ID = 4343')
ax3.set_ylabel('ID = 941')

ax3.plot(x,y, c='r', label='warp path')

leg = ax3.legend()

plt.show()