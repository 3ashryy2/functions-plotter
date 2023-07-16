# Function Plotter
This is a simple Python application for plotting mathematical functions.

# Features
Allows user to input a function f(x) to plot
Specify x-axis limits
Plots the function using Matplotlib
Validates function and input values
Provides a GUI built with Qt and PySide2

# Usage

The main interface consists of:

Function input box - Enter a function like sin(x)
Xmin/Xmax input - Range of x-axis
Plot button - Generate plot
Matplotlib toolbar - Pan, zoom, etc.
Code Overview
The main classes are:

PlotWidget - Matplotlib canvas for showing the plot
MainWindow - Main application window, contains GUI elements

Key methods:

validate_func - Validate function string
validate_xlimit - Validate Xmin/Xmax inputs
validate_input - Overall input validation
plot_graph - Plot the function

# Requirements
Python 3
Matplotlib
NumPy
PySide2
Qt5
# Installation

Clone the repository
git clone https://github.com/3ashryy2/function-plotter


Install requirements
pip install -r requirements.txt

Run the app
python function_plotter.py

# Contributing
Contributions are welcome! Please open an issue or PR for bug fixes and improvements.


