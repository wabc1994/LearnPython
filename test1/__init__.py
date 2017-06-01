# -*-coding:utf-8-*-
import string
import random
a=string.letters
print a
b=string.digits
print b
#如何讲几个处理函数联系起来
def print_key():
    keylist=[random.choice(a+b) for i in range(10)]
     #将序列转换为字符的形式输出
    return (" ".join(keylist))
def print_keynum(num,result=None):
    if result is None:
        result=[]
    for i in range(num):
        result.append(print_key())
    return  result
def print_1(result):
    a=len(result)
    for i in range(len(result)):
        print result[i]
if __name__ == "__main__":
    print_1(print_keynum(20))


