import data
import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib


dfs = []
for day in ['Fri', 'Sat', 'Sun']:
    dfday = data.read_data(day, 'key-points').set_index('Timestamp')
    dfs += [dfday]
df = pd.concat(dfs)
totals = data.get_attraction_totals()
kp = data.read_key_points().set_index('place_id')


def get_category_ids(categories):
    return kp[kp.category.isin(categories)].index


def plot_scatter(place_ids, ax, types=None, alpha=0.5, size=10, palette=None, margin=0.04):
    if types is None:
        types = ['start']
    if palette is None:
        palette = data.palette20
    ax.autoscale(True)
    ax.grid(linestyle='-', alpha=0.2)
    for place_id, color in zip(place_ids, palette):
        df2 = df[df['place_id'] == place_id]
        ts = df2['timespan']
        y = ts.values
        xmin = ts.index.to_pydatetime()
        xmax = (ts.index + (y * np.timedelta64(1, 's'))).to_pydatetime()
        if 'lines' in types:
            ax.hlines(y, xmin, xmax, color=color, alpha=0.5 * alpha)
        if 'start' in types:
            ax.scatter(xmin, y, s=size, color=color, alpha=alpha, linewidth=0)
        if 'end' in types:
            ax.scatter(xmax, y, s=size, color=color, alpha=alpha, linewidth=0)
            # ts.plot(ax=ax, style='.', color='black', alpha=0.5)
    ax.yaxis.set_major_formatter(data.timedelta_formatter)
    if 'lines' in types or ('start' in types and 'end' in types):
        ax.set_xlabel('Times spent at attraction')
    elif 'start' in types:
        ax.set_xlabel('Time of arrival')
    else:
        ax.set_xlabel('Time of departure')
    ax.set_ylabel('Length of visit')
    ax.margins(margin, margin)


def plot_stacked_area(place_ids, ax, palette=None):
    if palette is None:
        palette = data.palette20
    ts = pd.date_range('2014-06-06 08:00:00', '2014-06-08 23:55:00', freq='1T')
    df2 = (
        # filter out any ids that aren't in place_ids
        totals.loc[totals['place_id'].isin(place_ids)]
            .set_index(['place_id', 'Timestamp'])
            .unstack(0)
            .reindex(ts)
            .fillna(0)
            .loc[:, 'total']
    )
    ax.grid(linestyle='-', alpha=0.2)
    ax.autoscale(True)
    ax.stackplot(ts, df2.transpose(), linewidth=0, colors=palette)
    ax.set_xlabel('Time')
    ax.set_ylabel('Total occupants')


def add_legend(place_ids, ax, font_size=8, palette=None):
    if palette is None:
        palette = data.palette20
    # reverse the order so it matches the stack plot
    # probably not that efficient, but this will only be done with a few items so that's ok
    names = kp.loc[list(reversed(place_ids)), 'name']
    patches = [mpatches.Patch(color=palette[i % len(palette)]) for i in reversed(range(len(place_ids)))]
    ax.legend(patches, names, loc='upper left', prop={'size': font_size})


def main():
    fig, ax = plt.subplots(2, 1)
    # fig, ax = plt.subplots(1, 1)

    plot_scatter([32], ax[0], ['end', 'lines'])
    add_legend([32], ax[0])
    ax[0].set_title(kp.loc[32, 'name'])

    food_ids = get_category_ids(['Food'])
    plot_scatter(food_ids, ax[1])
    add_legend(food_ids, ax[1])
    ax[1].set_title('Category = Food')

    plt.show()


if __name__ == '__main__':
    main()
