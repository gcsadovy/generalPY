#point_distance.py
#gcsadovy
#Garik Sadovy

import arcpy, os, sys
arcpy.env.workspace = "C:\Temp\\ncshape.mdb"
arcpy.env.overwriteOutput = True
output = "C:\Temp"


n=1
while n<=5:
    arcpy.PointDistance_analysis("firestations", "schools_wake", output + "\dist{0}.dbf".format(n), "{0} Miles".format(n))
    n = n +1
    