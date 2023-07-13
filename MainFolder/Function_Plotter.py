import re
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

        self.input_gb = QtWidgets.QGroupBox("Input")
        self.func_le = QtWidgets.QLineEdit()
        self.xmin_le = QtWidgets.QLineEdit()
        self.xmax_le = QtWidgets.QLineEdit()

        input_layout = QtWidgets.QFormLayout()
        input_layout.addRow("Function f(x):", self.func_le)
        input_layout.addRow("X min:", self.xmin_le)
        input_layout.addRow("X max:", self.xmax_le)
        self.input_gb.setLayout(input_layout)

        self.plot_btn = QtWidgets.QPushButton("Plot")
        self.plot_btn.clicked.connect(self.plot_graph)

        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addWidget(self.input_gb)
        main_layout.addWidget(self.plot_btn)
        main_layout.addWidget(self.plot)

        self.central_widget = QtWidgets.QWidget()
        self.central_widget.setLayout(main_layout)
        self.setCentralWidget(self.central_widget)

        self.setWindowTitle("Function Plotter")

    def plot_graph(self):


        try:
            tmp = self.func_le.text()
            func_str=tmp.replace('^','**')
            x_min = float(self.xmin_le.text()) 
            x_max = float(self.xmax_le.text())


            if not re.match(r'^[0-9+\-*/^x()]+$', func_str):
                raise ValueError("Invalid function string")
            
            if (x_min>x_max):
                raise ValueError("min must be less than max")

            x = np.linspace(x_min, x_max)
            y = eval(func_str,{},{'x':x})
            

            self.plot.ax.clear()
            self.plot.ax.plot(x, y,color='red')
            self.plot.ax.set_xlabel('X')
            self.plot.ax.set_ylabel('Y')
            self.plot.ax.grid()
            self.plot.draw()

        except Exception as e:
            error_msg = str(e)
            print(error_msg)
            QtWidgets.QMessageBox.critical(self, "Error", error_msg)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow() 
    window.show()
    app.exec_()