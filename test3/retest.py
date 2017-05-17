#encoding:utf-8
import re
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