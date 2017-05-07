# -*-coding:utf-8-*-
"""
解c语言的人，一定会知道struct结构体在c语言中的作用，它定义了一种结构，
里面包含不同类型的数据(int,char,bool等等)，方便对某一结构对象进行处理。而在网络通信当中，
大多传递的数据是以二进制流（binary data）存在的。当传递字符串时，不必担心太多的问题，
而当传递诸如int、char之类的基本数据的时候，就需要有一种机制将某些特定的结构体类型打包成二进制流的字符串然后再网络传输，
而接收端也应该可以通过某种机制进行解包还原出原始的结构体数据。python中的struct模块就提供了这样的机制，
"""
import struct
values=(1,'abc',2.7)
s='I3sf'
packed_data=struct.pack(s,*values)
#unpacked_data=s.unpack(packed_data)
print 'original values',packed_data
#print 'Formating string' ,s.format
