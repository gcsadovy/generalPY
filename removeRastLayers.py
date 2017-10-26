#removeRastLayers.py
#gcsadovy
#Garik Sadovy
#input full map file path name
#removes any rasters from a map and saves a copy

import arcpy, os, sys

inputFile = sys.argv[1]

mxd = arcpy.mapping.MapDocument(inputFile)
dfs = arcpy.mapping.ListDataFrames(mxd)
for df in dfs:
    layers = arcpy.mapping.ListLayers(mxd, "*", df)
    for layer in layers:
        if layer.isRasterLayer == True:
            arcpy.mapping.RemoveLayer(df, layer)

copyName = inputFile[:-4] + "2.mxd"
mxd.saveACopy(copyName)
del mxd