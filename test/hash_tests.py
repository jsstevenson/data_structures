import hash_table
import unittest
import random


class TestBasic(unittest.TestCase):

    def test_basic(self):
        table = hash_table.HashTable()
        for i in range(20):
            table.add(random.randrange(100))
