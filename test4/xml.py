#-*-coding:utf-8-*-
import requests
from lxml import html
from bs4 import BeautifulSoup
page=requests.get("http://www.dbmeinv.com/")
tree=html.fromstring(page.text)
intro_raw=tree.xpath('//a[@href="http://www.dbmeinv.com/dbgroup/1269717"]/text()')
print intro_raw
for i in intro_raw:
      intro=i.encode('utf-8')
      print intro
SOUP=BeautifulSoup(page.content)
a=SOUP.find_all('a',attrs={'class':"link"})
print type(a)
for a1 in a:
      print a1.string