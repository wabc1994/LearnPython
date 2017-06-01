#encode:utf-8
from lxml import html
html=html.fromstring('text.xml')
title=html.xpath('//bookstore/book[1]/title')
print title
