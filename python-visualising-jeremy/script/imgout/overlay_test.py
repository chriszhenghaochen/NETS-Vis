import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import data

plt.ioff()
fig = plt.gcf()
fig.set_size_inches(20, 20)

# im = data.read_image()
# implot = plt.imshow(im, extent=[0, 100, 0, 100])

df = data.read_data('Fri')

for name, group in df.groupby('id'):
    x = group.loc[:, 'X']
    x = x + np.random.normal(0, 1, x.size)
    y = group.loc[:, 'Y']
    y = y + np.random.normal(0, 1, y.size)
    plt.plot(x, y, alpha=0.01, linewidth=0.1, color='black', rasterized=True)

plt.axis([0, 100, 0, 100])
plt.savefig('friday', bbox_inches='tight', dpi=100)
