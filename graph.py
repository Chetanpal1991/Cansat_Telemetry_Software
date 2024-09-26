from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QHBoxLayout,QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

class Tab2(QWidget):
    def __init__(self):
        super().__init__()

        self.fig1 = Figure(figsize=(10, 6))
        self.canvas1 = FigureCanvas(self.fig1)
        self.fig1.set_facecolor((0.5, 0.3, 0.8, 0.5))
        self.canvas1.setStyleSheet("border-radius:25%;")
        self.canvas1.setFixedSize(1800, 700)
        self.canvas1.setParent(self)  # Set the parent of canvas1 as the current widget (self)
        self.canvas1.setGeometry(50, 0, 1800, 700)
        

        self.plot_telemetry_graphs1()

    def plot_telemetry_graphs1(self):
        ax1 = self.fig1.add_subplot(231)
        ax2 = self.fig1.add_subplot(232)
        ax3 = self.fig1.add_subplot(233)
        ax4 = self.fig1.add_subplot(234)
        ax5 = self.fig1.add_subplot(235)
        ax6 = self.fig1.add_subplot(236)

        t = range(100)
        altitude = [i + (i % 5) * 2 for i in t]
        pressure = [1000 - i for i in t]
        voltage = [5 - (i % 3) for i in t]
        gyro = [i / 2 for i in t]
        accel = [i / 3 for i in t]
        velocity = [i / 1.5 for i in t]

        # Plot the data
        ax1.plot(t, altitude, label='Altitude')
        ax2.plot(t, pressure, label='Pressure')
        ax3.plot(t, voltage, label='Voltage')
        ax4.plot(t, gyro, label='Gyro')
        ax5.plot(t, accel, label='Accel')
        ax6.plot(t, velocity, label='Velocity')

        # Set bold titles with larger font size
        title_font = {'fontsize': 14, 'fontweight': 'bold'}  # Font size and bold
        ax1.set_title('Altitude vs Time', fontdict=title_font)
        ax2.set_title('Pressure vs Time', fontdict=title_font)
        ax3.set_title('Voltage vs Time', fontdict=title_font)
        ax4.set_title('Gyro vs Time', fontdict=title_font)
        ax5.set_title('Accel vs Time', fontdict=title_font)
        ax6.set_title('Velocity vs Time', fontdict=title_font)

        # Set larger font size for axis tick labels
        for ax in [ax1, ax2, ax3, ax4, ax5, ax6]:
            ax.tick_params(axis='both', which='major', labelsize=12)  # Increase the tick label font size
            ax.legend(fontsize=10)
            ax.grid(True)  # Legend font size

        # Adjust the layout of subplots
        self.fig1.subplots_adjust(left=0.1, right=0.9, top=0.93, bottom=0.12, hspace=0.25, wspace=0.4)
        self.canvas1.draw()

        