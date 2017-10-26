#fieldProc.py
#Garik Sadovy
#gcsadovy

import arcpy, os, sys, math

def printFields (input):
    print "Fields in {0}".format(input)
    fields = arcpy.ListFields(input)
    for field in fields:
        print field.name

arcpy.env.overwriteOutput = True

input = arcpy.GetParameterAsText(0)
fields1 = printFields(input)
print fields1

output = input[:-4] + "Copy" + input[-4:]
arcpy.Copy_management(input, output)
arcpy.AddField_management(output, "AREA", "FLOAT")

fields2 = printFields(output)
print fields2