#landUse.py
#gcsadovy
#Garik Sadovy

landUse = {'res': 1, 'com': 2, 'int': 3, 'other' :[4,5,6,7]}

print landUse['com']
print landUse.has_key("res")
print landUse['int']
landUse['agr'] = 0
print landUse
landUse['res'] = 10
print landUse
print landUse.keys()
for k,v in landUse.items():
    print v
print landUse.items()
del landUse['int']
print landUse
print 'int' in landUse

     