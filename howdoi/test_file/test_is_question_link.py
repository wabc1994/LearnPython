#!/usr/bin/env python 2.7
# -*-coding:utf-8-*-
# @Author: liuxiongcheng
# @CREATED Time:6/3/17 11:26 AM
# @ software:pycharm

import re


def _is_question(link):
    return re.search('question/\d+', link)


def _get_questions(links):
    return [link for link in links if _is_question(link)]

links_test = ['http://question/134', 'question/ajfla', 'quafjald', 'question/134']
link_test_one = 'question/89990'


if _is_question(link_test_one) is not None:
    print "successful check"

print _get_questions(links_test)

