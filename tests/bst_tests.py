from bst import BinarySearchTree
import unittest


class TestAdd(unittest.TestCase):

    def test_add(self):
        x = BinarySearchTree()
        x.add(3)
        x.add(7)
        x.add(9)
        self.assertEqual("[3, 7, 9]", x.print_inorder())


class TestRemove(unittest.TestCase):

    def test_remove(self):
        x = BinarySearchTree()
        with self.assertRaises(KeyError):
            x.remove(5)
        x.add(5)
        x.remove(5)
        self.assertEqual([], x.list_inorder())
        x.add(5)
        x.add(3)
        x.add(7)
        x.remove(5)
        self.assertEqual([3, 7], x.list_inorder())


class TestHeight(unittest.TestCase):

    def test_size(self):
        x = BinarySearchTree()
        self.assertEqual(-1, x.height())
        self.assertNotEqual(0, x.height())
        x.add(1)
        self.assertEqual(0, x.height())
        x.add(0)
        x.add(2)
        self.assertEqual(1, x.height())


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
        self.assertEqual(x.get(5), 5)


if __name__ == '__main__':
    unittest.main()
