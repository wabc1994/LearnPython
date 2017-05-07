#defines a class(DBDB)whic implements the Python dictionary API using the concrete BinaryTree implemention.This is how you would use DBDB inside a Python
from physical import storage
from binary_tree import BinaryTree
class DBDB(object):
    def __init__(self,f):
        self._storage=storage(f)
        self._tree=BinaryTree(self._storage)
    def close(self):
        self._storage.close()
    def __getitem__(self,key):
        self._assert_not_closed()
        return self._tree.get(key)
    def __setitem__(self,key,value):
        self._assert_not_closed()
        return self._tree.set(key,value)
    def __contains__(self, key):
        try:
            self[key]
        except KeyError:
            return False
        else:
            return True
    def __delitem__(self, key):
        self._assert_not_closed()
        return self._tree.pop(key)
    def commit(self):
        self._assert_not_closed()
        self._tree.commit()
    def _assert_not_closed(self):
        if self._storage.closed:
            raise ValueError('Database closed.')

    def __len__(self):
        return len(self._tree)