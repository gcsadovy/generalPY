#addRaster.py
#Garik Sadovy
#gcsadovy
#adds raster to map file
#input map file and raster dataset

import arcpy, os, sys

inputFile = sys.argv[1]
inputRaster = sys.argv[2]

mxd = arcpy.mapping.MapDocument(inputFile)
dfs = arcpy.mapping.ListDataFrames(mxd)
df = dfs[0]
addLayer = arcpy.mapping.Layer(inputRaster) #make the raster into a layer

arcpy.mapping.AddLayer(df, addLayer)

copyName = inputFile[:-4] + "2.mxd"
mxd.saveACopy(copyName)

del mxd

