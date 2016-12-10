"""
Little script that draws two trajectories at a time.

Used to quickly find matching trajectories.
"""

import data
import matplotlib.pyplot as plt
import script.plot.timecube as tc
import itertools

df = data.read_data('Fri', 'subset-100')
ids = df['id'].unique()

for id1, id2 in itertools.combinations(ids, 2):
    fig, ax = plt.subplots(1, 1, subplot_kw={'projection':'3d'})
    df2 = df[df['id'].isin([id1, id2])]

    tc.plot_trajectories(ax=ax, df=df2)
    plt.title('id {} and id {}'.format(id1, id2))
    plt.show()