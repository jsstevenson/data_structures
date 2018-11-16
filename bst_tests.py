from bst import BinarySearchTree
from binary_tree import BinaryTreeNode
import unittest


# class TestDictPair(unittest.TestCase):

#     def test_all(self):
#         x = DictPair(7)
#         y = DictPair(5)
#         self.assertGreater(x, y)
#         x = DictPair(4)
#         self.assertLess(x, y)
#         x = DictPair(5)
#         self.assertEqual(x, y)
#         self.assertLessEqual(x, y)
#         x = DictPair(9)
#         y = DictPair(9)
#         self.assertGreaterEqual(x, y)


# class TestNodeDict(unittest.TestCase):

#     def test_node_with_dict(self):
#         x = BSTNode(5)
#         self.assertEqual(x.data, DictPair(5))
#         y = BSTNode(5)
#         self.assertEqual(x, y)


class TestAdd(unittest.TestCase):

    def test_add(self):
        x = BinarySearchTree()
        x.add(3)
        x.add(7)
        x.add(9)
        self.assertEqual("[3, 7, 9]", x.print_inorder())


class TestHeight(unittest.TestCase):

    def test_size(self):
        x = BinarySearchTree()
        self.assertEqual(0, x.get_height())
        self.assertNotEqual(-1, x.get_height())
        x.add(1)
        self.assertEqual(1, x.get_height())


class TestContains(unittest.TestCase):

    def test_contains(self):
        x = BinarySearchTree()
        x.add(5)
        self.assertEqual(True, x.contains(5))
        self.assertEqual(False, x.contains(3))
        x.add(3)
        self.assertEqual(True, x.contains(3))


class TestGet(unittest.TestCase):

    def test_get(self):
        x = BinarySearchTree()
        x.add(5)
        x.add(9)
        x.add(33)
        x.add(31)
        self.assertEqual(x.get(5).data, BinaryTreeNode(5).data)


if __name__ == '__main__':
    unittest.main()
