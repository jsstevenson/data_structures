'''
TODO
* Fill out more methods (get?)
'''


class HashTable(object):
    def __init__(self, max_load=0.75):
        self.items = [None for i in range(16)]
        self.load_balance_max = max_load
        self.size = 0

    def hash(self, array, item):
        raise Exception('hash function not implemented')

    def resize(self, elem=None):
        new_items = [elem for i in range(self.items * 2)]
        for item in self.items:
            if item:
                hash(new_items, item)

    def add(self, item):
        if self.size / len(self.items) > self.load_balance_max:
            self.resize()
        hash(self.items, item)
        self.size += 1
