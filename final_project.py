#final_project_code
#gcsadovy
#Garik Sadovy
#takes a data series of coordinates of fisher sightings over a period of years
#in kml files, returns statistics on clustering, and creates a weighted
#overlay, then loading the data to a map
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
    print list2

except:
    arcpy.GetMessages()
        
        
        
    

    

#part 4 - geoprocessing

#try:
    #for shapeFile in list:
        #arcpy.gp.Kriging_sa(shapeFile, 
        
        
        

