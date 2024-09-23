
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtCore import Qt

class Tab1(QWidget):
    def __init__(self):
        super().__init__()

        self.fig1 = Figure(figsize=(10, 6))
        self.canvas1 = FigureCanvas(self.fig1)
        self.canvas1.setStyleSheet("border-radius:25%;")
        self.canvas1.setFixedSize(400, 550)

        layout = QHBoxLayout()
        layout.addWidget(self.canvas1)

        self.setLayout(layout)

        self.plot_telemetry_graphs1()

        telemetry_data = QWidget()
        layout1 = QHBoxLayout(telemetry_data)
        telemetry_data.setFixedSize(800, 550)
        telemetry_data.setStyleSheet("border: 4px solid #084705;border-radius:25%;")

        layout.addWidget(telemetry_data)

        data_column1 = QWidget()
        data_column1.setStyleSheet("border:None;")
        data_column2 = QWidget()
        data_column2.setStyleSheet("border:None;")
        layout1.addWidget(data_column1)
        layout1.addWidget(data_column2)

        sub_layout1 = QVBoxLayout(data_column1)
        sub_layout2 = QVBoxLayout(data_column2)

        columns = [
            "ALTITUDE", "PRESSURE",
            "TEMP", "VOLTAGE", "TVOC", "eCO2", "ACC_R", "ACC_P", "ACC_Y", "GYRO_R",
            "GYRO_P", "GYRO_Y"
        ]

        label_style = """
            QLabel {
                font-size: 18px; 
                color: white; 
                background-color: #994a0e;
                padding: 8px;
                border-radius: 10px; 
                border: 2px solid #4b0082;
                margin: 5px;
                text-align: center;
            }
        """

        for column in columns[:6]:
            label = QLabel(column, self)
            label.setStyleSheet(label_style)
            label.setAlignment(Qt.AlignCenter)
            sub_layout1.addWidget(label)

        for column in columns[6:]:
            label = QLabel(column, self)
            label.setStyleSheet(label_style)
            label.setAlignment(Qt.AlignCenter)
            sub_layout2.addWidget(label)

        self.fig2 = Figure(figsize=(10, 6))
        self.canvas2 = FigureCanvas(self.fig2)
        self.canvas2.setStyleSheet("border: 5px solid red; margin: 5px;")
        self.canvas2.setFixedSize(400, 550)

        self.plot_telemetry_graphs2()

        layout.addWidget(self.canvas2)

    def plot_telemetry_graphs1(self):
        ax1 = self.fig1.add_subplot(311)
        ax2 = self.fig1.add_subplot(312)
        ax3 = self.fig1.add_subplot(313)

        t = range(100)
        altitude = [i + (i % 5) * 2 for i in t]
        pressure = [1000 - i for i in t]
        voltage = [5 - (i % 3) for i in t]

        ax1.plot(t, altitude, label='Altitude')
        ax2.plot(t, pressure, label='Pressure')
        ax3.plot(t, voltage, label='Voltage')

        ax1.set_title('Altitude vs Time')
        ax2.set_title('Pressure vs Time')
        ax3.set_title('Voltage vs Time')

        ax1.legend()
        ax2.legend()
        ax3.legend()

        self.fig1.subplots_adjust(left=0.1, right=0.9, top=0.95, bottom=0.05, hspace=0.5, wspace=0.4)
        self.canvas1.draw()

    def plot_telemetry_graphs2(self):
        ax4 = self.fig2.add_subplot(311)
        ax5 = self.fig2.add_subplot(312)
        ax6 = self.fig2.add_subplot(313)

        t = range(100)
        gyro = [i / 2 for i in t]
        accel = [i / 3 for i in t]
        velocity = [i / 1.5 for i in t]

        ax4.plot(t, gyro, label='Gyro')
        ax5.plot(t, accel, label='Accel')
        ax6.plot(t, velocity, label='Velocity')

        ax4.set_title('Gyro vs Time')
        ax5.set_title('Accel vs Time')
        ax6.set_title('Velocity vs Time')

        ax4.legend()
        ax5.legend()
        ax6.legend()

        self.fig2.subplots_adjust(left=0.1, right=0.9, top=0.95, bottom=0.05, hspace=0.5, wspace=0.4)
        self.canvas2.draw()
