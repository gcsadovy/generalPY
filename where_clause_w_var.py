# whereClauseWithVar.py

# Example: C:/Temp/fires.shp FID FireName
import arcpy, sys

fc = sys.argv[1]
numericField = sys.argv[2]
fieldToPrint = sys.argv[3]

query3Var = '{0} > 6'.format( numericField ) # string formatting

with arcpy.da.SearchCursor( fc, [ fieldToPrint ], query3Var ) as cursor:
	recordList = [row[0] for row in cursor]
del cursor

print recordList  