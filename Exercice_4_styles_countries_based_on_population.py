from pyqgis_scripting_ext.core import *

folder = "C:\\Users\\00mar\\Desktop\\Master_Bolz\\Semester_2\\Advance_geomatics\\Archivos_Gis\\natural_earth_vector.gpkg\\packages\\"
geopackagePath = folder + "natural_earth_vector.gpkg"
countriesName = "ne_50m_admin_0_countries"

countriesLayer = HVectorLayer.open(geopackagePath, countriesName)

ranges = [
   [80000000, float ('inf')],
   [1000000,80000000],
   [float('-inf'),1000000]
]

styles = [
    HFill("255,0,0,70"),
    HFill("0,255,0,70"),
    HFill("0,0,255,70"),
]

labelStyle = HLabel ("POP_EST") + HHalo ()

countriesLayer.set_graduated_style ("POP_EST", ranges, styles, labelStyle)

HMap.add_layer(countriesLayer)