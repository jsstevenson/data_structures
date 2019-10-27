from double_linked_list import DoubleLinkedList
import unittest


class TestAdd(unittest.TestCase):
    def test_general(self):
        x = DoubleLinkedList()
        self.assertEqual(x.__str__(), '[]')
        x.add(5)
        x.add(10)
        self.assertEqual(x.__str__(), '[5, 10]')


class TestRemoveIndex(unittest.TestCase):
    def test_general(self):
        x = DoubleLinkedList()
        x.add(5)
        x.add(11)
        x.remove_index(1)
        self.assertEqual(x.__str__(), '[5]')

    def test_zero(self):
        x = DoubleLinkedList()
        x.add(5)
        x.add(11)
        x.remove_index(0)
        self.assertEqual(x.__str__(), '[11]')

    def test_remove_all(self):
        x = DoubleLinkedList()
        x.add(5)
        x.add(11)
        x.remove_index(1)
        x.remove_index(0)
        self.assertEqual(x.__str__(), '[]')

    def test_unordered(self):
        x = DoubleLinkedList()
        x.add(3)
        x.add(9)
        x.add(13)
        x.remove_index(0)
        x.remove_index(1)
        x.remove_index(0)
        self.assertEqual(x.__str__(), '[]')


class TestGet(unittest.TestCase):
    def test_general(self):
        x = DoubleLinkedList()
        x.add('a')
        x.add('b')
        x.add('c')
        x.add('d')
        self.assertEqual(x.get(1), 'b')
        self.assertEqual(x.get(0), 'a')
        self.assertEqual(x.get(3), 'd')
        x.add('e')
        self.assertEqual(x.get(4), 'e')


class TestGetIndex(unittest.TestCase):
    def test_general(self):
        x = DoubleLinkedList()
        self.assertEqual(x.get_index('a'), -1)
        x.add('a')
        self.assertEqual(x.get_index('a'), 0)
        x.add('b')
        self.assertEqual(x.get_index('a'), 0)
        self.assertEqual(x.get_index('b'), 1)
        x.add('c')
        x.add('d')
        self.assertEqual(x.get_index('b'), 1)
        self.assertEqual(x.get_index('f'), -1)


if __name__ == '__main__':
    unittest.main()
