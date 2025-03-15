import pyqtgraph as pg
from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QVBoxLayout
from PyQt5.QtCore import Qt, QTimer
import pandas as pd
import numpy as np
from datetime import datetime
from geopy.distance import distance
import os;

base_dir = os.path.dirname(os.path.abspath(__file__))  # Get script directory
file_link = os.path.join(base_dir, "Add Ons", "trial_data.csv")

class Tab2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 1880, 1080)

        widget2 = QWidget(self)
        layout = QGridLayout(widget2)
        widget2.setStyleSheet("background-color:#9867C5;")
        widget2.setGeometry(80, 60, 1730, 600)

        # Create graph widgets
        self.altitude_graph = altitude_graph()
        self.pressure_graph = Pressure_graph()
        self.velocity_graph = VelocityGraph()
        self.voltage_graph = voltage_graph()
        self.accel_graph = accelgraph()
        self.gyro_graph = gyrograph()

        # Add graphs to layout
        layout.addWidget(self.altitude_graph, 0, 0)
        layout.addWidget(self.pressure_graph, 0, 1)
        layout.addWidget(self.velocity_graph, 0, 2)
        layout.addWidget(self.voltage_graph, 1, 0)
        layout.addWidget(self.accel_graph, 1, 1)
        layout.addWidget(self.gyro_graph, 1, 2)

        self.setCentralWidget(widget2)
        self.show()


class altitude_graph(QWidget):
    def __init__(self):
        super().__init__()
        self.df = pd.read_csv(file_link)

        layout = QVBoxLayout(self)
        self.plotwidget = pg.PlotWidget()
        self.plotwidget.setBackground("w")
        self.plotwidget.setLabel("left", "Altitude", **{"font-size": "16pt", "font-family": "Arial"})
        self.plotwidget.setLabel("bottom", "Time (s)", **{"font-size": "16pt", "font-family": "Arial", "bold": True})
        self.pen = pg.mkPen(color=(0, 0, 255), style=Qt.SolidLine, width=2)

        self.plotwidget.getAxis("left").setStyle(tickFont=pg.Qt.QtGui.QFont("Arial", 14, pg.Qt.QtGui.QFont.Bold))
        self.plotwidget.getAxis("bottom").setStyle(tickFont=pg.Qt.QtGui.QFont("Arial", 14, pg.Qt.QtGui.QFont.Bold))

        layout.addWidget(self.plotwidget)

        self.row = 0
        self.time_index = 0
        self.rows = []

        self.timer = QTimer()
        self.timer.start(1000)
        self.timer.timeout.connect(self.display_graph)

    def display_graph(self):
        if self.row < len(self.df):
            row_data = self.df.iloc[self.row]["ALTITUDE"]
            self.rows.append(row_data)
            y_data = self.rows
            x_data = range(self.time_index + 1)
            self.row += 1
            self.time_index += 1
            self.plotwidget.plot(x_data, y_data, symbol="o", pen=self.pen, symbolSize=10, symbolBrush="black")
        else:
            self.timer.stop()


