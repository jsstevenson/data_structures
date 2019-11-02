from binary_tree import BinaryTree, BinaryTreeNode
from ds_exceptions import EmptyContainerError


class BSTDict(BinaryTree):

    def __init__(self, overall_root=None):
        super().__init__(overall_root)

    '''
    Helper method for put(). Checks key against root, and either replaces
    root's current value with provided value, puts it at a new child to the
    left or right, or continues the traversal from the left or right child.
    '''
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

    '''
    Put key-value pair into tree.
    Raises TypeError if key is None.
    '''
    def put(self, key, value):
        if key is None:
            raise TypeError('Cannot accept key of type None')
        if self.overall_root is None:
            self.overall_root = BSTDictNode(key, value)
        else:
            try:
                key > self.overall_root.data.key
            except TypeError:
                raise TypeError('cannot accept key of this type')
            self.put_traverse(self.overall_root, key, value)

    '''
    Helper method for contains_key(). Continues search for key against current
    node ('root') and continues search downward if not found.
    '''
    def contains_key_traverse(self, root, key):
        if root is None:
            return False
        elif root.data.key == key:
            return True
        else:
            left = self.contains_key_traverse(root.left, key)
            right = self.contains_key_traverse(root.right, key)
            return left or right

    '''
    Check whether dict contains key
    '''
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

    '''
    Get value for provided key. Raises KeyError if key isn't in tree,
    and EmptyContainerError if tree is empty.
    '''
    def get(self, key):
        if self.overall_root is None:
            raise EmptyContainerError('Tree is empty')
        else:
            return self.get_traverse(self.overall_root, key)

    '''
    Helper method for readd(). Once we're in the tree, traverse it recursively
    to find the correct location for the disconnected branch.
    '''
    def reput_traverse(self, root, branch):
        if root.left is None and branch.data < root.data:
            root.left = branch
        elif root.right is None and branch.data > root.data:
            root.right = branch
        elif branch.data < root.data:
            self.reput_traverse(root.left, branch)
        else:
            self.reput_traverse(root.right, branch)

    '''
    Helper method for remove(). For any branches disconnected by removal,
    perform in-order traversal to find their correct position and re-add them.
    Branch could be None - we want to call it on child branches without
    any prior check on their existence.

    TODO: Less naive implementation. Currently it manually readds every node
    individually. This is undobutedly suboptimal.
    '''
    def readd(self, branch):
        if branch is not None:
            # add kid nodes + None out child branches
            if branch.left is not None:
                temp = branch.left
                branch.left = None
                self.readd(temp)
            if branch.right is not None:
                temp = branch.right
                branch.right = None
                self.readd(temp)
            # add this node back
            if self.overall_root is None:
                self.overall_root = branch
            else:
                self.reput_traverse(self.overall_root, branch)

    def remove_traverse(self, root, key):
        if root is None:
            raise KeyError('Not contained in tree')
        elif root.left.data == key:
            temp = root.left
            root.left = None
            self.readd(temp.left)
            self.readd(temp.right)
            return temp.data
        elif root.right.data == key:
            temp = root.right
            root.right = None
            self.readd(temp.left)
            self.readd(temp.right)
            return temp.data
        elif root.data > key:
            return self.remove_traverse(self, root.left, key)
        else:
            return self.remove_traverse(self, root.right, key)

    '''
    Remove key/value pair with specified key from tree. Raises KeyError if key
    isn't contained in the tree. Returns the removed KVPair object.
    '''
    def remove(self, key):
        if self.overall_root is None:
            raise KeyError('Not contained in tree')
        elif self.overall_root.data == key:
            temp = self.overall_root
            self.overall_root = None
            self.readd(temp.left)
            self.readd(temp.right)
            return temp.data
        else:
            return self.remove_traverse(self.overall_root, key)

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

    def __str__(self):
        return self.print_inorder()

    def __repr__(self):
        return self.__str__()


class BSTDictNode(BinaryTreeNode):

    '''
    Calls BinaryTreeNode constructor, supplying its data field with a new
    KVPair object. Leaves left and right children fields empty if not given
    any arguments.
    '''
    def __init__(self, key, value, left=None, right=None):
        super().__init__(KVPair(key, value), left, right)

    '''
    Return string formatting a la standard dict representation
    e.g., {key: value}
    '''
    def __str__(self):
        return f'{{{self.data}}}'

    def __repr__(self):
        return self.__str__()


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
