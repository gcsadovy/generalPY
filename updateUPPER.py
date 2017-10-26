#updateUPPER.py
#gcsadovy
#Garik Sadovy

import arcpy, os, sys

arcpy.env.overwriteOutput = True

fc = sys.argv[1]
fieldToPrint = sys.argv[2]
output = fc[:-4] + "Copy" + fc[-4:]

arcpy.Copy_management(fc, output)

with arcpy.da.UpdateCursor(fc, fieldToPrint) as cursor:
    for row in cursor:
        row[0] = row[0].upper()
        cursor.updateRow(row)
del cursor
