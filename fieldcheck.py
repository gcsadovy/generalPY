# fieldCheck.py
# Purpose: check if the specified field name exists in the given table 
# Input: tableName fieldName 
# Example input: "C:/Temp/Cover63p.shp" "RECNO"
# Output: Exists does_Not_Exist (both are either true or false) passed as parameters to a model. 
# Example output: True False (values passed as parameters to a model.)

import arcpy, sys

tableName = sys.argv[1]
fieldName = sys.argv[2]

print "Checking table:", tableName
print "for fieldname", fieldName

fields = arcpy.ListFields(tableName, fieldName)

fieldNames = [field.name for field in fields]

if fieldName in fieldNames:
    print "Field", fieldName, "found in", tableName
    arcpy.AddMessage("Field", fieldName, "found in", tableName)
    arcpy.SetParameterAsText(2, "True")
    arcpy.SetParameterAsText(3, "False")

else:
    print "Field", fieldName, "NOT found in", tableName
    arcpy.AddMessage("Field", fieldName, "NOT found in", tableName)
    arcpy.SetParameterAsText(2, "False")
    arcpy.SetParameterAsText(3, "True")

    