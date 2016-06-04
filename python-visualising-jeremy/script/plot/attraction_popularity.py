import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import data

im = data.read_image()

for (i, name) in enumerate(['Fri']):
    plt.figure()
    plt.imshow(im, extent=[0, 100, 0, 100])
    plt.title(name)

    df = data.read_data(name)
    freqs1 = df[df['type'] == 'check-in'].groupby(['X', 'Y']).size()
    (x1, y1) = zip(*freqs1.index.values)

    # not sure if this is the most efficient way, but it works
    df2 = df.sort_values(['id', 'Timestamp'])
    stay_points = df2[(df2.Timestamp.diff().shift(-1) > np.timedelta64(30, 's')) & (df2.id == df2.id.shift(-1))]
    freqs2 = stay_points.groupby(['X', 'Y']).size()
    (x2, y2) = zip(*freqs2.index.values)

    plt.scatter(x2, y2, s=0.1 * freqs2.values, color='blue')
    plt.scatter(x1, y1, s=0.1 * freqs1.values, color='red')
    # plt.scatter(x2, y2, marker='x', color='blue')

    plt.axis([0, 100, 0, 100])
plt.show()
