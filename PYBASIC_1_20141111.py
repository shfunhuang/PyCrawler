# 20141111-2.py
# Regular Expression (正規表達式)
import re 
m = re.match(r"(\w+)@(\w+)", "david@numerinfo.com") 
print m.groups()
 
m = re.match(r"(\w+)@([a-z.]+)", "david@numerinfo.com") 
print m.groups() 

m = re.match(r"(\d+)\.(\d+)", "1999.5") 
print m.groups() 

m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "David Chiu") 
print m.group('first_name'), m.group('last_name')
 
str1 = 'scp file.txt root@10.0.0.1:./' 
m=re.search('^scp ([\w\.]+) (\w+)@([\w\.]+):(.+)',str1) 
if m: 
    print m.group(1), m.group(2), m.group(3), m.group(4)
	
# declare dictionary 
dic = {'a':100, 'b':"yes", 'c':0.98} 
print dic 

# get keys in dictionary 
print dic.keys() 

# get values in dictionary 
print dic.values()

# get value of given key 
print dic['a'] 

# get value of given key 
print dic.get('a')

# update entry into dictionary 
dic['d'] = 'new' 
print dic 

# update entry into dictionary 
dic.update({'e':123}) 
print dic

# iter the dictionary 
for rec in dic: 
    print rec, dic[rec]
	
print dic.keys()

del dic['d']

print dic

# 使用repr 找出formatting
a = r'\t\t string \n\t' 
print a 
print repr(a)

dic = {"標的分類":""}
for rec in dic: 
    print repr(rec), repr(dic[rec])
    print rec, dic[rec]
	
for rec in dic: 
    print repr(rec), repr(dic[rec])
	
# 將資料依分隔符號切成陣列
a = '123,555,111,99' 
print a.split(',') 
print a.split(',', 1) 

c = "What is real? How do you define real?"
print(c)
print(c.split(" ", 2))

# 將陣列單元依分隔符號合成字串
a = '123,555,111,99' 
ary = a.split(',') 
#print ary
print '|'.join(ary)

# 如何移除字串中內含的 換行符號及空白
dic = {"標的分類":""}
for rec in dic: 
    #print rec
    print ''.join(dic[rec].split())
	
# 如何替換跳脫字元 by HTMLParser
import HTMLParser 
h = HTMLParser.HTMLParser() 
a = '&lt;qoo&gt; 123,555,111,99' 
print h.unescape(a)

# 如何替換跳脫字元 by replace
a = '&lt;qoo&gt; 123,555,111,99' 
print a.replace('&lt;', '<').replace('&gt;', '>')

# 時間跟字串轉換
from datetime import date,datetime 
# Times -> String
currenttime = datetime.now() 
#print currenttime
print currenttime.strftime("%Y-%m-%d %H:%M:%S") 

# String -> Times
a = '2014-05-03 14:00:00' 
print datetime.strptime(a, "%Y-%m-%d %H:%M:%S")

# 取得年分
response_date = '102/12/10 10:30' 
getyear = response_date.split('/', 1) 
print "year:" + getyear[0]

# 轉換成西元年
bctime= str(int(getyear[0]) + 1911) + "/" + ''.join(getyear[1:]) 
print bctime

# 轉換成時間格式
response_date = '102/12/10 10:30' 
getyear = response_date.split('/', 1) 
bctime= str(int(getyear[0]) + 1911) + "/" + ''.join(getyear[1:]) 
print bctime
print datetime.strptime(bctime, "%Y/%m/%d %H:%M")

# 使用資料宣告
tenderer_dic = {"廠商代碼":"tenderer_code", 
                "廠商名稱":"tenderer_name", 
                "是否得標":"awarded", 
                "組織型態":"orgnization_type"} 
result_dic = {} 

# 找到award_table_tr_3
tender_table = soup.find('table', { "class" : "table_block tender_table" }) 
award_table_tr_3 = tender_table.findAll( 'tr',{'class':'award_table_tr_3'})
#print award_table_tr_3

# 取得廠商編號
import re 
m = re.match(r'投標廠商(\d+)' ,'投標廠商101') 
print m.group(1)

# Strip 範例
# Remove Space
s = " \t string test \t \n\n\r" ' \t string test \t \n\n\r' 
print s

print s.strip()

print s.rstrip()

print s.lstrip()

# 處理金額問題
import re 
m = re.match( r"\$?-?([0-9,]+)", '352,111元') 
print m.group().split(',')
print 'yaya'.join(m.group(1).split(','))

str1 = '$123,456,789'
m = re.match('\$([0-9,]+)', str1)
print m.group()
print m.group(1).split(',')
print ''.join(m.group(1).split(','))





