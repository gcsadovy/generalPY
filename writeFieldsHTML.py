#writeFieldsHTML.py
#gcsadovy
#Garik Sadovy
#argument: full path file name of input file
# writes out field names to html file

import arcpy, os, sys
arcpy.env.overwriteOutput = True

input = sys.argv[1]
output = input[:-4] + ".html"

fields1 = arcpy.ListFields(input)
fields2 = []
for field in fields1:
    fields2.append(field.name)

listItems = """</li>\n    <li>""".join(fields2)
body = """  <ul>\n    <li>{0}</li>\n </ul>""".format(listItems)

n1 = os.path.basename(input)
n2 = n1.lower()
n3 = n2[0].upper() + n2[1:]
#or could use .title for this one

header = """<!DOCTYPE html>
<html>
 <body>
   <h1> {0} {1} </h1>
""".format(n3, "Fields")

footer = """
 </body>
</html>
"""

outf = open(output, 'w')
outf.write(header + body + footer)
outf.close()



