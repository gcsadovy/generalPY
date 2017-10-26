#describetest

import arcpy, os, sys

arcpy.env.workspace = arcpy.GetParameterAsText(0)
arcpy.env.overwriteOutput = True

print arcpy.env.workspace

rastfile = "getty_rast"

inrast = os.path.basename(arcpy.GetParameterAsText(0))
print inrast
desc = arcpy.Describe(inrast)
print desc
