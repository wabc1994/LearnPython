#-*-coding:utf-8-*-
#http://stackoverflow.com/questions/12179271/meaning-of-classmethod-and-staticmethod-for-beginner?noredirect=1&lq=1
#the url above is a wonderful account for classmethod use in python
class Date(object):
    def __init__(self,day=0,month=0,year=0):
        self.day=day
        self.month=month
        self.year=year
    @classmethod
    def from_string(cls,data_as_string):
        day,month,year=map(int,data_as_string.split('-'))
        date1=cls(day,month,year)
        return date1
    @staticmethod
    def is_date_valid(date_as_string):
        day,month,year=map(int ,date_as_string.split('-'))
        return day<=31 and month <=12 and year<=3999
is_date=Date.is_date_valid('11-0-2012')
date2=Date.from_string('11-09-2013')
print date2.day
print date2.month
print date2.year