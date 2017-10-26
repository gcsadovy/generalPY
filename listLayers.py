#listLayers.py
#Garik Sadovy
#gcsadovy

import arcpy, sys, os
arcpy.env.workspace = "C:/Temp"

input = sys.argv[1]

mxd = arcpy.mapping.MapDocument(input)
dfs = arcpy.mapping.ListDataFrames(mxd)
n = 0
for df in dfs:
    print "Frame {0}: {1}".format(n, df.name)
    layers = arcpy.mapping.ListLayers(mxd, "*", df)
    m = 0
    for layer in layers:
        print "Layer {0}: {1}   {2}".format(m, layer.name, layer.dataSource)
        m = m + 1
    n = n+1

del mxd

        
    