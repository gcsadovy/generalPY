dir = "C:/Temp"
print dir

files = os.listdir(dir)
print files

dic = {}

for file in files:
    fullPath = dir + "/" + file
    print fullPath
    timestamp = os.path.getmtime(fullPath)
    print timestamp
    dic[file] = timestamp
    print dic
    print 'done'