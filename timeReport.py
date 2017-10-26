# timeReport.py
import time
import datetime

def reportTime( ):
         #Report the current time
         t = datetime.datetime.now( ) # Get a datetime object
         print t.ctime( ) # Print the date time in an easy-to-read format

def getTime( ):
         # Return the current time
         t = datetime.datetime.now ( ) # Get a datetime object
         return t # Return the datetime object to the caller

def diffTime( start, end, message= "Time elapsed:"):
         difference = end - start
         weeks, days = divmod(difference.days, 7)
         minutes, seconds = divmod(difference.seconds, 60)
         hours, minutes = divmod(minutes, 60)
         print message
         print "%d weeks, %d days, %d:%d:%d" % (weeks, days, hours, minutes, seconds)