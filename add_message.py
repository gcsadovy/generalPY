import os, arcpy
         
dir = "C:/Temp"
filelist = os.listdir(dir) # Lists all the files in the given directory
print "Directory", dir, "contains", len(filelist), "files." # Prints in the Interactive Window (and command window)
arcpy.AddMessage("Directory " + dir + " contains " + str(len(filelist)) + " files.") 