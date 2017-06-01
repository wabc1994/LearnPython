# -*- coding:utf-8 -*-
"""
https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html

"""
# some code help you how to use beatifulsoup to parse htmml
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
from bs4 import  BeautifulSoup
from lxml import html
import requests
soup=BeautifulSoup(html_doc)
print soup.select("title")
print soup.select('body a')
print soup.select(".sister")
print soup.select("#link1")
soup.select('a[href="http://example.com/elsie"]')
page=requests.get('http://econpy.pythonanywhere.com/ex/001.html')
tree=html.fromstring(page.content)
buyers=tree.xpath('//div[@title="buyer-name"]/text()')
print buyers