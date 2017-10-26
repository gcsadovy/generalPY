#inPoint.py
#Garik Sadovy
#gcsadovy
#script tool to determine if a feature layer is point; if so applies an average nearest neighbor tool to it
#part of the messaging section
#using scripts in tool boxes

import arcpy, os, sys

input = arcpy.GetParameterAsText(0)
arcpy.env.workspace = os.path.dirname(input)
arcpy.env.overwriteOutput = True

desc = arcpy.Describe(input)

if desc.shapeType == "Point":
    print input + " is a point shapefile."
    arcpy.AddMessage("File " + os.path.basename(input) + " is a point shapefile.")
    arcpy.SetParameterAsText(1, "True")
    arcpy.SetParameterAsText(2, "False")

else:
    print input + " is not a point shapefile."
    arcpy.AddMessage("File " + os.path.basename(input) + " is not a point shapefile.")
    arcpy.SetParameterAsText(1, "False")
    arcpy.SetParameterAsText(2, "True")

raw_input("Click ENTER to close the window.")

