#countLines.py
#garik Sadovy
#gcsadovy

import arcpy, os, sys

inputFileName = sys.argv[1]

try:
    infile = open(inputFileName, 'r')
    count = 1
    for line in infile:
        count = count + 1
    print inputFileName + " has " + count + " lines."

except:
    print "File Does Not Exist"
    arcpy.GetMessages()
    


    