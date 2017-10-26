# manageParcels.py

import parcelClass

myParcel = parcelClass.parcel(145000, "residential") 
print "Value:", myParcel.value
print "Zoning:", myParcel.zoning
mytax = myParcel.calculateTax()
print "Tax:", mytax