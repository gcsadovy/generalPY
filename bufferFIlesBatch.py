#buffer files batch

import arcpy, os, sys
arcpy.env.overwriteOutput = True
arcpy.env.workspace = "C:\Temp"
try:
    fcs = arcpy.ListFeatureClasses("*fire*", "")
    for file in fcs:
        print file
        fcBuffer = file[:-4] + "_buffer.shp"
        arcpy.Buffer_analysis(file, fcBuffer, "1 mile")
    print "all done"
    print arcpy.ListFeatureClasses("*_buffer.shp")
except:
    arcpy.GetMessages()

