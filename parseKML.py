#parseKML.py
#gcsadovy
#Garik Sadovy
#parses an input kml file

import os, sys
curDir = os.path.dirname(sys.argv[1])

sys.path.append(curDir)
import BeautifulSoup

fileName = sys.argv[1]

data = open(fileName, 'r') #file object
soup = BeautifulSoup.BeautifulSoup(data) #makes a soup object
data.close()

#Get KML with name and description tags
names = soup.findALL("name")
descriptions = soup.findAll("description")

for index, desc in enumerate(description): #enumerate gives you an index and a value
    print
    print names[index].contents[0] #contents is a soup trick; has attribute called contents
    for item in desc.contents:
        print "\t"+item