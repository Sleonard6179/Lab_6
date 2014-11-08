__author__ = 'sleonard'
# This Script will search a folder and copy all raster files into a specified
# Geodatabase.
import arcpy
from arcpy import env
from arcpy.sa import *
#
infile = env.workspace = "F:/GIS/A_Masters_Program/Python/Data/Exercise09"
outFile = "F:/GIS/A_Masters_Program/Python/Data/Exercise09/Results/Lab_9_results.gdb/"
# List to hold raster names
rasters = []
# Lists all raster files in workspace, and appends them to list.
lists = arcpy.ListRasters()
# Iterates through workspace and appends each raster to list.
for rstr in lists:
    rasters.append(rstr)
# Copies rasters from list to Geodatabase.
arcpy.RasterToGeodatabase_conversion(rasters,"Results/Lab_9_results.gdb")
