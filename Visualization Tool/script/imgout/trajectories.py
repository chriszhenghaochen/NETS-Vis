import matplotlib.pyplot as plt
import data

df = data.read_data()

plt.ioff()

df2 = df.sort_values(by=['id', 'Timestamp'])
ids = df2['id'].unique().tolist()

for i in ids:
    plt.cla()
    plt.clf()
    path = df2.loc[df2.id == i]
    x = path.loc[:, 'X']
    y = path.loc[:, 'Y']
    plt.plot(x, y, alpha=0.7, linewidth=1, color='black', rasterized=True)
    plt.axis([0, 100, 0, 100])
    plt.savefig('trajectory{0:07d}.png'.format(i), bbox_inches='tight')

