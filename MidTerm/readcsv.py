import csv
from collections import Counter

with open('Data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    array = []
    for row in reader:
        for column in row:
            array.append(column)
    c = Counter(array)
csvfile.close()
data = open('Data.txt', 'w')
data.write('8 \nLabor-Department %d\nHispanic-Ethnicity %d\nGender(female) %d\nEducation-Level(College) %d\nUniversity(Harvard) %d\nMajor(English) %d\n1990-Grad-Yr %d\n2001-Grad-Yr %d' % (c['labor dept'],c['african american'], c['female'], c['college'], c['harvard university'], c['english'], c['1990'], c['2001']))
data.close()
