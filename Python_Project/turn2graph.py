# import csv
# import collections
#
# counts = collections.Counter()
# with open('Data.csv') as input_file:
#     for row in csv.reader(input_file, delimiter=','):
#         counts[row[1]] += 1
#
# print ('level in school: %s' % counts['college'])


import csv

my_reader = csv.reader(open('Data.csv'))
ctr = 0
for record in my_reader:
    if record[1] == 'level':
        ctr += 1

print(ctr)
