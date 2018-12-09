'''
TODO
* Finish out work on table functions, ie actually returning items
* Write unit tests
'''

import hash_table
import double_linked_list.DoubleLinkedList as chain


class ChainedHashTable(hash_table.HashTable):

    def __init__(self, max_load=0.75):
        super().__init__(max_load)
        self.items = [chain() for i in len(self.items)]

    def hash(self, array, item):
        try:
            hash_code = hash(item)
            index = hash_code % array.size
            array[index].add(item)
        except TypeError:
            raise TypeError(f'Cannot hash {item}')

    def resize(self):
        super().resize(chain())
        
