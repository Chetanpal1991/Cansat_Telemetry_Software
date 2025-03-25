# from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout
# from PyQt5.QtCore import  Qt, QTimer
# from PyQt5.QtGui import QPixmap, QImage, QPixmap
# import cv2

# class Tab4(QWidget):
#     def __init__(self):
#         super().__init__()
#         main_layout = QVBoxLayout(self)  # Main layout as vertical to stack header and feed

#         text = QLabel("code under process",self)
#         text.setStyleSheet("font-size: 45px;")
#         text.setAlignment(Qt.AlignCenter)
#         main_layout.addWidget(text)

#         # Live feed header
#         live_feed_header = QLabel("LIVE TELECAST", self)
#         live_feed_header.setStyleSheet("font-size: 50px; color: #cbe6ca; background-color: None; font-weight:Bold;")
#         live_feed_header.setAlignment(Qt.AlignCenter)

#         # Widget for live feed
#         image_widget = QWidget(self)
#         image_widget.setStyleSheet("""
#             QWidget {
#                 background-color: None;
#                 padding: 20px;
#             }
#         """)

#         image_layout = QHBoxLayout(image_widget)
#         #image_layout.setContentsMargins(450, 60, 400, 400)

#         self.live_feed_label = QLabel(image_widget)
#         self.live_feed_label.setFixedSize(1000, 562)  # Dimensions of the image
#         image_layout.addWidget(self.live_feed_label)

#         # Add widgets to the main layout
#         main_layout.addWidget(live_feed_header)
#         main_layout.addWidget(image_widget)

#         # Start live feed
#         self.stream_url = "http://192.168.29.156:8080/video"  # Replace with your phone camera stream URL
#         self.capture = cv2.VideoCapture(self.stream_url)

#         # Timer for updating live feed
#         self.timer = QTimer(self)
#         self.timer.timeout.connect(self.update_frame)
#         self.timer.start(30)  # Update every 30ms

#     def update_frame(self):
#         ret, frame = self.capture.read()
#         if ret:
#             frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
#             height, width, channels = frame.shape
#             qimg = QImage(frame.data, width, height, channels * width, QImage.Format_RGB888)
#             pixmap = QPixmap.fromImage(qimg).scaled(
#                 self.live_feed_label.width(), self.live_feed_label.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation
#             )
#             self.live_feed_label.setPixmap(pixmap)


import sys
import cv2
import os;
import numpy as np
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget ,QHBoxLayout
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer, Qt



class Tab4(QWidget):
    def __init__(self):
        super().__init__()

        # Setup window
        self.setWindowTitle("Live Telecast in PyQt5")
        self.setGeometry(0, 0, 1920, 1080)

       
        heading = QLabel(" Live Telecast of the Cansat", self)
        heading.setStyleSheet("""
                              font-weight:800;
                              color: #cbe6ca;
                              font-size:30px;
                              background-color:#15144a;
                              padding:10px;
                              padding-left: 50px; 
                              padding-right: 50px; 
                              border-radius:20px;
                              """)  
         # Video Label
        self.video_label = QLabel(self)
        self.video_label.setFixedSize(1400, 650)
        self.video_label.setAlignment(Qt.AlignCenter)
        # Layout
        
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter) 
        layout.addSpacing(20)
        layout.addWidget(heading, alignment=Qt.AlignCenter)
        layout.addSpacing(20)
        layout.addWidget(self.video_label, alignment=Qt.AlignHCenter)
        self.setLayout(layout)
        
        # OpenCV Video Capture
        
        self.cap = cv2.VideoCapture("http://192.168.1.35:8080/video") # 0 is default video-http://192.168.29.156:8080/video
        # if not self.cap.isOpened():
        #     self.video_label.setFixedSize(0, 0)
        #     h2=QLabel("Error : Could not open webcam ",self)
        #     h2.setStyleSheet(""" 
        #         font-weight:800;
        #         color:#e1dfe3;
        #         font-size:18px;
        #         background-color:red;
        #         padding:10px;
        #         padding-left: 30px; 
        #         padding-right: 30px; 
        #         border-radius:10px;
        #         border: 2px solid black;
        #         """)
        #     layout.addWidget(h2,alignment=Qt.AlignCenter)
        #     self.timer = QTimer(self)
        #     self.timer.timeout.connect(self.update_frame)
        #     self.timer.timeout.connect(self.update_cam)
        #     self.timer.start(30) 
        #     # return

        # Timer to update frames
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)  # Update every 30ms
    
    def update_frame(self):
        if not hasattr(self, 'cap') or not self.cap.isOpened():
            self.video_label.setText("Waiting ....")
            self.video_label.setStyleSheet("color:red;font-size:30px;")
            self.cap = cv2.VideoCapture("http://192.168.1.35:8080/video")
        ret, frame = self.cap.read()
        if not ret : 
            self.cap.release()
            self.cap = cv2.VideoCapture("http://192.168.1.35:8080/video")
        if ret:
            # Convert BGR to RGB for PyQt
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame.shape
            bytes_per_line = ch * w
            q_img = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
            # Display in QLabel
            pixmap = QPixmap.fromImage(q_img).scaled(
                self.video_label.width(), self.video_label.height(),
                Qt.KeepAspectRatio, Qt.SmoothTransformation
            )
            self.video_label.setPixmap(pixmap)

    def closeEvent(self, event):
        """ Close the camera when exiting the application """
        self.cap.release()
        event.accept()


# Run the Application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Tab4()
    window.show()
    sys.exit(app.exec_())
