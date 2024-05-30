from pyqgis_scripting_ext.core import*

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
radiusKm = 20.0

csvPath= "C:\\Users\\00mar\\Desktop\\Master_Bolz\\Semester_2\\Advance_geomatics\\lessons\\stations.txt"
print(csvPath)
with open(csvPath,"r") as file:
    lines=file.readlines()
    
crsHelper = HCrs()
crsHelper.from_srid(4326)
crsHelper.to_srid(32632)
 
centerPoint = HPoint(lon, lat)

centerPoint32632= crsHelper.transform(centerPoint)

buffer = centerPoint32632.buffer(radiusKm*1000)

for line in lines:
    if line.startswith("#") or len(line)==0:
        continue
    line = line.strip()
    
    lineSplit=line.split(",")
    name = lineSplit[1].strip()
    latString = lineSplit[3]
    lonString = lineSplit[4]
    
    latDec = fromLatString(latString)
    lonDec = fromLonString(lonString)
    
    point = HPoint(lonDec, latDec)
    point32632 = crsHelper.transform(point)
    
    if buffer.intersects(point32632):
        distance = point32632.distance(centerPoint32632)
        print (name, distance/1000,"km", point)
   
   
        

        
        
