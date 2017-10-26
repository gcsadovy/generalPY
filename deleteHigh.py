#deleteHigh.py
#gcsadovy
#Garik Sadovy
#uses cursor to delete records in a table higher than an input value
#arguments: file, field, value

import arcpy, sys, os

inputTable = sys.argv[1]
numericFieldName = sys.argv[2]
value = sys.argv[3]

with arcpy.da.UpdateCursor(inputTable, numericFieldName) as cursor:
    for row in cursor:
        if int(row[0]) > 8:
            cursor.deleteRow()
        