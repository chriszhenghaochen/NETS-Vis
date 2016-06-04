"""
Script to check the distances between members of each group.

The purpose of this is to check for false positives with grouping people.

Perhaps it could also check the distances between every group, to look for false negatives.
"""

import data
import itertools
import script.analyse.trajectory_distance as td
import matplotlib.pyplot as plt
import numpy as np
import os
import time
from datetime import timedelta
import script.plot.timecube as tc


def check_dist_within_group():
    for day in data.days:
        print('-- {} --'.format(day))
        td.initialise(day)
        groups = data.read_groups(day)
        max_max_dist = -1
        max_dist_group = -1
        dists = []
        for group_id, df in groups.groupby('group_id'):
            ids = df['id']
            max_dist = -1
            for id1, id2 in itertools.combinations(ids, 2):
                dist = td.get_distances(id1, id2)
                dists.append([group_id, dist])
                if dist > max_dist:
                    max_dist = dist
            if max_dist > max_max_dist:
                max_max_dist = max_dist
                max_dist_group = group_id
            # print('group {}: max dist = {}'.format(group_id, max_dist))
        print('max group dist: group {}, dist = {}'.format(max_dist_group, max_max_dist))
        dists = np.array(dists)

        fig, ax = plt.subplots()
        ax.scatter(dists[:, 0], dists[:, 1], lw=0)
        ax.set_title(day)
        ax.grid(linestyle='-', alpha=0.2)
        ax.yaxis.set_ticks_position('none')
        ax.xaxis.set_ticks_position('none')


def check_dist_between_groups(days=None):
    if days is None:
        days = data.days
    out_dir = os.path.join(data.data_out_path, 'group_dist/')
    os.makedirs(out_dir, exist_ok=True)
    for day in days:
        print('-- {} --'.format(day))
        t0 = time.clock()
        td.initialise(day)
        groups = data.read_group_typical_ids(day)
        n_groups = len(groups)
        dists = np.zeros([n_groups, n_groups])
        for i1, i2 in itertools.combinations(range(n_groups), 2):
            print('\r{}, {} / {}'.format(i1, i2, n_groups), end='')
            dist = td.get_distances(groups.iloc[i1]['id'], groups.iloc[i2]['id'])
            dists[i1, i2] = dist
            dists[i2, i1] = dist
        print('\nDone!')
        save_path = os.path.join(out_dir, day)
        np.save(save_path, dists)
        t1 = time.clock()
        print('Take Taken = {}'.format(timedelta(seconds=t1-t0)))

        fig, ax = plt.subplots()
        ax.pcolormesh(dists)
        ax.set_title(day)


def plot_dists(day='Fri'):
    df = data.read_data(day, grouped=True)
    dists = data.read_group_distances(day)

    # y, x = np.histogram(dists, 100)
    # plt.figure()
    # plt.bar(x[:-1], y, x[1]-x[0])
    #
    # plt.figure()
    # plt.pcolormesh(dists)
    #
    # plt.figure()
    # ix = np.indices(dists.shape)
    # plt.scatter(dists.flat, ix[0], s=2, lw=0)

    close_dists = np.unique(dists)
    for dist in close_dists[1:10]:
        matches = np.where(dists == dist)
        n_matches = len(matches)
        if n_matches > 2:
            print('More than 2 matches ({})'.format(n_matches))
        ids = np.where(dists == dist)[0]
        fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
        tc.plot_trajectories(ax=ax, df=df[df['group_id'].isin(ids)], id_str='group_id')
        ax.set_title('group {} & {}\ndistance = {}'.format(ids[0], ids[1], dist))


def main():
    # check_dist_between_groups(['Sun'])
    plot_dists('Sun')
    plt.show()


if __name__ == '__main__':
    main()

