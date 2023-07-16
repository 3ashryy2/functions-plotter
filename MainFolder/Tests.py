from PySide2.QtWidgets import QApplication
import pytest
from pytestqt.qt_compat import qt_api

from Function_Plotter import MainWindow

# Create QT app once for all tests
app = QApplication([]) 

@pytest.fixture
def main_window(qtbot):
    window = MainWindow()
    qtbot.addWidget(window)
    return window

def test_valid_plot(main_window, qtbot):
    # Test code 
    qtbot.keyClicks(main_window.func_le, "x^2")
    qtbot.keyClicks(main_window.xmin_le, "-5")
    qtbot.keyClicks(main_window.xmax_le, "5")

    qtbot.mouseClick(main_window.plot_btn, qt_api.QtCore.Qt.LeftButton)

    assert main_window.plot.ax.has_data()

def test_invalid_function(main_window, qtbot):
    # Test code
    qtbot.keyClicks(main_window.func_le, "x^y")
    qtbot.keyClicks(main_window.xmin_le, "-5")
    qtbot.keyClicks(main_window.xmax_le, "5")
    qtbot.mouseClick(main_window.plot_btn, qt_api.QtCore.Qt.LeftButton)

    assert not main_window.plot.ax.has_data()
    assert len(main_window.plot.ax.lines) == 0
   
def test_invalid_range(main_window, qtbot):
    qtbot.keyClicks(main_window.func_le, "x*2")
    qtbot.keyClicks(main_window.xmin_le, "10")
    qtbot.keyClicks(main_window.xmax_le, "5")

    qtbot.mouseClick(main_window.plot_btn, qt_api.QtCore.Qt.LeftButton)

    assert not main_window.plot.ax.has_data()
    assert len(main_window.plot.ax.lines) == 0   



def test_missing_input(main_window, qtbot):
    # Test that an error is raised when the user tries to plot with missing input
    qtbot.keyClicks(main_window.func_le, "x*2")
    qtbot.keyClicks(main_window.xmin_le, "-5")

    error_msg = main_window.validate_input()
    assert error_msg == "Invalid input for Xmax"


def test_invalid_input(main_window, qtbot):
    # Test that an error is raised when the user enters invalid input
    qtbot.keyClicks(main_window.func_le, "x*2")
    qtbot.keyClicks(main_window.xmin_le, "-5")
    qtbot.keyClicks(main_window.xmax_le, "not a number")

    error_msg = main_window.validate_input()
    assert error_msg == "Invalid input for Xmax"

def test_large_range(main_window, qtbot):
    # Test that the plot displays correctly for a large range of x values
    qtbot.keyClicks(main_window.func_le, "x^2")
    qtbot.keyClicks(main_window.xmin_le, "-100")
    qtbot.keyClicks(main_window.xmax_le, "100")

    qtbot.mouseClick(main_window.plot_btn, qt_api.QtCore.Qt.LeftButton)

    assert main_window.plot.ax.has_data()

def test_negative_x(main_window, qtbot):
    # Test that the plot displays correctly for negative x values
    qtbot.keyClicks(main_window.func_le, "x+10*x-5")
    qtbot.keyClicks(main_window.xmin_le, "-10")
    qtbot.keyClicks(main_window.xmax_le, "0")

    qtbot.mouseClick(main_window.plot_btn, qt_api.QtCore.Qt.LeftButton)

    assert main_window.plot.ax.has_data()

def test_zero_input(main_window, qtbot):
    # Test that the plot displays correctly for input values of zero
    qtbot.keyClicks(main_window.func_le, "0")
    qtbot.keyClicks(main_window.xmin_le, "-5")
    qtbot.keyClicks(main_window.xmax_le, "5")

    qtbot.mouseClick(main_window.plot_btn, qt_api.QtCore.Qt.LeftButton)

    assert not main_window.plot.ax.has_data()

# Shut down QT app after all tests done
app.exit()