# -*-coding:utf-8-*-
class Map(object):
    def __init__(self,attrs):
        self.attrs=attrs
        self.next_maps={}
    def get_index(self,filename):
        return self.attrs.get(filename,-1)
    def next_map(self,filename):
        assert filename not in self.attrs
        if filename in self.next_maps:
            return self.next_map[filename]
        attrs=self.attrs.copy()
        attrs[filename]=len(attrs)
        result=self.next_maps[filename]=Map(attrs)
        return result
EMPTY_MAP=Map({})
EMPTY_MAP.next_map('A')
EMPTY_MAP.next_map('b')
print EMPTY_MAP.next_maps
print EMPTY_MAP.get_index('A')
print EMPTY_MAP.get_index('b')
def test_callmethod_simple():
    class A(object):
        def f(self):
            return self.x+1
    obj=A()
    obj.x=1
    assert obj.f()==2
    class B(A):
        pass
    obj=B()
    obj.x=1
    assert obj.f()==2  #work for subclass too
    def f_A(self):
        return self.read_attr()
def test_read_write_field():
    # Python code
    class A(object):
        pass
    obj = A()
    obj.a = 1
    assert obj.a == 1

    obj.b = 5
    assert obj.a == 1
    assert obj.b == 5

    obj.a = 2
    assert obj.a == 2
    assert obj.b == 5
A=Class(name='A',base_class=OBJECT,fields={},metaclass=Type)
class Base(object):
    def __init__(self,cls,fields):
        self.cls=cls
        self._fields=fields
    def rea_attr(self,fieldname):
        return self._read_dict(fieldname)
    def _read_dict(self,fieldname):
        return  self._fields[fieldname]
    def  write_attr(self,fieldname,value):
        self._write._dict(fieldname,value)
    def _write._dict(self,fieldname,value)
        self._field[fieldname]=value
class Instance(Base):
    def__init__(self,cls):
        assert isinstance(cls,class)

