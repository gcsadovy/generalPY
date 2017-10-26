#listComprehension.py
#Garik Sadovy
#gcsadovy

# Create a list of all uppercase field names 
fieldNames = ['FID', 'Shape', 'COVER', 'RECNO']
fieldNames2 = [ i.upper() for i in fieldNames ]
print "1. All cap field names:", fieldNames2

# Create a list of rounded float values 
strList = ['3.34', '1.07', '4.21', '4.56', '4.5']
intList = [float(int(float(i))) for i in strList] #modify this 
print "2. Rounded float values:", intList

# Create a list of reciprocal values (the reciprocal of a number n is defined as 1/n)
values = [8.0, 4.0, 4.0, 1.0, 5.0, 4.0, 4.0, 2.0]
reciprocal = [(1/float(i)) for i in values] #modify this 
print "3. The reciprocal values:", reciprocal

# Create a list in which all the slash marks ('/') are replaced with underscores ('_').
fieldNames = [ "FireType/Protection-Type", "Time/Date", "Condition/Status/Role"]
fieldNames2 = [i.replace('/', '_') for i in fieldNames] #modify this 
print "4. No slashes:", fieldNames2

# Create a list of output file names
import os
inputFiles = os.listdir("C:/Temp") 
# Sample output below for inputFiles = ["COVER.shp", "Fires.shp", "Data.txt"]
outputFiles = [(os.path.basename(i[:-4]))+"out"+(os.path.basename(i[-4:])) for i in inputFiles] #modify this 
print "5. Output files:", outputFiles

# Create a list file extensions -- You may assume file extensions are the last
# 4 characters or for an extra challenge, find a solution using the 'os.path.splitext' method
import arcpy
inputFiles = os.listdir("C:/Temp") 
# Sample output below for inputFiles = ["COVER.shp", "Fires.shp", "Data.txt"]
extensions = [os.path.basename(i[-4:]) for i in inputFiles] #modify this
print "6. File extensions:", extensions