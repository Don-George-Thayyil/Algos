import ctypes

class TheArray:
    
    def __init__(self,size):
        assert size > 0, "Array size must be greater than zero"
        self._size = size
        self._array_ = (ctypes.py_object * size)()
        self.clear(None)
        self._curindex = 0
   
    def __len__(self):
       return self._size
   
    def __getitem__(self,index):
        assert index>=0 and index < len(self), "Array subscript out of range"
        return self._array_[index]
   
    def __setitem__(self,index,value):
        assert index>=0 and index < len(self), "Array subscript out of range"
        self._array_[index] = value

    def clear(self,value = "Don"):
        for i in range(len(self)):
            self._array_[i] = value

#    def __iter__(self):
#        return self
#    
#    def __next__(self):
#        if self._curindex > len(self.array):
#            raise StopIteration
#        value = self.array[self._curindex]
#        self._curindex += 1
#        return value
#

class _ArrayIterator:
    
    def __init__(self,array):
        self._array = array
        self._curindex = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._curindex < len(self._array):
            element = self._array[self._curindex]
            self._curindex +=1
            return element
        else:
            raise stopIteration


arr = TheArray(10)
arr.clear(120)
for i in range(10):
    print(arr[i])
