#encoding:utf-8
import re
class ZhihuError(Exception):
    def __init__(self,*args,**kwargs):
        Exception(self,*args,**kwargs)
def log(email,phone):
    email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    phone_regex = r"(^1\d{10}$)"
    email_pattern = re.compile(email_regex)
    phone_pattern = re.compile(phone_regex)
    if email_pattern.match(email):
        print 'emial'
    elif phone_pattern.match(phone):
        print 'phone'
log('liuxiongchenggmail.com','13456789101')

def _user_slug(profile_url):
    pattern = re.compile("https?://www.zhihu.com/people/([\w-]+)")
    match=pattern.search(profile_url)
    match1=pattern.match(profile_url)
    if  match:
        user_slug =match.group(1)
        return user_slug
    else:
        raise ZhihuError("invalid profile url")
print _user_slug('https://www.zhihu.com/people/sjk')
