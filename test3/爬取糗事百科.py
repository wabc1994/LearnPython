#encoding:utf-8
import requests
import re
import urlparse
import lxml.html
import requests
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
def parse_item(url,item):
    rows=[]
    html=requests.get(url)
    soup=BeautifulSoup(html.content)
    frames=soup.find_all('div',attrs={'class':"article block untagged mb15"})
    #frame=tree.xpath('//*[@id="content-left"]/div[@class="article block untagged mb15"]')
    for frame in frames:
        row=[]
        authors=frame.find_all('h2')
        file=open('data.txt','wb')
        for author_name in authors:
             authorname=author_name.string
             print authorname
             file.write("data string%s" % authorname)
             row.append(authorname)
        file.close()
        print dict(zip(item,row))
        #rows.append(row)
    return rows
item=['author']
url='http://www.qiushibaike.com/text/'
data=parse_item(url,item)
print data
