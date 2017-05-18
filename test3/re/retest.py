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
    for eachline  in  f:
        res = re.search(r'<([a-z]+)>(.*)</\1>',eachline)
        print res.group(1)+":"+res.group(2)



fh = open("tags.txt")
for i in fh:
      res = re.search(r"<([a-z]+)>(.*)</\1>",i)
      print res.group(1) + ": " + res.group(2)
fh.close()

contactInfo="Doe, John: 555-2222"
result=re.search(r'(\w+), (\w+): (\S+)',contactInfo)
print result.group(1)+" "+result.group(2)+" "+result.group(3)

resultwithname=re.search(r'(?P<first>\w+), (?P<second>\w+): (?P<last>\S+)',contactInfo)
print resultwithname.group('first')
print resultwithname.group('second')
print resultwithname.group('last')