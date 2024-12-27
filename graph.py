import sys
import pyqtgraph as pg
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QIcon, QPixmap, QPalette, QBrush
import pandas as pd
import numpy as np
from datetime import datetime
from geopy.distance import distance

file_link = "Cansat_Telemetry_Software\\Add Ons\\trial_data.csv"

class Tab2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,1880,1080)
        widget2 = QWidget(self)
        layout = QGridLayout(widget2)
        widget2.setStyleSheet('''background-color:#9867C5;''')
        #self.setCentralWidget(widget2)
        widget2.setGeometry(80, 60, 1730, 600)
        self.altitude_graph = altitude_graph(self)
        self.Pressure_graph = Pressure_graph(self)
        self.voltageGraph = voltageGraph(self)
        self.AccelGraph = AccelGraph(self)
        self.GyroGraph = GyroGraph(self)
        self.VelocityGraph = VelocityGraph(self)
        
        self.altitude_graph.setParent(self.centralWidget())
        self.Pressure_graph.setParent(self.centralWidget())  
        self.voltageGraph.setParent(self.centralWidget()) 
        self.AccelGraph.setParent(self.centralWidget()) 
        self.GyroGraph.setParent(self.centralWidget())
        self.VelocityGraph.setParent(self.centralWidget())
        
         # Add both graphs to the layout in different grid positions
        layout.addWidget(self.altitude_graph, 0, 0)  # Altitude graph at row 0, column 0
        layout.addWidget(self.Pressure_graph, 0, 1)  # Pressure graph at row 1, column 0
        layout.addWidget(self.VelocityGraph,0,2)
        layout.addWidget(self.voltageGraph, 1,0)
        layout.addWidget(self.AccelGraph, 1,1)
        layout.addWidget(self.GyroGraph,1,2)
            
        self.show()

class altitude_graph(QMainWindow):
    def __init__(self,parent = None):
        super().__init__()
        self.df = pd.read_csv(file_link)
        
        widget = QWidget(self)
        self.setCentralWidget(widget)
        layout = QGridLayout(widget)
        
        
        self.row = 0
        self.time_index = 0
        self.rows = []
        self.plotwidget = pg.PlotWidget()
        self.plotwidget.setBackground('w')
        self.plotwidget.setLabel('left','Altitude',**{'font-size':'16pt','font-family':'Arial'})
        self.plotwidget.setLabel('bottom','Time (s)',**{'font-size':'16pt','font-family':'Arial','bold': True})
        self.pen = pg.mkPen(color=(0,0,255),style = Qt.SolidLine, width = 2)
        
        self.plotwidget.getAxis('left').setStyle(tickFont = pg.Qt.QtGui.QFont('Arial',14,pg.Qt.QtGui.QFont.Bold))
        self.plotwidget.getAxis('bottom').setStyle(tickFont= pg.Qt.QtGui.QFont('Arial',14,pg.Qt.QtGui.QFont.Bold))
        self.timer = QTimer()
        self.timer.start(1000)
        self.timer.timeout.connect(self.display_graph)
        self.setCentralWidget(self.plotwidget)
        
        
    def display_graph(self):
        if self.row < len(self.df):
         row_data = self.df.iloc[self.row]['ALTITUDE']
         self.rows.append(row_data)
         y_data = self.rows
         x_data = range(self.time_index + 1)
         self.row += 1
         self.time_index += 1
         self.plotwidget.plot(x_data,y_data,symbol = 'o',pen = self.pen,symbolSize = 10, symbolBrush = 'black') 
        else:
            self.timer.stop()

class Pressure_graph(QMainWindow):
    def __init__(self,parent = None):
        super().__init__()
        
        widget = QWidget(self)
        widget.setGeometry(40,40,200,400)
        layout = QGridLayout(widget)
        self.setCentralWidget(widget)
        self.df = pd.read_csv(file_link, usecols =['PRESSURE'])
        self.row_index = 0
        self.time_index = 0
        self.pressure_values = []
        self.plot_widget = pg.PlotWidget()
        self.plot_widget.setBackground('w')
        
        self.plot_widget.setLabel('left','Pressure',**{'font-size':'16pt','font-family':'Arial'})
        self.plot_widget.setLabel('bottom','Time (s)',**{'font-size':'16pt','font-family':'Arial'})
        self.plot_widget.getAxis('left').setStyle(tickFont = pg.Qt.QtGui.QFont('Arial',16,pg.Qt.QtGui.QFont.Bold))
        self.plot_widget.getAxis('bottom').setStyle(tickFont = pg.Qt.QtGui.QFont('Arial',16,pg.Qt.QtGui.QFont.Bold))
        self.pen1 = pg.mkPen(color=(0,0,255),style = Qt.SolidLine, width = 2)
        layout.addWidget(self.plot_widget)

        
        self.timer = QTimer()
        self.timer.start(1000)
        self.timer.timeout.connect(self.update_graph)
        
        
    def update_graph(self):
        if len(self.df) <= self.row_index:
            self.timer.stop()
            return
        item = self.df.iloc[self.row_index]['PRESSURE']
        x_data = range(self.time_index+1)
        self.pressure_values.append(item)
        self.plot_widget.plot(x_data,self.pressure_values,symbol = 'o',symbolSize= 10, symbolBrush = 'black',pen = self.pen1)
        self.row_index += 1
        self.time_index += 1
        
