import json

with open ('input.json') as json_data:
    data = json.load(json_data)

    for r in data['Employee']:
        # fo = open(r['id'] + "_" + r['name']+ ".txt", "wb")

        fo = open('test.csv', 'w')

        fo.write(r(['name']+['manager'])

        fo.close()

        # print r['name']
