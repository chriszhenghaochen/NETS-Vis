import script.plot.timecube as tc
import data
import matplotlib.pyplot as plt


def plot_group(day=None, group_id=0, ax=None, df=None):
    if df is None:
        df = data.read_data(day)
    groups = data.read_groups(day)
    ids = groups.loc[groups['group_id'] == group_id, 'id']
    if ax is None:
        fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
    tc.plot_trajectories(ax=ax, df=df[df['id'].isin(ids)])
    return ax


def main():
    # plot_group(day='Fri', group_id=0)
    sus_groups = {
        'Fri': [70,
                404,
                467,
                502,
                960],
        'Sat': [1,
                81,
                456,
                1296,
                1308,
                1384,
                1498,
                1554,
                ],
        'Sun': [605,
                1046,
                1489,
                1764,
                1923,
                2180]
    }
    for day, group_ids in sus_groups.items():
        print('-- {} --'.format(day))
        df = data.read_data(day)
        for group_id in group_ids:
            ax = plot_group(day=day, group_id=group_id, df=df)
            ax.set_title('{} Group {}'.format(day, group_id))

    plt.show()


if __name__ == '__main__':
    main()