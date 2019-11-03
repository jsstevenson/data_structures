from ds_exceptions import NoSuchKeyError
from bst_dict import BSTDict, BSTDictNode, KVPair


class AVLDict(BSTDict):

    def __init__(self, overall_root=None):
        super().__init__(overall_root)

    def update_height(self, node):
        '''
        Update relative height data for given node.
        '''
        if node.left and node.right:
            node.height = max(node.left.height, node.right.height) + 1
        elif node.left:
            node.height = node.left.height + 1
        elif node.right:
            node.height = node.right.height + 1
        else:
            node.height = 0

    def left_rotate(self, parent, pivot):
        '''
        Helper method for balancing -- performs left rotation for right-right
        case or kink cases. Parent is the root where the imbalance occurs.
        Pivot is the node which will become the new parent (ie, it would be the
        immediate parent of the inserted node that causes the
        imbalance.
        '''
        parent.right = pivot.left
        pivot.left = parent
        self.update_height(parent.left)
        return pivot

    def right_rotate(self, parent, pivot):
        '''
        Helper method for balancing -- performs right rotation for left-left
        case or kink cases. Parent is the root where the imbalance occurs.
        Pivot is the node which will become the new parent (ie, it would be the
        immediate parent of the inserted node that causes the
        imbalance.
        '''
        parent.left = pivot.right
        pivot.right = parent
        self.update_height(parent.right)
        return pivot

    def put_traverse(self, node, key, value):
        if key == node.key:
            node.data.value = value
        elif key > node.key:
            if node.right:
                self.put_traverse(node.right, key, value)
                # TODO balance
            else:
                node.right = AVLNode(key, value)
                # TODO balance
        else:
            if node.left:
                self.put_traverse(node.left, key, value)
                # TODO balance
            else:
                node.left = AVLNode(key, value)
                # TODO balance

    def put(self, key, value):
        if not self.root:
            self.root = AVLNode(key, value)
        else:
            self.put_traverse(self.root, key, value)
            # TODO balance

    def get(self, key):
        pass

    def remove(self, key):
        pass


class AVLNode(BSTDictNode):

    def __init__(self, key, value, left=None, right=None):
        '''
        Calls parent constructors, creating a new node with a data field
        containing a KVPair populated with given key/value. Sets height to 0.
        Leaves left and right children fields empty if not given any arguments.
        '''
        super().__init__(KVPair(key, value), left, right)
        self.height = 0 