class VelocityGraph(QMainWindow):
    def __init__(self, parent = None):
        super().__init__()
        self.df = pd.read_csv(file_link)
        
        self.plotwidget = pg.PlotWidget()  
        self.plotwidget.setBackground('w')
        self.plotwidget.setLabel('left','Velocity (m/s)',**{'font-size':'16pt','font-family':'Arial'})
        self.plotwidget.setLabel('bottom','Time (s)',**{'font-size':'16pt','font-family':'Arial'})
        self.plotwidget.getAxis('left').setStyle(tickFont = pg.Qt.QtGui.QFont('Arial',16,pg.Qt.QtGui.QFont.Bold))
        self.plotwidget.getAxis('bottom').setStyle(tickFont = pg.Qt.QtGui.QFont('Arial',16,pg.Qt.QtGui.QFont.Bold))
        self.pen2 = pg.mkPen(color = (0,0,255),style = Qt.SolidLine, width = 2)
        
        widget = QWidget(self)
        self.setCentralWidget(widget)
        layout = QVBoxLayout(widget)
        layout.addWidget(self.plotwidget)
        self.plotwidget.setBackground('w')
        
        self.row_index = 0
        self.start_time = 0
        self.velocity = []
        self.time = []
        
        self.timer = QTimer()
        self.timer.start(1000)
        self.timer.timeout.connect(self.updateGraph)
        
    def updateGraph(self):
        if self.row_index >= len(self.df)-1:
            self.timer.stop()
            return       
        point1 = self.df.iloc[self.row_index][['GNSS_LATITUDE','GNSS_LONGITUDE','GNSS_ALTITUDE']].values
        point2 = self.df.iloc[self.row_index+1][['GNSS_LATITUDE','GNSS_LONGITUDE','GNSS_ALTITUDE']].values
        time1 = self.df.iloc[self.row_index]['GNSS_TIME']
        time2 = self.df.iloc[self.row_index+1]['GNSS_TIME']
        
        time_difference = self.calculate_total_time(time1,time2)
        total_distance = self.calculate_total_distance(point1,point2)
        velocity = total_distance/time_difference if time_difference != 0 else 0
        self.velocity.append(velocity)
        self.time.append(self.start_time)
        self.plotwidget.plot(self.time,self.velocity,symbol = 'o', symbolSize = 10, symbolBrush = 'black', pen = self.pen2)
        self.row_index += 1
        self.start_time += time_difference
        
    def calculate_total_time(self,time1,time2):
        t1 = datetime.strptime(time1,"%H:%M:%S")
        t2 = datetime.strptime(time2,"%H:%M:%S")
        time_difference = (t2 - t1).total_seconds()
        return time_difference
        
    def calculate_total_distance(self, point1,point2):
        lat1, lon1, alt1 = point1
        lat2, lon2, alt2 = point2
        
        vertical_dis = abs(alt2 - alt1)
        horizontal_dis = distance((lat1,lon1),(lat2,lon2)).meters
        
        total_distance = np.sqrt(vertical_dis**2 + horizontal_dis**2)
        return total_distance
       
