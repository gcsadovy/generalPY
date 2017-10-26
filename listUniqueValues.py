#listUniqueValues.py
#gcsadovy
#Garik Sadovy

import sys, arcpy
sys.path.append("C:\Temp")

import listManager

inputFile = sys.argv[1]
inputField = sys.argv[2]

cursor = arcpy.da.SearchCursor(inputFile, [inputField])
list1 = listManager.uniqueList(cursor)
print list1





