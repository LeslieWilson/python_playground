import csv
import json

jsondata = json.load(open('input.json'))

with open('Data.csv', 'a', newline='') as csvfile:

    jsonwriter = csv.writer(csvfile, delimiter=',' )
    jsonwriter.writerow([jsondata['name']] + [jsondata['manager']])

print (jsondata['name'])
