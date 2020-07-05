#!/usr/bin/env python3
import shutil
import os, glob
from PIL import Image

#/home/student-01-371d6501f80a/supplier-data/images
newsize = 600,400
#converts file from TIFF to JPG
tiffPath = "/home/student-01-371d6501f80a/supplier-data/images/*.tiff"
for file in glob.glob(tiffPath):
       name = os.path.basename(file)
       name = name[0:3]
       im = Image.open(file).convert('RGB').resize((newsize)).save(name+".jpeg", "JPEG")

#move JPEG files to the required destinations
jpgPath = "*.jpeg"
move = "/home/student-01-371d6501f80a/supplier-data/images/"
for file in glob.glob(jpgPath):
       shutil.move(file,move)
