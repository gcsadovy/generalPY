#centralPoint.py
#Garik Sadovy
#gcsadovy
#usage: input - full path polygon shapefile

import arcpy, os, sys, datetime

def reportTime():
    t = datetime.datetime.now()
    print t.ctime()

def getTime():
    t = datetime.datetime.now()
    return t

def diffTime(before, after, message):
    difference = after - before
    weeks, days = divmod(difference.days, 7)
    minutes, seconds = divmod(difference.seconds, 60)
    hours, minutes = divmod(minutes, 60)
    print message
    print "%d weeks, %d days, %d:%d:%d" % (weeks, days, hours, minutes, seconds)

input = arcpy.GetParameterAsText(0)

#Feature2Point

before = getTime()
output1 = input[:-4] + "Points" + input[-4:]
arcpy.FeatureToPoint_management(input, output1, "CENTROID")
after = getTime()

message = "Time for FeatureToPoint to create {0}:".format(output1)
diffTime(before, after, message)

#CentralFeature

before = getTime()
output2 = input[:-4] + "Central" + input[-4:]
arcpy.CentralFeature_stats(output1, output2, "EUCLIDEAN_DISTANCE")
after = getTime()

message = "Time for CentralFeature to create {0}:".format(output2)
diffTime(before, after, message)

#MeanCenter

before = getTime()
output3 = input[:-4] + "Mean" + input[-4:]
arcpy.MeanCenter_stats(output2, output3)
after = getTime()

message = "Time for MeanCenter to create {0}:".format(output3)
diffTime(before, after, message)

#PointDistance

before = getTime()
output4 = input[:-4] + "Mean2Central" + ".dbf"
arcpy.PointDistance_analysis(output2, output3, output4)
after = getTime()

message = "Time for PointDistance to create {0}:".format(output4)
diffTime(before, after, message)