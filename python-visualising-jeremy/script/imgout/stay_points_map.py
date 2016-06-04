import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import data


def plot_stay_points(df, stop_time):
    stay_points = df[(df.Timestamp.diff().shift(-1) >= np.timedelta64(stop_time, 's')) & (df.id == df.id.shift(-1))]
    # stay_points = df[(df.Timestamp.diff().shift(-1) == np.timedelta64(stop_time, 's')) & (df.id == df.id.shift(-1))]
    freqs2 = stay_points.groupby(['X', 'Y']).size()
    (x2, y2) = zip(*freqs2.index.values)
    plt.scatter(x2, y2, s=0.1 * freqs2.values, color='blue')
    plt.axis([0, 100, 0, 100])
    plt.title("t = {} s".format(stop_time))


def main():
    im = data.read_image()
    df = data.read_data('Fri').sort_values(by=['id', 'Timestamp'])
    for i in range(25, 40):
        plt.figure(figsize=[12, 9])
        plt.imshow(im, extent=[0, 100, 0, 100])
        plot_stay_points(df, i)
        plt.savefig('stop time {} s.png'.format(i), bbox_inches='tight')

if __name__ == '__main__':
    main()
