"""
Leslie Wilson
Sunday April 15, 2018
input2csv.py
"""

# THIS FILE IS THE FIRST THAT NEEDS TO BE RUN. IT CREATES THE CSV FILE FROM THE PREEXISTING JSON FILE. IT CHANGES EVERYTHING TO COMMA-SEPARATED VALUES BY SETTING A DELIMITER. AT THE VERY BOTTEM I AM TELLING THE PROGRAM THE CATEGORIES FROM THE JSON FILE I'M LOOKING TO HAVE WRITTEN TO THE CSV FILE. THE CSV FILE POPULATES W THIS INFORMATION FOR EVERY PERSON.

import csv
import json

jsondata = json.load(open('input.json'))
"""function takes premade json data and loads it into another file"""

with open('Data.csv', 'a', newline='') as csvfile:
    """function takes __ and turns it into a csv file"""

    jsonwriter = csv.writer(csvfile, delimiter=',' )
    for info in jsondata:
        for degree in info['degrees']:
            # print(info['name'])
            # print(degree['level'])
            jsonwriter.writerow([info['name']] + [info['dept']] + [info['ethnicity']] + [info['gender']] + [degree['level']] + [degree['location']] + [degree['subject']] + [degree['grad year']])
