#batch_getcount.py
import arcpy, os, sys
dir = "C:/Temp"
files = os.listdir(dir)
print files
for filename in files:
    desc = arcpy.Describe(filename)
    if desc.dataType == "ShapeFile" and desc.shapeType == "Point" and "fire" in filename:
        count = arcpy.GetCount_management(filename)
        print "{0} has {1} entries.".format(filename, count)
    
