#batch_fieldnames.py
#gcsadovy
#script author: Garik Sadovy

import arcpy, sys, os
arcpy.env.workspace = arcpy.GetParameterAsText(0)
arcpy.env.overwriteOutput = True

try:
    in1 = arcpy.ListRasters("*land*", "")
    for raster in in1:
        print raster
        in2 = arcpy.ListFields(raster)
        for field in in2:
            print field.name
        print " "

except:
    arcpy.GetMessages()
        