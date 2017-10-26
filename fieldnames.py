#fieldnames.py
#gcsadovy
#Garik Sadovy

import arcpy, os, sys

arcpy.env.workspace = arcpy.GetParameterAsText(0)
arcpy.env.overwriteOutput = True
file = arcpy.GetParameterAsText(0)

list = arcpy.ListFields(file)
list2 = [i.name for i in list]

print list2
    
