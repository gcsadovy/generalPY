#fieldProperties.py
#gcsadovy
#Garik Sadovy

import arcpy, os, sys
arcpy.env.workspace = os.path.dirname(arcpy.GetParameterAsText(0))
arcpy.env.overwriteOutput = True

input = arcpy.GetParameterAsText(0)

fields = arcpy.ListFields(input)
for index, field in enumerate(fields):
    print "Field {0}:".format(index) + " Name={0}, Type={1}, Length={2}".format(field.name, field.type, field.length)
