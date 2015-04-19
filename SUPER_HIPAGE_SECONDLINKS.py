# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 20:13:12 2015

@author: Shfun Huang
"""
### Super hiPage中華黃頁網路電話簿
from bs4 import BeautifulSoup 
import requests

### 取得 第二層連結 
url1 = "https://www.iyp.com.tw/food-catering/"
res1 = requests.session().get(url1)
#print res1.encoding
res1.encoding = 'utf-8'
print res1.encoding
res_text = res1.text.encode('utf-8')
soup1 = BeautifulSoup(res1.text)

### 取得 第二層連結 以及 中文化desc
f1 = open("./data/Super_hiPage/first_links.txt", "r")
f2 = open("./data/Super_hiPage/second_links.txt", "w")

for links1 in f1.readlines():
    #time.sleep(abs(numpy.random.randn()))
    
    try:
        #print "https://www.iyp.com.tw/" + links1.strip()
        res1 = requests.session().get("https://www.iyp.com.tw/" + links1)
        res1.encoding = 'utf-8'
        res_text = res1.text.encode('utf-8')
        soup1 = BeautifulSoup(res1.text)
        div = soup1.find('div', {'id':'category-title'})
        cate_title =div.find('h2').text
        
        for sub in soup1.findAll('ul', {'class':'sub clearfix'}):
            for li in sub.select('li'):                
                for a in li.select('a'):
                    print a['href'] + "," + cate_title + "," + a.text.strip()
                    f2.write(a['href'] + "," + cate_title.encode('utf-8') + "," + a.text.encode('utf-8').strip())
                    f2.write("\n")
    except BaseException, e:
        print e  
        
f1.close()
f2.close()

### 計算抓取連結數
line_num2 = 0
f2 = open('./data/Super_hiPage/second_links.txt', 'r')
for line2 in f2.readlines():
    line_num2 = line_num2 + 1
print line_num2
f2.close()
