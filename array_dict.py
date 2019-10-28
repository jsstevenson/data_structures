from ds_exceptions import EmptyContainerError, NoSuchKeyError


class ArrayDict:
    def __init__(self):
        self.pairs = []

    def add(self, key, value):
        if key is None:
            raise TypeError('Cannot have key equal to None')
        self.pairs.append([key, value])

    def get(self, key):
        if not self.pairs:
            raise EmptyContainerError('Dictionary is empty')
        else:
            for pair in self.pairs:
                if pair[0] == key:
                    return pair[1]
            raise NoSuchKeyError('Does not contain key')

    def put(self, key, value):
        if not self.pairs:
            self.pairs.append([key, value])
        elif key is None:
            raise TypeError('Key cannot be equal to None')
        else:
            contains_key = False
            for pair in self.pairs:
                if pair[0] == key:
                    pair[1] = value
                    contains_key = True
                    break
            if not contains_key:
                self.pairs.append([key, value])

    def remove(self, key):
        if not self.pairs:
            raise EmptyContainerError('Dictionary is empty')
        else:
            to_delete = None
            for i, pair in enumerate(self.pairs):
                if pair[0] == key:
                    to_delete = i
                    break
            if to_delete is not None:
                del(self.pairs[to_delete])
            else:
                raise NoSuchKeyError('Does not contain key')

    def contains_key(self, key):
        if not self.pairs:
            raise EmptyContainerError('Dictionary is empty')
        else:
            for pair in self.pairs:
                if pair[0] == key:
                    return True
            return False

    def size(self):
        return len(self.pairs)

    def is_empty(self):
        return not self.pairs

    def __str__(self):
        return str(self.pairs)
