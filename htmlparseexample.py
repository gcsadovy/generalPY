#parseHTMLimages.py
#gcsadovy
#Garik Sadovy

import arcpy, os, sys, urllib2
curDir = os.path.dirname("C:\Temp")

sys.path.append(curDir)
import BeautifulSoup

url = sys.argv[1]
response = urllib2.urlopen(url)

soup = BeautifulSoup.BeautifulSoup(response)

refs = soup.findAll("img")
count = len(refs)
print "{0} images found.".format(count)
for r in refs:
    for attr, value in r.attrs:
        if attr == "src":
            print "image src:", value