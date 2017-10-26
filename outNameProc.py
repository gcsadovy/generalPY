#outNameProc.py
#Garik Sadovy
#gcsadovy

#proceedure to return files of adjusted name

import os

def outName(input, fix = "Out", ext = "shp"):
    return os.path.basename(input)[:-4] + fix + "." + ext

input1 = "C:/Data/NC.shp"
input2 = "Raleigh.shp"

# Set feature to point output name
centroids = outName(input1, "Points", "shp")
print centroids

# Set central feature output name
centralFeature = outName(input1, "Central","shp")
print centralFeature

# Set mean center output name
meanCenter = outName(input1, "Mean")
print meanCenter

# Set point distance output name
distanceTable = outName(input1, "Mean2Central", "dbf")
print distanceTable

# Set generic output name
myoutput = outName(input2)
print myoutput


    
        
        
        