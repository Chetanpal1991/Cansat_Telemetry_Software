from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QTabWidget,
                             QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QLabel)
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QPixmap
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtWebEngineWidgets import QWebEngineView

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(0, 0, 1920, 1080)
        self.setWindowTitle("Manual Layout Example")
        self.setStyleSheet("""
            QMainWindow {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 0,
                    stop: 0 #003366, stop: 1 #009688
                );
            }
        """)

        widget1 = QWidget(self)
        widget2 = QWidget(self)
        widget3 = QWidget(self)

        widget1.setGeometry(10, 10, 1900, 150)
        widget1.setStyleSheet("background-color:#15144a;")

        header_1 = QLabel("SOFTWARE STATE", widget1)
        header_1.setStyleSheet("font-size: 20px; color: #cbe6ca; background-color: None; font-weight:Bold;")
        header_1.setGeometry(25, 20, 600, 30)
        header_1.setAlignment(Qt.AlignCenter)

        header_1_input = QLabel("LAUNCH_PAD", widget1)
        header_1_input.setStyleSheet("font-size: 20px; color: Black; background-color: white; border: 4px solid brown;border-radius:25%;")
        header_1_input.setGeometry(225, 80, 200, 50)
        header_1_input.setAlignment(Qt.AlignCenter)

        header_2 = QLabel("TEAM KALPANA : 2022ASI-049", widget1)
        header_2.setStyleSheet("font-size: 30px; color: #cbe6ca; background-color: None;font-weight:Bold;")
        header_2.setGeometry(650, 20, 600, 30)
        header_2.setAlignment(Qt.AlignCenter)

        logo_image = QPixmap("Add Ons\\Team Kalpana Logo 1.png").scaledToWidth(100, Qt.TransformationMode.SmoothTransformation)
        logo_label = QLabel(widget1)
        logo_label.setPixmap(logo_image)
        logo_label.setGeometry(900, 60, 100, 100)

        header_3 = QWidget(widget1)
        header_3.setGeometry(1275, 20, 600, 30)
        header_3.setStyleSheet("background-color: None;")

        header_3_wid_1 = QLabel("TIME", header_3)
        header_3_wid_1.setStyleSheet("font-size: 20px; color: #cbe6ca;font-weight:Bold;")
        header_3_wid_1.setGeometry(40, 0, 240, 30)
        header_3_wid_1.setAlignment(Qt.AlignCenter)

        header_3_wid_1_input = QLabel("0", widget1)
        header_3_wid_1_input.setStyleSheet("font-size: 20px; color: Black; background-color: white; border: 4px solid brown;border-radius:25%;")
        header_3_wid_1_input.setGeometry(1335, 80, 200, 50)
        header_3_wid_1_input.setAlignment(Qt.AlignCenter)

        header_3_wid_2 = QLabel("PACKET COUNT", header_3)
        header_3_wid_2.setStyleSheet("font-size: 20px; color: #cbe6ca;font-weight:Bold;")
        header_3_wid_2.setGeometry(320, 0, 240, 30)
        header_3_wid_2.setAlignment(Qt.AlignCenter)

        header_3_wid_2_input = QLabel("0", widget1)
        header_3_wid_2_input.setStyleSheet("font-size: 20px; color: Black; background-color: white; border: 4px solid brown;border-radius:25%;")
        header_3_wid_2_input.setGeometry(1275 + 340, 80, 200, 50)
        header_3_wid_2_input.setAlignment(Qt.AlignCenter)

        widget2.setGeometry(10, 125, 1900, 875)
        widget2.setStyleSheet("background-color: None;")

        self.tabs = QTabWidget(self)
        self.tabs.setGeometry(10, 175, 1900, 725)
        self.tabs.addTab(Tab1(), "Telemetry Data")
        self.tabs.addTab(Tab2(), "Location and Cordinates")
        self.tabs.setStyleSheet("""
            QTabWidget::pane {
                border-top: 2px solid #c3c7c3;
                background: #c3c7c3;
                border-radius: 40%
            }
            QTabBar::tab {
                background: #c3c7c3;
                color: white;
                font-size: 15px;
                font-weight: Bold;
                border: 1px solid #c3c7c3;
                border-radius:25%;
                width: 925%;
                padding: 10px;
                margin: 2px;
            }
            QTabBar::tab:selected {
                background: #a2a3a2;
                border-color: #a2a3a2;
                width: 925%;
            }
            QTabBar::tab:hover {
                background: #6f6f6f;
            }
        """)

        widget3.setGeometry(10, 900, 1900, 100)

        layout3 = QHBoxLayout(widget3)

        footer_button_style = """
           QPushButton {
                border: 3px solid black; 
                border-radius: 15px;
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 0,
                    stop: 0 #230636, stop: 1 #7516b5
                );
                font-size: 20px; 
                color: orange;
            }

            QPushButton:hover {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 0,
                    stop: 0 #7516b5 , stop: 1 #230636
                );
            }

            QPushButton:pressed {
                background-color:#15144a;
            }
        """

        def boot_function():
            print("BOOT button pressed")

        def set_time_function():
            print("Set Time button pressed")

        def calibrate_function():
            print("calibrate button pressed")

        def on_off_function():
            print("on_off button pressed")

        def cx_function():
            print("cx button pressed")

        def simulation_function():
            print("simulation button pressed")

        button1 = QPushButton("BOOT")
        button1.setStyleSheet(footer_button_style)
        button1.setFixedSize(150, 50)
        button1.clicked.connect(boot_function)
        layout3.addWidget(button1)

        button2 = QPushButton("Set Time")
        button2.setStyleSheet(footer_button_style)
        button2.setFixedSize(150, 50)
        button2.clicked.connect(set_time_function)
        layout3.addWidget(button2)

        button3 = QPushButton("Calibrate")
        button3.setStyleSheet(footer_button_style)
        button3.setFixedSize(150, 50)
        button3.clicked.connect(calibrate_function)
        layout3.addWidget(button3)

        button4 = QPushButton("ON / OFF")
        button4.setStyleSheet(footer_button_style)
        button4.setFixedSize(150, 50)
        button4.clicked.connect(on_off_function)
        layout3.addWidget(button4)

        button5 = QPushButton("CX")
        button5.setStyleSheet(footer_button_style)
        button5.setFixedSize(150, 50)
        button5.clicked.connect(cx_function)
        layout3.addWidget(button5)

        button6 = QPushButton("SIMULATION")
        button6.setStyleSheet(footer_button_style)
        button6.setFixedSize(150, 50)
        button6.clicked.connect(simulation_function)
        layout3.addWidget(button6)

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


class Tab2(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(80, 0, 0, 0)

        url = QUrl("https://www.google.com/maps")
        self.map_view = QWebEngineView(self)
        self.map_view.setUrl(url)
        self.map_view.setFixedSize(750, 650)
        self.map_view.setStyleSheet("""
            QWebEngineView {
                border: 2px solid #4b0082;
                border-radius: 25%;
            }
        """)
        main_layout.addWidget(self.map_view)

        coordinates_data = QWidget()
        layout1 = QGridLayout(coordinates_data)
        coordinates_data.setStyleSheet("padding-left: 400px;")

        columns = [
            "GNSS_TIME", "GNSS_LATITUDE", "GNSS_LONGITUDE",
            "GNSS_ALTITUDE", "GNSS_SATS"
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

        for column in columns:
            label = QLabel(column, self)
            label.setStyleSheet(label_style)
            label.setAlignment(Qt.AlignCenter)
            label.setFixedSize(400, 100)
            layout1.addWidget(label)

        main_layout.addWidget(coordinates_data)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.showMaximized()
    app.exec_()
