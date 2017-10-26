#Purpose: Count the number of records of the input file, then buffer the file.
#Author: Laura Tateosian
#Date: July 28, 2008
import arcpy, sys 

inputFile = sys.argv[1]

count = arcpy.GetCount_management(inputFile)
print arcpy.GetMessages() 

print "\n\nThere are", count, "polygons in", inputFile, "\n\n"

arcpy.buffer_Analysis(inputFile, "buffer.shp", "1 mile")
print arcpy.GetMessages()

# Output looks like this: