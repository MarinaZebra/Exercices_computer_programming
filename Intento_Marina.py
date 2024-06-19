from pyqgis_scripting_ext.core import *

folder = "C:\\Users\\00mar\\Desktop\\Master_Bolz\\Semester_2\\Advance_geomatics\\Ejercicio_examen\\"

# import the http requests library to get stuff from the internet
import requests
# import the url parsing library to urlencode the query
import urllib.parse
# define the query to launch
endpointUrl = "https://query.wikidata.org/sparql?query=";
# define the query to launch
query = """SELECT ?place ?placeLabel ?placeDescription ?location ?elev ?image WHERE
{
    ?place p:P2044/psv:P2044 ?placeElev.
    ?place wdt:P17 wd:Q38.
    ?placeElev wikibase:quantityAmount ?elev.
    ?placeElev wikibase:quantityUnit ?unit.
    bind(0.01 as ?km).
    filter( (?elev < ?km*1000 && ?unit = wd:Q11573)
    || (?elev < ?km*3281 && ?unit = wd:Q3710)
    || (?elev < ?km && ?unit = wd:Q828224) ).
    ?place wdt:P625 ?location.
    optional { ?place wdt:P18 ?image }
    SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en" }
} """

# URL encode the query string
encoded_query = urllib.parse.quote(query)
# prepare the final url
url = f"{endpointUrl}{encoded_query}&format=json"
# run the query online and get the produced result as a dictionary
r=requests.get(url)
result = r.json()
#print(result)

#create a geopackage based on the result, both the georaphic and aphanumeric part
crsHelper = HCrs()
crsHelper.from_srid(4326)
crsHelper.to_srid(3857)
#therefore first set the outline of the geopackage
fields = {
    "place": "String",
    "place_Label": "String",
    "elevation": "Integer"
}
#location not because this is saved as the point
entityslayer = HVectorLayer.new("locations", "Point", "EPSG:3857", fields)

for entity in result['results']['bindings']:
    place = entity['place']['value']
    place_Label = entity['placeLabel']['value']
    elevation = float(entity['elev']['value'])
    location = entity['location']['value']
    
    coordssplit = location.split(" ")
    lon = coordssplit[0][6:]
    lon = float(lon)
    
    lat = coordssplit[1][:-1]
    lat = float(lat)
    
    POINT = HPoint(lon, lat)
    Point = crsHelper.transform(POINT)
    
    entityslayer.add_feature(Point, [place, place_Label, elevation])

path = folder + "locations.gpkg"
hopenotError = entityslayer.dump_to_gpkg(path, overwrite = True)
if hopenotError:
    print(hopenotError)
# place_Description = location['placeDescription']['value']
    
print(f"Place: {place}")
print(f"Label: {place_Label}")
#print(f"Place Description: {place_Description}")
print(f"Elevation: {elevation}")
print(f"Location: {location}")
print(coordssplit)
print(lat)
print(lon)
print(Point)

# needs to go in the loop stationslayer.add_feature(POINT, [ID, NAME, COUNTRY, ELEVATION])

# Accessing the attribute table
geopackagePath = folder + "locations.gpkg"
Points_Italy = "locations"

#load the Point_Layer
PointsLayer = HVectorLayer.open(geopackagePath, Points_Italy)

osm = HMap.get_osm_layer()
HMap.add_layer(osm)

canvas = HMapCanvas.new()
canvas.set_layers([osm])

print("Points_Italy")
nameIndex=PointsLayer .field_index("elevation")
countriesFeatures = PointsLayer.features()
for feature in countriesFeatures:
    name = feature.attributes[nameIndex]
    if name > 10:
       print(feature.attributes[nameIndex])
       italy_geometry = feature.geometry
       canvas.add_geometry(italy_geometry)

crsHelper = HCrs()
crsHelper.from_srid(4326)#open street map data (latlong)
crsHelper.to_srid(3857)#reference system for webmapping adapted to the all word

# italy_geometry= crsHelper.transform(italy_geometry

# canvas.add_geometry(italy_geometry)
canvas.set_extent([-18000000,-8000000,18000000,8000000])
canvas.show()

#then, loop and extract as lists all the values from the output
#create a new geopackge and dump the lists into them