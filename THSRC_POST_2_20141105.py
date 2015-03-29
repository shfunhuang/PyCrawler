##使用requests.post 台灣高鐵時刻表與票價查詢 台北-台中
### 高鐵時刻表查詢
import requests
from bs4 import BeautifulSoup 
from datetime import date,datetime 
url = 'http://www.thsrc.com.tw/tw/TimeTable/SearchResult'
### 台鐵時刻表查詢
#url = 'http://twtraffic.tra.gov.tw/twrail/EasySearch.aspx'
currenttime = datetime.now() 
payload = {
	'StartStation':'977abb69-413a-4ccf-a109-0272c24fd490',
	'EndStation':'3301e395-46b8-47aa-aa37-139e15708779',
	'SearchDate':currenttime.strftime("%Y/%m/%d"),
	'SearchTime':currenttime.strftime("%H:%M"),
	'SearchWay':'DepartureInMandarin'
}
res = requests.post(url, data=payload)
#print res.text.encode('utf-8')
soup = BeautifulSoup(res.text)
print '車次,'+'出發時間,'+'抵達時間,'+'備註'
for table in soup.findAll('table', {'class': 'touch_table'}):
    print table.findAll('td')[0].text + "," + table.findAll('td')[1].text + "," + table.findAll('td')[2].text + "," + table.findAll('td')[3].text
