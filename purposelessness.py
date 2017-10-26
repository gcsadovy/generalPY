#purposelessness
def findslope (x1, y1, x2, y2):
    rise = y2 - y1
    run = x2 - x1
    if run ==0:
        slope = "unefined"
    else:
        slope = rise/run
    return slope

x1 = arcpy.GetParameterAsText(0)
y1 = arcpy.GetParameterAsText(1)
x2 = arcpy.GetParameterAsText(2)
y2 = arcpy.GetParameterAsText(3)

a1 = int(x1)
b1 = int(y1)
a2 = int(x2)
b2 = int(y2)

myslope = findslope(a1, b1, a2, b2)
print myslope