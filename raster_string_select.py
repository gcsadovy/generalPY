import arcpy
arcpy.env.workspace = "C:\Temp"

try:
    fire_point = arcpy.ListFeatureClasses("*fire*", "POINT")
    for file in fire_point:
        print file

except:
    arcpy.GetMessages()
    