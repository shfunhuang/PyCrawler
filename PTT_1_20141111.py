# 取得 PTT 資訊
# PTT FOOD
import requests
res = requests.get('http://www.ptt.cc/bbs/Food/index.html', verify=False)
#print res.text

# 取得一頁連結
import requests
from BeautifulSoup import BeautifulSoup
res = requests.get('http://www.ptt.cc/bbs/Food/index.html', verify=False)
soup = BeautifulSoup(res.text)
links = [tag['href'] for tag in soup.findAll('a', {'href': True})] 
#print links
for i in range(9, len(links)):
    print "https://www.ptt.cc" + links[i] + "\t"

# 有未滿18歲認證處理方式
# PTT SEX
# -*- encoding = utf-8 -*-
import requests
payload = {
    'from':'/bbs/Sex/index.html',
    'yes':'yes'
}
rs = requests.session()
res = rs.post('http://www.ptt.cc/ask/over18', verify=False, data=payload)
res2 = rs.get('https://www.ptt.cc/bbs/sex/index.html', verify=False)
print res2.text




