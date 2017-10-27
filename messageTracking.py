#!/usr/bin/python

__author__ = 'Garik'

#Get messaging counts for a tenant in a message directory sorted by date and hour

import os, sys, time, timeit, collections, xml.etree.ElementTree as ET
from collections import defaultdict

#get paths for every files and check validity as message

def pathCheck(d):
  files = list()
  for f in os.listdir(d):
    if 'WS' in f:
      files.append(os.path.join(d,f))
  return files

#parse each file for the tenant, date and hour

def xmlParse(tenant, d):
  files = pathCheck(d)
  dic = defaultdict(list)
  xCount = 0 # count for # of broken xml files that raise exceptions as script is run
  dic['xCnt'] = xCount #create dictionary key for exception files
  for f in files:
    try:
      root = ET.parse(f).getroot()
      if str(tenant) in root[0][0].text:
        year = (root[0][4].text[0:4])
        month = (root[0][4].text[5:7])
        day = (root[0][4].text[8:10])
        date = year + month + day
        hour = (root[0][4].text[11:13])
        dic[date].append(hour)
    except KeyboardInterrupt: #bail with keystroke
      return
    except: # increase count for exceptions (ExpatError) and update key value
      xCount = xCount + 1
      dic["xCnt"] = xCount
  return dic

#take a list of hours and turn them into a dictionary with hours as keys and counts as values

def hourCount(hourList):
  dic = defaultdict(int)
  for hour in hourList:
    dic[hour] += 1
  return dic

#write a text file with dates, hours, and counts
#2 sysarg values are tenant as text and the directory path

def main():

  os.chdir('/home/garik/scripts/output') #change output directory here
  filename = 'callCount.' + str(sys.argv[1]) + '.' + time.strftime('%Y%m%d-%H%M%S') + '.txt'

  with open(filename, 'w') as f:
    dic =  xmlParse(sys.argv[1], sys.argv[2])
    xCount = dic['xCnt'] #get # of broken files
    dic.pop('xCnt', None) #remove exception key from dictionary
    for date in sorted(dic.keys()):
      dic2 = defaultdict(int)
      f.write('__________________' '\n' '\n')
      f.write(str(date[0:4])+'/'+str(date[4:6])+'/'+str(date[6:8]))
      f.write('\n')
      f.write('\n')
      for item in sorted(hourCount(sorted(dic[date])).items()):
        f.write(str(item[0]) + ':00 ->  ' + str(item[1]))
        f.write('\n')
      f.write('\n')
    f.write('___________________')
    f.write('\n')
    f.write('\n')
    f.write("Number of Broken Files -> " + str(xCount)) #write out number of broken xml files
    f.write('\n')
    f.write('___________________')

if __name__ == '__main__':
  main()
