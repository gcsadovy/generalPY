#cursorLoop.py

import arcpy

fc = 'C:/Temp/fires.shp'
fields = ['FID', 'FireID', 'FireName']

cursor = arcpy.da.SearchCursor('C:/Temp/fires.shp', ['FireName'])
for row in cursor:
    print row[0]