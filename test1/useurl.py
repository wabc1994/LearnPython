import requests
from bs4 import BeautifulSoup
def get_html(url):
    #requests.get
    r=requests.get(url)
    return r.text
def extract_images(text):
    soup=BeautifulSoup(text,"lxml")
    elems=soup.find_all("img",{'class:BDF_Image'})
    return  [elems.get("src") for elem in elems if elem.get('src').find('forum')>-1]
def main(url):
    html=get_html(url)
    img_urls=extract_images(html)
    print('\n'.join(img_urls))
if __name__=='__main__':
    main('http://tieba.baidu.com/p/2166231880')
    html=get_html('http://tieba.baidu.com/p/2166231880')
    imag_urls=extract_images(html)
    print imag_urls