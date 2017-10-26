# shape3text_loop.py
# Purpose: Convert shapefiles to text
# Author Chris Snyder
# Usage: Directory containing shapefiles
# Example: "C:/Temp/My data"
# Modified by Laura Tateosian to convert every shapefile in workspace
import sys, string, os, arcgisscripting

try:
    gp = arcgisscripting.create()

    try:    
        gp.workspace = sys.argv[1]

        fcs = gp.ListFeatureClasses( ) # ListFeatureClasses method returns an object which contains a list of strings. 
        fcs.Reset( ) # Place the cursor just before the first item in the list 
        fc = fcs.Next( ) # Return the first item in the list
        # For every shapefile in this directory
        while fc:
            # Give the output text file the same name as the shapefile        
            # SET text output file name
            txtFile = gp.workspace + "/"+ fc.split(".")[0] + ".txt"
          
            fieldList = []
            fieldEnum = gp.ListFields(fc)
            field = fieldEnum.next()

            # Get a list of the fields in the the current shapefile
            while field:
                if field.name != "Shape":
                    fieldList.append(field.name)
                field = fieldEnum.next()
            line = ""

            # Copy the field names to a variable called line
            for field in fieldList:
                line = line + field + ","
                
            # Print the field names in the current output text fie
            print line[:-1]; print >> open(txtFile, 'a'), line[:-1]
            line = ""
            searchCur = gp.SearchCursor(fc)
            searchRow = searchCur.next()
            # For each row in the current shapefile
            while searchRow:

                # Copy the field values into a variable called line
                for field in fieldList:
                    line = line + str(searchRow.getvalue(field)) + ","

                # Print the current line to the current output text file
                print line[:-1]; print >> open(txtFile, 'a'), line[:-1]
                line = ""
                searchRow = searchCur.next()
                
            # Prepare for next shapefile.
            del searchCur
            del searchRow
            fc = fcs.Next()
    except IndexError:
        print "Usage: Directory containing shapefiles"
except:
    gp.getmessages( )