class HashTable(object):
    def __init__(self, max_load=0.75):
        self.chains = [None for i in range(16)]
        self.load_balance_max = max_load
        self.size = 0

    def rehash(self, array, item):
        raise Exception('hash function not implemented')

    def resize(self, elem=None):
        new_chains = [elem for i in range(len(self.chains) * 2)]
        for chain in self.chains:
            if chain:
                for item in chain:
                    self.rehash(new_chains, item) # need to update rehash method appropriately
        self.chains = new_chains

    def get(self, key):
        pass

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
        hash(self.chains, item)
        self.size += 1

    def remove(self, key):
        pass

    def size(self):
        return self.size

    def is_empty(self):
        pass
