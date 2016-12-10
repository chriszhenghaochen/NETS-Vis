import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import data


def plot_key_points(ax):
    palette = data.palette20
    df = data.read_key_points()
    for i, (name, group) in enumerate(df.groupby(by='category', sort=False)):
        # the colour input has some issues here when the size is three
        ax.scatter(group.X, group.Y, s=100, c=palette[i], label=name, lw=0)
    ax.legend(loc='lower left', scatterpoints=1, ncol=2, fontsize=8)


def main():
    im = data.read_image('Grey')

    fig, ax = plt.subplots(1, 1)
    ax.imshow(im, extent=[0, 100, 0, 100])
    plot_key_points(ax)
    plt.show()

if __name__ == '__main__':
    main()