from bst_dict import BSTDict
import unittest


class TestAdd(unittest.TestCase):

    def test_add(self):
        x = BSTDict()
        x.put('a', 5)
        x.put('b', 7)
        x.put('c', 9)
        x.put('b', 6)
        self.assertEqual(6, x.get('b'))
        self.assertEqual(9, x.get('c'))
        with self.assertRaises(TypeError):
            x.put(9, 'c')
        x.put('z', 110)


class TestContainsKey(unittest.TestCase):

    def test_contains(self):
        x = BSTDict()
        self.assertTrue(not x.contains_key(5))
        x.put(5, 'a')
        self.assertTrue(x.contains_key(5))


class TestGet(unittest.TestCase):

    def test_get(self):
        x = BSTDict()
        x.put(1, 'a')
        self.assertEqual('a', x.get(1))
        x.put(2, 'b')
        self.assertEqual('a', x.get(1))
        self.assertEqual('b', x.get(2))
        x.put(3, 'c')


if __name__ == '__main__':
    unittest.main()
