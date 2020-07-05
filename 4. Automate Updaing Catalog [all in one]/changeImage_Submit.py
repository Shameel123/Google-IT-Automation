#!/usr/bin/env python3
import shutil
import os, glob
from PIL import Image

#/home/student-01-371d6501f80a/supplier-data/images

#converts file from TIFF to JPG
size = 600,400
tiffPath = "/home/student-02-a0a7adf929ff/supplier-data/images/*.tiff"
for file in glob.glob(tiffPath):
       name = os.path.basename(file)
       name = name[0:3]
       im = Image.open(file).convert('RGB').resize((size)).save(name+".jpeg", "JPEG")

#move JPEG files to the required destinations
jpgPath = "*.jpeg"
move = "/home/student-02-a0a7adf929ff/supplier-data/images/"
for file in glob.glob(jpgPath):
       shutil.move(file,move)
