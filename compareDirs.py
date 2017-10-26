#compareDirs.py
#garik sadovy
#gcsadovy
#takes 2 input arguments; 2 full folder pathnames; compares the time stamps of one directory to the other for a backup procedure

import arcpy, sys, os

def getEpochTime(filepath):
    return os.path.getmtime(filepath)

inputdir = sys.argv[1]
outputdir = sys.argv[2]

workinglist = os.listdir(inputdir)
backuplist = os.listdir(outputdir)
workingdir = {}
backupdir = {}

for file in workinglist:
    fullpath = inputdir + "/" + file
    timestamp = getEpochTime(fullpath)
    workingdir[file] = timestamp

for file2 in backuplist:
    fullpath = outputdir + "/" + file2
    timestamp2 = getEpochTime(fullpath)
    backupdir[file2] = timestamp2


for k, v in workingdir.items():
    if backupdir.has_key(k) == True and v > backupdir[k]:
        print k
    elif backupdir.has_key(k) == False:
        print k
    


