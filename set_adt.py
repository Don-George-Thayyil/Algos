class SetADT:
    def __init__(self):
        self._set = list()

    def __length__(self):
        return len(self._set)

    def __contain__(self,value):
        return value in self._set
    
    def add(self,element):
        if element not in self._set:
            self._set.append(element)
        else:
            raise "Element is a duplicate"
    
    def remove(self,element):
        if element in self._set:
            self._set.remove(element)
        else:
            raise "Didn't find the element"

    def __eq__(self, setB):
        if len(self._set) != len(setB):
            return False
        else:
            return check(self,setB)
    
    def check(self,setB):
        for element in self._set:
            if element in setB:
                return True
            else:
                return False

