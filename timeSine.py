#timeSine.py
#gcsadovy
#Garik SAdovy

import sys, arcpy

sys.path.append("C:\Temp")

import timeReport

arcpy.CheckOutExtension("Spatial")

input = sys.argv[1]
output = sys.argv[2]


before = timeReport.getTime()
arcpy.sa.Sin(input)
after = timeReport.getTime()

print "Calculating Sine took:"
print timeReport.diffTime(before, after)
