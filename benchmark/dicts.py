import time
import random
import sys
sys.path.append('.')  # relative import -- must execute from main directory
from bst_dict import BSTDict
from array_dict import ArrayDict


def test_dict_rand(test_dict_class):
    test_dict = test_dict_class()
    print(f'testing {test_dict_class} on random')
    start = time.time()
    keys = []
    for i in range(400):
        x = random.randint(0, 1000)
        if x not in keys:
            keys.append(x)
        test_dict.put(x, 'a')
    for i in keys:
        test_dict.remove(i)
    end = time.time()
    print(end - start)


def test_dict_ordinal(test_dict):
    x = test_dict()
    print(f'testing {test_dict} on ordinal keys')
    start = time.time()
    for i in range(500):
        x.put(i, 'a')
    for i in range(500):
        x.remove(i)
    end = time.time()
    print(end - start)


def main():
    dicts = [BSTDict, ArrayDict]
    for i in dicts:
        test_dict_rand(i)
        test_dict_ordinal(i)


if __name__ == '__main__':
    main()
