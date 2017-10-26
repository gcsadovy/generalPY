#freq_field_loop.py
#Garik Sadovy
#gcsadovy
#performs frequency analysis on all of the string type variable in a dataset.

import arcpy, os, sys

arcpy.env.workspace = arcpy.GetParameterAsText(0)
arcpy.env.overwriteOutput = True

try:
    shapefiles = arcpy.ListFeatureClasses()
    for file in shapefiles:
        fields = arcpy.ListFields(file)
        for field in fields:
            name = field.name
            output = file[:-4]+"_"+(field.name).upper()+"freq.dbf"
            arcpy.Frequency_analysis(file, output, name, "#")
            print "done"

except:
    arcpy.GetMessages()