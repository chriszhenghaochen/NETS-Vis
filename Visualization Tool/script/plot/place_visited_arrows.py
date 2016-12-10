import data
import numpy as np
import matplotlib.pyplot as plt

kp = data.read_visited_key_points('Fri', extra=['X', 'Y'], grouped=True)
groups = data.read_group_info('Fri')

# the group that visited the least things
shortest_group = kp.groupby('group_id').size().argmin()
# the group that visited the most things
longest_group = kp.groupby('group_id').size().argmax()
# the largest group
largest_group = groups['size'].argmax()

df = kp[kp['group_id'] == longest_group]

im = data.read_image('grey')
plt.imshow(im, extent=[0, 100, 0, 100])

cmap = plt.get_cmap('rainbow')
for i in range(len(df) - 1):
    amt = i / (len(df) - 2)
    color = np.array(cmap(amt))
    color[:-1] *= 0.8
    prev = df.iloc[i]
    next = df.iloc[i + 1]
    # tdiff = next.Timestamp - prev.Timestamp
    # size = 0.001 * (tdiff / np.timedelta64(1, 's'))
    # text = '{} -> {}'.format(prev.place_id, next.place_id)
    arrowprops = {'arrowstyle': 'simple',
                  # 'mutation_scale': size,
                  'lw': 0,
                  'color': color,
                  'connectionstyle': "arc3,rad=-0.1"}

    plt.annotate('', xy=(next.X, next.Y), xytext=(prev.X+0.01, prev.Y+0.01), arrowprops=arrowprops)

plt.show()