#export2JPG.py
#gcsadovy
#Garik Sadovy
#map document to jpg file

import arcpy, sys, os
arcpy.env.workspace = "C:/Temp"

input = sys.argv[1]
output = input[:-4] + ".jpg"

mxd = arcpy.mapping.MapDocument(input)
arcpy.mapping.ExportToJPEG(mxd, output)

del mxd