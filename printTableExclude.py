#printTableExclude.py
# Print the names of the non-geometry non-OID type fields in the 
# input file and the value of these fields for each record.

import arcpy

def excludeFields (table, types = []):
    fieldNames = []
    fds = arcpy.ListFields(table)
    for f in fds:
        if f.type not in types:
            fieldNames.append[f.name]
        return fieldNames

fc = "C:/Temp/fires.shp"
excludeTypes = ['Geometry', 'OID']
fields = excludeFields(fc, excludeTypes)

cursor = arcpy.da.SearchCursor(fc, fields)
print cursor.fields