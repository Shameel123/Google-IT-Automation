#!/usr/bin/env python3
import requests
import os, glob
# This example shows how a file can be uploaded using
# The Python Requests module

#/home/student-01-371d6501f80a/supplier-data/images

url = "http://localhost/upload/"
path = '/home/student-02-a0a7adf929ff/supplier-data/images/*.jpeg'
for i in glob.glob(path):
 with open(i, 'rb') as opened:
    r = requests.post(url, files={'file': opened})
