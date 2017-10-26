#buggyCursor.py
#gcsadovy
#Garik Sadovy
#counts records with specifications

#count_other_debug.py
# WARNING: This script contains  6 BUGS!  Remove them if you can.
#Purpose:   Count the number of records in COVER63p.shp with 'COVER'
#           field value that is neither 'woods' and nor 'orch'

import arcpy # need to import arcpy to run script

filename = 'C:/Temp/COVER63p.shp'
fields = ['COVER', 'FID']

count = 0   #Initialize count to zero

with arcpy.da.SearchCursor(filename, fields) as cursor: # have to switch the object with the method, 'filename' needs to match 'fileName'
    for row in cursor:
        cover = row[0] #needs to start at 0 not 1
        if cover != "woods" and cover != "orch": #and is the appropriate statement operator
            count = count + 1
del cursor #del cursor should be at the same position as the while loop
print "Number of records with other cover types:", count