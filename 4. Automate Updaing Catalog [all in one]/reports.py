#!/usr/bin/env python3
import os
from reportlab.platypus import Paragraph, Spacer, Image, SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(file, title, add_info):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(file)
    report_title = Paragraph(title, styles['h1'])
    report_info = Paragraph(add_info, styles['BodyText'])
    empty_line = Spacer(1,20)

    report.build([report_title, empty_line, report_info, empty_line])

path = "descriptions\\"
dir = os.listdir(path)
for i in dir:
    #print(i)
    with open(path+i, "r") as file:
        data = file.readlines()
        #print(data)
        for line in data:
            word = line.strip()
            print(word)
#generate_report("abc.pdf","hi","hello")
