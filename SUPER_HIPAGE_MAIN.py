# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 23:50:30 2015

@author: Shfun Huang
"""

### Super hiPage中華黃頁網路電話簿
from bs4 import BeautifulSoup 
from math import ceil
import requests
import numpy
import time

### 取得 各子分類 cate_id, 店家總數(record_total), 第一頁店家數(page1), 子分類頁種數(page_number),第一層分類名稱(lv1), 子分類名稱(lv3)

f2 = open("./data/Super_hiPage/second_links.txt", "r")
#f3 = open("./data/Super_hiPage/third_links.txt", "w")
f4 = open("./data/Super_hiPage/index.txt", "w")

for catg in f2.readlines():
    
    ### 取得店家總數
    lv1 = catg.split('/')[1]
    lv3 = catg.split('/')[2].split('.')[0]
    time.sleep(abs(numpy.random.randn()))
    
    try:
        url2 = "https://www.iyp.com.tw/" + lv1 + "/" + lv3 + ".html"
        res2 = requests.get(url2)
        res2.encoding = 'utf-8'
        res_text = res2.text.encode('utf-8')
        soup2 = BeautifulSoup(res2.text)
        cate_id = soup2.findAll('ul', {'a_id':'0'})[0]['cate_id']
        
        url = "https://www.iyp.com.tw/showroom.php?main=ajax&func=get_area"
        payload = {
            'cate_id': cate_id,
            'a_id': '0',
            'eng_lv1': lv1,
            'eng_lv3': lv3
        }
        res = requests.session().post(url, data=payload)
        res.encoding = ('utf-8')
        res_text = res.text.encode('utf-8')
        soup = BeautifulSoup(res.text)
        record_total = soup.find('span', {'class':'rt'}).text
        #print record_total
        
        ### 取得第一頁 店家數
        rec = soup2.findAll('span', {'class':'list-id'})
        for list_id in rec:
            page1 =  list_id.text
        #print page1
        
        ### 計算分類頁數 公式
        page_number = str(round(ceil(((int(record_total) - int(page1) + 1) // 10)  + 1), 0))
        #print page_number
        
        print cate_id + "," + record_total + "," + page1 + "," + page_number + "," + lv1 + "," + lv3
        f4.write(cate_id + "," + record_total + "," + page1 + "," + page_number + "," + lv1 + "," + lv3)
        f4.write("\n")
        
    except BaseException, e:
        print e    
        
f2.close()
f4.close()

### index.txt 連結數
line_num4 = 0
f4 = open("./data/Super_hiPage/index.txt", "r")
for line4 in f4.readlines():
    line_num4 = line_num4 + 1
print line_num4
f4.close()

### 從 index.txt 取得所有指標
### 從 取得所有子分類連結

f4 = open("./data/Super_hiPage/index.txt", "r")
f5 = open("./data/Super_hiPage/index_links.txt", "w")
url1 = "https://www.iyp.com.tw/showroom.php?cate_name_eng_lv1="
url2 = "&cate_name_eng_lv3="
url3 = "&p="

for index in f4.readlines():

    for p in range(int(index.split(',')[3].split('.')[0])+1):
        
        url_links = url1 + index.split(',')[4] + url2 + index.split(',')[5].strip('\n') + url3 + str(p)

        # 第一頁不存
        if p == 0:
            continue
        
        f5.write(url_links)
        f5.write("\n")
        
f4.close()
f5.close()

### 取得 分類 &子分類 &電話 &店家名稱
# -*- coding: utf8 -*-
f5 = open("./data/Super_hiPage/index_links.txt", "r")
f6 = open("./data/Super_hiPage/index_tele.txt", "w")

for url_catg in f5.readlines():
    #print url_catg
    lv1 = url_catg.split('cate_name_eng_lv1=')[1].split('&cate_name_eng_lv3=')[0]
    lv3 = url_catg.split('cate_name_eng_lv1=')[1].split('&cate_name_eng_lv3=')[1].split('&p=')[0]
    
    res_catg = requests.get(url_catg)
    res_catg.encoding = 'utf-8'
    soup_catg = BeautifulSoup(res_catg.text)    

    for h3 in soup_catg.findAll('ol', {'class':'general'}):
        for a in h3.findAll('a'):
            try:             
                tele = a['href'].split("//www.iyp.com.tw/")[1].split("/")[0] + "," + a['title']
                print lv1 + "," + lv3 + "," + tele
                f6.write(lv1 + "," + lv3 + "," + tele.encode('utf-8').strip())
                f6.write("\n")
                
            except BaseException, e:
                #f6.write("null")
                #f6.write("\n")
                print e       

f5.close()
f6.close()

### 取得分類 &子分類 &關鍵字
f2 = open("./data/Super_hiPage/second_links.txt", "r")
f8 = open("./data/Super_hiPage/second_links_keys.txt", "w")

for url_links in f2.readlines():
    #time.sleep(abs(numpy.random.randn()))
    lv1 = url_links.split('/')[1]
    lv3 = url_links.split('/')[2].strip()
    
    try:
        url_links_full = "https://www.iyp.com.tw" + url_links
        res_links = requests.get(url_links_full)
        res_links.encoding = 'utf-8'
        soup_links = BeautifulSoup(res_links.text)
        related_keys = soup_links.find('div', {'id':'related-keyword'})
    
        keys_list = []
        for keys in related_keys.findAll('li'):
            keys_list.append(keys.text)
        print lv1 + "," + lv3 + "," + ';'.join(keys_list)
        f8.write(lv1 + "," + lv3 + "," + (';'.join(keys_list)).encode('utf-8')) 
        f8.write("\n")
        
    except BaseException, e:
        print e   
    
f2.close()
f8.close()