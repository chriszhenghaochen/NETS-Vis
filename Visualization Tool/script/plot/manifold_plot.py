import data
import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from mpl_toolkits.mplot3d import Axes3D
import PIL.Image as Image
import colormaps as cm

timecube = True
z_min = 0


def draw(axs):
    for ax, (name, item) in zip(axs, files.items()):
        ax.clear()
        try:
            ax.scatter(item[:, 0], item[:, 1], c=c, cmap=cm.viridis, linewidth=0, alpha=0.5, picker=2)
        except IndexError:
            pass
        ax.set_title(name)


def draw_paths(ind):
    global z_min
    ids = all_ids[ind]
    map_ax.clear()
    if len(ind) > 0:
        if timecube:
            z_min = np.Infinity
            for name, group in df[df['id'].isin(ids)].groupby('id'):
                g2 = group.sort_values('Timestamp')
                x = g2['X'].values.astype('float64')
                y = g2['Y'].values.astype('float64')
                z = g2['Timestamp'] - pd.Timestamp(datetime(2014, 6, 6, 8))
                z = z / np.timedelta64(1, 's')
                zm = z.min()
                if zm < z_min:
                    z_min = zm
                x += np.random.normal(0, 0.1, x.size)
                y += np.random.normal(0, 0.1, y.size)
                map_ax.plot(xs=x, ys=y, zs=z.values)
        else:
            for name, group in df[df['id'].isin(ids)].groupby('id'):
                g2 = group.sort_values('Timestamp')
                x = g2['X'].values.astype('float64')
                y = g2['Y'].values.astype('float64')
                x += np.random.normal(0, 0.1, x.size)
                y += np.random.normal(0, 0.1, y.size)
                map_ax.plot(x, y, alpha=0.5)
    draw_map_image()
    map_ax.set_title('Paths for ids {}'.format(ids))


def draw_map_image():
    if timecube:
        pass
        # this is way too slow, skip it
        # map_ax.plot_surface(im_x, im_y, z_min, rstride=1, cstride=1, facecolors=im)
    else:
        map_ax.imshow(im, extent=[0, 100, 0, 100])


def on_pick(event):
    # print('pick')
    c.fill(0)
    c[event.ind] = 1
    draw(axs)
    draw_paths(event.ind)
    fig.canvas.draw()

if timecube:
    image = Image.open(data.get_image_path())
    image = image.resize((100, 100))
    im = np.asarray(image) / 255
    im_x, im_y = np.ogrid[0:im.shape[0], 0:im.shape[1]]
else:
    im = data.read_image()

files = data.read_manifold('Fri', 'category_timespans')
c = np.zeros(len(files.items()[0][1]), 'int64')
df = data.read_data('Fri')
all_ids = df['id'].unique()
all_ids.sort()

gs = gridspec.GridSpec(3, 3, width_ratios=[2, 1, 1])
fig = plt.figure()
if timecube:
    map_ax = fig.add_subplot(gs[:, 0], projection='3d')
    map_ax.view_init(10, 30)
else:
    map_ax = fig.add_subplot(gs[:, 0])
draw_map_image()
if timecube:
    map_ax.set_zlim(0, 100)

axs = []
for i in range(5):
    col = (i % 2) + 1
    row = i // 2
    ax = fig.add_subplot(gs[row, col])
    axs += [ax]
draw(axs)
fig.canvas.mpl_connect('pick_event', on_pick)
plt.show()