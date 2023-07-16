import re
from PySide2 import QtWidgets
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
import numpy as np

class PlotWidget(FigureCanvasQTAgg):
    """
    A matplotlib-based widget for displaying plots.

    This widget handles creating the matplotlib figure and axes, 
    and drawing the plot onto the canvas.
    """

    def __init__(self, parent=None):
        """
        Initialize the plot widget.

        Parameters:
        parent (QWidget) - The parent widget
        """
        # Create matplotlib figure and axes
        fig, self.ax = plt.subplots(figsize=(5, 4), dpi=150)
        
        # Call superclass init
        super().__init__(fig) 

        # Set the figure canvas to the widget
        self.setParent(parent)

class MainWindow(QtWidgets.QMainWindow):
    """
    The main application window.

    This class handles the GUI and plotting functionality.
    """

    def __init__(self):
        """
        Initialize the main window.
        
        Create and arrange the GUI elements, including:
        - Input group box
        - Function line edit
        - Xmin/Xmax line edits
        - Plot button
        - Matplotlib toolbar 
        - Plot widget 
        """
        super().__init__()

        # Create plot widget
        self.plot = PlotWidget(self)  

        # Create input group box
        self.input_gb = QtWidgets.QGroupBox("Input")
        self.func_le = QtWidgets.QLineEdit()
        self.xmin_le = QtWidgets.QLineEdit()
        self.xmax_le = QtWidgets.QLineEdit()

        # Arrange input elements vertically
        input_layout = QtWidgets.QFormLayout()
        input_layout.addRow("Function f(x):", self.func_le)
        input_layout.addRow("X min:", self.xmin_le)
        input_layout.addRow("X max:", self.xmax_le)
        self.input_gb.setLayout(input_layout)

        # Add plot button
        self.plot_btn = QtWidgets.QPushButton("Plot")
        self.plot_btn.clicked.connect(self.plot_graph)

        # Create navigation toolbar 
        self.toolbar = NavigationToolbar(self.plot, self)  

        # Arrange GUI elements vertically 
        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addWidget(self.input_gb)
        main_layout.addWidget(self.plot_btn)
        main_layout.addWidget(self.toolbar)
        main_layout.addWidget(self.plot)

        # Set central widget
        self.central_widget = QtWidgets.QWidget()
        self.central_widget.setLayout(main_layout)
        self.setCentralWidget(self.central_widget)

        # Set window title
        self.setWindowTitle("Function Plotter")

    def validate_func(self, func_str):
        """
        Validate the input function string.

        Checks that:
        - The string contains 'x' 
        - Contains only valid characters

        Parameters:
        func_str (str) - The function string

        Returns:
        0 if valid, -1 if invalid
        """
        # Function must contain x
        if 'x' not in func_str:
            return -1 
        
        # Check for valid characters
        if not re.match(r'^[0-9+\-*/^x]+$', func_str):
            return -1
        return 0
    
    def validate_xlimit(self, xlimit):
        """
        Validate the x-limit input string.

        Checks that string contains a valid floating point number.

        Parameters:
        xlimit (str) - The x-limit string

        Returns:
        0 if valid, -1 if invalid
        """
        # Use a regex to check for valid floating point string
        if not re.match(r'^[+-]?\d+(\.\d+)?$', xlimit):
            return -1
        
        return 0

    def validate_input(self):
        """
        Validate the input function and x-limits.

        Checks that:
        - Function input is valid
        - Xmin and Xmax are valid
        - Xmin < Xmax

        Returns:
        0 if valid, error message string if invalid
        """
        try:
            # Replace ^ with **
            tmp = self.func_le.text()  
            func_str = tmp.replace('^','**')

            # Validate function
            if self.validate_func(func_str)==-1:
                raise ValueError("Invalid function input")
            
            # Validate Xmin
            if self.validate_xlimit(self.xmin_le.text())==-1:
                raise ValueError("Invalid input for Xmin")
            
            # Validate Xmax
            if self.validate_xlimit(self.xmax_le.text())==-1:
                raise ValueError("Invalid input for Xmax")
            
            # Convert to float
            x_min = float(self.xmin_le.text())
            x_max = float(self.xmax_le.text())

            # Check min less than max
            if x_min >= x_max:
                raise ValueError("Xmin must be less than Xmax")
            
            # Input is valid
            return 0

        except Exception as e:
            # Return error message
            error_msg = str(e)
            print(error_msg)
            QtWidgets.QMessageBox.critical(self, "Error", error_msg)
            return error_msg

    def plot_graph(self):
        """
        Plot the function with the given x-limits.
        """
        # Validate input
        err = self.validate_input()
        if err:
            return

        # Get values
        tmp = self.func_le.text()
        func_str = tmp.replace('^','**')  
        x_min = float(self.xmin_le.text())
        x_max = float(self.xmax_le.text())

        # Generate x data
        x = np.linspace(x_min, x_max)
        
        # Evaluate function
        y = eval(func_str)

        # Clear old plot
        self.plot.ax.clear()

        # Plot data
        self.plot.ax.plot(x, y)

        # Set labels
        self.plot.ax.set_xlabel('X')
        self.plot.ax.set_ylabel('Y')

        # Add grid
        self.plot.ax.grid()

        # Draw plot
        self.plot.draw()

if __name__ == "__main__":
    # Create Qt application
    app = QtWidgets.QApplication([])

    # Create and show main window
    window = MainWindow()
    window.show()

    # Run event loop
    app.exec_()