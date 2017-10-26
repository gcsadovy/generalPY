import arcpy, sys, os

arcpy.env.workspace = arcpy.GetParameterAsText(0)
arcpy.env.overwriteOutput = True

list = arcpy.ListRasters()
for raster in list:
    desc = arcpy.Describe(raster)
    if desc.dataType == "RasterDataset":
        if desc.format == "GRID":
            print raster + " was converted."
            print desc.format
        else:
            print "Warning: not converted"
            print desc.format
            print desc.dataType
        
    

        