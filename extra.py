from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import  Qt, QTimer
from PyQt5.QtGui import QPixmap, QImage, QPixmap
import cv2

class Tab4(QWidget):
    def __init__(self):
        super().__init__()

        print("Hello world")

    #     main_layout = QVBoxLayout(self)  # Main layout as vertical to stack header and feed

    #     # Live feed header
    #     live_feed_header = QLabel("LIVE TELECAST", self)
    #     live_feed_header.setStyleSheet("font-size: 50px; color: #cbe6ca; background-color: None; font-weight:Bold;")
    #     live_feed_header.setAlignment(Qt.AlignCenter)

    #     # Widget for live feed
    #     image_widget = QWidget(self)
    #     image_widget.setStyleSheet("""
    #         QWidget {
    #             background-color: None;
    #             padding: 20px;
    #         }
    #     """)

    #     image_layout = QHBoxLayout(image_widget)
    #     #image_layout.setContentsMargins(450, 60, 400, 400)

    #     self.live_feed_label = QLabel(image_widget)
    #     self.live_feed_label.setFixedSize(1000, 562)  # Dimensions of the image
    #     #self.live_feed_label.setStyleSheet("background-color: black;")  # Placeholder background
    #     image_layout.addWidget(self.live_feed_label)

    #     # Add widgets to the main layout
    #     main_layout.addWidget(live_feed_header)
    #     main_layout.addWidget(image_widget)

    #     # Start live feed
    #     self.stream_url = "http://192.168.0.186:8080/video"  # Replace with your phone camera stream URL
    #     self.capture = cv2.VideoCapture(self.stream_url)

    #     # Timer for updating live feed
    #     self.timer = QTimer(self)
    #     self.timer.timeout.connect(self.update_frame)
    #     self.timer.start(30)  # Update every 30ms

    # def update_frame(self):
    #     ret, frame = self.capture.read()
    #     if ret:
    #         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
    #         height, width, channels = frame.shape
    #         qimg = QImage(frame.data, width, height, channels * width, QImage.Format_RGB888)
    #         pixmap = QPixmap.fromImage(qimg).scaled(
    #             self.live_feed_label.width(), self.live_feed_label.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation
    #         )
    #         self.live_feed_label.setPixmap(pixmap)


