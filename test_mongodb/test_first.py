#!/usr/bin/env python 2.7
# -*-coding:utf-8-*-
# @Author: liuxiongcheng
# @CREATED Time:6/3/17 11:26 AM
# @ software:pycharm

from pymongo import MongoClient
import datetime
from pprint import pprint

client = MongoClient('localhost', 27017)
# getting a Database or db=client[test-database]
db = client.test_database
# getting a  collection
collection = db.test_collection
# getting a document
post = {
    "author": "Mike",
    "text": "my first blog post",
    "tags": ["mongodb", "python", "pymongo"],
    "date": datetime.datetime.utcnow()
}
# insert a document into a db
posts = db.posts
post_id = posts.insert_one(post).inserted_id
print post_id
db.collection_names(include_system_collections=False)
pprint(posts.find_one())
# find_one post_id
pprint(posts.find_one({'_id': post_id}))
# insert many document
new_posts = [{"author": "Mike",
              "text": "Another post!",
              "tags": ["bulk", "insert"],
              "date": datetime.datetime(2009, 11, 12, 11, 14)},
             {"author": "Eliot",
               "title": "MongoDB is fun",
               "text": "and pretty easy too!",
               "date": datetime.datetime(2009, 11, 10, 10, 45)}]
insert_result = posts.insert_many(new_posts)
print insert_result.inserted_ids


