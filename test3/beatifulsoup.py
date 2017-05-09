#-*- coding:utf-8 -*-
"""
https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html
 
"""
#some code help you how to use beatifulsoup to parse htmml
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
from bs4 import BeautifulSoup
soup=BeautifulSoup(html_doc)     #获取一个beatuifulsoup对象

#几个简单的浏览结构化的数据方法
print soup.prettify()
#从文档中找到所有<a>标签的链接
print soup.find_all('a')
soup.find(id="link1")
for link in soup.find_all('a'):
    print(link.get('href'))
#从文档中获取所有文字内容
print(soup.get_text())
#将一段文档穿输入Beautifulsoup
soup=BeautifulSoup(open('html_doc.html'))
soup=BeautifulSoup("<html>data</html>")
print soup.get_text()
soup=BeautifulSoup('<b class="boldest">Extremely bold</b>',"lxml")
#Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象,所有对象可以归纳为4种:
# Tag , NavigableString ,
# BeautifulSoup , Comment .

