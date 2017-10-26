#countWalk.py
#Garik Sadovy
#gcsadovy

import arcpy, sys, os
path = sys.argv[1]

for (path, dirs, files) in os.walk(path):
    for file in files:
        if file.endswith(".shp") == True:
            count = arcpy.GetCount_management(file)
            print "{0}/{1} has {2} entries.".format(path, file, count)