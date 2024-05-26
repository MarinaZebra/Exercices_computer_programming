from pyqgis_scripting_ext.core import*
# HMap.remove_layers_by_name(["OpenStreetMap"]
#Reading the file 
csvPath= "C:\\Users\\00mar\\Desktop\\Master_Bolz\\Semester_2\\Advance_geomatics\\Exam_simulation\\22yr_T10MX"

print(csvPath)
with open(csvPath,"r") as file:
    lines=file.readlines()

canvas = HMapCanvas.new()
osm = HMap.get_osm_layer()
HMap.add_layer(osm)
canvas.set_extent([-18000000,-8000000,18000000,8000000])
canvas.set_layers([osm])

crsHelper = HCrs()
crsHelper.from_srid(4326)#open street map data (latlong)
crsHelper.to_srid(3857)#reference system for webmapping adapted to the all word

folder = "C:\\Users\\00mar\\Desktop\\Master_Bolz\\Semester_2\\Advance_geomatics\\Archivos_Gis\\natural_earth_vector.gpkg\\packages\\"
geopackagePath = folder + "natural_earth_vector.gpkg"
countriesName = "ne_50m_admin_0_countries"
countriesLayer = HVectorLayer.open(geopackagePath, countriesName)
# print("Attributes for France:")
nameIndex=countriesLayer.field_index("NAME")
countriesFeatures = countriesLayer.features()
for feature in countriesFeatures:
    name = feature.attributes[nameIndex]
    if name == "Canada":
        france_geometry = feature.geometry#geometry is the polygon of france

country_geometry3857= crsHelper.transform(france_geometry)
canvas.add_geometry(country_geometry3857,"green", 3)

#Cleaning the file 
for line in lines[16:]:
    line = line.strip()
    if len(line) != 0 and line[0] != "#":
        line= line.strip()
        line_split=line.split(" ")
    
        lon_south = float(line_split[0])
        lat_west= float(line_split[1])
        average= float(line_split[14])
    
#Create the corners of the polygon 

        lat_east = lat_west + 1
        lon_north = lon_south + 1
    
 # creating a square polygon    
 
        corner1 = (lat_west, lon_south)
        corner2 = (lat_west, lon_north)
        corner3 = (lat_east, lon_north)
        corner4 = (lat_east, lon_south)
        corner5 = (lat_west, lon_south)
    
        coords = [corner1,corner2,corner3,corner4,corner5]
        polygon4326 = HPolygon.fromCoords(coords)
        polygon3857= crsHelper.transform(polygon4326)
        if polygon3857.intersects(country_geometry3857) == True:
            if average < 0:
                canvas.add_geometry(polygon3857.intersection(country_geometry3857),"blue", 1)
            elif 0 <= average < 10:
                canvas.add_geometry(polygon3857.intersection(country_geometry3857),"olive", 1)
            elif 10 <= average < 15:
                canvas.add_geometry(polygon3857.intersection(country_geometry3857),"green", 1)
            elif 15 <= average < 25:
                canvas.add_geometry(polygon3857.intersection(country_geometry3857),"orange", 1)
            elif average > 25:
                canvas.add_geometry(polygon3857.intersection(country_geometry3857),"red", 1)

# canvas.set_extent([-90,-180,90,180])
# canvas.set_extent(polygon3857.bbox())

canvas.show()

print(g1.intersects(g2)) 
    