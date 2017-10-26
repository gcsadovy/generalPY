#get field names
import arcpy
try:
    filename = "C:/Temp/COVER63p.shp"
    fields = arcpy.ListFields( filename ) # Returns a Python list of field objects for the given file 
    for field in fields:
        print field.length# Object.Property 
except:
    arcpy.GetMessages()