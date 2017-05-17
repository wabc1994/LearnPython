#encoding:utf-8
#演示如何将python dictionary and turn it into XML
from xml.etree.ElementTree import Element,tostring
def  dict_to_xml(tag,d):
    """
    turn a simple dict of key/value paris into xml
    :param tag: 
    :param d: 
    :return: 
    """
    elem=Element(tag)
    for key,val in d.items():
        #将一个字符串变量装换成为标签节点
        child=Element(key)
        child.text=str(val)
        #节点添加子节点
        elem.append(child)
    return elem
s={'name':'GOOG','shares':100,'price':490.1}
e=dict_to_xml('stock',s)
print e
print tostring(e)
#make xml through string,本质上都是字符串
def dict_to_xml_str(tag,d):
    parts=['<{}>'.format(tag)]
    for key,val in d.items():
        parts.append('<{0}><{1}></{0}>'.format(key,val))
        return ''.join(parts)
d={'name':'spam'}
print dict_to_xml_str('item',d)

