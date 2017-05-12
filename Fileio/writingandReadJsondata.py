#encoding:utf-8
import json
from collections import OrderedDict
#简单将字典编码成json数据格式
data={'name':'ACME','shares':100,'price':542.23}
data_json=json.dumps(data)
#data=json.loads(data_json)
#writing JSON data
with open('data.json','w') as f:
     json.dump(data,f)
#reading data back，json.load(file)用与文件，json.loads（字符床）
with open('data.json','r') as f:
     data=json.load(f)
     print data
s='{"name":"ACME","Shares":50,"price":490.1}'
datajsons=json.loads(s,object_pairs_hook=OrderedDict)
print datajsons
print type(datajsons)
#change a json dictionary into a python object
class JSONObject:
    def __init__(self,d):
        self.__dict__=d

data1=json.loads(s,object_hook=JSONObject)
print data1.name
print(json.dumps(datajsons,indent=4))
#serialize instances,演示如何序列对象
def serialize_instance(obj):
    d={'__classname__':type(obj).__name__}
    d.update(vars(obj))
    return d
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
classes={'Point': Point}

def unserialize_object(d):
    clsname=d.pop('__name__',None)
    if  clsname:
        cls=classes[clsname]
        #create an object of class cls without __init__ method
        obj=cls.__new__(cls)
        for key,value in d.items():
            setattr(obj,key,value)
            return obj
    else:
        return d