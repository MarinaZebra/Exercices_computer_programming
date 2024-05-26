from pyqgis_scripting_ext.core import*

csvPath= "C:\\Users\\00mar\\Desktop\\Master_Bolz\\Semester_2\\Advance_geomatics\\lessons\\stations.txt"
print(csvPath)
with open(csvPath,"r") as file:
    lines=file.readlines()

LAT_List=[]
LON_List=[]
pointList=[]
canvas = HMapCanvas()
for line in lines[1:]: 
    line= line.strip()
    line_split=line.split(",")
    LAT=line_split[3].split(":")
    LON=line_split[4].split(":")
    lat = float(LAT[0])+float(LAT[1])/60+float(LAT[2])/3600
    lon = float(LON[0])+float(LON[1])/60+float(LON[2])/3600
    LAT_List.append(lat)
    LON_List.append(lon) 
    pointList.append([lon, lat])
multiPoints = HMultiPoint.fromCoords(pointList)
#print(multiPoints.asWkt())
canvas.add_geometry(multiPoints,"magenta",5)


bounds = [0,0,70,100]
canvas.set_extent(bounds)
canvas.show()
        






