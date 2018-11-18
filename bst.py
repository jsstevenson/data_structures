from binary_tree import BinaryTree, BinaryTreeNode


class BinarySearchTree(BinaryTree):

    def __init__(self, overall_root=None):
        super().__init__(overall_root)

    def add_traverse(self, root, item):
        if root.left is None and item < root.data:
            root.left = BinaryTreeNode(item)
        elif root.right is None and item > root.data:
            root.right = BinaryTreeNode(item)
        elif item < root.data:
            self.add_traverse(root.left, item)
        else:
            self.add_traverse(root.right, item)

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
            self.add_traverse(self.overall_root, item)

    def height_traverse(self, root):
        if root is None:
            return 0
        else:
            return 1 + max(self.height_traverse(root.left),
                           self.height_traverse(root.right))

    def height(self):
        if self.overall_root is None:
            return -1
        else:
            return self.height_traverse(self.overall_root) - 1

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
            return('[]')
        else:
            result = '['
            result += self.print_inorder_traverse(self.overall_root)
            result = result[:-2] + ']'
            return result

    def __repr__(self):
        return self.print_inorder()

    def list_inorder_traverse(self, root):
        if root is None:
            return []
        else:
            result = []
            result += self.list_inorder_traverse(root.left)
            result += [root.data]
            result += self.list_inorder_traverse(root.right)
            return result

    def list_inorder(self):
        if self.overall_root is None:
            return []
        else:
            return self.list_inorder_traverse(self.overall_root)

    def contains_traverse(self, root, data):
        if root is None:
            return False
        elif root.data == data:
            return True
        else:
            left = self.contains_traverse(root.left, data)
            right = self.contains_traverse(root.right, data)
            return left or right

    def contains(self, data):
        if self.overall_root is None:
            return False
        else:
            return self.contains_traverse(self.overall_root, data)

    def get_traverse(self, root, data):
        if root is None:
            raise KeyError('Not contained in tree')
        elif data == root.data:
            return root.data
        elif data < root.data:
            return self.get_traverse(root.left, data)
        else:
            return self.get_traverse(root.right, data)

    def get(self, data):
        if self.overall_root is None:
            raise KeyError('Not contained in tree')
        else:
            return self.get_traverse(self.overall_root, data)

    def readd_traverse(self, root, to_add):
        if root.left is None and to_add.data < root.data:
            root.left = to_add
        elif root.right is None and to_add.data > root.data:
            root.right = to_add
        elif to_add.data < root.data:
            self.readd_traverse(root.left, to_add)
        else:
            self.readd_traverse(root.right, to_add)

    def readd(self, to_readd):
        if to_readd is not None:
            # add kid nodes + None out child branches
            if to_readd.left is not None:
                temp = to_readd.left
                to_readd.left = None
                self.readd(temp)
            if to_readd.right is not None:
                temp = to_readd.right
                to_readd.right = None
                self.readd(temp)
            # add this node back
            if self.overall_root is None:
                self.overall_root = to_readd
            else:
                self.readd_traverse(self.overall_root, to_readd)

    def remove_traverse(self, root, data_to_remove):
        if root is None:
            raise KeyError('Not contained in tree')
        elif root.left.data == data_to_remove:
            temp = root.left
            root.left = None
            self.readd(temp.left)
            self.readd(temp.right)
            return temp.data
        elif root.right.data == data_to_remove:
            temp = root.right
            root.right = None
            self.readd(temp.left)
            self.readd(temp.right)
            return temp.data
        elif root.data > data_to_remove:
            return self.remove_traverse(self, root.left, data_to_remove)
        else:
            return self.remove_traverse(self, root.right, data_to_remove)

    def remove(self, data_to_remove):
        if self.overall_root is None:
            raise KeyError('Not contained in tree')
        elif self.overall_root.data == data_to_remove:
            temp = self.overall_root
            self.overall_root = None
            self.readd(temp.left)
            self.readd(temp.right)
            return temp.data
        else:
            return self.remove_traverse(self.overall_root, data_to_remove)
