"""
A quick GUI program for examining an id

Could be expanded in the future (maybe when I learn how to use qt better)
"""

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

import matplotlib
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

import script.plot.timecube as tc


class IdWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.fig = Figure()
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self)
        self.axes = self.fig.add_subplot(111)
        self.mpl_toolbar = NavigationToolbar(self.canvas, self)

        self.label = QLabel('ID')
        self.text_field = QLineEdit()
        self.button = QPushButton('Go')

        ui_hbox = QHBoxLayout()
        ui_hbox.addWidget(self.label)
        ui_hbox.addWidget(self.text_field)
        ui_hbox.addWidget(self.button)

        vbox = QVBoxLayout()
        vbox.addWidget(self.mpl_toolbar)
        vbox.addWidget(self.canvas)
        vbox.addLayout(ui_hbox, 0)
        self.setLayout(vbox)


def main():
    app = QApplication(sys.argv)

    w = IdWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()