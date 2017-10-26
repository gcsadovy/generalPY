#buffer_debug.py
#script by Garik Sadovy
#gcsadovy

# Name: buffer.py
# Purpose: Buffer a file by 1 mile.
# Input: Full path file name of file to buffer (optional)
# Example input: C:/Temp/COVER63p.shp
# Output: buffer shapefile (Example output named C:/Temp/COVER63p_buff.shp)

import arcpy, os, sys


default = "C:\Temp\NEROfires.shp"
length = "1 mile"
outputFile = default[:-4] + "_buff.shp"

try:
    if len(arcpy.GetParameterAsText(0)) > 1:
        inFeatureLayer = arcpy.GetParameterAsText(0)
        outputFile = inFeatureLayer[:-4] + "_buff.shp"
    arcpy.env.workspace = os.path.dirname(inFeatureLayer)
    print "Workspace Set..."
    arcpy.env.overwriteOutput = True
    print "Overwrite set..."
    print "Calling buffer_analysis..."
    arcpy.Buffer_analysis(inFeatureLayer, outputFile, length)
    print "Created output file: " + os.path.basename(outputFile)
        
except:
    arcpy.GetMessages()