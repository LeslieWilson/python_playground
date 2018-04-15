"""
Leslie Wilson
Sunday April 15, 2018
readcsv.py

"""

# THIS FILE IS THE SECOND THAT NEEDS TO RUN. IT CREATES THE DATA.TXT FILE, WHICH THEN GETS ACOUNTS OF THE NUMBER OF TIMES ANY GIVEN CATEGORY SHOWS UP(IN THE JSON FILE), APPENDED INTO IT. FOR INSTANCE, THERE ARE TWO PEOPLE WHO FALL INTO THE FEMALE CATEGORY. SO BELOW AT DATA.WRITE, I'M MAKING THE NES. SPACES FOR THE CATEGORIES NEXT TO WHICH I WANT COUNTS TO APPEAR, AND THEN IT POPULATES WHEN I RUN THE PROGRAM. 


import csv
from collections import Counter
"""collections is a counter tool provided to support convient tallies"""

with open('Data.csv', 'r') as csvfile:
    """function takes a file an opens it, reads it"""

    reader = csv.reader(csvfile)
    array = []
    for row in reader:
        for column in row:
            array.append(column)
    c = Counter(array)
csvfile.close()


data = open('Data.txt', 'w')
"""function takes a file and opens it, writes to it"""

data.write('8 \nLabor-Department %d\nHispanic-Ethnicity %d\nGender(female) %d\nEducation-Level(College) %d\nUniversity(Harvard) %d\nMajor(English) %d\n1990-Grad-Yr %d\n2001-Grad-Yr %d' % (c['labor dept'],c['african american'], c['female'], c['college'], c['harvard university'], c['english'], c['1990'], c['2001']))
data.close()
