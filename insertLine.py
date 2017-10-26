#insertLine.py
#gcsadovy
#Garik Sadovy

#insertLine.py
# Purpose: Find the centroids of two polygons in COVER63p, then
#          crreate a line segment connecting these points
#          and add it to parkLines with left_fid set to 50.
# Solution is similar to the insertPolygon.py example

import arcpy

fcPoly = "C:/Temp/COVER63p.shp"
fcLine = "C:/Temp/parkLines.shp"

with arcpy.da.SearchCursor(fcPoly, ['SHAPE@XY']) as sc:
    # Get 2 centroids
    row = sc.next()
    point1 = arcpy.Point(row[0][0], row[0][1])
    row = sc.next()
    point2 = arcpy.Point(row[0][0], row[0][1])
del sc

myArray = arcpy.Array([point1, point2])

line = arcpy.Polyline(myArray)

ic = arcpy.da.InsertCursor(fcLine, ['SHAPE@', 'LEFT_FID'])

newRow = (line, 50)

ic.insertRow(newRow)

del ic