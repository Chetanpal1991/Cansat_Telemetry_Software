from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QHBoxLayout
from PyQt5.QtCore import QTimer
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
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
        layout.setHorizontalSpacing(0)
        layout.setVerticalSpacing(0)

        # Create graph widgets
        self.altitude_graph = Graphs("Altitude", 'ALTITUDE' , [0.18 , 0.95 , 0.95, 0.1])
        self.pressure_graph = Graphs("Pressure", "PRESSURE" , [0.2 , 0.95 , 0.9, 0.2])
        self.voltage_graph = Graphs("Voltage", "VOLTAGE" , [0.18 , 0.95 , 0.9, 0.2])
        self.accel_graph = MultiGraphs("Accelerometer", ["ACC_R", "ACC_P", "ACC_Y"] , [0.2 , 0.95 , 0.9, 0.2])
        self.gyro_graph = MultiGraphs("Gyrometer", ["GYRO_R", "GYRO_P", "GYRO_Y"] , [0.2 , 0.95 , 0.9, 0.2])
        self.temp_graph = Graphs("Temperature", "TEMP" , [0.18 , 0.95 , 0.9, 0.2])
        self.velocity_graph = VelocityGraph([0.15 , 0.95 , 0.9, 0.2])

        # Add graphs to layout
        layout.addWidget(self.altitude_graph, 0, 0 , 0 , 1)
        layout.addWidget(self.pressure_graph, 0, 1)
        layout.addWidget(self.voltage_graph, 0, 2)
        layout.addWidget(self.temp_graph, 1, 1)
        layout.addWidget(self.velocity_graph, 1, 2)
        layout.addWidget(self.accel_graph, 0, 3)
        layout.addWidget(self.gyro_graph, 1, 3)

    def process_data():
        # Logic to handle telemetry data processing
        print("Tab1: Processing telemetry data...")


class Graphs(QWidget):
    def __init__(self, col_name, col_value , dim):
        super().__init__()
        self.df = pd.read_csv(file_link)

        layout = QHBoxLayout(self)
        self.setLayout(layout)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)
        self.ax.figure.patch.set_facecolor('#0080FF20') 
        self.ax.figure.patch.set_edgecolor('green')
        self.ax.set_facecolor('orange')
        self.ax.set_xlabel("Time (s)",fontsize=12)
        self.ax.set_ylabel(col_name , fontsize=12)
        layout.addWidget(self.canvas)
        self.figure.subplots_adjust(left=dim[0], right=dim[1], top=dim[2], bottom=dim[3])

        self.row = 0
        self.time_index = 0
        self.rows = []

        self.timer = QTimer(self)
        self.timer.timeout.connect(lambda: self.display_graph(col_value))
        self.timer.start(1000)

    def display_graph(self, col_value):
        if self.row < len(self.df):
            row_data = self.df.iloc[self.row][col_value]
            self.rows.append(row_data)

            y_data = self.rows[-5:]
            x_data = range(len(self.rows))[-5:]

            self.ax.plot(x_data, y_data, marker="o", color="blue")
            if len(self.rows) > 5:
                self.ax.set_xlim(len(self.rows) - 5, len(self.rows))
            self.canvas.draw()

            self.row += 1
        else:
            self.timer.stop()

class MultiGraphs(QWidget):
    def __init__(self, col_names, col_values , dim):
        super().__init__()
        self.df = pd.read_csv(file_link)

        layout = QHBoxLayout(self)
        self.setLayout(layout)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)
        self.ax.set_xlabel("Time (s)",fontsize=12)
        self.ax.set_ylabel(col_names,fontsize=12)
        self.ax.legend()
        layout.addWidget(self.canvas)
        self.ax.figure.patch.set_facecolor('#0080FF20') 
        self.ax.figure.patch.set_edgecolor('green')
        self.ax.set_facecolor('orange')

        self.figure.subplots_adjust(left=dim[0], right=dim[1], top=dim[2], bottom=dim[3])


        self.row = 0
        self.time_index = 0
        self.rows1, self.rows2, self.rows3 = [], [], []


        self.timer = QTimer()
        self.timer.timeout.connect(lambda: self.display_graph(col_values))
        self.timer.start(1000)


    def display_graph(self, col_values):
        if self.row < len(self.df):
            self.rows1.append(self.df.iloc[self.row][col_values[0]])
            self.rows2.append(self.df.iloc[self.row][col_values[1]])
            self.rows3.append(self.df.iloc[self.row][col_values[2]])

            x_data = list(range(len(self.rows1)))
            x_last = x_data[-5:]

            rows1_last = self.rows1[-5:]
            rows2_last = self.rows2[-5:]
            rows3_last = self.rows3[-5:]

            self.ax.plot(x_data, self.rows1, marker="o", color="red", label=col_values[0])
            self.ax.plot(x_data, self.rows2, marker="s", color="green", label=col_values[1])
            self.ax.plot(x_data, self.rows3, marker="^", color="blue", label=col_values[2])
            if x_last:
                self.ax.set_xlim(x_last[0], x_last[-1])

            if self.row < 1:
                self.ax.legend()
            
            self.canvas.draw()

            self.row += 1
        else:
            self.timer.stop()

class VelocityGraph(QWidget ):
    def __init__(self , dim):
        super().__init__()
        layout = QHBoxLayout(self)
        self.setLayout(layout)

        self.df = pd.read_csv(file_link)
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)
        self.ax.set_xlabel("Time (s)", fontsize=12)
        self.ax.set_ylabel("Velocity (m/s)", fontsize=12)
        layout.addWidget(self.canvas)

        self.ax.figure.patch.set_facecolor('#0080FF20') 
        self.ax.figure.patch.set_edgecolor('green')
        self.ax.set_facecolor('orange')

        self.figure.subplots_adjust(left=dim[0], right=dim[1], top=dim[2], bottom=dim[3])


        self.row_index = 0
        self.start_time = 0
        self.velocity = []
        self.time = []

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_graph)
        self.timer.start(1000)

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

        times_last = self.time[-5:]
        velocity_last = self.velocity[-5:]

        self.ax.plot(self.time, self.velocity, marker="o", color="blue")
        
        if times_last:
            self.ax.set_xlim(times_last[0], times_last[-1])
        
        self.canvas.draw()


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
