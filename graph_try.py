import pyqtgraph as pg
from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QVBoxLayout
from PyQt5.QtCore import Qt, QTimer
import pandas as pd
import numpy as np
from datetime import datetime
from geopy.distance import distance

file_link = "Cansat_Telemetry_Software\\Add Ons\\trial_data.csv"


class Tab2(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 1880, 1080)

        # Main layout for the widget
        layout = QGridLayout(self)
        self.setLayout(layout)

        # Create graph widgets
        self.altitude_graph = graphs("Trajectory", 'ALTITUDE')
        self.pressure_graph = graphs("Pressure", "PRESSURE")
        self.voltage_graph = graphs("Voltage", "VOLTAGE")
        self.accel_graph = multi_graphs("Accelerometer", ["ACC_R", "ACC_P", "ACC_Y"])
        self.gyro_graph = multi_graphs("Gyrometer" , ["GYRO_R", "GYRO_P", "GYRO_Y"])
        self.temp_graph = graphs("Temperature", "TEMP")
        self.velocity_graph = VelocityGraph()

        # Add graphs to layout
        layout.addWidget(self.altitude_graph, 0, 0, 0, 1)
        layout.addWidget(self.pressure_graph, 0, 1)
        layout.addWidget(self.voltage_graph, 0, 2)
        layout.addWidget(self.temp_graph, 1, 1)
        layout.addWidget(self.velocity_graph, 1, 2)
        layout.addWidget(self.accel_graph, 0, 3)
        layout.addWidget(self.gyro_graph, 1, 3)


class graphs(QWidget):
    def __init__(self , col_name , col_value):
        super().__init__()
        self.df = pd.read_csv(file_link)

        layout = QVBoxLayout(self)
        self.plotwidget = pg.PlotWidget()
        self.plotwidget.setBackground("w")
        self.plotwidget.setLabel("left", col_name, **{"font-size": "16pt", "font-family": "Arial"})
        self.plotwidget.setLabel("bottom", "Time (s)", **{"font-size": "16pt", "font-family": "Arial", "bold": True})
        self.pen = pg.mkPen(color=(0, 0, 255), style=Qt.SolidLine, width=2)

        self.plotwidget.getAxis("left").setStyle(tickFont=pg.Qt.QtGui.QFont("Arial", 14, pg.Qt.QtGui.QFont.Bold))
        self.plotwidget.getAxis("bottom").setStyle(tickFont=pg.Qt.QtGui.QFont("Arial", 14, pg.Qt.QtGui.QFont.Bold))

        layout.addWidget(self.plotwidget)

        self.row = 0
        self.time_index = 0
        self.rows = []

        self.timer = QTimer(self)
        self.timer.timeout.connect(lambda: self.display_graph(col_value))
        self.timer.start(1000)

    def display_graph(self , col_value):
        if self.row < len(self.df):
            row_data = self.df.iloc[self.row][col_value]
            self.rows.append(row_data)
            y_data = self.rows
            x_data = range(self.time_index + 1)
            self.row += 1
            self.time_index += 1
            self.plotwidget.plot(x_data, y_data, symbol="o", pen=self.pen, symbolSize=10, symbolBrush="black")
        else:
            self.timer.stop()


class multi_graphs(QWidget):
    def __init__(self, col_names, col_values):
        super().__init__()
        self.df = pd.read_csv(file_link)

        layout = QVBoxLayout(self)
        self.plotwidget = pg.PlotWidget()
        self.plotwidget.setBackground("w")
        self.plotwidget.setLabel("left", col_names, **{"font-size": "16pt", "font-family": "Arial"})
        self.plotwidget.setLabel("bottom", "Time (s)", **{"font-size": "16pt", "font-family": "Arial", "bold": True})

        # Create pens for 3 lines
        self.pen1 = pg.mkPen(color=(255, 0, 0), style=Qt.SolidLine, width=2)   # Red
        self.pen2 = pg.mkPen(color=(0, 255, 0), style=Qt.SolidLine, width=2)   # Green
        self.pen3 = pg.mkPen(color=(0, 0, 255), style=Qt.SolidLine, width=2)   # Blue

        # Style the axis
        self.plotwidget.getAxis("left").setStyle(tickFont=pg.Qt.QtGui.QFont("Arial", 14, pg.Qt.QtGui.QFont.Bold))
        self.plotwidget.getAxis("bottom").setStyle(tickFont=pg.Qt.QtGui.QFont("Arial", 14, pg.Qt.QtGui.QFont.Bold))

        layout.addWidget(self.plotwidget)

        self.legend = self.plotwidget.addLegend(size=(150, 80), offset=(20, 20))

        # Initialize variables for plotting
        self.row = 0
        self.time_index = 0
        self.rows1, self.rows2, self.rows3 = [], [], []

        self.line1 = self.plotwidget.plot([], [], symbol="o", pen=self.pen1, symbolSize=10, symbolBrush="red", name=col_names[0])
        self.line2 = self.plotwidget.plot([], [], symbol="s", pen=self.pen2, symbolSize=10, symbolBrush="green", name=col_names[1])
        self.line3 = self.plotwidget.plot([], [], symbol="t", pen=self.pen3, symbolSize=10, symbolBrush="blue", name=col_names[2])

        self.timer = QTimer()
        self.timer.start(1000)
        self.timer.timeout.connect(lambda: self.display_graph(col_values))

    def display_graph(self, col_values):
        if self.row < len(self.df):
            row_data1 = self.df.iloc[self.row][col_values[0]]
            row_data2 = self.df.iloc[self.row][col_values[1]]
            row_data3 = self.df.iloc[self.row][col_values[2]]

            self.rows1.append(row_data1)
            self.rows2.append(row_data2)
            self.rows3.append(row_data3)

            y_data1 = self.rows1
            y_data2 = self.rows2
            y_data3 = self.rows3

            x_data = range(self.time_index + 1)
            self.time_index += 1
            self.row += 1

            self.line1.setData(x_data, y_data1)
            self.line2.setData(x_data, y_data2)
            self.line3.setData(x_data, y_data3)
            
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
