from bst import BinarySearchTree
from binary_tree import BinaryTreeNode


class BSTDict(BinarySearchTree):
    def __init__(self, overall_root=None):
        super(BSTDict, self).__init__(overall_root)

    def add_find(self, root, item):
        if root.left_child is None and item < root:
            root.left_child = item
        elif root.right_child is None and item > root:
            root.right_child = item
        elif item < root:
            self.add_find(root.left_child, item)
        else:
            self.add_find(root.right_child, item)

    def add(self, key, value):
        if key is None:
            raise TypeError('cannot accept type None for key')
        if self.overall_root is None:
            self.overall_root = BSTDictNode(key, value)
        else:
            item = BSTDictNode(key, value)
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
            result += str(self.key) + ': ' + str(self.value) + ', '
            result += self.inorder(root.right_child)
            return result

    def print_inorder(self):
        if self.overall_root is None:
            print('{}')
        else:
            result = '{'
            result += self.inorder(self.overall_root)
            result = result[:-2] + '}'
            return result

    def __repr__(self):
        return self.print_inorder()

    def contains_key_find(self, root, key):
        if root is None:
            return False
        try:
            if root.key == key:
                return True
            elif root.key < key:
                return self.contains_key_find(root.left, key)
            else:
                return self.contains_key_find(root.right, key)
        except TypeError:
            raise TypeError('Cannot compare provided key to tree')

    def contains_key(self, key):
        if self.overall_root is None:
            return False
        else:
            return self.contains_key_find(self.overall_root, key)

    def get_find(self, root, key):
        if root is None:
            raise KeyError('Not contained in tree')
        try:
            if root.key == key:
                return root.value
            elif root.key < key:
                return self.get_find(root.left, key)
            else:
                return self.get_find(root.right, key)
        except TypeError:
            raise TypeError('Cannot compare key to tree')

    def get(self, key):
        if self.overall_root is None:
            raise KeyError('Tree is empty')
        else:
            return self.get_find(self.overall_root, key)


class BSTDictNode(BinaryTreeNode):
    def __init__(self, key, value, left, right):
        if key is None:
            raise TypeError('Cannot initialize key as None')
        else:
            self.key = key
            self.value = value

    def __eq__(self, other_node):
        try:
            return self.key == other_node.key
        except TypeError:
            raise TypeError('Cannot compare values with other node')

    def __lt__(self, other_node):
        try:
            return self.key < other_node.key
        except TypeError:
            raise TypeError('Cannot compare values with other node')

    def __le__(self, other_node):
        try:
            return self.key <= other_node.key
        except TypeError:
            raise TypeError('Cannot compare values with other node')

    def __gt__(self, other_node):
        try:
            return self.key > other_node.key
        except TypeError:
            raise TypeError('Cannot compare values with other node')

    def __ge__(self, other_node):
        try:
            return self.key >= other_node.key
        except TypeError:
            raise TypeError('Cannot compare values with other node')
