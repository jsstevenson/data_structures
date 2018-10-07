class Linked_List:
    
    def __init__(self, front = None):
        self.front = front
    
    def add(self, value):
        if value is None:
            raise TypeError('cannot add value None')
        elif not self.front:
            self.front = Linked_List_Node(value)
        else:
            current = self.front
            while current.nextNode:
                current = current.nextNode
            current.nextNode = Linked_List_Node(value)
    
    def get(self, index):
        if index < 0:
            raise IndexError('index out of range')
        elif self.front is None:
            raise IndexError('index out of range')
        elif index == 0:
            return self.front.data
        else:
            current = self.front
            while index > 0:
                if current.nextNode is None:
                    raise IndexError('index out of range')
                else:
                    current = current.nextNode
                    index -= 1
            return current.data

    def get_index(self, value):
        if value is None:
            raise TypeError('value cannot be None')
        elif self.front is not None:
            index = 0
            if self.front.data == value:
                return index
            current = self.front
            while current.nextNode is not None:
                index += 1
                current = current.nextNode
                if current.data == value:
                    return index
        return -1

    def remove_index(self, index):
        if index < 0:
            raise IndexError('index out of range')
        elif self.front is None:
            raise IndexError('index out of range')
        elif index == 0:
            self.front = self.front.nextNode
        else:
            current = self.front
            while index > 1: # loop until one before index to remove
                try:
                    current = current.nextNode
                    index -= 1
                except AttributeError: # this check may be redundant
                    raise IndexError('index out of range')
            if current.nextNode is None:
                raise IndexError('index out of range')
            else:
                current.nextNode = current.nextNode.nextNode

    def clear(self):
        self.front = None

    def __str__(self):
        string = '['
        if self.front:
            string += str(self.front.data)
            current = self.front
            while current.nextNode:
                string += f', {current.nextNode.data}'
                current = current.nextNode
        string += ']'
        return string

class Linked_List_Node:

    def __init__(self, data = None, nextNode = None):
        self.data = data
        self.nextNode = nextNode
    