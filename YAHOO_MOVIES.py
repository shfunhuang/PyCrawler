# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 12:09:25 2015

@author: Shfun Huang
"""

import requests
import numpy
import time
import re
from BeautifulSoup import BeautifulSoup

f0 = open("./data/Yahoo/miss.txt", "w")
f1 = open("./data/Yahoo/movie.txt", "w")
f2 = open("./data/Yahoo/director.txt", "w")
f3 = open("./data/Yahoo/performer.txt", "w")

### 電影id區間 
miss = 0
start_id = 1
end_id = 5808

for m_id in range(start_id, end_id + 1):
    time.sleep(abs(numpy.random.randn()))
    try:
        url = 'https://tw.movies.yahoo.com/movieinfo_main.html/id=' + str(m_id)
    
        res = requests.get(url)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text)
        
        item = soup.find('div',{'class':'item clearfix'})
        vote = soup.find('div', {'class':'vote clearfix'})
        vsum = soup.find('div', {'class':'sum'})
        
        ### 跳過無資料頁面
        if len(item) == 13:
            miss = miss + 1
            f0.write(url)
            f0.write("\n")
            continue
        
        dta = []
        for p in item.findAll('p'):
            dta.append(p.find('span', {'class':'dta'}).text)
        
        name = []
        ### 演員過濾中文 & 特殊符號 & 數字
        for i in ",".join(dta).split(",")[3:-2]:
            for j in re.sub(r'[\x80-\xff]{3,}|(\d+)', '', str(i.encode('utf-8'))).split(")("):
                name.append(re.sub('\\n', ',', re.sub('\(|\)|', '', j)))
                #print re.sub('\(|\)', '', j)
        #print str(m_id) + ";" + name[0]
        #print str(m_id)  + ";" + ','.join(name[1:])                  
        #print item.find('h4').text.encode('utf-8') + "," + item.find('h5').text.encode('utf-8') + "," + ','.join(dta).encode('utf-8')
        #f1.write(item.find('h4').text.encode('utf-8') + ";" + item.find('h5').text.encode('utf-8') + ";" + ','.join(dta).encode('utf-8') + ";" + vote.find("strong").text.encode('utf-8') + ";" + vote.find("q").text.encode('utf-8') + ";" + vsum.find("em").text.encode('utf-8') + ";" + vsum.find("q").text.encode('utf-8'))
        f1.write(str(m_id) + ";" + item.find('h4').text.encode('utf-8') + ";" + item.find('h5').text.encode('utf-8') + ";" + vote.find("strong").text.encode('utf-8') + ";" + vote.find("q").text.encode('utf-8') + ";" + vsum.find("em").text.encode('utf-8') + ";" + vsum.find("q").text.encode('utf-8'))
        f1.write("\n")
        f2.write(str(m_id) + ";" + name[0])
        f2.write("\n")
        f3.write(str(m_id)  + ";" + ','.join(name[1:]))
        f3.write("\n")
        
    except BaseException, e:
        print e

print "missing:" + str(miss)
f0.close()
f1.close()
f2.close()
f3.close()