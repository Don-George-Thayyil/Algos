class Map:
    def __init__(self):
        self._map = list()

    def __add__(self,key,value):
        index = self._find_index(key)
        if self._map[index] is not None:
            self._map[index].value = value
            return False
        else:
            entry = _mapper(key,value)
            self._map.append(entry)
            return True

    def _find_index(self,key):
        for i in range(len(self._map)):
            if self._map[i].key == key:
                return i

class _mapper:
    def __init__(self,key,value):
        self.key = key
        self.value = value

