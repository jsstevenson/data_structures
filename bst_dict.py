from binary_tree import BinaryTree, BinaryTreeNode
from ds_exceptions import EmptyContainerError


class BSTDict(BinaryTree):

    def __init__(self, overall_root=None):
        super().__init__(overall_root)

    def put_traverse(self, root, key, value):
        if root.data == key:
            root.data.value = value
        elif root.left is None and key < root.data:
            root.left = BSTDictNode(key, value)
        elif root.right is None and key > root.data:
            root.right = BSTDictNode(key, value)
        elif key < root.data:
            self.put_traverse(root.left, key, value)
        else:
            self.put_traverse(root.right, key, value)

    def put(self, key, value):
        if key is None:
            raise TypeError('Cannot accept key of type None')
        if self.overall_root is None:
            self.overall_root = BSTDictNode(key, value)
        else:
            self.put_traverse(self.overall_root, key, value)

    def contains_key_traverse(self, root, key):
        if root is None:
            return False
        elif root.data.key == key:
            return True
        else:
            left = self.contains_key_traverse(root.left, key)
            right = self.contains_key_traverse(root.right, key)
            return left or right

    def contains_key(self, key):
        if self.overall_root is None:
            return False
        else:
            return self.contains_key_traverse(self.overall_root, key)

    def get_traverse(self, root, key):
        if root is None:
            raise KeyError('Not contained in tree')
        elif key == root.data.key:
            return root.data.value
        elif key < root.data.key:
            return self.get_traverse(root.left, key)
        else:
            return self.get_traverse(root.right, key)

    def get(self, key):
        if self.overall_root is None:
            raise EmptyContainerError('Tree is empty')
        else:
            return self.get_traverse(self.overall_root, key)

    def print_inorder_traverse(self, root):
        if root is None:
            return ''
        else:
            result = ''
            result += self.print_inorder_traverse(root.left)
            result += str(root.data) + ', '
            result += self.print_inorder_traverse(root.right)
            return result

    def print_inorder(self):
        if self.overall_root is None:
            return('{}')
        else:
            result = '{'
            result += self.print_inorder_traverse(self.overall_root)
            result = result[:-2] + '}'
            return result

    def __repr__(self):
        return self.print_inorder()


class BSTDictNode(BinaryTreeNode):

    def __init__(self, key, value, left=None, right=None):
        super().__init__(KVPair(key, value), left, right)


class KVPair(object):

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return f'{self.key}: {self.value}'

    def __eq__(self, other_pair):
        try:
            return self.key == other_pair
        except TypeError:
            raise TypeError('Cannot compare value with other key')

    def __lt__(self, other_pair):
        try:
            return self.key < other_pair
        except TypeError:
            raise TypeError('Cannot compare value with other key')

    def __le__(self, other_pair):
        try:
            return self.key <= other_pair
        except TypeError:
            raise TypeError('Cannot compare value with other key')

    def __gt__(self, other_pair):
        try:
            return self.key > other_pair
        except TypeError:
            raise TypeError('Cannot compare value with other key')

    def __ge__(self, other_pair):
        try:
            return self.key >= other_pair
        except TypeError:
            raise TypeError('Cannot compare value with other key')
