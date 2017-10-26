#tableGUI.py
#gcsadovy
#Garik SAdovy

import tkFileDialog, arcpy
fobject = tkFileDialog.askopenfilename(filetypes=[("shapefiles","*.shp"),("tables","*dsb")], initialfile='COVER63p.shp', initialdir='C:\Temp', title='Pick a file')

fields = arcpy.ListFields(fobject)
for field in fields:
    print field.name



