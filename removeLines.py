#removeLines.py
#gcsadovy
#Garik Sadovy
# takes full path of input file as argument
#cleans up data in rows of input file
# and writes to output file

import arcpy, os, sys

input = sys.argv[1]
output = os.path.dirname(input) + "\wheat_yield_sites_edited.txt"

try:
    infile = open(input, 'r')
    outfile = open(output, 'w')

    line = infile.readline()
    outfile.write(line)

    for line in infile:
        lineList = line.split('\t')
        print lineList
        for x in lineList:
            goodData = 0
            y = float(x)
            print x
            if float(x) < 0:
                goodData = goodData + 1
                
            elif x == '\n':
                goodData = goodData + 1
                
            else:
                goodData = goodData
               
            if goodData < 1:
                outfile.write(line)

    infile.close()
    outfile.close()
            

except:
    arcpy.GetMessages()
    
  #what if I asked for the number of objects within the list and if it was less, skip the list
    