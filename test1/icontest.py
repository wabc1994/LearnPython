# -*- coding:utf-8 -*-
# 第 0000 题：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果

import random,string
def rand_str(num,length=7):
    f=open('text.txt','wb')
    for i in range(num):
        chars=string.letters+string.digits
        s=[random.choice(chars) for i in range(length)]
        f.write(''.join(s)+'\n')
    f.close()
if __name__=='__main__':
    rand_str(200)