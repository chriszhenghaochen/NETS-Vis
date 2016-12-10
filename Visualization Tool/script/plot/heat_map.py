import data
from datetime import datetime
import matplotlib.pyplot as plt

totals = data.read_position_totals()


def plot_heatmap(time, type='heatmap', ax=None, alpha=1):
    if ax is None:
        fig, ax = plt.subplots()

    time2 = time.replace(second=0, microsecond=0)

    place_totals = totals[totals['Timestamp'] == time2]
    if type == 'heatmap':
        matrix = (
            place_totals.set_index(['X', 'Y'])
            .loc[:, 'total']
            .unstack(0)
            .reindex(index=list(reversed(range(100))), columns=range(100))
            .fillna(0)
        )
        ax.imshow(matrix.values, extent=[0, 100, 0, 100], interpolation='nearest', alpha=alpha, origin='upper')
    elif type == 'scatter':
        ax.scatter(x=place_totals['X'], y=place_totals['Y'], s=place_totals['total'], lw=0, alpha=1)


def main():
    time = datetime(2014, 6, 6, 12)
    plot_heatmap(time)
    plt.show()


if __name__ == '__main__':
    main()
