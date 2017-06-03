#!/usr/bin/env python 2.7
# -*-coding:utf-8-*-
# @Author: liuxiongcheng
# @CREATED Time:6/3/17 11:26 AM
# @ software:pycharm

PROXIES = {'http': 'dfjsaf', 'ftp': 'stackoverflow1.om', 'htutppp': 'asdfjafa', 'https': 'http://stackoverflow2.com'}


def get_proxiex(proxies):
    filtered_proxies = {}
    for key, value in proxies.items():
        if key.startswith('http'):
            if not value.startswith('http'):
                filtered_proxies[key] = 'http://%s' % value
            else:
                filtered_proxies[key] = value
    return filtered_proxies

print get_proxiex(PROXIES)

