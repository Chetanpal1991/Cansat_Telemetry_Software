import sys
from PyQt5.QtWidgets import QMainWindow, QScrollArea, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QGridLayout, QLineEdit
from PyQt5.QtCore import Qt, QTimer
import pandas as pd

file_link = "Cansat_Telemetry_Software\\Add Ons\\trial_data.csv"

environment_columns = ["ALTITUDE", "PRESSURE", "TEMP", "TVOC", "eCO2"]
voltage_current_columns = ["VOLTAGE"]
gnss_columns = ["GNSS_TIME", "GNSS_LATITUDE", "GNSS_LONGITUDE", "GNSS_ALTITUDE", "GNSS_SATS"]
Accel_columns = ["ACC_R", "ACC_P", "ACC_Y"]
Gyro_columns = ["GYRO_R", "GYRO_P", "GYRO_Y"]

class Tab1(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()
        self.setLayout(layout)
        #self.widget = QWidget()
        #self.widget.setLayout(layout)

        telemetry_data1 = QWidget()  # my name is Ankur pal
        telemetry_data2 = QWidget()
        telemetry_data1.setStyleSheet(" border-radius:25%;")
        telemetry_data2.setStyleSheet(" border-radius:25%;")

        layout1 = QVBoxLayout(telemetry_data1)
        layout2 = QVBoxLayout(telemetry_data2)

        environment_data = QWidget()
        voltage_current = QWidget()
        gnss = QWidget()
        gnss.setFixedHeight(450)

        Accel = QWidget()
        Gyro = QWidget()

        layout1.addWidget(gnss)
        layout1.addWidget(voltage_current)
        layout2.addWidget(Accel)
        layout2.addWidget(Gyro)

        layout.addWidget(telemetry_data1)
        layout.addWidget(environment_data)
        layout.addWidget(telemetry_data2)

        environment_data_layout = QGridLayout()
        voltage_current_layout = QGridLayout()
        gnss_layout = QGridLayout()
        Accel_layout = QGridLayout()
        Gyro_layout = QGridLayout()

        environment_data.setLayout(environment_data_layout)
        voltage_current.setLayout(voltage_current_layout)
        gnss.setLayout(gnss_layout)
        Accel.setLayout(Accel_layout)
        Gyro.setLayout(Gyro_layout)

        # Labels and input fields for each section
        label1 = QLabel("ENVIRONMENTAL STATS", environment_data)
        label1.setStyleSheet("font-size: 20px; color: #cbe6ca;font-weight:Bold; border:None;")
        label1.setGeometry(160, 10, 270, 30)
        label1.setAlignment(Qt.AlignCenter)

        label2 = QLabel("ELECTRICAL STATS", voltage_current)
        label2.setStyleSheet("font-size: 20px; color: #cbe6ca;font-weight:Bold; border:None;")
        label2.setGeometry(160, 10, 270, 30)
        label2.setAlignment(Qt.AlignCenter)

        label3 = QLabel("GNSS STATS", gnss)
        label3.setStyleSheet("font-size: 20px; color: #cbe6ca;font-weight:Bold; border:None;")
        label3.setGeometry(160, 10, 270, 30)
        label3.setAlignment(Qt.AlignCenter)

        label4 = QLabel("ACCELEROMETER STATS", Accel)
        label4.setStyleSheet("font-size: 20px; color: #cbe6ca;font-weight:Bold; border:None;")
        label4.setGeometry(160, 10, 270, 30)
        label4.setAlignment(Qt.AlignCenter)

        label5 = QLabel("GYROSCOPE STATS", Gyro)
        label5.setStyleSheet("font-size: 20px; color: #cbe6ca;font-weight:Bold; border:None;")
        label5.setGeometry(160, 10, 270, 30)
        label5.setAlignment(Qt.AlignCenter)

        all_columns = [environment_columns, voltage_current_columns, gnss_columns, Accel_columns, Gyro_columns]
        component_layout_list = [environment_data_layout, voltage_current_layout, gnss_layout, Accel_layout, Gyro_layout]
        component_list = [environment_data, voltage_current, gnss, Accel, Gyro]

        # Create labels and input fields dynamically and store references to input fields
        self.input_fields = []
        for k, l, m in zip(all_columns, component_layout_list, component_list):
            input_field_list = []
            for i, j in zip(k, range(len(k))):
                label = QLabel(i, m)
                label.setStyleSheet("""
                    font-size: 20px;
                    color: white;
                    padding: 8px;
                    border-radius: 10px;
                    border: None;
                """)
                label.setFixedSize(300, 40)
                l.addWidget(label, j, 0)

                input_field = QLineEdit("0", m)
                input_field.setStyleSheet("""
                    font-size: 25px; 
                    color: black; 
                    background-color: white; 
                    border: 2px solid brown; 
                    border-radius: 10px;
                """)
                input_field.setFixedSize(200, 40)
                input_field.setAlignment(Qt.AlignCenter)
                l.addWidget(input_field, j, 1)
                input_field_list.append(input_field)
            self.input_fields.append(input_field_list)

            m.setStyleSheet("border: 4px solid #084705; border-radius:25%;")
            
        #self.Altitude = Altitude(self)
        #self.Altitude.setParent(self.centralWidget())  
        self.altitude_window = Altitude(input_fields=self.input_fields)
        #self.altitude_window.show() 
        self.show()

class Altitude(QMainWindow):
    def __init__(self, parent=None, input_fields=None):
        super().__init__()
        self.widget = QWidget()
        self.layout = QVBoxLayout()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)
        self.setStyleSheet('''border: 2px solid black''')
        
        # Store the input_fields so it can be accessed later in displayRow
        self.input_fields = input_fields

        self.data = pd.read_csv(file_link)
        self.row = 0
        self.rows = ["ALTITUDE"]

        self.label = QLabel()
        self.label.setWordWrap(True)
        self.scrollArea = QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.label)
        self.layout.addWidget(self.scrollArea)

        self.timer = QTimer()
        self.timer.timeout.connect(self.displayRow)
        self.timer.start(1000) 

    def displayRow(self):
        
        if self.row < len(self.data):
            # Read data from CSV and update corresponding fields
            row_data = self.data.iloc[self.row]
            for idx, column_name in enumerate(self.input_fields[0]):  # Update environment data fields
                column_value = str(row_data[environment_columns[idx]])  # Get the respective column data
                column_name.setText(column_value)  # Update the respective field with data

            for idx, column_name in enumerate(self.input_fields[1]):  # Update voltage data fields
                column_value = str(row_data[voltage_current_columns[idx]])  # Get the respective column data
                column_name.setText(column_value)

            for idx, column_name in enumerate(self.input_fields[2]):  # Update GNSS data fields
                column_value = str(row_data[gnss_columns[idx]])  # Get the respective column data
                column_name.setText(column_value)

            for idx, column_name in enumerate(self.input_fields[3]):  # Update accelerometer data fields
                column_value = str(row_data[Accel_columns[idx]])  # Get the respective column data
                column_name.setText(column_value)

            for idx, column_name in enumerate(self.input_fields[4]):  # Update gyroscope data fields
                column_value = str(row_data[Gyro_columns[idx]])  # Get the respective column data
                column_name.setText(column_value)

            # Move to the next row
            self.row += 1
        else:
            self.timer.stop()

        self.label.setText("\n".join(self.rows))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet("font-size: 25px; font-weight: bold;")