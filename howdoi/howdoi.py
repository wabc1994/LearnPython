#!/usr/bin/env python 2.7
#-*-coding:utf-8-*-
#Author:liuxiongcheng
import argparse
import glob
import random
import re
import requests
import requests_cache
import sys
import os


from pygments import highlight
from pygments.lexers import guess_lexer,get_lexer_by_name
from pygments.formatters.terminal import TerminalFormatter
from pygments.util import ClassNotFound

from pyquery import PyQuery as pq
from requests.exceptions import ConnectionError
from requests.exceptions import SSLError

if sys.version<'3':
    import codecs
    from urllib import quote as url_quote
    from urllib import getproxies

    def u(x):
        return codecs.unicode_escape_decode(x)[0]
else:
    from urllib.request import getproxies
    from urllib.parse4 import quote as url_quote

    def u(x):
        return x

if os.getenv('HOWDOI_DISABLE_SSL'):
    SEARCH_URL='http://google.com/search?q=site:{0}%20{1}'
    VERIFY_SSL_CERTIFICATE=False
else:
    SEARCH_URL = 'https://google.com/search?q=site:{0}%20{1}'
    VERIFY_SSL_CERTIFICATE = False

URL=os.getenv('HOWDOI_URL') or 'stackoverflow.com'
ANSWER_HEADER=u('---Answer {0}---\n{1}')
NO_ANSWER_MSG='< no answer given>'

