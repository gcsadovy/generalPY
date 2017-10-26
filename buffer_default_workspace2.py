# buffer_default_workspace2.py
import arcpy, sys 


try:
       fc = sys.argv[1] # Get input shape file name from user 
       print "Input shapefile =", fc 

except IndexError:
       print "Need input for processing"
       print "Usage: <shapefile name (required)> <workspace(optional) default='C:/Temp'>"
       sys.exit(0) #Program exists here. No more lines of code are executed 

try:
       arcpy.env.workspace = sys.argv[2] # Get a full path filename from the user
       print "Workspace =", arcpy.env.workspace 

except IndexError:
       print "Warning: no workspace specified. Using default workspace 'C:/Temp'" 
       arcpy.env.workspace = "C:/Temp"

buffer = fc[:-4] + "_buffer.shp"
arcpy.Buffer_analysis(fc, buffer, "1 mile")
print "Created: ", buffer