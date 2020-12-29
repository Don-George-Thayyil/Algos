#make a linked list

class Bag:
    def __init__(self):
        self._head = None
        self.size = 0
    def __len__(self):
        return self.size
    def __contains__(self,target):
        current_node = self._head
        while current_node != None and current_node != target:
            current_node = current_node.next
        return True
    def add(self,item):
        new_node = LinkedItem(item)
        new_node.next = self._head
        self._head = new_node
        self.size += 1
    def remove(self,target):
        prenode = None
        current_node = self._head
        while current_node != None and current_node.data != target:
            prenode = current_node
            current_node = current_node.next
        assert current_node != None, "Item is not in the bag"
        self.size -= 1
        if current_node is self._head:
            self._head = current_node.next
        else:
            prenode.next = current_node.next
        
    def __iter__(self):
        return BagIterator(self._head)
    
class BagIterator:
    def __init__(self,head):
        self.node = head
    def __iter__(self):
        return self
    def __next__(self):
        if self.node != None:
            item = self.node.data
            self.node = self.node.next
            return item
        else:
            raise StopIteration
class LinkedItem(object):
    def __init__(self,item):
        self.data = item
        self.next = None

#testing the code

bag = Bag()
bag.add(23)
bag.add(30)
bag.add(221)
print("printing out every items, iterating through bag")
for i in bag:
    print(i)
print("----------")
print("value 30 is removed:")
bag.remove(30)

for i in bag:
    print(i)
print("----------")
print("Checking if bag contains 221:")
print(bag.__contains__(221))
print("---------")
print("Checking the size of the bag:")

print(bag.__len__())
