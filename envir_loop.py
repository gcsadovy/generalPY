#envr_loop.py
#Garik Sadovy
#gcsadovy

import arcpy, os, sys
arcpy.env.workspace = "C:\Temp"
arcpy.env.overwriteOutput = True

try:
    variables = arcpy.ListEnvironments()
    for variable in variables:
        print variable
        arcpy.AddMessage(variable)

except:
    arcpy.GetMessages()

raw_input("Click ENTER to close the window")
