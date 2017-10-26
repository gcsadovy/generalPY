#segProc.py
#Garik Sadovy
#gcsadovy
#procedure for finding euclidian distance between two points

import arcpy, os, sys, math

def segLength (a1, b1, a2, b2):
    dist1 = math.pow(a1 - a2, 2)
    dist2 = math.pow(b1 - b2, 2)
    edistance = math.sqrt(dist1 + dist2)
    return edistance

a1 = float(arcpy.GetParameter(0))
b1 = float(arcpy.GetParameter(1))
a2 = float(arcpy.GetParameter(2))
b2 = float(arcpy.GetParameter(3))

edist = segLength(a1, b1, a2, b2)
print "Segment ({0},{1}) to ({2},{3}) has length: {4}".format("%.2f" % a1, "%.2f" % b1, "%.2f" % a2, "%.2f" % b2, edist)