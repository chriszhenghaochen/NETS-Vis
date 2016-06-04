import data
import numpy as np
from sklearn import manifold, datasets
from time import time
import matplotlib.pyplot as plt
from time import time
import os

labels = ['LLE', 'Isomap', 'MDS', 'TSNE', 'SpectralEmbedding']

n_neighbors = 10
n_components = 2
fitters = [
    manifold.LocallyLinearEmbedding(n_neighbors, n_components, eigen_solver='auto', method='standard'),
    manifold.Isomap(n_neighbors, n_components),
    manifold.MDS(n_components, max_iter=100, n_init=1),
    manifold.TSNE(n_components=n_components, init='pca', random_state=0),
    manifold.SpectralEmbedding(n_components=n_components, n_neighbors=n_neighbors)
]


def main():
    for day in ['Fri', 'Sat', 'Sun']:
        print('{sep} Day: {day} {sep}'.format(day=day, sep=15*'='))
        for data_name in ['category_freqs', 'category_timespans']:
            print('{sep} Type: {type} {sep}'.format(type=data_name, sep=5*'-'))
            df = data.read_matrix(day, data_name)
            x = np.array(df)
            ys = {}

            # fig, ax = plt.subplots(2, 3)
            # ax = ax.ravel()

            for fitter, label in zip(fitters, labels):
                t0 = time()
                try:
                    y = fitter.fit_transform(x)
                except AssertionError:
                    y = None
                t1 = time()
                ys[label] = y
                print('{} took {} seconds'.format(label, t1 - t0))
                # if y is not None:
                #     ax[i].scatter(y[:, 0], y[:, 1], linewidths=0, c='black', alpha=0.5)

            path = os.path.join(data.data_out_path, 'manifold/{}_{}'.format(data_name, day))
            np.savez(path, **ys)

if __name__ == '__main__':
    main()