import csv
import json
from collections import OrderedDict
import time

csvfile = open('./data/CAvideos.csv', 'r')
jsonfile = open('./youtube-json/CAvideos.json', 'w')

# 'key' extraction
spamreader = csv.reader(csvfile, delimiter=',')
key = tuple(next(spamreader))
print("key", key)
main_key = "video_id"


data = OrderedDict()

# json generation
reader = csv.DictReader(csvfile, key)
for row in reader:
    #print(row)
    data[row[main_key]] = row

json.dump(data, jsonfile, indent='\t')
