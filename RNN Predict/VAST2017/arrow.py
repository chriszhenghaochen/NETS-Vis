import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.image as mpimg
import numpy as np

img=mpimg.imread('map.jpg')
plt.imshow(img, extent=[0,100,0,100])

#position dic
pos = pd.read_csv('key points.csv')[['x', 'y']].values

print(pos)

#io dic
io = pd.read_csv('Random Forest.csv').values


dic1 = {}
dic2 = {}


for i in range(len(pos)):
    dic1[i + 1] = pos[i]

print(dic1)


for row in io:
    key = str(int(row[0])) + ',' + str(int(row[1]))

    if key in dic2:
        dic2[key] += 1
    else:
        dic2[key] = 1

print(dic2)

plt.figure(1, figsize=(100,100))
ax = plt.subplot(111)

for k, v in dic2.items():
    x = k.split(',')[0]
    y = k.split(',')[1]

    if y != '0' and x != '0':
        start, end = dic1[int(x)], dic1[int(y)]
        print(start, end)
        x1, y1 = start[0], start[1]
        x2, y2 = end[0], end[1]
        ax.annotate("",
                    xy=(x1, y1), xycoords='data',
                    xytext=(x2, y2), textcoords='data',
                    size=v, va="center", ha="center",
                    arrowprops=dict(arrowstyle="simple",
                                    connectionstyle="arc3,rad=-0.2"),
                    )

#heat
# point = pd.read_csv('input.csv')['o'].astype('int').tolist()
#
# dic3 = {}
#
# for p in point:
#     if p != 0:
#         if p in dic3:
#             dic3[p] += 1
#         else:
#             dic3[p] = 1
#
# ks = dic3.keys()
# vs = dic3.values()
# kss = []
#
# for k in ks:
#     print(k)
#     kss.append(dic1[k].tolist)
#
# kss = np.asarray(kss)
# vc = np.asarray(vs)
# plt.scatter(kss[:, 0], kss[:, 1], s=100 * vs, color='red')

plt.show()
