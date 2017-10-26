#Name: gridToPolygon_debug.py
#Purpose: Convert a raster data set to a polygon shapefile, only if it is in Esri 'GRID' format.
#Usage: <full path input file name> <output file name> 
#Example: "C:/My Documents/Rast1" "poly1.shp"
#Date: September 14, 2008
#gcsadovy
#Garik Sadovy

import arcpy, sys, os

arcpy.env.workspace = os.path.dirname(arcpy.GetParameterAsText(0))

arcpy.env.overwriteOutput = True
rasterIn = os.path.basename(arcpy.GetParameterAsText(0))
shapeOut = arcpy.GetParameterAsText(1)

desc = arcpy.Describe(rasterIn)

try:

    if desc.dataType == "RasterDataset":
        if desc.format == "GRID":
            arcpy.RasterToPolygon_conversion(rasterIn,shapeOut)
            print "Conversion complete to:", shapeOut
        else:
            print "Warning: Conversion not performed." 
            print "Input dataType: " + desc.dataType
            print "Input format: " + desc.format
    else:
        print "Warning: Conversion not performed."
        print "Input dataType: " + desc.dataType
except:
    arcpy.GetMessages()