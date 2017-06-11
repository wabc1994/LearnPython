#!/usr/bin/env python 2.7
# -*-coding:utf-8-*-
# @Author: liuxiongcheng
# @CREATED Time:6/3/17 11:26 AM
# @ software:pycharm

import os
from urllib import urlretrieve
from urllib import urlopen
from bs4 import BeautifulSoup

downloadDirectory = "download"
baseUrl = "http://pythonscrapying.com"


def getAbsoluteURL(baseUrl, source):
    if source.startwith("http://www."):
        url = "http://"+source[11:]
    elif source.startwith("http://"):
        url = source
    elif source.startwith("www."):
        url = "http://"+source[4:]
    else:
        url = baseUrl + "/"+source

    if baseUrl not in url:
        return None
    return url


def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory):
    path = absoluteUrl.replace('www', "")
    path = path.replace(baseUrl, "")
    path = downloadDirectory
    directory = os.path.dirname(path)

    if not os.path.exists(directory):
        os.makedirs(directory)
 # 下载路劲
    return path

html = urlopen("http://www.pythonscraping.com")
bsObj = BeautifulSoup(html)
downloadlist = bsObj.findAll(src=True)

for download in downloadlist:
    fileUrl = getAbsoluteURL(baseUrl, download['src'])
    if fileUrl:
        print(fileUrl)
urlretrieve(fileUrl, getDownloadPath(baseUrl, fileUrl, downloadDirectory))