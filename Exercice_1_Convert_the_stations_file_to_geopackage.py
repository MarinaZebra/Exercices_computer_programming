from pyqgis_scripting_ext.core import *

folder = "C:\\Users\\00mar\\Desktop\\Master_Bolz\\Semester_2\\Advance_geomatics\\Archivos_Gis\\natural_earth_vector.gpkg\\packages\\"
tmpFolder = f"{folder}/tmp"

stationsPath = "C:\\Users\\00mar\\Desktop\\Master_Bolz\\Semester_2\\Advance_geomatics\\lessons\\stations.txt"

# necessary functions 
def fromLatString(latString):
    sign_lat = latString [0]
    latDegrees = float(latString[1:3])
    latMinutes = float(latString[4:6])
    latSeconds = float(latString[7:9])
    lat = latDegrees + latMinutes/60 + latSeconds/3600
    if sign_lat == '-':
        lat = lat * -1 
    return lat 
    
def fromLonString(lonString):
    sign_lon = lonString [0]
    lonDegrees = float(lonString[1:4])
    lonMinutes = float(lonString[5:7])
    lonSeconds = float(lonString[8:10])
    lon = lonDegrees + lonMinutes/60 + lonSeconds/3600
    if sign_lon == '-':
        lon = lon * -1 
    return lon 

with open(stationsPath, 'r') as file:
    lines= file.readlines()
    
schema = {
    "stationid": "int",
    "name": "string",
    "country": "string",
    "height": "double"
}
stationsLayer= HVectorLayer.new("stations","Point","EPG:4326", schema)
for line in lines :
    line = line.strip()
    
    if not line.startswith("#"):
        lineSplit = line.split(",")
        latString = lineSplit[3]
        lonString = lineSplit[4]
        lat = fromLatString (latString)
        lon = fromLonString (lonString)
        
    point = HPoint (lon, lat)
    
    attributes = [
        int(lineSplit[0]),
        lineSplit[1],
        lineSplit[2],
        lineSplit[-1],
    ]
    
    stationsLayer.add_feature(point,attributes)

outputPath = f"{tmpFolder}/stations.gpkg"
error = stationsLayer.dump_to_gpkg(outputPath,overwrite=True)
if error:
    print(error)

dumpedStationsLayer = HVectorLayer.open(outputPath, "stations")
HMap.add_layer(stationsLayer)
print(line)
    