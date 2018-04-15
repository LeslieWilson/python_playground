import csv
import json

jsondata = json.load(open('input.json'))

with open('Data.csv', 'a', newline='') as csvfile:
    jsonwriter = csv.writer(csvfile, delimiter=',' )
    for info in jsondata:
        for degree in info['degrees']:
            jsonwriter.writerow([info['name']] + [info['dept']] + [info['ethnicity']] + [info['gender']] + [degree['level']] + [degree['location']] + [degree['subject']] + [degree['grad year']])
