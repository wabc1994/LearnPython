import pickle,random
from binary_tree import BinaryTree,BinaryNode,BinaryNodeRef

class StuStorage(object):
    def __init__(self):
        self.d=[0]
        self.locked=False
    def lock(self):
        if not self.locked:
            self.locked=True
            return True
        else:
            return False
    def unlock(self):
        pass
    def get_root_address(self):
        return 0
    def write(self,string):
        address=len(self.d)
        self.d.append(string)
        return address
    def read(self,address):
        return self.d[address]
class TestBinaryTree(object):
    def setup(self):
        self.tree=BinaryTree(StuStorage)
    def test_get_missing_key_raise_key_erroe(self):
        with asser_raises(KeyError):
            self.tree.get('not a key in the tree')
    def test_set_and_get_key(self):
        self.tree.set('a','b')

