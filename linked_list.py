class LinkedList:

    def __init__(self, front=None):
        self.front = front

    def add(self, value):
        if value is None:
            raise TypeError('cannot add value None')
        elif not self.front:
            self.front = LinkedListNode(value)
        else:
            current = self.front
            while current.next:
                current = current.next
            current.next = LinkedListNode(value)

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
                if current.next is None:
                    raise IndexError('index out of range')
                else:
                    current = current.next
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
            while current.next is not None:
                index += 1
                current = current.next
                if current.data == value:
                    return index
        return -1

    def remove_index(self, index):
        if index < 0:
            raise IndexError('index out of range')
        elif self.front is None:
            raise IndexError('index out of range')
        elif index == 0:
            self.front = self.front.next
        else:
            current = self.front
            while index > 1:  # loop until one before index to remove
                try:
                    current = current.next
                    index -= 1
                except AttributeError:  # this check may be redundant
                    raise IndexError('index out of range')
            if current.next is None:
                raise IndexError('index out of range')
            else:
                current.next = current.next.next

    def clear(self):
        self.front = None

    def __str__(self):
        string = '['
        if self.front:
            string += str(self.front.data)
            current = self.front
            while current.next:
                string += f', {current.next.data}'
                current = current.next
        string += ']'
        return string


class LinkedListNode:

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node
