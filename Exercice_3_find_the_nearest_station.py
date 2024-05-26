from pyqgis_scripting_ext.core import *

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
    
#Here the script starts
lon=11.34999
lat=46.4908
csvPath= "C:\\Users\\00mar\\Desktop\\Master_Bolz\\Semester_2\\Advance_geomatics\\lessons\\stations.txt"
print(csvPath)
with open(csvPath,"r") as file:
    lines=file.readlines()
    
    minDistance = 9999
    nearestStationName = "none"
    nearestStationPoint = None
    
    
for line in lines [1:10]:
    line=line.strip()
    
    lineSplit=line.split(",")
    name = lineSplit[1].strip()
    latString = lineSplit[3]
    lonStrip = lineSplit[4]
    latr= fromLatString(latString)
    print(name, latString, lonStrip)
    
    latDec = fromLatString(latString)
    lonDec = fromLonString(lonString)
    
    # print mame, Lat Dec, lonDeC)
    Point = HPoint(lonDec, latDec)
    
    distance = point. distance(centerPoint)
    if distance < minDistance: 
        miniDistance = distance 
        nearestStationName = name 
        nearestStationPoint = point 
        
print(nearestStationName, "->",nearestStationPoint)