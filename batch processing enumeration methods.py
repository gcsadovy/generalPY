#batch processing enumeration methods
import arcpy, os, sys

try:
    
arcpy.env.workspace = "C:\Temp"
fcs = arcpy.ListFeatureClasses() #returns python list of strings

fcs_fire = arcpy.ListFeatureClasses("", "POINT")
print fcs_fire

flds = arcpy.ListFields("COVER63p.shp", "", "")
print flds

rstrs = arcpy.ListRasters()
print rstrs

except:
    arcpy.GetMessages()
    