#encoding:utf-8
"""
<composer>Wolfgang Amadeus Mozart</composer>
<author>Samuel Beckett</author>
<city>London</city>
reuslt

composer: Wolfgang Amadeus Mozart
author: Samuel Beckett
city: London
"""
import re

with open('tags.txt','r') as f:
    for eachline in f:
        res=re.search(r'<([a-z]+)>(.*)</\1>',eachline)
        print res.group(1)+":"+res.group(2)

import re
fh = open("tags.txt")
for i in fh:
     res = re.search(r"<([a-z]+)>(.*)</\1>",i)
     print res.group(1) + ": " + res.group(2)
fh.close()