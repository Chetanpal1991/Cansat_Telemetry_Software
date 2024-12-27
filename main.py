from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QTabWidget, QHBoxLayout, QPushButton, QLabel)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap
import pandas as pd
from telemetry import Tab1
from graph import Tab2
from map import Tab3
from extra import Tab4

file_link = "Cansat_Telemetry_Software\\Add Ons\\trial_data.csv"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(0, 0, 1920, 1080)
        self.setWindowTitle("Manual Layout Example")
        self.setStyleSheet("""
            QMainWindow {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 0,
                    stop: 0 #000, stop: 1 #8e82cd
                );
            }
        """)

        widget1 = QWidget(self)
        widget2 = QWidget(self)
        widget3 = QWidget(self)
        
        self.df = pd.read_csv(file_link)
        self.row_index = 0

        widget1.setGeometry(10, 10, 1900, 150)
        widget1.setStyleSheet("background-color:#15144a;")

        header_1 = QLabel("SOFTWARE STATE", widget1)
        header_1.setStyleSheet("font-size: 25px; color: #cbe6ca; background-color: None; font-weight:Bold;")
        header_1.setGeometry(25, 20, 580, 30)
        header_1.setAlignment(Qt.AlignCenter)

        self. header_1_input = QLabel("LAUNCH_PAD", widget1)
        self. header_1_input.setStyleSheet("font-size: 35px; color: Black; background-color: white; border: 4px solid brown;border-radius:25%;")
        self. header_1_input.setGeometry(190, 80, 240, 50)
        self. header_1_input.setAlignment(Qt.AlignCenter)

        header_2 = QLabel("TEAM KALPANA : 2024-CANSAT-ASI-023", widget1)
        header_2.setStyleSheet("font-size: 30px; color: #cbe6ca; background-color: None;font-weight:Bold;")
        header_2.setGeometry(640, 15, 630, 30)
        header_2.setAlignment(Qt.AlignCenter)

        logo_image = QPixmap("Cansat_Telemetry_Software\Add Ons\Team Kalpana Logo 1.png").scaledToWidth(100, Qt.TransformationMode.SmoothTransformation)
        logo_label = QLabel(widget1)
        logo_label.setPixmap(logo_image)
        logo_label.setGeometry(900, 60, 150, 100)

        header_3 = QWidget(widget1)
        header_3.setGeometry(1275, 20, 580, 30)
        header_3.setStyleSheet("background-color: None;")

        header_3_wid_1 = QLabel("TIME", header_3)
        header_3_wid_1.setStyleSheet("font-size: 25px; color: #cbe6ca;font-weight:Bold;")
        header_3_wid_1.setGeometry(40, 0, 240, 30)
        header_3_wid_1.setAlignment(Qt.AlignCenter)

        self.header_3_wid_1_input = QLabel("0", widget1)
        self.header_3_wid_1_input.setStyleSheet("font-size: 35px; color: Black; background-color: white; border: 4px solid brown;border-radius:25%;")
        self.header_3_wid_1_input.setGeometry(1335, 80, 200, 50)
        self.header_3_wid_1_input.setAlignment(Qt.AlignCenter)

        header_3_wid_2 = QLabel("PACKET COUNT", header_3)
        header_3_wid_2.setStyleSheet("font-size: 25px; color: #cbe6ca;font-weight:Bold;")
        header_3_wid_2.setGeometry(320, 0, 240, 30)
        header_3_wid_2.setAlignment(Qt.AlignCenter)

        self.header_3_wid_2_input = QLabel("0", widget1)
        self.header_3_wid_2_input.setStyleSheet("font-size: 35px; color: Black; background-color: white; border: 4px solid brown;border-radius:25%;")
        self.header_3_wid_2_input.setGeometry(1275 + 340, 80, 200, 50)
        self.header_3_wid_2_input.setAlignment(Qt.AlignCenter)

        widget2.setGeometry(10, 125, 1900, 875)
        widget2.setStyleSheet("background-color: None;")

        self.tabs = QTabWidget(self)
        self.tabs.setGeometry(10, 175, 1900, 725)
        self.tabs.addTab(Tab1(), "Telemetry Data")
        self.tabs.addTab(Tab2(), "Graphs")
        self.tabs.addTab(Tab3(), "Location and 3D Plotting")
        self.tabs.addTab(Tab4(), "Live Telecast")
        self.tabs.setStyleSheet("""
    QTabWidget::pane {
        border-top: 2px solid None;
        background: None;
    }
    QTabBar::tab {
        background:#b4d7e0;
        color: white;
        font-size: 25px;
        font-weight: Bold;
        border: 1px solid #b4d7e0;
        border-radius: 20px;  /* More rounded for pill shape */
        padding: 10px 20px;  /* Add more horizontal padding */
        margin: 2px;
        width: 429%;  
        height: 30px;  
    }
    QTabBar::tab:selected {
        background: #848f91;
        border-color: #848f91;
        border-radius: 20px;  /* Keep the selected tab pill-shaped */
    }
    QTabBar::tab:hover {
        background: #89a4ab;
        border-radius: 20px;  /* Ensure hover state also maintains the pill shape */
    }
""")

        widget3.setGeometry(10, 900, 1900, 100)

        layout3 = QHBoxLayout(widget3)

        footer_button_style = """
           QPushButton {
                border: 3px solid black; 
                border-radius: 15px;
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 1,
                    stop: 0 #230636, stop: 1 #00FFFF
                );
                font-size: 20px; 
                color: orange;
            }

            QPushButton:hover {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 1,
                    stop: 0 #00FFFF , stop: 1 #230636
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

        button6 = QPushButton("SIM Enable")
        button6.setStyleSheet(footer_button_style)
        button6.setFixedSize(150, 50)
        button6.clicked.connect(simulation_function)
        layout3.addWidget(button6)

        button7 = QPushButton("SIM Activate")
        button7.setStyleSheet(footer_button_style)
        button7.setFixedSize(150, 50)
        button7.clicked.connect(simulation_function)
        layout3.addWidget(button7)

        button8 = QPushButton("SIM Disable")
        button8.setStyleSheet(footer_button_style)
        button8.setFixedSize(150, 50)
        button8.clicked.connect(simulation_function)
        layout3.addWidget(button8)
       
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_data)
        self.timer.start(1000)  # Update every 1 second
        
    def update_data(self):
        #Method to update labels from CSV data.
        if self.row_index < len(self.df):
            # Get the current row's data
            current_row = self.df.iloc[self.row_index]
            # Update labels with the corresponding data
            time_stamping = current_row["TIME_STAMPING"]
            packet_count = current_row["PACKET_COUNT"]
            flight_software_state = current_row["FLIGHT_SOFTWARE_STATE"]
            # Set the label text
            self.header_3_wid_1_input.setText(str(time_stamping))
            self.header_3_wid_2_input.setText(str(packet_count))
            self.header_1_input.setText(str(flight_software_state))
            # Increment row index to move to the next row
            self.row_index += 1

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.showMaximized()
    app.exec_()