import csv
import json

data = {}

with open('status-codes.tsv', 'r') as tsvfile:
    reader = csv.reader(tsvfile, delimiter=';')
    for row in reader:
        data[row[0]] = row[1]

with open('status-codes.json', 'w') as jsonfile:
    json.dump(data, jsonfile, indent=4)