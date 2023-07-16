import re
from PySide2 import QtWidgets
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
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

        self.toolbar = NavigationToolbar(self.plot, self)


        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addWidget(self.input_gb)
        main_layout.addWidget(self.plot_btn)
        main_layout.addWidget(self.toolbar)
        main_layout.addWidget(self.plot)
        

        self.central_widget = QtWidgets.QWidget()
        self.central_widget.setLayout(main_layout)
        self.setCentralWidget(self.central_widget)

        self.setWindowTitle("Function Plotter")

    def validate_func(self,func_str):
        
        if not re.match(r'^[0-9+\-*/^x()]+$', func_str):
            return -1
        return 0
    
    def validate_xlimit(self,xlimit):
        
        if not re.match(r'^\d+$', xlimit):
            return -1
        
        return 0
        

    def validate_input(self):
        try:
            tmp = self.func_le.text()
            func_str=tmp.replace('^','**')

            if self.validate_func(func_str)==-1:
                raise ValueError("Invalid function input")
            
            if  self.validate_xlimit(self.xmax_le.text())==-1:
                raise ValueError("Invalid input in Xmax")
            
            if self.validate_xlimit(self.xmin_le.text())==-1:
                raise ValueError("Invalid input in Xmin")
            
            x_min = float(self.xmin_le.text()) 
            x_max = float(self.xmax_le.text())


            if (x_min>x_max):
                raise ValueError("min must be less than max")
            
            return 0

        except Exception as e:
            error_msg = str(e)
            print(error_msg)
            QtWidgets.QMessageBox.critical(self, "Error", error_msg)
            return -1


    def plot_graph(self):
        
            if self.validate_input()==0:
                tmp = self.func_le.text()
                func_str=tmp.replace('^','**')
                x_min = float(self.xmin_le.text()) 
                x_max = float(self.xmax_le.text())


                x = np.linspace(x_min, x_max)
                y = eval(func_str)
            

                self.plot.ax.clear()
                self.plot.ax.plot(x, y)
                self.plot.ax.set_xlabel('X')
                self.plot.ax.set_ylabel('Y')
                self.plot.ax.grid()
                self.plot.draw()
            

        
import re
from PySide2 import QtWidgets
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
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

        self.toolbar = NavigationToolbar(self.plot, self)


        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addWidget(self.input_gb)
        main_layout.addWidget(self.plot_btn)
        main_layout.addWidget(self.toolbar)
        main_layout.addWidget(self.plot)
        

        self.central_widget = QtWidgets.QWidget()
        self.central_widget.setLayout(main_layout)
        self.setCentralWidget(self.central_widget)

        self.setWindowTitle("Function Plotter")

    def validate_func(self,func_str):

        if 'x' not in func_str:
            return -1 
        
        if not re.match(r'^[0-9+\-*/^x()]+$', func_str):
            return -1
        return 0
    
    def validate_xlimit(self,xlimit):

        if not re.match(r'^[+-]?\d+(\.\d+)?$', xlimit):
            return -1
        
        return 0
        

    def validate_input(self):
        try:
            tmp = self.func_le.text()
            func_str=tmp.replace('^','**')

            if self.validate_func(func_str)==-1:
                raise ValueError("Invalid function input")
            
            if self.validate_xlimit(self.xmin_le.text())==-1:
                raise ValueError("Invalid input in Xmin")
            
            if  self.validate_xlimit(self.xmax_le.text())==-1:
                raise ValueError("Invalid input in Xmax")
            
            x_min = float(self.xmin_le.text()) 
            x_max = float(self.xmax_le.text())


            if (x_min>x_max):
                raise ValueError("min must be less than max")
            
            return 0

        except Exception as e:
            error_msg = str(e)
            print(error_msg)
            QtWidgets.QMessageBox.critical(self, "Error", error_msg)
            return error_msg


    def plot_graph(self):
            e=self.validate_input()
            if e==0:
                tmp = self.func_le.text()
                func_str=tmp.replace('^','**')
                x_min = float(self.xmin_le.text()) 
                x_max = float(self.xmax_le.text())


                x = np.linspace(x_min, x_max)
                y = eval(func_str)
            

                self.plot.ax.clear()
                self.plot.ax.plot(x, y)
                self.plot.ax.set_xlabel('X')
                self.plot.ax.set_ylabel('Y')
                self.plot.ax.grid()
                self.plot.draw()
            

        

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow() 
    window.show()
    app.exec_()
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow() 
    window.show()
    app.exec_()