from PIL import Image
from torchvision import transforms

import json
import os
import time

jsonfile = open('../youtube-json/new_CAvideos.json', 'r')
fpath = "../thumbnail_img/"

d = json.load(jsonfile)["nodes"]

ext = ".jpg" # image file extension

for i in d:
    fn = fpath + i["id"] + ext

    input_image = Image.open(fn)
    print(input_image.size)


