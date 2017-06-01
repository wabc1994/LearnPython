#encoding:utf-8
import requests
from bs4 import BeautifulSoup
from lxml import etree
import requests
download_url="http://coalchem.anychem.com/category/industry"
r=requests.get(download_url)
#from——encoding制定编码方式
soup=BeautifulSoup(r.content,from_encoding='uft-8')
unicode(soup)
soup.encode('utf-8')

a=soup.select('a')
a1=a[0]
a2=a[1]
print a1.get_text()

text_file=open('data.txt','w')
#对获取到的字符串进行编码
text_file.write("string of a1[0]%s" % a1.string.encode('utf-8')+'\n')
#常用的方法str.format()
with open('data.txt','w') as text_file1:
    text_file1.write("purchase amout{0}".format('format 好1111'))
#text_file.write("string of a[1]%" % a2.string.encode('uft-8')+'\n')
text_file.close()
list=[]
for i in range(len(a)):
    list.append(a[i].stripped_strings.encoding('uft-8'))
print list



 

print a1.string
print type(a)
print type(a1)
print a1['href']
print len(a)

