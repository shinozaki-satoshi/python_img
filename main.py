# coding: UTF-8
import requests
from bs4 import BeautifulSoup
import time
import os
import pandas as pd
import codecs
from urllib.parse import urljoin
import urllib.request
import sys
import cv2

quary_word=sys.argv[1]
max_num=int(sys.argv[2])

for num in range(max_num):
    url="https://search.yahoo.co.jp/image/search?p={0}&ei=UTF-8&b={1}".format(quary_word,1+20*num)
    res = requests.get(url,timeout=1)
    res.raise_for_status()
    html = BeautifulSoup(res.text, 'html.parser')

    imgs=html.find_all(alt="「{}」の画像検索結果".format(quary_word))

    for i in range(len(imgs)):
        dir_name="data/{0}/faceCheck/".format(quary_word)
        if not os.path.isdir(dir_name):
            os.makedirs(dir_name)
        filepath = dir_name + "{0}-{1}.jpg".format(num,i)
        urllib.request.urlretrieve(imgs[i]["src"],filepath)

faceCount=0
for num in range(max_num):
    for i in range(len(imgs)):
        img =cv2.imread("data/{0}/faceCheck/{1}-{2}.jpg".format(quary_word,num,i))

        cascade_file_face="face.xml"
        cascade_face=cv2.CascadeClassifier(cascade_file_face)

        #画像を白黒に変換
        img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        face_list=cascade_face.detectMultiScale(img_gray,minSize=(10,10))


        for (x,y,w,h) in face_list:
            color =(0,0,225)
            pen_w=2
            cv2.rectangle(img,(x,y),(x+w,y+h),color,thickness=pen_w)
            faceCount+=1

        cv2.imwrite("{0}/{1}-{2}.jpg".format(dir_name,num,i),img)
print("顔検出数："+str(faceCount))
