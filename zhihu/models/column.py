# encoding: utf-8

import re

from zhihu.auth import need_login
from zhihu.error import ZhihuError
from zhihu.models import Model
from zhihu.setting import ZHUANLAN_HEADERS
from zhihu.url import URL
class Column(Model):

    def __init__(self,slug=None,url=None):
        slug=slug if slug  is not None else self._extract_slug(url)
        if not slug:
            raise ZhihuError("没有指定专栏的slug或者url")
        self.slug=slug
        super(Column,self).__init__(headers=ZHUANLAN_HEADERS)
        self._session.headers["x-xsrf-token"]=self._get_xsrf()


    @staticmethod
    def _extract_slug(url):

        pattern=re.compile("http://zhuanlan.zhihu.com/(\w+)?.*?")
        match=pattern.search(url)
        return match.group(1) if match else None

    @need_login
    def followers(self,limit=500,offset=0,**kwargs):

        r=self._session.get(URL.column_followers(self.slug),params={"limit":limit,"offset":offset},**kwargs)

        return r.json()

    @need_login
    def follow(self,**kwargs):

        r=self._execute(method='put',url=URL.follow_column(self.slug),**kwargs)

        if r.ok():
            print "关注专栏成功"
        else:
            raise ZhihuError("操作失败%s"% r.text)
    @need_login
    def unfollow(self,**kwargs):

        r=self._execute(method='delete',url=URL.unfollow_column(self.slug),**kwargs)

        if r.ok:
            print "取消关注成功"
        else:
            raise ZhihuError("操作失败%s" % r.text)
