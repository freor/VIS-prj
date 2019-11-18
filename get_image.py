import json
import os
import time

jsonfile = open('./youtube-json/CAvideos.json', 'r')

d = json.load(jsonfile)

for i in d:
    print(i)
    os.system("wget -O " + d[i]["thumbnail_link"])
    time.sleep(5)

