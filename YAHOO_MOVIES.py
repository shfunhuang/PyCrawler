# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 12:11:00 2015

@author: Shfun Huang
"""

import requests
#import sys
import numpy
import time
import re
from bs4 import BeautifulSoup
import contextlib
#reload(sys)
#sys.setdefaultencoding('utf8')



### 電影id區間 
miss = 0
start_id = 1
end_id = 10

with contextlib.nested(open('data/Yahoo/miss.txt', 'w'), 
                       open('data/Yahoo/movie.txt', 'w'),
                       open('data/Yahoo/director.txt', 'w'),
                       open('data/Yahoo/performer.txt', 'w'),
                       open('data/Yahoo/ymvmodule.txt', 'w')) as (f0, f1, f2, f3, f4):   
 
    for m_id in range(start_id, end_id + 1):
        
        try:
            time.sleep(abs(numpy.random.randn()))
            url = 'https://tw.movies.yahoo.com/movieinfo_main.html/id=' + str(m_id)
            res = requests.get(url, verify=True)
            res.encoding = 'utf-8'
        
            soup = BeautifulSoup(res.text)
            item = soup.find('div', {'class':'item clearfix'})
            
            ### f0 ### 
            # 無資料頁面
            if len(item) == 13:
                miss = miss + 1
                f0.write(url)
                f0.write("\n")
                continue
            
            ### f1 ###
            #print item.find('h4').text.encode('utf-8') #中文片名 
            #print item.find('h5').text.encode('utf-8') #英文片名
    
            dta1 = []
            for p in item.findAll('p'):
                dta1.append(p.find('span', {'class':'dta'}).text)
    
            detail = []
            for d in ",".join(dta1).split(",")[0:3]:
                detail.append(d)
        
            #print detail[0].encode('utf-8') #上映日期
            #print detail[1].encode('utf-8').replace('、',',') #類型
            #print detail[2].encode('utf-8') #片長
    
            vote = soup.find('div', {'class':'vote clearfix'})
            vsum = soup.find('div', {'class':'sum'})
    
            #print re.sub('%','',vote.find("strong").text.encode('utf-8')) #想看人數(%)
            #print vote.find("q").text.encode('utf-8') #投票人數
            #print vsum.find("em").text.encode('utf-8') #總評分
            #print vsum.find("q").text.encode('utf-8') #評分人數
    
            f1.write(str(m_id)+";"+item.find('h4').text.encode('utf-8')+";"+item.find('h5').text.encode('utf-8')+";"+detail[0].encode('utf-8')+";"+detail[1].encode('utf-8').replace('、',',')+";"+detail[2].encode('utf-8')+ ";" + re.sub('%','',vote.find("strong").text.encode('utf-8')) + ";" + vote.find("q").text.encode('utf-8') + ";" + vsum.find("em").text.encode('utf-8') + ";" + vsum.find("q").text.encode('utf-8'))
            f1.write("\n")
            
            ### f2 ###
            dta2 = []
            for p2 in item.findAll('p'):
                dta2.append(p2.find('span', {'class':'dta'}))
        
            director1 = []
            for dta22 in dta2[3].findAll('a'):
                director1.append(re.sub('(\w+)|\(|\)|\.', '', dta22['href'].replace('/artist_filmography.html?name=','')).strip())
            
            #print ''.join(director1) #中文導演名稱
    
            dta21 = []
            for p in item.findAll('p'):
                dta21.append(p.find('span', {'class':'dta'}).text)
    
            director2 = []
            ### 過濾中文 & 特殊符號 & 數字
            for i in ",".join(dta21).split(",")[3:-2]:
                for j in re.sub(r'[\x80-\xff]{3,}|(\d+)', '', str(i.encode('utf-8'))).split(")("):
                    director2.append(re.sub('\\n', ',', re.sub('\(|\)|', '', j)).strip())
    
            #print director2[0] #英文導演名稱
            
            f2.write(str(m_id) + ";" + ''.join(director1).encode('utf-8') + ";" + director2[0])
            f2.write("\n")
            
            ### f3 ###
            dta3 = []
            for p3 in item.findAll('p'):
                dta3.append(p3.find('span', {'class':'dta'}))

            performer1 = []
            for dta3 in dta2[4].findAll('a'):
                performer1.append(dta3['href'].replace('/artist_filmography.html?name=','').replace('\r\n',''))

            #print ','.join(performer1) #中文演員名稱
    
            dta21 = []
            for p in item.findAll('p'):
                dta21.append(p.find('span', {'class':'dta'}).text)
    
            performer2 = []
            ### 過濾中文 & 特殊符號 & 數字
            #for i in ",".join(dta21).split(",")[3:-2]:
            #    for j in re.sub(r'[\x80-\xff]{3,}|(\d+)', '', str(i.encode('utf-8'))).split(")("):
            #        performer2.append(re.sub('\\n', ',', re.sub('\(|\)|', '', j)))
                    
            ### 找出()內的英文演員名字
            for i in ",".join(dta21).split(",")[4:-2]:
                text =  re.sub(r'[\x80-\xff]{3,}|(\d+)', '', str(i.encode('utf-8')))
                #print text
                m1 = re.split(r'\(\)' ,text) 
                for m2 in m1:
                    for m3 in re.sub('\)(\w+)', '', m2).split("("):
                        #print m3.replace(')','').replace(";","")
                        performer2.append(re.sub('\)|;','', m3).replace('\r\n',''))
                        
            #print ','.join(performer2[1:]) #英文演員名稱
            
            f3.write(str(m_id) + ";" + ','.join(performer1).encode('utf-8') + ";" + ','.join(performer2[1:]))
            f3.write("\n")
            
            ### f4 ###
            try:
                ymvs = soup.find('div', {'id':'ymvs'}).find('div', {'class':'text full'}).find('p')
                f4.write(str(m_id)+";"+ymvs.text.encode('utf-8').replace('《','(').replace('》',')'))
                f4.write("\n")
                #print ymvs.text #劇情簡介
                
            except BaseException, e:
                ymvs = soup.find('div', {'id':'ymvs'}).find('div', {'class':'text show'}).find('p')
                f4.write(str(m_id)+";"+ymvs.text.encode('utf-8').replace('《','(').replace('》',')'))
                f4.write("\n")
            
        except BaseException, e:
            print e
            
print miss





