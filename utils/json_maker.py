import csv
import json
from collections import OrderedDict
import time

csvfile = open('../data/GBvideos.csv', 'r')

# 'key' extraction
spamreader = csv.reader(csvfile, delimiter=',')
key = tuple(next(spamreader))
print("key", key)
main_key = "video_id"

n_top = 100 # extract top-100
sort_base = "views" # "likes"
jsonfile = open('../youtube-json/' + sort_base + '_GBvideos.json', 'w')

data = []

# json generation
reader = csv.DictReader(csvfile, key)
for row in reader:
    #data.append({"id": row[main_key], "group" : row})
    data.append(row)

data.sort(key=lambda x: x[sort_base], reverse=True)
datas = OrderedDict()

#datas["nodes"] = data[:n_top]

datas = data[:n_top]

json.dump(datas, jsonfile, indent='\t')



