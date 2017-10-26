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
            print "Input dataType: " + dsc.dataType
            print "Input format: " + dsc.format
    else:
        print "Warning: Conversion not performed."
        print "Input dataType: " + dsc.dataType
except:
    arcpy.GetMessages()