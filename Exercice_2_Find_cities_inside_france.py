from pyqgis_scripting_ext.core import*

#cleanup
HMap.remove_layers_by_name(["OpenStreetMap"])

folder = "C:\\Users\\00mar\\Desktop\\Master_Bolz\\Semester_2\\Advance_geomatics\\Archivos_Gis\\natural_earth_vector.gpkg\\packages\\"

geopackagePath = folder + "natural_earth_vector.gpkg"

countriesName = "ne_50m_admin_0_countries"

#load openstreetmap titles layer

osm = HMap.get_osm_layer()
HMap.add_layer(osm)

#load the countries layer
countriesLayer = HVectorLayer.open(geopackagePath, countriesName)

# crs = countriesLayer.prjcode
# print("Projection: ", crs)
# print("Spatial extent:", countriesLayer.bbox())
# print("Feature count:", countriesLayer.size())

print("Attributes for France:")
nameIndex=countriesLayer.field_index("NAME")
countriesFeatures = countriesLayer.features()
for feature in countriesFeatures:
    name = feature.attributes[nameIndex]
    if name == "France":
        france_geometry = feature.geometry#geometry is the polygon of france
        polygon = "Geom:",france_geometry.asWkt()[:50]+"..."
        print(polygon)

crsHelper = HCrs()
crsHelper.from_srid(4326)#open street map data (latlong)
crsHelper.to_srid(3857)#reference system for webmapping adapted to the all word

france_geometry= crsHelper.transform(france_geometry)

canvas = HMapCanvas.new()
canvas.set_layers([osm])
canvas.add_geometry(france_geometry)


cities = "ne_50m_populated_places"
citiesLayer = HVectorLayer.open(geopackagePath, cities)


print("Attributes for cities:")
nameIndex=citiesLayer.field_index("NAME")
citiesFeatures = citiesLayer.features()
for feature in citiesFeatures:
    cities_geometry=feature.geometry
    cities_geometry=crsHelper.transform(cities_geometry)
    if cities_geometry.intersects(france_geometry):
        print(feature.attributes[nameIndex])
        canvas.add_geometry(cities_geometry)

canvas.set_extent([-18000000,-8000000,18000000,8000000])
canvas.show()


