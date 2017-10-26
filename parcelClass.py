#parcelClass.py

class parcel: 
    def __init__(self, value, zoning): 
        self.value = value 
        self.zoning = zoning

    def calculateTax(self ):
        rate = 0.076 
        if self.zoning == "residential":
            rate = 0.075 
        elif self.zoning == "industrial":
            rate = 0.77
        tax = self.value*rate
        return tax