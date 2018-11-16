'''
Current state:
Tried to make nodes comparable in a few ways. Seem to have broken everything.
'''


class BinarySearchTree:

    def __init__(self, overall_root=None):
        self.overall_root = overall_root

    def add_find(self, root, item):
        if root.left_child is None and item < root:
            root.left_child = BSTNode(item)
        elif root.right_child is None and item > root:
            root.right_child = BSTNode(item)
        elif item < root:
            self.add_find(root.left_child, item)
        else:
            self.add_find(root.right_child, item)

    def add(self, item):
        if item is None:
            raise TypeError('cannot accept type None')
        if self.overall_root is None:
            self.overall_root = BSTNode(item)
        else:
            item = BSTNode(item)
            try:
                item > self.overall_root
            except TypeError:
                raise TypeError('cannot accept item of this type')
            self.add_find(self.overall_root, item)

    def height(self, root):
        if root is None:
            return 0
        else:
            result = []
            result.append(self.height(root.left_child))
            result.append(self.height(root.right_child))
            return 1 + max(result)

    def get_height(self):
        if self.overall_root is None:
            return 0
        else:
            return self.height(self.overall_root)

    def inorder(self, root):
        if root is None:
            return ''
        else:
            result = ''
            result += self.inorder(root.left_child)
            result += str(root.data) + ', '
            result += self.inorder(root.right_child)
            return result

    def print_inorder(self):
        if self.overall_root is None:
            print('[]')
        else:
            result = '['
            result += self.inorder(self.overall_root)
            result = result[:-2] + ']'
            return result

    def __repr__(self):
        return self.print_inorder()

    def contains_find(self, root, data):
        if root is None:
            return False
        elif root.data == data:
            return True
        else:
            left = self.contains_find(root.left_child, data)
            right = self.contains_find(root.right_child, data)
            return left or right

    def contains(self, data):
        if self.overall_root is None:
            return False
        else:
            return self.contains_find(self.overall_root, data)

    def get_find(self, root, data):
        if root is None:
            raise KeyError('Not contained in tree')
        elif data == root.data:
            return root
        elif data < root.data:
            return self.get_find(root.left_child, data)
        else:
            return self.get_find(root.right_child, data)

    def get(self, data):
        if self.overall_root is None:
            raise KeyError('Not contained in tree')
        else:
            return self.get_find(self.overall_root, data)


class BSTNode:

    def __init__(self, data, left=None, right=None):
        if data is None:
            raise TypeError('Cannot create Node instance of data None')
        self.data = DictPair(data)
        self.left_child = None
        self.right_child = None

    def __eq__(self, other):
        try:
            return self.data.key == other.data.key
        except TypeError:
            raise TypeError('Cannot compare BSTNode to other data')
        except AttributeError:
            raise TypeError('Cannot compare BSTNode to other object')

    def __lt__(self, other):
        try:
            return self.data.key < other.data.key
        except TypeError:
            raise TypeError('Cannot compare BSTNode to other data')
        except AttributeError:
            raise TypeError('Cannot compare BSTNode to other object')

    def __gt__(self, other):
        try:
            return self.data.key > other.data.key
        except TypeError:
            raise TypeError('Cannot compare BSTNode to other data')
        except AttributeError:
            raise TypeError('Cannot compare BSTNode to other object')

    def __le__(self, other):
        try:
            return self.data.key <= other.data.key
        except TypeError:
            raise TypeError('Cannot compare BSTNode to other data')
        except AttributeError:
            raise TypeError('Cannot compare BSTNode to other object')

    def __ge__(self, other):
        try:
            return self.data.key >= other.data.key
        except TypeError:
            raise TypeError('Cannot compare BSTNode to other data')
        except AttributeError:
            raise TypeError('Cannot compare BSTNode to other object')


class DictPair:

    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value

    # def __eq__(self, other):
    #     try:
    #         return self.key == other.key
    #     except TypeError:
    #         raise TypeError('Cannot compare DictPair to other key')
    #     except AttributeError:
    #         raise TypeError('Cannot compare DictPair to other object')

    # def __lt__(self, other):
    #     try:
    #         return self.key < other.key
    #     except TypeError:
    #         raise TypeError('Cannot compare DictPair to other key')
    #     except AttributeError:
    #         raise TypeError('Cannot compare DictPair to other object')

    # def __gt__(self, other):
    #     try:
    #         return self.key > other.key
    #     except TypeError:
    #         raise TypeError('Cannot compare DictPair to other key')
    #     except AttributeError:
    #         raise TypeError('Cannot compare DictPair to other object')

    # def __le__(self, other):
    #     try:
    #         return self.key <= other.key
    #     except TypeError:
    #         raise TypeError('Cannot compare DictPair to other key')
    #     except AttributeError:
    #         raise TypeError('Cannot compare DictPair to other object')

    # def __ge__(self, other):
    #     try:
    #         return self.key <= other.key
    #     except TypeError:
    #         raise TypeError('Cannot compare DictPair to other key')
    #     except AttributeError:
    #         raise TypeError('Cannot compare DictPair to other object')

    # def __ne__(self, other):
    #     try:
    #         return self.key != other.key
    #     except TypeError:
    #         raise TypeError('Cannot compare DictPair to other key')
    #     except AttributeError:
    #         raise TypeError('Cannot compare DictPair to other object')
