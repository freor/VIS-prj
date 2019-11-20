import json
import os
import time

jsonfile = open('../youtube-json/new_CAvideos.json', 'r')

d = json.load(jsonfile)["nodes"]

for i in d:
    img_id = i["id"]
    link = i["group"]["thumbnail_link"]
    os.system("wget -O ../thumbnail_img/" + img_id + ".jpg " + link)


