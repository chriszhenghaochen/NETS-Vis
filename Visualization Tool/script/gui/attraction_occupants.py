import sys
import random

from PyQt4 import QtGui

import matplotlib
matplotlib.use('Qt4Agg')
import matplotlib.pyplot as plt

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

import data
from script.plot.place_occupants import *


def get_random_name():
    adjectives = ['cool', 'great', 'fun', 'scary', 'new', 'gooey',
                  'yummy', 'powerful', 'green', 'red', 'blue']
    types = ['place', 'ride', 'restaurant', 'stadium', 'show']
    adjective = random.choice(adjectives)
    type = random.choice(types)
    return "{adj}, {adj} {type}".format(adj=adjective, type=type)


class MainWidget(QtGui.QWidget):

    def __init__(self):
        super(MainWidget, self).__init__()

        # categories = ['category {}'.format(i) for i in range(1, 10)]
        # attractions = ['[{}] {}'. format(i, self.get_random_name()) for i in range(1, 100)]
        self.categories = kp.category.unique()
        self.attractions = kp.index.astype(str) + ' - ' + kp['name'].astype(str)

        # state variables
        self.category_or_ride = 'category'
        self.selected_category = -1
        self.selected_ride = -1
        self.show_start_points = True
        self.show_lines = False
        self.show_end_points = False

        self.init_ui()

    # qt slots
    def set_selected_category(self, category_index):
        category = self.categories[category_index]
        should_update = False
        if self.category_or_ride != 'category':
            should_update = True
        self.category_or_ride = 'category'
        if self.selected_category != category:
            self.selected_category = category
            should_update = True
        if should_update:
            self.update_plot()

    def set_selected_ride(self, ride_index):
        # note, ride_index is based on the position of the ride in the sorted list
        ride_id = kp.index[ride_index]
        should_update = False
        if self.category_or_ride != 'ride':
            should_update = True
        self.category_or_ride = 'ride'
        if self.selected_ride != ride_id:
            self.selected_ride = ride_id
            should_update = True
        if should_update:
            self.update_plot()

    def set_show_start_points(self, value):
        if self.show_start_points != value:
            self.show_start_points = value
            self.update_plot()

    def set_show_lines(self, value):
        if self.show_lines != value:
            self.show_lines = value
            self.update_plot()

    def set_show_end_points(self, value):
        if self.show_end_points != value:
            self.show_end_points = value
            self.update_plot()

    # ui
    def init_ui(self):
        # self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Layout Test')

        self.main_vbox = QtGui.QVBoxLayout()
        self.setLayout(self.main_vbox)

        self.init_matplotlib_ui()
        self.init_options_ui()

        self.show()

    def init_matplotlib_ui(self):
        # matplotlib ui
        self.fig, self.axs = plt.subplots(2, 1, True)
        self.fig.patch.set_color('#EEEEEE')
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self)
        self.mpl_toolbar = NavigationToolbar(self.canvas, self)

        self.main_vbox.addWidget(self.mpl_toolbar)
        self.main_vbox.addWidget(self.canvas)

    def init_options_ui(self):
        # other ui
        self.options_hbox = QtGui.QHBoxLayout()
        # combobox
        combo_vbox = QtGui.QVBoxLayout()

        cat_combobox = QtGui.QComboBox()
        cat_combobox.addItems(self.categories)
        cat_combobox.activated.connect(self.set_selected_category)
        combo_vbox.addWidget(cat_combobox)

        attraction_combobox = QtGui.QComboBox()
        attraction_combobox.addItems(self.attractions)
        attraction_combobox.activated.connect(self.set_selected_ride)
        combo_vbox.addWidget(attraction_combobox)

        self.options_hbox.addLayout(combo_vbox, 1)

        # checkboxes
        check_vbox = QtGui.QVBoxLayout()

        checkbox_labels = ['start points', 'lines', 'end points']
        checkboxes = []
        for label in checkbox_labels:
            checkbox = QtGui.QCheckBox(label)
            # checkbox.setChecked(getattr(self, variable))
            # checkbox.stateChanged.connect(set_plot_parameter)
            checkboxes.append(checkbox)
            check_vbox.addWidget(checkbox)
        checkboxes[0].setChecked(self.show_start_points)
        checkboxes[0].stateChanged.connect(self.set_show_start_points)
        checkboxes[1].setChecked(self.show_lines)
        checkboxes[1].stateChanged.connect(self.set_show_lines)
        checkboxes[2].setChecked(self.show_end_points)
        checkboxes[2].stateChanged.connect(self.set_show_end_points)

        self.options_hbox.addLayout(check_vbox, 0)
        self.main_vbox.addLayout(self.options_hbox)

    def update_plot(self):
        print('-- Update! --')
        if self.category_or_ride == 'category':
            print('Plotting category {}'.format(self.selected_category))
        else:
            print('Plotting ride {}'.format(self.selected_ride))

        if self.show_start_points:
            print('with start points')
        if self.show_lines:
            print('with lines')
        if self.show_end_points:
            print('with end points')
        print()

        types = []
        if self.show_start_points:
            types.append('start')
        if self.show_lines:
            types.append('lines')
        if self.show_end_points:
            types.append('end')

        for ax in self.axs:
            ax.clear()
        if len(types) > 0:
            if self.category_or_ride == 'category':
                ids = get_category_ids([self.selected_category])
            else:
                ids = [self.selected_ride]

            # if len(ids) > 10:
            #     palette = data.palette20
            # else:
            #     palette = data.palette10
            palette = data.palette20

            plot_stacked_area(ids, self.axs[0], palette=palette)
            plot_scatter(ids, self.axs[1], types, palette=palette)

            for ax in self.axs:
                add_legend(ids, ax, palette=palette)
            self.fig.tight_layout()
        self.canvas.draw()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = MainWidget()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()