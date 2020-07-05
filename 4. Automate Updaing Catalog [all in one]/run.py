#! /usr/bin/env python3
import os,requests

 #=========================================
#All files are written in the following format, with each piece of information on its own line:
#
# name
# weight (in lbs)
# description
# #=========================================
# The data model in the Django application fruit has the following fields: name, weight, description and image_name. The weight field is defined as an integer field. So when you process the weight information of the fruit from the .txt file, you need to convert it into an integer. For example if the weight is "500 lbs", you need to drop "lbs" and convert "500" to an integer.

#============================================

# The final JSON object should be similar to:
#
# {
# "name": "Watermelon",
# "weight": 500,
# "description": "Watermelon is good for relieving heat, eliminating annoyance and quenching thirst. It contains a lot of water, which is good for relieving the symptoms of acute fever immediately. The sugar and salt contained in watermelon can diuretic and eliminate kidney inflammation. Watermelon also contains substances that can lower blood pressure.",
# "image_name": "010.jpeg"}

#=========================================

dict_data = {
        "name":"Experienced salespeople",
        "weight": 500,
        "description": "Watermelon is good for relieving heat, eliminating annoyance and quenching thirst. It contains a lot of                              water, which is good for relieving the symptoms of acute fever immediately. The sugar and salt contained in                          watermelon can diuretic and eliminate kidney inflammation. Watermelon also contains substances that can lower                        blood pressure.",
        "image_name":"010.jpeg"
}


path = "descriptions\\" #"/data/feedback"

#dir = os.listdir("/data/feedback")
dir = os.listdir(path)


counter = 0
for i in dir:
     image_name = i[0:3]+".jpeg"
     print(image_name)
     with open(path+i, "r") as file:
             data = file.readlines()
             #print(data)
             for line in data:
                 word = line.strip()
                 print(word)
                 if counter==0:
                         dict_data["name"]=word
                 elif counter ==1:
                         dict_data["weight"]=int(word[0:3])
                 elif counter ==2:
                         dict_data["description"]=word
                         dict_data["image_name"]=image_name
    #             elif counter ==3:
    #                     dict_data["image_name"]=word
                 counter +=1
    #
    #             #print(word)
             print(dict_data)
             postData = requests.post("http://34.71.173.235/fruits/",data=dict_data)
             #for k,v in dict_data.items():
             #     postData = requests.post("http://34.71.173.235/fruits/",data={k:v})
              #    print(postData.status_code)
    #
             counter=0
