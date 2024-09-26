from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QGridLayout
from PyQt5.QtCore import Qt

class Tab1(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()
        self.setLayout(layout)

        telemetry_data1 = QWidget() #my name is Ankur pal
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

        environment_columns = ["ALTITUDE", "PRESSURE", "TEMP", "TVOC", "eCO2"]
        voltage_current_columns = ["Voltage"]
        gnss_columns = ["GNSS_TIME","GNSS_LATITUDE","GNSS_LONGITUDE","GNSS_ALTITUDE","GNSS_SATS"]
        Accel_columns = ["ACC_R    (Roll)","ACC_P    (Pitch)","ACC_Y    (Yaw)"]
        Gyro_columns =  ["GYRO_R   (Roll)","GYRO_P   (Pitch)","GYRO_Y   (Yaw)"]

        component_list = [environment_data,voltage_current,gnss,Accel,Gyro]
        component_layout_list = [environment_data_layout,voltage_current_layout,gnss_layout,Accel_layout,Gyro_layout]
        all_columns = [environment_columns,voltage_current_columns,gnss_columns,Accel_columns,Gyro_columns]

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

        for k,l,m in zip(all_columns,component_layout_list,component_list):
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

                input_field = QLabel("0", environment_data)
                input_field.setStyleSheet("""
                    font-size: 20px; 
                    color: black; 
                    background-color: white; 
                    border: 2px solid brown; 
                    border-radius: 10px;
                """)
                input_field.setFixedSize(200, 40)
                input_field.setAlignment(Qt.AlignCenter)
                l.addWidget(input_field, j, 1)
                m.setStyleSheet("border: 4px solid #084705; border-radius:25%;")



