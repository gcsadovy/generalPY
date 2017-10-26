#Name: gridToPolygon.py
#Purpose: Convert a raster data set to a polygon shapefile, only if it is in Esri 'GRID' format.
#Usage: <full path input file name> <output file name> 
#Example: "C:/My Documents/Rast1" "poly1.shp"
#Date: September 14, 2008

import arcpy, sys 
arcpy.env.overwriteOutput = True
arcpy.env.workspace = arcpy.GetParameterAsText(0)
InRaster = os.path.basename(arcpy.env.workspace)
print InRaster
dsc = arcpy.Describe(InRaster)
OutPolygon = arcpy.GetParameterAsText(1)
if dsc.dataType == "Raster Dataset":
    arcpy.RasterToPolygon_conversion(InRaster,OutPolygon)
    print "Conversion complete to:", Outpolygon
elif dsc.format == "GRID":
    arcpy.RasterToPolygon_conversion(InRaster,OutPolygon)
    print "Conversion complete to:", Outpolygon
else:
    print "Warning: Conversion not performed."
    print "Input dataType:", dsc.dataType
    print "Input data Format:", dsc.Format