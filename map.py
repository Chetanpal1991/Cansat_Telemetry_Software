# tab2.py

from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QHBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, Qt

class Tab3(QWidget):
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
