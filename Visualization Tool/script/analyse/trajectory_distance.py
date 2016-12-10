"""
Calculates a distance metric between two trajectories.

This resamples and pads out each trajectory so they're the same length.
It's good at finding trajectories that are very similar (i.e. for finding
groups), but not very good at comparing different trajectories, particularly
trajectories that start at different times.

The initialise function must be called first.
"""

import numpy as np
import data

# just added these so pycharm knows that they exist
all_ids = None
df = None
df2 = None


def initialise(day=None, type=None, dataframe=None):
    global all_ids, df, df2
    if dataframe is None:
        print('Reading data')
        df = data.read_data(day, type)
    else:
        df = dataframe
    print('Reorganising data')
    all_ids = df['id'].unique()
    # overwriting variable so the garbage collector can kick in, hopefully
    df2 = (
        # remove 'type' column, not needed here
        df.drop('type', 1)
        .set_index('Timestamp')
        .groupby('id')
        # does the resampling, and fill the gaps forward
        # replaces emplty values in the middle with the thing before
        .resample('15T', how='last', label='right', closed='right', fill_method='pad')
        .unstack(0)

        # -- different ways of padding data --

        # filling with 0 (seems ok, 0 is far enough away to penalise starting times without going overboard)
        .fillna(0)

        # # duplicating the first and last point (penalises for starting at different points, but perhaps too much)
        # .ffill()
        # .bfill()

        # # filling with 50 (a point near the middle, results in not as much penalty when a )
        # .fillna(50)

        # # filling with a large number (to penalise different starting times a lot).
        # # I think this weighs different starting times too much though
        # .fillna(1000)

        .swaplevel(0, 1, axis=1)
        .sort_index(axis=1)
    )


# TODO: optimise this better for comparing an id to every other id?
def get_distances(id, other_ids=None):
    return_list = True
    if other_ids is None:
        other_ids = all_ids
    elif not hasattr(other_ids, '__iter__'):  # add to a list if not already an iterable
        other_ids = [other_ids]
        return_list = False
    dists = []
    xy = df2.loc[:, id]
    for id2 in other_ids:
        dist = _get_trajectory_distance(xy, df2.loc[:, id2])
        dists.append(dist)
    if return_list:
        return dists
    else:
        return dists[0]


def _get_trajectory_distance(xy1, xy2):
    xy_dif = xy1 - xy2
    return np.hypot(xy_dif.X, xy_dif.Y).sum()
