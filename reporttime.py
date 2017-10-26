#repottime

import time
import datetime

def reportTime():
    t = datetime.datetime.now()
    print t.ctime()