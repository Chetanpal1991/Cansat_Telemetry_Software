import sys, csv
import numpy as np
import pandas as pd
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QApplication, QMainWindow, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, QTimer
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class DataPlotter3D(QWidget):
    def __init__(self, csv_file):
        super().__init__()

        self.csv_file = csv_file
        self.data = pd.read_csv(self.csv_file)
        self.index = 0  # To keep track of current data point
        
        # Create a matplotlib figure
        self.fig = Figure(figsize=(24, 6))
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setFixedSize(750, 650)  # Set size for the canvas
        self.fig.set_facecolor((0.5, 0.3, 0.8, 0.5))  # Set background color for the figure
        
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.ax.set_facecolor("None")

        # Set up a timer for updating the plot every 1 second (1Hz)
        self.timer = QTimer(self)
        self.timer.setInterval(1000)  # 1000 ms = 1 second
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()
 
    def update_plot(self):
        if self.index >= len(self.data):
            self.timer.stop()
            return

        gyro_r = self.data['GYRO_R'][:self.index + 1].to_numpy()
        gyro_p = self.data['GYRO_P'][:self.index + 1].to_numpy()
        gyro_y = self.data['GYRO_Y'][:self.index + 1].to_numpy()

        # Convert 1D arrays to 2D grids for surface plotting
        LON, LAT = np.meshgrid(gyro_r, gyro_p)
        ALT = np.tile(gyro_y, (len(gyro_p), 1))

        # Clear the previous plot
        self.ax.clear()

        # Plot the surface
        self.ax.plot_surface(LON, LAT, ALT, cmap='viridis', edgecolor='none')

        # Set bold title and labels
        self.ax.set_title('3D Surface Plot', fontsize=24, fontweight='bold')
        self.ax.set_xlabel('GYRO_R', fontsize=16)
        self.ax.set_ylabel('GYRO_P', fontsize=16)
        self.ax.set_zlabel('GYRO_Y', fontsize=16)

        # Refresh the canvas
        self.canvas.draw()

        # Move to the next data point
        self.index += 1

class MapApp(QWidget):
    def __init__(self, csv_file):
        super().__init__()
        self.setWindowTitle("Google Maps in PyQt5")
        self.resize(800, 600)

        # Layout
        layout = QVBoxLayout(self)
        self.browser = QWebEngineView()
        layout.addWidget(self.browser)

        # Load the HTML file
        self.browser.setHtml(open("map.html").read())

        # Load coordinates from CSV
        self.coordinates = self.load_coordinates(csv_file)
        self.current_index = 0

        # Timer for 1 Hz updates
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_map)
        self.timer.start(1000)  # 1 Hz

    def load_coordinates(self, csv_file):
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            return [{"latitude": float(row["latitude"]), "longitude": float(row["longitude"])} for row in reader]

    def update_map(self):
        if self.current_index < len(self.coordinates):
            coord = self.coordinates[self.current_index]
            lat, lng = coord["latitude"], coord["longitude"]
            self.browser.page().runJavaScript(f"updateMarker({lat}, {lng});")
            self.current_index += 1
        else:
            self.timer.stop()  # Stop updating when data ends

class Tab3(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        
        # Load and display the map
        
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

        # Create an instance of DataPlotter3D
        self.plotter = DataPlotter3D(r'Cansat_Telemetry_Software\Add Ons\trial_data.csv')  # Replace with your CSV file path
        self.plotter.setFixedSize(750, 650)  # Ensure the plotter has the same size as the map
        main_layout.addWidget(self.plotter.canvas)  # Add only the canvas to the layout

    def process_data():
        # Logic to handle telemetry data processing
        print("Tab1: Processing telemetry data...")

if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainWindow = QMainWindow()
    mainWindow.setWindowTitle('Google Maps and 3D Line Plot Example')

    tab = Tab3()
    mainWindow.setCentralWidget(tab)

    mainWindow.show()
    sys.exit(app.exec_())