import os
from shutil import copy2
from datetime import datetime
from PIL import Image
from sys import argv

username = argv[1]
dest = argv[2]
source = "C:/Users/" + username + "/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets"
currentImgs = []
for filename in os.listdir(dest):
    try:
        image = Image.open(dest + "/" + filename)
        currentImgs.append(image)
    except:
        print(filename)

i = 0
for filename in os.listdir(source):
    sourceFile = source + "/" + filename
    try:
        im = Image.open(sourceFile)
        width, height = im.size

        if width != 1920 or height != 1080:
            continue

        h = im.histogram()
        if any(h == ci.histogram() for ci in currentImgs):
            continue

        destFile = "{0}/{1:%Y-%m-%d-%H-%M-%S}{2}.jpg".format(
            dest, datetime.now(), i)
        i += 1
        copy2(sourceFile, destFile)
        currentImgs.append(im)
    except:
        print(filename)
