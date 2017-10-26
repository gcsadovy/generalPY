class parcel:
    def __init__(self, value, zoning):
        self.value = value
        self.zoning = zoning

    def calculateTax(self):
        rate = 0.076
        if self.zoning == "residential":
            rate = 0.075
        elif self.zoning == "industrial":
            rate = 0.77
        tax = self.value*rate
        return tax

if __name__ == "__main__":
    myParcel = parcel(145000, "residential")
    print "Value:", myParcel.value
    print "Zoning:", myParcel.zoning
    myParcel.zoning = "other"
    print "Zoning:", myParcel.zoning
    mytax = myParcel.calculateTax()
    print "Tax:", mytax

    print "\n"

    myParcel2 = parcel(290000, "industrial")
    print "Value:", myParcel2.value
    print "Zoning:", myParcel2.zoning
    mytax = myParcel2.calculateTax()
    print "Tax:", mytax
    myParcel2.value = 290
    mytax = myParcel2.calculateTax()
    print "Tax:", mytax
    print "Parcel 1 Zoning:", myParcel.zoning

