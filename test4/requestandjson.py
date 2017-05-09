import requests
from bs4 import BeautifulSoup
import json
r = requests.get('https://api.github.com/events')
r.json()
print r.json()
type(r.json())
r1=requests.get("https://www.vevo.com/watch/harry-styles/Sign-of-the-Times/USSM21700469")
soup=BeautifulSoup(r1.content)
print(soup.prettify())









