#sqlQueryCursor.py
import  arcpy
fc = 'C:/Temp/fires.shp'
query1 = "SizeClass = 'A'"
sc = arcpy.da.SearchCursor( fc, [ 'CalendarYe' ], query1 )
for row in sc:
    print row[0],
del sc