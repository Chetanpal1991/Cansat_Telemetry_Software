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

class MapWidget(QWebEngineView):
    def __init__(self, csv_file):
        super().__init__()
        self.setFixedSize(750, 650)
        self.setStyleSheet(""" 
            QWebEngineView {
                border: 2px solid #4b0082;
                border-radius: 25%;
            }
        """)
        
        # Create HTML with embedded Google Maps and JavaScript functions
        self.html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Google Maps with Marker</title>
            <style>
                html, body, #map {
                    height: 100%;
                    margin: 0;
                    padding: 0;
                }
            </style>
            <script src="https://maps.googleapis.com/maps/api/js?v=3.exp"></script>
            <script>
                var map;
                var marker;
                var path = [];
                var polyline;
                
                function initMap() {
                    // Default center (can be anywhere, will be updated)
                    var center = {lat: 0, lng: 0};
                    
                    map = new google.maps.Map(document.getElementById('map'), {
                        zoom: 15,
                        center: center,
                        mapTypeId: google.maps.MapTypeId.HYBRID
                    });
                    
                    // Create initial marker
                    marker = new google.maps.Marker({
                        position: center,
                        map: map,
                        title: 'Current Position'
                    });
                    
                    // Create polyline to show path
                    polyline = new google.maps.Polyline({
                        path: path,
                        geodesic: true,
                        strokeColor: '#FF0000',
                        strokeOpacity: 1.0,
                        strokeWeight: 2,
                        map: map
                    });
                }
                
                function updateMarker(lat, lng) {
                    var newPosition = new google.maps.LatLng(lat, lng);
                    
                    // Update marker position
                    marker.setPosition(newPosition);
                    
                    // Add point to path
                    path.push(newPosition);
                    polyline.setPath(path);
                    
                    // Center map on marker
                    map.setCenter(newPosition);
                }
                
                // Initialize the map when the page loads
                google.maps.event.addDomListener(window, 'load', initMap);
            </script>
        </head>
        <body>
            <div id="map"></div>
        </body>
        </html>
        """
        
        # Load the HTML
        self.setHtml(self.html)
        
        # Load coordinates from CSV
        self.coordinates = self.load_coordinates(csv_file)
        self.current_index = 0
        
        # Timer for 1 Hz updates
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_map)
        self.timer.start(1000)  # 1 Hz
    
    def load_coordinates(self, csv_file):
        try:
            # Read the CSV file to inspect its structure
            df = pd.read_csv(csv_file)
            print(f"CSV Headers: {df.columns.tolist()}")  # Debug info
            
            # Try to identify latitude and longitude columns
            lat_column = None
            lon_column = None
            
            # Common names for latitude columns
            lat_options = ['latitude', 'lat', 'GPS_LAT', 'gps_lat', 'LAT', 'Latitude', 'GPS_LATITUDE']
            # Common names for longitude columns
            lon_options = ['longitude', 'lon', 'lng', 'GPS_LON', 'gps_lon', 'LON', 'Longitude', 'GPS_LONGITUDE']
            
            # Find matching column names
            for option in lat_options:
                if option in df.columns:
                    lat_column = option
                    break
            
            for option in lon_options:
                if option in df.columns:
                    lon_column = option
                    break
            
            # If we couldn't find the columns by name, use mock data for testing
            if lat_column is None or lon_column is None:
                print("Could not find standard latitude/longitude columns.")
                print("Available columns:", df.columns.tolist())
                
                # Generate mock coordinates for testing
                print("Using mock GPS data for testing")
                coordinates = []
                
                # Create a spiral pattern of coordinates
                center_lat, center_lon = 37.7749, -122.4194  # San Francisco
                for i in range(100):
                    angle = 0.1 * i
                    radius = 0.0001 * i
                    lat = center_lat + radius * np.cos(angle)
                    lon = center_lon + radius * np.sin(angle)
                    coordinates.append({"latitude": lat, "longitude": lon})
                
                return coordinates
            
            # Process the actual data if columns were found
            coordinates = []
            for _, row in df.iterrows():
                try:
                    lat_value = float(row[lat_column])
                    lon_value = float(row[lon_column])
                    coordinates.append({"latitude": lat_value, "longitude": lon_value})
                except (ValueError, KeyError) as e:
                    print(f"Error processing row: {e}")
                    continue
                    
            return coordinates
                
        except Exception as e:
            print(f"Error loading coordinates: {e}")
            # Return mock data to prevent the application from crashing
            return [{"latitude": 37.7749, "longitude": -122.4194}]
    
    def update_map(self):
        if self.current_index < len(self.coordinates):
            coord = self.coordinates[self.current_index]
            lat, lng = coord["latitude"], coord["longitude"]
            
            # Use JavaScript to update the marker position
            js_code = f"updateMarker({lat}, {lng});"
            self.page().runJavaScript(js_code)
            
            self.current_index += 1
        else:
            self.timer.stop()  # Stop updating when data ends

class Tab3(QWidget):
    def __init__(self):
        super().__init__()

        # Debug: Print CSV contents
        csv_path = r'Cansat_Telemetry_Software\Add Ons\trial_data.csv'
        try:
            df = pd.read_csv(csv_path)
            print("CSV columns:", df.columns.tolist())
            print("First few rows:")
            print(df.head())
        except Exception as e:
            print(f"Error reading CSV: {e}")

        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        
        # Create the map widget with your CSV file
        self.map_view = MapWidget(r'Cansat_Telemetry_Software\Add Ons\trial_data.csv')
        main_layout.addWidget(self.map_view)

        # Create an instance of DataPlotter3D
        self.plotter = DataPlotter3D(r'Cansat_Telemetry_Software\Add Ons\trial_data.csv')
        main_layout.addWidget(self.plotter.canvas)  # Add only the canvas to the layout

if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainWindow = QMainWindow()
    mainWindow.setWindowTitle('Google Maps and 3D Line Plot Example')

    tab = Tab3()
    mainWindow.setCentralWidget(tab)

    mainWindow.show()
    sys.exit(app.exec_())