class voltageGraph(QMainWindow):
    def __init__(self,parent = None):
        super().__init__()
        self.df = pd.read_csv(file_link)
        self.row_index = 0
        self.time_index = 0
        
        self.plot_widget = pg.PlotWidget()
        self.plot_widget.setBackground('w')
        
        self.plot_widget.setLabel('left','Voltage',**{'font-size':'16pt','font-family':'Arial','family-weight':'bold'})
        self.plot_widget.setLabel('bottom','Time (s)',**{'font-size':'16pt','font-family':'Arial','family-weight':'bold'})
        
        self.plot_widget.getAxis('left').setStyle(tickFont = pg.Qt.QtGui.QFont('Arial',16,pg.Qt.QtGui.QFont.Bold))
        self.plot_widget.getAxis('bottom').setStyle(tickFont = pg.Qt.QtGui.QFont('Arial',16, pg.Qt.QtGui.QFont.Bold))
        self.pen3 = pg.mkPen(color = (0,0,255),style = Qt.SolidLine,width = 2)
        
        widget = QWidget(self)
        self.setCentralWidget(widget)
        layout = QVBoxLayout(widget)
        layout.addWidget(self.plot_widget)
        
        self.voltage = []
        
        self.timer = QTimer()
        self.timer.start(1000)
        self.timer.timeout.connect(self.updateGraph)
        
    def updateGraph(self):
        if self.row_index >= len(self.df):
            self.timer.stop()
            return 
        item = self.df.iloc[self.row_index]['VOLTAGE']
        self.voltage.append(item)
        x_data = range(self.time_index+1)
        self.plot_widget.plot(x_data,self.voltage,symbol = 'o', symbolSize = 10, symbolBrush = 'black',pen = self.pen3)
        self.row_index += 1
        self.time_index += 1

class AccelGraph(QMainWindow):
    def __init__(self,parent = None):
        super().__init__()
        self.df = pd.read_csv(file_link)
        
        self.plt_widget = pg.PlotWidget()
        self.plt_widget.setBackground('w')
        self.plt_widget.setLabel('left','Accel_R',**{'font-size': '16pt','font-family': 'Arial','family-weight':'bold'})
        self.plt_widget.setLabel('bottom','Time (s)',**{'font-size':'16pt','font-family':'Arial','family-weight':'bold'})
        self.plt_widget.getAxis('left').setStyle(tickFont = pg.Qt.QtGui.QFont('Arial',16, pg.Qt.QtGui.QFont.Bold))
        self.plt_widget.getAxis('bottom').setStyle(tickFont = pg.Qt.QtGui.QFont('Arial',16, pg.Qt.QtGui.QFont.Bold))
        
        self.pen4 = pg.mkPen(color = (0,0,255),width = 2,style = Qt.SolidLine)
        
        widget = QWidget(self)
        self.setCentralWidget(widget)
        layout = QVBoxLayout(widget)
        layout.addWidget(self.plt_widget)
        
        self.row_index = 0
        self.time_index = 0
        
        self.accel = []
        self.time = []
        
        self.timer = QTimer()
        self.timer.start(1000)
        self.timer.timeout.connect(self.updateGraph)
        
    def updateGraph(self):
        if self.row_index >= len(self.df):
            self.timer.stop()
            return 
        item = self.df.iloc[self.row_index]['ACC_R']
        self.accel.append(item)
        self.time.append(self.time_index)
        self.plt_widget.plot(self.time,self.accel,symbol = 'o',symbolSize = 10,symbolBrush = 'black',pen = self.pen4)
        self.row_index += 1
        self.time_index += 1
        
class GyroGraph(QMainWindow):
    def __init__(self,parent = None):
        super().__init__()
        self.df = pd.read_csv(file_link)
        
        self.plt_widget = pg.PlotWidget()
        self.plt_widget.setBackground('w')
        self.plt_widget.setLabel('left','GYRO_R',**{'font-size': '16pt','font-family': 'Arial','bold': True})
        self.plt_widget.setLabel('bottom','Time (s)',**{'font-size':'16pt','font-family':'Arial','bold': True})
        self.plt_widget.getAxis('left').setStyle(tickFont = pg.Qt.QtGui.QFont('Arial',16, pg.Qt.QtGui.QFont.Bold))
        self.plt_widget.getAxis('bottom').setStyle(tickFont = pg.Qt.QtGui.QFont('Arial',16, pg.Qt.QtGui.QFont.Bold))
        
        self.pen5 = pg.mkPen(color = (0,0,255),width = 2,style = Qt.SolidLine)
        
        widget = QWidget(self)
        self.setCentralWidget(widget)
        layout = QVBoxLayout(widget)
        layout.addWidget(self.plt_widget)
        
        self.row_index = 0
        self.time_index = 0
        
        self.gyro = []
        self.time = []
        
        self.timer = QTimer()
        self.timer.start(1000)
        self.timer.timeout.connect(self.updateGraph)
        
    def updateGraph(self):
        if self.row_index >= len(self.df):
            self.timer.stop()
            return 
        item = self.df.iloc[self.row_index]['GYRO_R']
        self.gyro.append(item)
        self.time.append(self.time_index)
        self.plt_widget.plot(self.time,self.gyro,symbol = 'o',symbolSize = 10,symbolBrush = 'black',pen = self.pen5)
        self.row_index += 1
        self.time_index += 1