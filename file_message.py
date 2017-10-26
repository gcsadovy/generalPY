import os, arcpy        
dir = "C:/Temp"
filelist = os.listdir(dir) # Lists all the files in the given directory 
for file in filelist:        # Loops through the list of files
        if file.endswith(".shp"): # if the current file is a shapefile
                print file
                arcpy.AddMessage(file)