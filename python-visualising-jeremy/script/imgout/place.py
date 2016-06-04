import pandas as pd
import numpy as np
import data
import matplotlib.pyplot as plt

x_coord = 33
y_coord = 32

for day in ['Fri', 'Sat', 'Sun']:
    plt.figure(figsize=[12, 9])
    df = data.read_data(day).sort_values(by=['id', 'Timestamp'])
    df = df[(df.X.diff() != 0) | (df.Y.diff() != 0)]  # drop consecutive duplicates
    tdiff = df.Timestamp.diff().shift(-1)
    tdiff[df.id != df.id.shift(-1)] = pd.NaT
    tdiff /= np.timedelta64(1, 's')  # convert to seconds so it works nicer
    df['tdiff'] = tdiff

    at_point = df[(df.X == x_coord) & (df.Y == y_coord)]
    plt.hist(at_point.tdiff.values, bins=range(0, 70), edgecolor='none')
    plt.axis([0, 70, 0, 1200])
    plt.savefig('stop time at x={}, y={} {}.png'.format(x_coord, y_coord, day), bbox_inches='tight')