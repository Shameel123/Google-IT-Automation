#!/usr/bin/env python3
import shutil
import os, glob
from PIL import Image

#converts file from TIFF to JPG
tiffPath = "images\\*.TIFF"
for file in glob.glob(tiffPath):
       name = os.path.basename(file)
       name = name[0:3]
       im = Image.open(file).convert('RGB').save(name+".jpeg", "JPEG")

#move JPEG files to the required destinations
jpgPath = "*.JPG"
move = "images\\"
for file in glob.glob(jpgPath):
       shutil.move(file,move)
