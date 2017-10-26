#dictionary.py
#Garik Sadovy
#gcsadovy

#Currently, this script reads a text file and prints the count for each species.
#Each row in the text file has this format: Block   Plot    Species     DBH
#Columns are tab separated.
#When completed, this script should also find the average DBH of each species in the given text file.
import string, os.path


filepath = "C:\\temp\\rdu_forest1.txt"
data=[]
#Open the text file
myfile=open(filepath,'r')
#Read the text file
myfile.readline() #read the field name line
row = myfile.readline()
count = 0
while row:
    myline = row.split('\t') #Creat a list of the values in this row.  Columns are tab separated.
    #Reads a file with columns: Block Plot  Species DBH MerchHeight
    data.append([float(myline[0]),float(myline[1]),myline[2].rstrip(),float(myline[3].rstrip())]) 
    #rstrip removes white space from the right side
    count = count + 1
    row = myfile.readline()
myfile.close()
mydict={}

#Create an emyty mydict2 here  *********
mydict2 ={}

for row in data:  # for each row
    # create or update a dictionary entry with the current count for that species
    species = row[2]  #Species is the third entry in the file
    DBH = row[3] #DBH is the fourth entry in the file 
    if mydict.has_key(species):  #if a dictionary entry already exists for this species
        #Update dict for this species
        cur_entry = mydict[species]
        cur_entry = int(cur_entry)+1
        mydict[species] = cur_entry
    if mydict2.has_key(species):
        curr_entry = mydict2[species]
        curr_entry = (int(curr_entry) + int(DBH))
        mydict2[species] = curr_entry
        
        #update mydict2 here  *********

    else:#This is the first dictionary entry for this species
        #Create new dict entry with sums and count for this species
        mydict[species]=1
        mydict2[species] = int(DBH)

        #Add a new entry to mydict2 here  *********

mykeys = mydict.keys()
#Print the count for each species
for key in mykeys:
    total = mydict2[key]
    count = int(mydict[key])

#use mydict2[key] to calculate average for each species here  *********
    print "The number of trees of species", key, "=", count
    print "The average for this species", key, "=", float(total)/float(mydict[key])

#print the average for this species here  *********
