import linked_list


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

    def insert(self, value, index):
        previous_tenant = self.go_to(index)
        new_node = DoubleLinkedListNode(value, previous_tenant.prev,
                                        previous_tenant)
        previous_tenant.prev.next = new_node
        previous_tenant.prev = new_node
        self.size += 1

    def get(self, index):
        return self.go_to(index).data

    def remove(self, index):
        to_remove = self.go_to(index)
        to_remove.prev.next = to_remove.next
        to_remove.next.prev = to_remove.prev
        self.size -= 1

    def clear(self):
        self.front = None
        self.back = None
        self.size = 0


class DoubleLinkedListNode(linked_list.LinkedListNode):

    def __init__(self, data=None, prev_node=None, next_node=None):
        self.data = data
        self.prev = prev_node
        self.next = next_node
