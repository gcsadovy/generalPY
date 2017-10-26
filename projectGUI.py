#projectGUI.py
#Garik Sadovy
#gcsadovy
#makes a conversion of a kml file which is loaded into the tool, to a layer file

import arcpy, sys, os

fileName = sys.argv[1]

print "Checking for kml file."

if fileName.endswith('.kml') == True:
    arcpy.SetParameterAsText(2, "True")
    arcpy.SetParameterAsText(3, "False")
    

if fileName.endswith('.kml') == False:
    arcpy.SetParameterAsText(2, "False")
    arcpy.SetParameterAsText(3, "True")
    

raw_input("click ENTER to close Window")