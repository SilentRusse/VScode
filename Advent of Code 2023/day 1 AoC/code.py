import values.txt
import re

allnumbers = []
for line in file:
    allnumbers =re.findall(r'\b\d+\b', line)
    last = len(allnumbers)
    firstnumber = allnumbers[0]
    lastnumber = allnumbers[last]
    print (firstnumber + lastnumber)
