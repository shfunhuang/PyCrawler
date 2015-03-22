# PTT Baseball
import requests
from bs4 import BeautifulSoup
url = "https://www.ptt.cc/bbs/baseball/index.html"
#print url
res = requests.get(url, verify=False)
soup = BeautifulSoup(res.text)
#print soup
# 取得 標題/作者
for ele in soup.select('.r-ent'): ## "#":id, ".":class
    if len(ele.select('a')) > 0:
        #print ele.select('a')[0]
        print ele.select('a')[0].text, ele.select('div')[5].text
        #print "https://www.ptt.cc" + ele.select('a')[0]['href']
        #print ele.findAll('a', {'href':'True'})
        #print ele.select('div')[5].text
        #print ele.find('div' ,{'class':'author'}).text
	
# 取得 標題/作者/連結
import requests
from bs4 import BeautifulSoup
url = "https://www.ptt.cc/bbs/baseball/index%s.html"
indexlist = range(2490,2499)
for index in indexlist:
    all_url = url%(index)
    #print all_url        
    res = requests.get(all_url, verify=False)
    soup = BeautifulSoup(res.text)
    for ele in soup.select('.r-ent'):
        # 避免遇到刪文錯誤
        if ele.find('a') is not None:
            print ele.select('a')[0].text, ele.select('div')[5].text
            print "https://www.ptt.cc" + ele.select('a')[0]['href']




		
