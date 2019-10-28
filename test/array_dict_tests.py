from array_dict import ArrayDict
from ds_exceptions import NoSuchKeyError, EmptyContainerError
import unittest


class TestAdd(unittest.TestCase):
    def add_general(self):
        self.x = ArrayDict()
        self.x.add('a', 1)
        self.x.add('b', 2)
        self.x.add('c', 3)


class TestGet(unittest.TestCase):
    def test_general(self):
        x = ArrayDict()
        x.add('a', 1)
        self.assertEqual(x.get('a'), 1)
        x.add('b', 2)
        self.assertEqual(x.get('b'), 2)
        x.add('c', 3)
        self.assertEqual(x.get('a'), 1)

    def test_exceptions(self):
        x = ArrayDict()
        x.add('a', 1)
        with self.assertRaises(NoSuchKeyError):
            x.get('b')


class TestPut(unittest.TestCase):
    def setUp(self):
        self.x = ArrayDict()
        self.x.add('a', 1)
        self.x.add('b', 2)
        self.x.add('c', 3)

    def tearDown(self):
        del(self.x)

    def test_general(self):
        self.x.add('d', 4)
        self.assertEqual(self.x.get('d'), 4)
        self.x.put('c', 5)
        self.assertEqual(self.x.get('c'), 5)
        self.x.put('e', 10)
        self.assertEqual(self.x.get('e'), 10)


class TestRemove(unittest.TestCase):
    def setUp(self):
        self.x = ArrayDict()
        self.x.add('a', 1)
        self.x.add('b', 2)
        self.x.add('c', 3)

    def tearDown(self):
        del(self.x)

    def test_general(self):
        self.x.remove('a')
        self.assertEqual(self.x.pairs[0][1], 2)
        self.x.remove('b')
        self.assertEqual(self.x.pairs[0][1], 3)

    def test_raises_empty(self):
        self.x.remove('b')
        self.x.remove('c')
        self.x.remove('a')
        with self.assertRaises(EmptyContainerError):
            self.x.remove('a')

    def test_raises_no_key(self):
        with self.assertRaises(NoSuchKeyError):
            self.x.remove('d')


class TestContains(unittest.TestCase):
    def test_general(self):
        x = ArrayDict()
        x.add('a', 1)
        self.assertTrue(x.contains_key('a'))
        self.assertFalse(x.contains_key('b'))
        x.add('b', 1)
        self.assertTrue(x.contains_key('b'))
        x.add('c', 2)
        self.assertTrue(x.contains_key('c'))
        self.assertFalse(x.contains_key('d'))

    def test_raises(self):
        x = ArrayDict()
        with self.assertRaises(EmptyContainerError):
            x.contains_key('a')
        x.add('a', 1)
        self.assertTrue(x.contains_key('a'))


class TestSize(unittest.TestCase):
    def test_general(self):
        x = ArrayDict()
        self.assertEqual(x.size(), 0)
        x.add('a', 1)
        self.assertEqual(x.size(), 1)
        x.add('b', 2)
        self.assertEqual(x.size(), 2)
        x.put('b', 3)
        self.assertEqual(x.size(), 2)
        x.remove('a')
        self.assertEqual(x.size(), 1)
        x.remove('b')
        self.assertEqual(x.size(), 0)

