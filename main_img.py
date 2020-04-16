	
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

quary_word=sys.argv[1]
max_num=int(sys.argv[2])

for num in range(max_num):
    url="https://search.yahoo.co.jp/image/search?p={0}&ei=UTF-8&b={1}".format(quary_word,1+20*num)
    res = requests.get(url,timeout=1)
    res.raise_for_status()
    html = BeautifulSoup(res.text, 'html.parser')

    imgs=html.find_all(alt="「{}」の画像検索結果".format(quary_word))

    for i in range(len(imgs)):
        dir_name="data/{0}/".format(quary_word)
        if not os.path.isdir(dir_name):
            os.makedirs(dir_name)
        filepath = dir_name + "{0}-{1}.jpg".format(num,i)
        urllib.request.urlretrieve(imgs[i]["src"],filepath)