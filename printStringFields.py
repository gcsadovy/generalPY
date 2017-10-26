#printStringFields.py
#gcsadovy
#Garik Sadovy

#printTableExclude.py
# Print the names of the non-geometry non-OID type fields in the
# input file and the value of these fields for each record.
import arcpy

def includeFields ( table, types = [] ):
    '''Return a list of fields plus those with specified field types'''
    fieldNames = []
    fds = arcpy.ListFields(table)
    for f in fds:
        if f.type in types:
            fieldNames.append(f.name)
    return fieldNames

fc = 'C:/Temp/fires.shp'
includeTypes = [ 'String' ]
fields = includeFields(fc, includeTypes)

with arcpy.da.SearchCursor(fc, fields) as cursor:
    print cursor.fields
    for row in cursor:
        print row