#! /usr/bin/env python3
import os
import requests

#=========================================
# {
# "title": "Experienced salespeople",
# "name": "Alex H.",
# "date": "2020-02-02",
# "feedback": "It was great to talk to the salespeople in the team, they understood my needs and were able to guide me in the right direction"}


#http://<corpweb-external-IP>/feedback


#=========================================

dict_data = {
        'title':"Experienced salespeople",
        'name':"Alex H",
        'date':"2020-02-02",
        'feedback':"It was great to talk to the salespeople in the team, they understood my needs and were able to guide me in the right direction"
}


# for k, v in dict_data.items():
#         dict_data[k] = "shameel"
# #        print("{0},{1}".format(k, v))
# print(dict_data['title'])


path = "text_files\\" #"/data/feedback"

#dir = os.listdir("/data/feedback")
dir = os.listdir(path)


counter = 0
for i in dir:
    #print(i)
    with open(path+i, "r") as file:
            data = file.readlines()
            for line in data:
                word = line.strip()
                if counter==0:
                        dict_data['title']=word
                elif counter ==1:
                        dict_data['name']=word
                elif counter ==2:
                        dict_data['date']=word
                elif counter ==3:
                        dict_data['feedback']=word
                counter +=1

                #print(word)
            print(dict_data)
            counter=0


