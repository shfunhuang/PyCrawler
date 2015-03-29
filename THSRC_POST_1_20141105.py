### 使用requests.get
import requests
res = requests.get('https://www.python.org/')
#print res.text
#print res.status_code 
print res.headers['content-type']
print res.headers['Date']

##使用requests.post 台灣高鐵時刻表與票價查詢 台北-台中
import requests
payload = {
'StartStation':'977abb69-413a-4ccf-a109-0272c24fd490',
'EndStation':'3301e395-46b8-47aa-aa37-139e15708779',
'SearchDate':'2014/11/07',
'SearchTime':'15:00',
'SearchWay':'DepartureInMandarin'
}
res = requests.post('http://www.thsrc.com.tw/tw/TimeTable/SearchResult', data=payload)
#print res.text

### 將網頁讀進BeautifulSoup 中
from bs4 import BeautifulSoup 
html_sample = ' \
<html> \
 <body> \
 <h1 id="title">Hello World</h1> \
 <a href="#" class="link">This is link1</a> \
 <a href="# link2" class="link">This is link2</a> \
 </body> \
 </html>'
soup = BeautifulSoup(html_sample)
print soup.text

### 使用findAll 找出含有a tag 的元素
soup = BeautifulSoup(html_sample) 
alink = soup.findAll('a') 
print alink
#print soup.find('a').text
#print soup.find('h1').text

### 使用Find 找出所有id為title的元素
alink = soup.find('h1', {'id':'title'}) 
print alink.text
#print soup.find('h1', {'id':'title'}) 

### 取得含有特定class的元素
soup = BeautifulSoup(html_sample) 
for link in soup.findAll('a', {'class': 'link'}): 
    print link
	#print link.text

### 取得所有a tag 內的連結
alinks = soup.findAll('a', {'href': True}) 
for link in alinks: 
    print link['href']       
	
### 取得所有a tag 內的內容
a = soup.select("a")
a





