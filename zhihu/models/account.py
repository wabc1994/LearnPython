
# encoding: utf-8
import logging
import re

from zhihu.models import Model
from zhihu.models import RequestDataType
from zhihu.url import URL

class Account(Model):
    def login(self, account, password, **kwargs):
        """
        账户登录
        :param account: email或者手机号码
        :param password:
        :param kwargs:
        :return:
        """
        email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        phone_regex = r"(^1\d{10}$)"
        email_pattern = re.compile(email_regex)
        phone_pattern = re.compile(phone_regex)
        if email_pattern.match(account):
            return self.login_with_email(account,password,**kwargs)
        elif phone_pattern.match(account):
            return self.login_with_phone(account,password,**kwargs)
        else:
            self.log("登录名错误，需要重新输入.",level=logging.ERROR)
            return False
    def login_with_phone(self,phone,password,**kwargs):
        data={
            '_xsrf':self._get_xsrf(),
            'password':password,
            'phone_num':phone,
            'return':True,
            'captcha':self._get_captcha(),
             }
        return self._login_execute(url=URL.phone_login(),data=data,**kwargs)
    def login_with_email(self,email,password,**kwargs):
        data={
            '_xsrf':self._get_xsrf(**kwargs),
            'password':password,
            'email':email,
            'return':True,
            'captcha':self._get_captcha(**kwargs),
             }
        return self._login_execute(url=URL.email_login(),data=data,**kwargs)
    def _login_execute(self,url=None,data=None,**kwargs):
        r = super(Account, self)._execute(method="post", url=url, data=data, data_type=RequestDataType.FORM_DATA,
                                          **kwargs)
        if r.ok:
            result=r.json()
            if result.get('r')==0:
                self.log(result.get("msg"))
                self._session.cookies.save(ignore_discard=True)
                return True
            else:
                self.log(result.get("msg"),level=logging.ERROR)
                return False
        else:
            self.log("登录失败",level=logging.ERROR)
            self.log(r.text)
            return False

