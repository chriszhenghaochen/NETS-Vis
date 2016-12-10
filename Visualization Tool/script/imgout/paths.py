import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os

filepath = 'C:/Users/jswanson/Documents/vast_to_student/data/MC1 Data June 2015 V3'

df = pd.read_csv(os.path.join(filepath, 'park-movement-Fri-FIXED-2.0.csv'))

plt.ioff()

for hour in range(8, 24):
    for minute in range(0, 60, 20):
        hour_string = '2014-6-06 {0:02d}:{1:02d}:00'.format(hour, minute)
        next_hour_string = '2014-6-06 {0:02d}:{1:02d}:00'.format(hour, minute + 20)
        df2 = df[(df.Timestamp >= hour_string) & (df.Timestamp < next_hour_string)]
        df2 = df2.sort_values(by=['id', 'Timestamp'])
        ids = df2['id'].unique().tolist()

        plt.cla()
        plt.clf()
        for i in ids:
            path = df2.loc[df2.id == i]
            x = path.loc[:, 'X'] + np.random.normal(0, 0.2)
            y = path.loc[:, 'Y'] + np.random.normal(0, 0.2)
            plt.plot(x, y, alpha=0.01, linewidth=1, color='black', rasterized=True)

        plt.axis([0, 100, 0, 100])
        plt.savefig('plot{0:02d}-{1:02d}.png'.format(hour, minute), bbox_inches='tight')
