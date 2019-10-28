import linked_list
from ds_exceptions import EmptyContainerError


class DoubleLinkedList(linked_list.LinkedList):

    def __init__(self):
        super().__init__(None)
        self.back = None
        self.size = 0

    def add(self, value):
        if value is None:
            raise TypeError('cannot add value None')
        elif not self.front:
            self.front = DoubleLinkedListNode(value)
            self.back = self.front
        else:
            self.back.next = DoubleLinkedListNode(value, self.back, None)
            self.back = self.back.next
        self.size += 1

    def pop(self):
        if not self.front:
            raise EmptyContainerError('List is empty')
        elif self.size == 1:
            result = self.front
            self.front = None
            self.back = None
            self.size = 0
        else:
            result = self.back
            self.back = self.back.prev
            self.back.next = None
            self.size -= 1
        return result

    def go_to(self, index):
        if index < 0 or index >= self.size:
            raise IndexError(f'Index {index} out of range')
        elif self.front is None:
            raise IndexError('Index is out of range')
        if index <= self.size / 2:
            current = self.front
            current_index = 0
            while current_index < index:
                current = current.next
                current_index += 1
        else:
            current = self.back
            current_index = self.size - 1
            while current_index > index:
                current = current.prev
                current_index -= 1
        return current

    def get(self, index):
        return self.go_to(index).data

    def get_index(self, value):
        if self.size < 1:
            return -1
        else:
            current = self.front
            current_ind = 0
            while current:
                if current.data == value:
                    return current_ind
                current = current.next
                current_ind += 1
            return -1

    def set_index(self, index, value):
        if (index < 0) or (index >= self.size):
            raise IndexError('Index out of range')
        else:
            self.go_to(index).data = value

    def insert(self, value, index):
        previous_tenant = self.go_to(index)
        new_node = DoubleLinkedListNode(value, previous_tenant.prev,
                                        previous_tenant)
        previous_tenant.prev.next = new_node
        previous_tenant.prev = new_node
        self.size += 1

    def remove_index(self, index):
        if index == 0:
            if self.size == 0:
                raise EmptyContainerError('List is already empty')
            elif self.size == 1:
                to_remove = self.front
                self.front = None
                self.back = None
            else:
                to_remove = self.front
                self.front = self.front.next
                self.front.prev = None
        elif index + 1 == self.size:
            to_remove = self.back
            self.back = self.back.prev
            self.back.next = None
        else:
            to_remove = self.go_to(index)
            to_remove.prev.next = to_remove.next
            to_remove.next.prev = to_remove.prev
        self.size -= 1
        return to_remove

    def clear(self):
        self.front = None
        self.back = None
        self.size = 0

    def contains(self, data):
        if not self.front:
            return False
        else:
            current = self.front
            while current:
                if current.data is data:
                    return True
            return False

    def __iter__(self):
        return self

    def __next__(self):
        if self.front:
            current = self.front
            while current:
                yield current
                current = current.next


class DoubleLinkedListNode(linked_list.LinkedListNode):

    def __init__(self, data=None, prev_node=None, next_node=None):
        self.data = data
        self.prev = prev_node
        self.next = next_node
