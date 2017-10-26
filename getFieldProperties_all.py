#get field names
import arcpy
try:
    filename = "C:/Temp/COVER63p.shp"
    fields = arcpy.ListFields( filename ) # Returns a Python list of field objects for the given file 
    for field in fields:
        print field.name# Object.Property 
except:
    arcpy.GetMessages()

import arcpy
try:
    filename = "C:/Temp/COVER63p.shp"
    fields = arcpy.ListFields( filename ) # Returns a Python list of field objects for the given file 
    for field in fields:
        print field.aliasname# Object.Property 
except:
    arcpy.GetMessages()

import arcpy
try:
    filename = "C:/Temp/COVER63p.shp"
    fields = arcpy.ListFields( filename ) # Returns a Python list of field objects for the given file 
    for field in fields:
        print field.domain# Object.Property 
except:
    arcpy.GetMessages()

import arcpy
try:
    filename = "C:/Temp/COVER63p.shp"
    fields = arcpy.ListFields( filename ) # Returns a Python list of field objects for the given file 
    for field in fields:
        print field.editable# Object.Property 
except:
    arcpy.GetMessages()

import arcpy
try:
    filename = "C:/Temp/COVER63p.shp"
    fields = arcpy.ListFields( filename ) # Returns a Python list of field objects for the given file 
    for field in fields:
        print field.isnullable# Object.Property 
except:
    arcpy.GetMessages()

import arcpy
try:
    filename = "C:/Temp/COVER63p.shp"
    fields = arcpy.ListFields( filename ) # Returns a Python list of field objects for the given file 
    for field in fields:
        print field.required# Object.Property 
except:
    arcpy.GetMessages()

import arcpy
try:
    filename = "C:/Temp/COVER63p.shp"
    fields = arcpy.ListFields( filename ) # Returns a Python list of field objects for the given file 
    for field in fields:
        print field.length# Object.Property 
except:
    arcpy.GetMessages()

import arcpy
try:
    filename = "C:/Temp/COVER63p.shp"
    fields = arcpy.ListFields( filename ) # Returns a Python list of field objects for the given file 
    for field in fields:
        print field.type# Object.Property 
except:
    arcpy.GetMessages()

import arcpy
try:
    filename = "C:/Temp/COVER63p.shp"
    fields = arcpy.ListFields( filename ) # Returns a Python list of field objects for the given file 
    for field in fields:
        print field.scale# Object.Property 
except:
    arcpy.GetMessages()

import arcpy
try:
    filename = "C:/Temp/COVER63p.shp"
    fields = arcpy.ListFields( filename ) # Returns a Python list of field objects for the given file 
    for field in fields:
        print field.precision# Object.Property 
except:
    arcpy.GetMessages()