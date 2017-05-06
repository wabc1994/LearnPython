#如何将一个json文件中的数据取出来，进行操作
import json
from pprint import pprint
with open('data.json') as data_file:
    data=json.load(data_file)
print(data)
print data['map'][1]['id']