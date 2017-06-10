#!/usr/bin/env python 2.7
# -*-coding:utf-8-*-
# @Author: liuxiongcheng
# @CREATED Time:6/3/17 11:26 AM
# @ software:pycharm
from mongoengine import *


class Student(DynamicDocument):
    meta = {
        'collection': 'student',
        'strict': False
    }
    stu_id = IntField()
    age = IntField()
    name = StringField()
    gender = StringField()


def insert_data():
    """ 插入数据 """
    # 一种方法
    peter = Student()
    peter.stu_id = 101
    peter.name = 'Peter'
    peter.gender = 'male'
    peter.save()

    # 另一种方法
    john = Student(stu_id=102, name="John Smith", gender='male').save()


def update_data():
    """ 更新数据 """
    # 年龄,注意用双下划线
    Student.objects(stu_id=101).update_one(set__age=23)
    Student.objects(stu_id=102).update_one(set__age=26)

    # 新增联系方式
    peter_contact = dict(phone='13238985676', email='peter@example.com')
    john_contact = dict(phone='18034567890', email='john@example.com')

    # peter
    Student.objects(stu_id=101).update_one(set__contact=peter_contact, upsert=True)
    # john
    Student.objects(stu_id=102).update_one(set__contact=john_contact, upsert=True)


def search_data():
    result_all = Student.objects().all()
    print "count of all records is : ", result_all.count()

    # 查找 stu_id 为 101 的学生
    result_1 = Student.objects(stu_id=101).first()
    print "result_1.name is : ", result_1.name
    print "result_1.gender is : ", result_1.gender
    # 查找性别为男, 手机号为 18034567890, 注意用双下划线
    result_2 = Student.objects(gender='male', contact__phone='18034567890').first()
    print "result_2.name is : ", result_2.name

    # 查找年龄大于 25, 注意用双下划线
    result_3 = Student.objects(age__gt=25).all()
    for element in result_3:
        print element.name


def delete_data():
    Student.objects(stu_id=101).update(unset__contact=1)

if __name__ == "__main__":
    connect('student')
    insert_data()
    update_data()
    search_data()
    delete_data()


#如何有连个