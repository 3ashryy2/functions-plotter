from PySide2 import QtWidgets
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import numpy as np

class PlotWidget(FigureCanvasQTAgg):

    def __init__(self, parent=None):
        fig, self.ax = plt.subplots(figsize=(5, 4), dpi=150)
        super().__init__(fig)

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.plot = PlotWidget(self)
        self.plot.ax.plot([1,2,3,4,5],[1,2,3,4,5],color='red')

        self.plot_btn = QtWidgets.QPushButton("Plot")
        self.plot_btn.clicked.connect(self.show())
        

        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addWidget(self.plot_btn)
        main_layout.addWidget(self.plot)

        self.central_widget = QtWidgets.QWidget()
        self.central_widget.setLayout(main_layout)
        self.setCentralWidget(self.central_widget)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow() 
    window.show()
    app.exec_()
