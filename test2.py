#freq_field_loop.py
#Garik Sadovy
#gcsadovy
#performs frequency analysis on all of the string type variables in a dataset.

import arcpy, sys, os
arcpy.env.workspace = arcpy.GetParameterAsText(0)
arcpy.env.overwriteOutput = True

dir = arcpy.env.workspace
fcs = arcpy.ListFeatureClasses()

try:
    for feature in fcs:
        print feature
        n = 1
        fields = arcpy.ListFields(fcs[n])
        
        print fields
        print " "
        n = n+1
        for field in fields:
            print field.name
             
except:
    arcpy.GetMessages
    