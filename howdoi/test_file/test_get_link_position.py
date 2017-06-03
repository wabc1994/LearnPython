#!/usr/bin/env python 2.7
# -*-coding:utf-8-*-
# @Author: liuxiongcheng
# @CREATED Time:6/3/17 11:26 AM
# @ software:pycharm

import unittest


def get_link_at_pos(links, position):
    if not links:
        return False
    # 参数满足题意要求
    if len(links) >= position:
        link = links[position-1]

    else:
        link = links[-1]
    return link

# test code


class test_link(unittest.TestCase):
    def test_get_link_pos(self):
        self.assertEqual(get_link_at_pos(['/question/42/'], 1), '/question/42')
        self.assertEqual(get_link_at_pos(['/question/42/'], 2), 'question/42/')
        self.assertEqual(get_link_at_pos(['howdoi', '/question/42'], 1), 'howdoi')
        self.assertEqual(get_link_at_pos(['howdoi', '/question/2'], 2), '/question/2')
        self.assertEqual(get_link_at_pos(['/questions/42/', '/questions/142/'], 1), '/questions/42/')