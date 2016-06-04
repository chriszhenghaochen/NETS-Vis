"""
Creates a plot for checking how effective the distance metric is for grouping similar trajectories
"""

import sys
import numpy as np
import matplotlib.pyplot as plt
import script.analyse.trajectory_distance as td
import script.plot.timecube as tc


def plot_random_dists():
    """
    Plots the distance of a random person to all other people
    """
    global dists
    global random_xs
    global id
    global annotations
    id = np.random.choice(td.all_ids)
    dists = td.get_distances(id)
    random_xs = np.random.uniform(size=len(dists))
    annotations = []
    ax.scatter(random_xs, dists, c='blue', lw=0, picker=True)
    ax.set_title('id {}'.format(id))
    ax.set_xlim([-0.1, 1.1])
    ax.set_ylabel('Distance')
    ax.margins(y=.1)
    ax.grid(linestyle='-', alpha=0.2)
    # turn off x axis ticks and grid lines (nothing meaningful here)
    ax.xaxis.set_major_locator(plt.NullLocator())
    # get rid of the ticks, just show the lines
    ax.yaxis.set_ticks_position('none')


def on_key_press(event):
    sys.stdout.flush()
    if event.key == 'r':
        ax.clear()
        ax3d.clear()
        plot_random_dists()
        fig.canvas.draw()


def on_pick(event):
    for an in annotations:
        an.remove()
    annotations.clear()
    for index in event.ind:
        x = random_xs[index]
        y = dists[index]
        an = ax.annotate(
            td.all_ids[index],
            xy=(x, y), xytext=(-20, 20),
            textcoords='offset points', ha='right', va='bottom',
            bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),
            arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))
        annotations.append(an)
    fig.canvas.draw()


def on_click(event):
    if event.inaxes is not ax:
        return
    cutoff = event.ydata
    ax.lines.clear()
    ax.plot([0, 1], [cutoff, cutoff], color='red', lw=2)
    ids_below = [id for i, id in enumerate(td.all_ids) if dists[i] <= cutoff]
    ax3d.clear()
    tc.plot_trajectories(ax=ax3d, df=td.df[td.df['id'].isin(ids_below)])
    ax3d.set_title('{0} trajectories.\nCutoff = {1:.2f}'.format(len(ids_below), cutoff))
    fig.canvas.draw()


td.initialise(day='Fri')

# initialise display
fig = plt.figure()
ax = fig.add_subplot(1, 2, 1)
ax3d = fig.add_subplot(1, 2, 2, projection='3d')
fig.canvas.mpl_connect('key_press_event', on_key_press)
fig.canvas.mpl_connect('pick_event', on_pick)
fig.canvas.mpl_connect('button_release_event', on_click)
fig.patch.set_color('#EEEEEE')

# plot a random person
plot_random_dists()

plt.show()