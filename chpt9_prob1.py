__author__ = 'sleonard'
# Script performs raster calculations.
import arcpy
from arcpy import env
from arcpy.sa import *
arcpy.CheckOutExtension("spatial")
env.workspace = "F:/GIS/A_Masters_Program/Python/Data/Exercise09"
# Sets rasters for calculations.
elev = arcpy.Raster("elevation")
land = arcpy.Raster("landcover.tif")
# Defines tools for raster calculator.
slope = Slope(elev)
aspect = Aspect(elev)
# Calculates raster values.
slope1 = ((slope > 5) & (slope < 20))
direct = ((aspect > 150) & (aspect < 270))
cover = ((land == 41) | (land == 42) | (land == 43))
goodspot = (slope1 & direct & cover)
# Saves file.
goodspot.save("trial")
arcpy.CheckInExtension("spatial")

