#bufferTry.py
#author: garik sadovy
#unity: gcsadovy
#Takes one or two arguments as input,
#a full path file name (required)
#and possibly a buffer distance (optional)

import arcpy, os, sys
arcpy.env.overwriteOutput = True


try:
    file = sys.argv[1]  #arcpy.GetParameterAsText(0)      
except IndexError:
    print  "Usage: <shapefile name (required)> <buffer distance (optional) default='1 mile'>"
    sys.exit(0)
try:
    dist = sys.argv[2]  #arcpy.GetParameterAsText(1)
except IndexError:
    dist = "1 Mile"
    print "No buffer distance given. Used default buffer distance of 1 mile." 


if file.endswith(".shp") == True:
    output = file[:-4] + "_buffer.shp"
    arcpy.Buffer_analysis(file, output, dist)
    print "Buffer distance: {0}".format(dist)
else:
    print "Input data format must be shapefile. Could not buffer input file {0}".format(file)