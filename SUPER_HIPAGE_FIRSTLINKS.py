# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 20:10:38 2015

@author: Shfun Huang
"""

### Super hiPage中華黃頁網路電話簿
from bs4 import BeautifulSoup 
import requests

### 取得 第一層連結數
url = "https://www.iyp.com.tw/"
rs = requests.session()
res = rs.get(url)
res.encoding = 'utf-8'
res_text = res.text.encode('utf-8')
soup = BeautifulSoup(res.text)

f1 = open('./data/Super_hiPage/first_links.txt', 'w')
for li in soup.findAll('ul', {'class':'items'}):
    #print li
    for tag in li.select('a'): 
        #print tag['href']
        f1.write(tag['href'])
        f1.write("\n")
f1.close()

### 計算抓取連結數
line_num1 = 0
f = open('./data/Super_hiPage/first_links.txt', 'r')
for line1 in f.readlines():
    line_num1 = line_num1 + 1
print line_num1
f.close()
