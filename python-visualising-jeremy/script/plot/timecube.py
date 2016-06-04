import data
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import numpy as np
from datetime import datetime
import PIL.Image as Image
import itertools

image = Image.open(data.get_image_path('Light'))
# image = image.resize((500, 500))
image = image.resize((100, 100))
im = np.asarray(image) / 255
im_x, im_y = np.ogrid[0:im.shape[0], 0:im.shape[1]]


def plot_map(ax, z):
    ax.plot_surface(im_y, 100 - im_x, z, rstride=1, cstride=1, facecolors=im, shade=False)


def plot_trajectories(df, ax=None, colors=None, show_map=False, id_str='id', line_kw=None):
    if colors is None:
        colors = data.palette10
    elif isinstance(colors, str):
        colors = [colors]
    elif not hasattr(colors, "__iter__"):
        # convert single item to a list
        colors = [colors]
    if ax is None:
        ax = plt.subplot(projection='3d')
    if line_kw is None:
        line_kw = {}

    # just so we don't create the extra 'z' field.
    df = df.copy()

    first_time = df['Timestamp'].min()
    first_day = pd.Timestamp(datetime(first_time.year, first_time.month, first_time.day))
    df['Z'] = (df['Timestamp'] - first_day) / np.timedelta64(1, 's')

    for (name, group), color in zip(df.groupby(id_str), itertools.cycle(colors)):
        ax.plot(group['X'].values, group['Y'].values, group['Z'].values, c=color, **line_kw)#, marker='o', mew=0, ms=4, mfc='black')
    ax.zaxis.set_major_formatter(data.timedelta_formatter)
    ax.set_zlim([df['Z'].min(), df['Z'].max()])

    if show_map:
        plot_map(ax, df['Z'].min())


def main():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    df = data.read_data('Fri', 'subset-300')
    # df = df[(df.id % 3) == 0]
    p_id = 391338
    path = df[df['id'] == p_id]
    # plot_trajectories(ax=ax, df=path, show_map=True, colors='#2FB787', line_kw=dict(lw=2))
    plot_trajectories(ax=ax, df=path, show_map=True, line_kw=dict(lw=2))

    # for angle in range(0, 360, 10):
    #     print(angle)
    #     ax.view_init(30, angle)
    #     plt.savefig('Data61 angle {}.png'.format(angle), bbox_inches='tight')

    plt.show()

if __name__ == '__main__':
    main()