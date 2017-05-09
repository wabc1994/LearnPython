#演示了如何将requests和Beautifulsoup结合起来处理数据
import requests
from bs4 import  BeautifulSoup
result=requests.get("http://oreilly.com/store/samplers.html")
print result.status_code
print result.headers
#requests 请求得到的一个对象，对象的content是html文件，Beautifulsoup 对这个html 文件操作得到一个Beautifulsoup
#对象
c=result.content
soup=BeautifulSoup(c)
samples=soup.find_all('a','item-titel')
samples[0]#输出如下
# <a class="item-title" href="http://cdn.oreilly.com/oreilly/booksamplers/9780596004927_sampler.pdf">
#Programming Perl
#</a>
data={}
for a in samples:
    title=a.string.strip()
    data[title]=a.attrs['href']
#接下来进行