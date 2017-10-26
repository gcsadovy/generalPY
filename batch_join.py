#batch_join.py
#gcsadovy
#code by garik sadovy

import arcpy, sys, os
arcpy.env.worspace = arcpy.GetParameterAsText(0)
arcpy.env.overwriteOutput = True

list = ""
try:
    
    tables = arcpy.ListTables("", "dBase")
    for table in tables:
        list = list + ";" + table

    print list[1:] 

except:
    arcpy.GetMessages()