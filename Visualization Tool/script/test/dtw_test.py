import data
import time
import dtw.dtw as dtw
from sklearn.metrics.pairwise import euclidean_distances
import matplotlib.pyplot as plt


print('Reading data')
df = data.read_data('Fri', 'subset-100')
print('Rearranging/Resampling data')
ids = df['id'].unique()
path1 = df[df['id'] == ids[0]].set_index('Timestamp')
path2 = df[df['id'] == ids[1]].set_index('Timestamp')


def get_xy(path, sample_minutes):
    return (
        path.resample('{}T'.format(sample_minutes), how='last',
                      label='right', closed='right', fill_method='pad')
        .loc[:, ['X', 'Y']]
        .values
        .reshape((-1, 1, 2))
    )

distances = []
times = []
time_gaps = []
for i in [60, 30, 15, 13, 10, 9, 8, 7, 6, 5]:
    for j in range(3):
        xy1 = get_xy(path1, i)
        xy2 = get_xy(path2, i)

        print('Calculating dtw for t = {} minutes (loop {})'.format(i, j))
        t0 = time.clock()
        dist, cost, acc, path = dtw.dtw(xy1, xy2, euclidean_distances)
        t1 = time.clock()

        print('Took {} seconds'.format(t1-t0))
        times.append(t1-t0)
        distances.append(dist)
        time_gaps.append(i)

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.scatter(time_gaps, times)
ax2.scatter(time_gaps, distances)
ax1.grid()
ax2.grid()
plt.show()