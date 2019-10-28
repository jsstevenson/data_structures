import hash_table
from double_linked_list import DoubleLinkedList
from ds_exceptions import NoSuchKeyError


class ChainedHashTable(hash_table.HashTable):

    def __init__(self, max_load=0.75):
        super().__init__(max_load)
        self.chains = [DoubleLinkedList() for i in self.chains]

    '''
    Re-hash 
    '''
    def rehash(self, chains, item_list):
        try:
            hash_code = hash(item_list)
            index = hash_code % chains.size
            chains[index].add(item_list)
        except TypeError:
            raise TypeError(f'Cannot hash {item_list}')k

    def resize(self):
        super().resize(DoubleLinkedList())

    def get(self, key):
        index = hash(key) % self.size()
        if (self.chains[index] is None or
                not self.chains[index].contains_key(key)):
            raise NoSuchKeyError(f'Does not contain {key}')
        else:
            self.chains[index].get(key)

    def contains_key(self, key):
        pass

    def get_or_default(self, key, default):
        if self.contains_key(key):
            return self.get(key)
        else:
            return default

    def put(self, item):
        if self.size / len(self.chains) > self.load_balance_max:
            self.resize()
        self.rehash(self.chains, item)
        self.size += 1

    def remove(self, key):
        pass

    def size(self):
        return self.size

    def is_empty(self):
        pass
        