class Pressure_graph(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        self.df = pd.read_csv(file_link, usecols=["PRESSURE"])

        self.plot_widget = pg.PlotWidget()
        self.plot_widget.setBackground("w")
        self.plot_widget.setLabel("left", "Pressure", **{"font-size": "16pt", "font-family": "Arial"})
        self.plot_widget.setLabel("bottom", "Time (s)", **{"font-size": "16pt", "font-family": "Arial"})
        self.pen = pg.mkPen(color=(0, 0, 255), style=Qt.SolidLine, width=2)

        layout.addWidget(self.plot_widget)

        self.row_index = 0
        self.time_index = 0
        self.pressure_values = []

        self.timer = QTimer()
        self.timer.start(1000)
        self.timer.timeout.connect(self.update_graph)

    def update_graph(self):
        if self.row_index >= len(self.df):
            self.timer.stop()
            return

        item = self.df.iloc[self.row_index]["PRESSURE"]
        self.pressure_values.append(item)
        x_data = range(self.time_index + 1)
        self.plot_widget.plot(x_data, self.pressure_values, symbol="o", symbolSize=10, symbolBrush="black", pen=self.pen)
        self.row_index += 1
        self.time_index += 1

class voltage_graph(QWidget):
    def __init__(self):
        super().__init__()
        self.df = pd.read_csv(file_link)

        layout = QVBoxLayout(self)
        self.plotwidget = pg.PlotWidget()
        self.plotwidget.setBackground("w")
        self.plotwidget.setLabel("left", "Voltage", **{"font-size": "16pt", "font-family": "Arial"})
        self.plotwidget.setLabel("bottom", "Time (s)", **{"font-size": "16pt", "font-family": "Arial", "bold": True})
        self.pen = pg.mkPen(color=(0, 0, 255), style=Qt.SolidLine, width=2)

        self.plotwidget.getAxis("left").setStyle(tickFont=pg.Qt.QtGui.QFont("Arial", 14, pg.Qt.QtGui.QFont.Bold))
        self.plotwidget.getAxis("bottom").setStyle(tickFont=pg.Qt.QtGui.QFont("Arial", 14, pg.Qt.QtGui.QFont.Bold))

        layout.addWidget(self.plotwidget)

        self.row = 0
        self.time_index = 0
        self.rows = []

        self.timer = QTimer()
        self.timer.start(1000)
        self.timer.timeout.connect(self.display_graph)

    def display_graph(self):
        if self.row < len(self.df):
            row_data = self.df.iloc[self.row]["VOLTAGE"]
            self.rows.append(row_data)
            y_data = self.rows
            x_data = range(self.time_index + 1)
            self.row += 1
            self.time_index += 1
            self.plotwidget.plot(x_data, y_data, symbol="o", pen=self.pen, symbolSize=10, symbolBrush="black")
        else:
            self.timer.stop()


class accelgraph(QWidget):
    def __init__(self):
        super().__init__()
        self.df = pd.read_csv(file_link)

        layout = QVBoxLayout(self)
        self.plotwidget = pg.PlotWidget()
        self.plotwidget.setBackground("w")
        self.plotwidget.setLabel("left", "Accel_R", **{"font-size": "16pt", "font-family": "Arial"})
        self.plotwidget.setLabel("bottom", "Time (s)", **{"font-size": "16pt", "font-family": "Arial", "bold": True})
        self.pen = pg.mkPen(color=(0, 0, 255), style=Qt.SolidLine, width=2)

        self.plotwidget.getAxis("left").setStyle(tickFont=pg.Qt.QtGui.QFont("Arial", 14, pg.Qt.QtGui.QFont.Bold))
        self.plotwidget.getAxis("bottom").setStyle(tickFont=pg.Qt.QtGui.QFont("Arial", 14, pg.Qt.QtGui.QFont.Bold))

        layout.addWidget(self.plotwidget)

        self.row = 0
        self.time_index = 0
        self.rows = []

        self.timer = QTimer()
        self.timer.start(1000)
        self.timer.timeout.connect(self.display_graph)

    def display_graph(self):
        if self.row < len(self.df):
            row_data = self.df.iloc[self.row]["ACC_R"]
            self.rows.append(row_data)
            y_data = self.rows
            x_data = range(self.time_index + 1)
            self.row += 1
            self.time_index += 1
            self.plotwidget.plot(x_data, y_data, symbol="o", pen=self.pen, symbolSize=10, symbolBrush="black")
        else:
            self.timer.stop()


class gyrograph(QWidget):
    def __init__(self):
        super().__init__()
        self.df = pd.read_csv(file_link)

        layout = QVBoxLayout(self)
        self.plotwidget = pg.PlotWidget()
        self.plotwidget.setBackground("w")
        self.plotwidget.setLabel("left", "GYRO_R", **{"font-size": "16pt", "font-family": "Arial"})
        self.plotwidget.setLabel("bottom", "Time (s)", **{"font-size": "16pt", "font-family": "Arial", "bold": True})
        self.pen = pg.mkPen(color=(0, 0, 255), style=Qt.SolidLine, width=2)

        self.plotwidget.getAxis("left").setStyle(tickFont=pg.Qt.QtGui.QFont("Arial", 14, pg.Qt.QtGui.QFont.Bold))
        self.plotwidget.getAxis("bottom").setStyle(tickFont=pg.Qt.QtGui.QFont("Arial", 14, pg.Qt.QtGui.QFont.Bold))

        layout.addWidget(self.plotwidget)

        self.row = 0
        self.time_index = 0
        self.rows = []

        self.timer = QTimer()
        self.timer.start(1000)
        self.timer.timeout.connect(self.display_graph)

    def display_graph(self):
        if self.row < len(self.df):
            row_data = self.df.iloc[self.row]["GYRO_R"]
            self.rows.append(row_data)
            y_data = self.rows
            x_data = range(self.time_index + 1)
            self.row += 1
            self.time_index += 1
            self.plotwidget.plot(x_data, y_data, symbol="o", pen=self.pen, symbolSize=10, symbolBrush="black")
        else:
            self.timer.stop()


class VelocityGraph(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        self.df = pd.read_csv(file_link)

        self.plotwidget = pg.PlotWidget()
        self.plotwidget.setBackground("w")
        self.plotwidget.setLabel("left", "Velocity (m/s)", **{"font-size": "16pt", "font-family": "Arial"})
        self.plotwidget.setLabel("bottom", "Time (s)", **{"font-size": "16pt", "font-family": "Arial"})
        self.pen = pg.mkPen(color=(0, 0, 255), style=Qt.SolidLine, width=2)

        layout.addWidget(self.plotwidget)

        self.row_index = 0
        self.start_time = 0
        self.velocity = []
        self.time = []

        self.timer = QTimer()
        self.timer.start(1000)
        self.timer.timeout.connect(self.update_graph)

    def update_graph(self):
        if self.row_index >= len(self.df) - 1:
            self.timer.stop()
            return

        point1 = self.df.iloc[self.row_index][["GNSS_LATITUDE", "GNSS_LONGITUDE", "GNSS_ALTITUDE"]].values
        point2 = self.df.iloc[self.row_index + 1][["GNSS_LATITUDE", "GNSS_LONGITUDE", "GNSS_ALTITUDE"]].values
        time1 = self.df.iloc[self.row_index]["GNSS_TIME"]
        time2 = self.df.iloc[self.row_index + 1]["GNSS_TIME"]

        time_difference = self.calculate_total_time(time1, time2)
        total_distance = self.calculate_total_distance(point1, point2)
        velocity = total_distance / time_difference if time_difference != 0 else 0
        self.velocity.append(velocity)
        self.time.append(self.start_time)
        self.plotwidget.plot(self.time, self.velocity, symbol="o", symbolSize=10, symbolBrush="black", pen=self.pen)
        self.row_index += 1
        self.start_time += time_difference

    def calculate_total_time(self, time1, time2):
        t1 = datetime.strptime(time1, "%H:%M:%S")
        t2 = datetime.strptime(time2, "%H:%M:%S")
        return (t2 - t1).total_seconds()

    def calculate_total_distance(self, point1, point2):
        lat1, lon1, alt1 = point1
        lat2, lon2, alt2 = point2
        vertical_dis = abs(alt2 - alt1)
        horizontal_dis = distance((lat1, lon1), (lat2, lon2)).meters
        return np.sqrt(vertical_dis ** 2 + horizontal_dis ** 2)


# Similarly, refactor `voltageGraph`, `AccelGraph`, and `GyroGraph` to inherit from `QWidget`
