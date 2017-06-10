#!/usr/bin/env python 2.7
# -*-coding:utf-8-*-
# @Author: liuxiongcheng
# @CREATED Time:6/3/17 11:26 AM
# @ software:pycharm

from mongoengine import *
# 如何没有用户的话，直接添加数据就可以了
connect('my_database')


class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)


class Comment(EmbeddedDocument):
    content = StringField()
    name = StringField(max_length=120)


class Post(Document):
    title = StringField(max_length=120, required=True)
    author = ReferenceField(User, reverse_delete_rule=CASCADE)
    tags = ListField(StringField(max_length=30))
    comments = ListField(EmbeddedDocumentField(Comment))

    meta = {'allow_inheritance': True}


class TextPost(Post):
    content = StringField()


class ImagePost(Post):
    content = StringField()


class LinkPost(Post):
    link_url = StringField()



ross = User(email='liuxiongcheng@gmail.com', first_name='ross', last_name='xiongcheng').save()
john = User(email='adfjla@gmial.com', first_name='john', last_name='adjfajd').save()
# ross=User(email = 'liu')
# ross.first_name = 'ross'
# ross.last_name = 'xiongcheng'
# ross.save()

post1 = TextPost(title='Fun with MongoEngine', author=john)
post1.content = 'Took a look at MongoEngine today, looks pretty cool.'
post1.tags = ['mongodb', 'mongoengine']
post1.save()

post2 = LinkPost(title='MongoEngine Documentation', author=ross)
post2.link_url = 'http://docs.mongoengine.com/'
post2.tags = ['mongoengine']
post2.save()

