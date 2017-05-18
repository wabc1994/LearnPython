#encoding:utf-8
"""
通用的操作放在此模块中
"""
from zhihu.auth import need_login
from zhihu.error import ZhihuError
from zhihu.models import  Model
from zhihu.url import URL
class Common(Model):
    @need_login
    def send_message(self,content,user_id=None,profile_url=None,user_slug=None,**kwargs):

        if  not any([user_id,profile_url,user_slug]):
            raise  ZhihuError('至少指定一个关键参数')

        if  user_id is None:
            user_slug=self._user_slug(
                profile_url) if user_slug is None else user_slug
        data={"type":"common","content":content,"receiver_hash":user_id}
        response=self._session.post(URL.message(),json=data,**kwargs)

        if response.ok:
            return response.json()
            self.log("发送成功")
        else:
            self.log("发送失败")
            raise ZhihuError("操作失败：%s" % response.text)

    @need_login
    def follow(self,user_slug=None,profile_url=None,**kwargs):
        if not any([user_slug,profile_url]):
            raise ZhihuError("至少指定一个关键字参数")
        user_slug=self._user_slug(profile_url) if user_slug is None else user_slug
        respones=self._session.post(URL.follow_people(),**kwargs)
        if respones.ok:
            return respones.json()

            self.log("关注成功")
        else:

            self.log("发送失败")
            raise ZhihuError("操作失败：%s"% respones.text)

    @need_login
    def unfollow(self,user_slug=None,profile_url=None,**kwargs):
        if not any([user_slug,profile_url]):
            raise ZhihuError("至少指定一个关键字参数")
        user_slug=self._user_slug(profile_url) if user_slug is None else user_slug
        response=self._session.delete(URL.follow_people(user_slug),**kwargs)
        if response.ok:
            return response.json()
            print "成功取消关注"
        else:
            raise ZhihuError('操作失败%s'%response.text)