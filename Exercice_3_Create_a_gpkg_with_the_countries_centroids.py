from pyqgis_scripting_ext.core import *

folder = "C:\\Users\\00mar\\Desktop\\Master_Bolz\\Semester_2\\Advance_geomatics\\Archivos_Gis\\natural_earth_vector.gpkg\\packages\\"
geopackagePath = folder + "natural_earth_vector.gpkg"
countriesName = "ne_50m_admin_0_countries"

osm = HMap.get_osm_layer()
HMap.add_layer(osm)

schema = {
    "name": "string"
}

centroidsLayer = HVectorLayer.new("centroids","Point","EPSG:4326", schema)

countryLayer = HVectorLayer.open(geopackagePath, countriesName)

nameIndex = countryLayer.field_index("NAME")
nonInCountryList = []
for country in countryLayer.features ():
    countryGeom = country.geometry
    name = country.attributes[nameIndex]
    
    centroid= countryGeom.centroid()
    centroidsLayer.add_feature(centroid, [name])
    if not centroid.intersects(countryGeom):
        nonInCountryList.append(name)
    
simpleStyle= HMarker("circle", 10) + HLabel("name") + HHalo ()
centroidsLayer.set_style(simpleStyle)
HMap.add_layer(centroidsLayer)
print("Countries with centroids not inside the main polygon: ")
if not centroid.intersects(countryGeom):
        nonInCountryList.append(centroid)
print(nonInCountryList)
    
   
  


    
    
    