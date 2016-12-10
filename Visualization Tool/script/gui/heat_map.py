import sys
import random

from PyQt4 import QtGui, QtCore

import matplotlib
matplotlib.use('Qt4Agg')
import matplotlib.pyplot as plt

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

import data
import script.plot.heat_map as hm
from datetime import datetime, timedelta

class HeatMapWidget(QtGui.QWidget):

    def __init__(self):
        super(HeatMapWidget, self).__init__()

        self.im = data.read_image('Grey')

        self.init_ui()

    # ui
    def init_ui(self):
        # self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Heat Map')

        self.main_vbox = QtGui.QVBoxLayout()
        self.setLayout(self.main_vbox)

        self.init_matplotlib_ui()
        self.init_slider_ui()

        self.show()

    def init_matplotlib_ui(self):
        # matplotlib ui
        self.fig, self.ax = plt.subplots()
        self.fig.patch.set_color('#EEEEEE')
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self)
        self.mpl_toolbar = NavigationToolbar(self.canvas, self)

        self.main_vbox.addWidget(self.mpl_toolbar)
        self.main_vbox.addWidget(self.canvas)

    def init_slider_ui(self):
        # other ui
        self.slider = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        self.slider.valueChanged.connect(self.draw_heatmap)
        self.slider.setMaximum(1000)

        self.main_vbox.addWidget(self.slider)

    def draw_heatmap(self, input):
        input_float = input / 1000
        basetime = datetime(2014, 6, 6, 8)
        newtime = basetime + input_float * timedelta(hours=16)

        self.ax.clear()
        self.ax.imshow(self.im, extent=[0, 100, 0, 100])
        hm.plot_heatmap(newtime, ax=self.ax, type='scatter')
        self.ax.set_ylim([0, 100])
        self.ax.set_xlim([0, 100])
        self.ax.set_title(newtime)
        self.canvas.draw()


def main():
    app = QtGui.QApplication(sys.argv)
    widget = HeatMapWidget()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
