#-*-coding:utf-8-*-
#show how to use @property in python
class Thing(object):
    def __init__(self,my_word):
        self._word=my_word
    @property
    def word(self):
        return self._word
print(Thing("with property").word) #使用了property word相当一个类的一个field而不是属性
class Thing2:
    def __init__(self, my_word):
        self._word = my_word
    def word(self):
        return self._word
print(Thing2('without property').word())
