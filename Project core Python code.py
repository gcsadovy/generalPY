#final_project_code
#gcsadovy
#Garik Sadovy
#takes a data series of coordinates of fisher sightings over a period of years in northern california
#in kml files, converts them to shape files, returns statistics on clustering, and creates a raster file of
#kriging interpolation for each shapefile
#input arguments: directory containing kml files to be used,
#beginning year, ending year, a folder to store geodatabase files and layers

import arcpy, sys, os

def dictionary(list, dictionary, begYear, endYear):
    n = int(begYear)
    while n <= int(endYear):
        for file in list:
            y = str(n)
            z = file
            if y in z:
                dictionary[z] = n
        n = n + 1
    return dictionary

def layer2shapefile(dictionary, directory):
    for k, v in dictionary.items():
        arcpy.FeatureClassToShapefile_conversion(v, directory)
    list1 = []
    for (directory, dirs, files) in os.walk(directory):
        for file in files:
            if file.endswith(".shp") == True:
                list1.append(file)
    return list1

def Stats(file):
    arcpy.AverageNearestNeighbor_stats(file, "EUCLIDEAN_DISTANCE", "GENERATE_REPORT", "#")
    
    



folderIn = sys.argv[1] #folder containing the kml files
begYear = sys.argv[2] #the year you want to start with
endYear = sys.argv[3] #the year you want to end with
gdbName = sys.argv[4] #the name of a folder for your geodatabase files
ZField = sys.argv[5] #the field for the kml files that holds the trapping count (usually 'PopupInfo')

arcpy.env.workspace = folderIn
arcpy.env.overwriteOutput = True

#get a list of all of the Fisher kml files in a directory
try:
    list1 = []
    for file in os.listdir(folderIn):
        if  'Fisher' in file and file.endswith('.kml') == True:
            list1.append(file)
except:
    arcpy.GetMessages()

#get a dictionary with file names as keys and corresponding years as values
#within beginning and ending parameters
try:
    dic1 = {}
    dic2 = dictionary(list1, dic1, begYear, endYear)
except:
    arcpy.GetMessages()

#convert kml files to layers
#create dictionary with years as keys and full pathways to gdb layer files as values
try:
    dic3 = {}
    for k, v in dic2.items():
        arcpy.KMLToLayer_conversion(folderIn+'/'+k, gdbName, k[:-4], "NO_GROUNDOVERLAY")
        if dic3.has_key(v):
            dic3[v].append(gdbName+'/'+k[:-4]+'.gdb/Placemarks/Points')
        else:
            dic3[v] = gdbName+'/'+k[:-4]+'.gdb/Placemarks/Points'

except:
    arcpy.GetMessages()

#create shapefiles from layers
try:
    list2 = layer2shapefile(dic3, gdbName)

except:
    arcpy.GetMessages()

#get statistical information on the points in the shapefile using average nearest neighbor
try:
    for file in list2:
        Stats(file)

except:
    arcpy.GetMessages()

#kriging with each of the files 
try:
    for file in list2:
        arcpy.gp.Kriging_sa(file, ZField, file[:-4]+"fisher_krig", "Spherical 0,000116","#","VARIABLE 12","#")
    list3 = arcpy.ListRasters({*fisher_krig*})

except:
    arcpy.GetMessages()


