from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QHBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtGui import QPixmap

class Tab4(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QHBoxLayout(self)

        live_feed_header = QLabel("LIVE TELECAST", self)
        live_feed_header.setStyleSheet("font-size: 50px; color: #cbe6ca; background-color: None; font-weight:Bold;")
        live_feed_header.setGeometry(695, 25, 600, 50)
        live_feed_header.setAlignment(Qt.AlignCenter)
        
        image_widget = QWidget(self)
        image_widget.setStyleSheet("""
            QWidget {
                background-color: None;
                padding: 20px;
            }
        """)  # You can adjust the padding, border, and background color as needed

        image_layout = QHBoxLayout(image_widget)
        image_layout.setContentsMargins(450, 60, 10, 10)

        logo_image = QPixmap("Cansat_Telemetry_Software/Add Ons/Live Feed Photo.png").scaledToWidth(1000, Qt.TransformationMode.SmoothTransformation)
        logo_label = QLabel(image_widget)
        logo_label.setPixmap(logo_image)

        image_layout.addWidget(logo_label)

        # Add the image_widget to the main layout with some spacing
        main_layout.addWidget(image_widget)
        main_layout.setSpacing(100)  # Spacing between the map and the image widget

    

        
