import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import matplotlib.gridspec as gridspec
import data


im = data.read_image()
df = data.read_data('Fri', 'subset-300')

p_id = df.id.head(1)[0]
path = df[df.id == p_id].copy()
t_diff = path.Timestamp.diff().fillna(0) / np.timedelta64(1,'s')
x_diff = path.X.diff().fillna(0)
y_diff = path.Y.diff().fillna(0)
diffs = np.hypot(x_diff, y_diff)
path['dist'] = diffs.cumsum()
path['speed'] = diffs / t_diff

check_ins = path[path.type == 'check-in']
stay_points = path[path.Timestamp.diff().shift(-1) > np.timedelta64(10, 's')]

gs = gridspec.GridSpec(2, 2)

ax1 = plt.subplot(gs[0, 0])
plt.plot(path.Timestamp, path.dist)
plt.plot(check_ins.Timestamp, check_ins.dist, linestyle='None', marker='o', color='green')
plt.plot(stay_points.Timestamp, stay_points.dist, linestyle='None', marker='x', color='red')

ax2 = plt.subplot(gs[1, 0])
plt.plot(path.Timestamp, path.speed)
plt.plot(check_ins.Timestamp, check_ins.speed, linestyle='None', marker='o', color='green')
plt.plot(stay_points.Timestamp, stay_points.speed, linestyle='None', marker='x', color='red')

ax3 = plt.subplot(gs[:, 1])
plt.imshow(im, extent=[0, 100, 0, 100])
plt.plot(path.X, path.Y)
plt.scatter(check_ins.X, check_ins.Y, marker='o', color='green')
plt.scatter(stay_points.X, stay_points.Y, marker='x', color='red')
plt.axis([0, 100, 0, 100])

plt.show()