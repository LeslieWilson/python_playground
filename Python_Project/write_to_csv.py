import csv
import json

jsondata = json.load(open('input.json'))

with open('Data.csv', 'a', newline='') as csvfile:
    jsonwriter = csv.writer(csvfile, delimiter=',' )
    for info in jsondata:
        for degree in info['degrees']:
            jsonwriter.writerow([info['name']] + [info['dept']] + [info['ethnicity']] + [info['gender']] + [degree['level']] + [degree['location']] + [degree['subject']] + [degree['grad year']])

#
# class DictQuery(dict):
#     def get(self, path, default = None):
#         keys = path.split("/")
#         val = None
#
#         for key in keys:
#             if val:
#                 if isinstance(val, list):
#                     val = [ v.get(key, default) if v else None for v in val]
#                 else:
#                     val = val.get(key, default)
#             else:
#                 val = dict.get(self, key, default)
#
#             if not val:
#                 break;
#
#         return val
#
#
# for item in jsondata:
#     print DictQuery(item).get("name/gender")
