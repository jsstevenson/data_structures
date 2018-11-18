from binary_tree import BinaryTree, BinaryTreeNode


class BinarySearchTree(BinaryTree):

    def __init__(self, overall_root=None):
        super().__init__(overall_root)

    def add_find(self, root, item):
        if root.left is None and item < root.data:
            root.left = BinaryTreeNode(item)
        elif root.right is None and item > root.data:
            root.right = BinaryTreeNode(item)
        elif item < root.data:
            self.add_find(root.left, item)
        else:
            self.add_find(root.right, item)

    def add(self, item):
        if item is None:
            raise TypeError('cannot accept type None')
        if self.overall_root is None:
            self.overall_root = BinaryTreeNode(item)
        else:
            try:
                item > self.overall_root.data
            except TypeError:
                raise TypeError('cannot accept item of this type')
            self.add_find(self.overall_root, item)

    def height(self, root):
        if root is None:
            return 0
        else:
            result = []
            result.append(self.height(root.left))
            result.append(self.height(root.right))
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
            result += self.inorder(root.left)
            result += str(root.data) + ', '
            result += self.inorder(root.right)
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
            left = self.contains_find(root.left, data)
            right = self.contains_find(root.right, data)
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
            return self.get_find(root.left, data)
        else:
            return self.get_find(root.right, data)

    def get(self, data):
        if self.overall_root is None:
            raise KeyError('Not contained in tree')
        else:
            return self.get_find(self.overall_root, data)
