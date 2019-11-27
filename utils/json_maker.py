import csv
import json
from collections import OrderedDict
import time

csvfile = open('../data/INvideos.csv', 'r')

# 'key' extraction
spamreader = csv.reader(csvfile, delimiter=',')
key = tuple(next(spamreader))
print("key", key)
main_key = "video_id"

n_top = 100 # extract top-100
sort_base = "likes" # "likes"
jsonfile = open('../youtube-json/' + sort_base + '_INvideos.json', 'w')

data = []

keys = ["video_id", "title", "channel_title", "category_id", "views", "likes", "dislikes", "thumbnail_link"]

# json generation
reader = csv.DictReader(csvfile, key)
for row in reader:
    #data.append({"id": row[main_key], "group" : row})
    d = {}
    for i in keys:
        d[i] = row[i]
    d["group"] = ""
    data.append(d)

data.sort(key=lambda x: x[sort_base], reverse=True)
datas = OrderedDict()

#datas["nodes"] = data[:n_top]

datas = data[:n_top]

json.dump(datas, jsonfile, indent='\t')



