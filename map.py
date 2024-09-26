from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

class Tab3(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(80, 0, 0, 0) 

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

        # Create the figure and canvas for the 3D plot
        self.fig4 = Figure(figsize=(24, 6))
        self.canvas4 = FigureCanvas(self.fig4)
        self.canvas4.setFixedSize(750, 650)  # Set size for the canvas
        self.fig4.set_facecolor((0.5, 0.3, 0.8, 0.5))  # Set background color for the figure
        

        main_layout.addWidget(self.canvas4)

        # Call the function to plot the 3D graph
        self.plot_3d_graph()

        # Create a new widget to wrap the image
    def plot_3d_graph(self):
        # Add a 3D subplot
        ax = self.fig4.add_subplot(111, projection='3d')
        ax.set_facecolor("None")

        # Sample 3D data
        x = np.linspace(-5, 5, 100)
        y = np.linspace(-5, 5, 100)
        x, y = np.meshgrid(x, y)
        z = np.sin(np.sqrt(x**2 + y**2))

        # Plot a 3D surface
        ax.plot_surface(x, y, z, cmap='viridis')

        # Set bold title and labels
        ax.set_title('3D Surface Plot', fontsize=24, fontweight='bold')
        ax.set_xlabel('GNSS Latitude', fontsize=16)
        ax.set_ylabel('GNSS Longitude', fontsize=16)
        ax.set_zlabel('GNSS Altitude', fontsize=16)

        # Draw the plot on the canvas
        self.canvas4.draw()
        

        
