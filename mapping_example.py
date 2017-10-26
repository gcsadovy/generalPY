#example mapping
#Garik sadovy
#gcsadovy

import arcpy, os, sys

arcpy.env.overwriteOutput = True

mapName = "C:/Temp/test.mxd"
mxd = arcpy.mapping.MapDocument(mapName)
dfs = arcpy.mapping.ListDataFrames(mxd)
df = dfs[0]
layers = arcpy.mapping.ListLayers(mxd, "*", df)
for layer in layers:
    print layer.name