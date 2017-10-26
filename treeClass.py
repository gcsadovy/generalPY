class tree:
    def __init__(self, block, plot, species, dbh):
        self.block = block
        self.plot = plot
        self.species = species
        self.dbh = dbh
    def calculateDIB(self):
        DIB = self.dbh*0.917
        return DIB
    def calculateHeight(self):
        height = self.dbh * .15 + 86.6
        if self.species == "LP":
            height = self.dbh * .025 + 98.8
        return height
    def report(self, num):
        print "\nReport Tree",num
        print "-------------"
        print "Block: ", self.block
        print "Plot: ", self.plot
        print "Species: ", self.species
        print "DBH: ", self.dbh
        print "DIB: ", self.calculateDIB()
        print "Height: ", self.calculateHeight()
        print "\n"


if __name__ == "__main__":        
    t1 = tree(5,91,"SG",14) # Create a tree object t1 from record 1 of rdu_forest.txt
    print "Tree 1 Species:", t1.species  # Print t1's species
    dib = t1.calculateDIB()  # Calculate t1's DIB
    print "Tree 1 DIB:", dib  # Print t1's DIB
    t1.report(1) # report t1 information

    t2 = tree(5,91,"LP",23) # Create a tree object t2 from record 2 of rdu_forest.txt
    print "Tree 2 DBH:", t2.dbh
    height2 = t2.calculateHeight()
    print "Tree 2 Height:", height2

    t3 = tree(5, 91, "LP", 17)
    print "Tree 3 Block:", t3.block
    print "Tree 3 Plot:", t3.plot

    t4 = tree(5, 91, "LP", 18)
    print t4.report(4)


