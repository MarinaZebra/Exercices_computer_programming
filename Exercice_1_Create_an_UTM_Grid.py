# Initialize an empty list to hold the polygons
polygons = []

# Set the extent (width) of each zone to 6 degrees
extent = 6

# Loop over the range of longitudes from -180 to 180 in increments of 6 degrees
for lon in range(-180, 180, extent):
    minX = lon             # Set the minimum longitude (west boundary of the zone)
    maxX = lon + extent    # Set the maximum longitude (east boundary of the zone)
    minY = -84             # Set the minimum latitude (south boundary)
    maxY = 84              # Set the maximum latitude (north boundary)
    
    # Define the coordinates of the polygon representing the zone
    coords = [[minX, minY], [minX, maxY], [maxX, maxY], [maxX, minY], [minX, minY]]
    
    # Create a polygon object from the coordinates
    polygon = HPolygon.fromCoords(coords)
    
    # Add the polygon to the list of polygons
    polygons.append(polygon)

# Create a new canvas for displaying the map
canvas = HMapCanvas.new()   

# Add each polygon to the canvas
for polygon in polygons: 
    canvas.add_geometry(polygon)

# Set the extent of the canvas to cover the specified longitude and latitude range
canvas.set_extent([-370,-90,370,90])
# Display the canvas with the polygons
canvas.show()
