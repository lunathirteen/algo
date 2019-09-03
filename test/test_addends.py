import unittest
from addends import addends
from random import randint


class TestAddends(unittest.TestCase):
    def test_1(self):
        n = 4
        self.assertEqual(addends(n), [1, 3])

    def test_2(self):
        n = 6
        self.assertEqual(addends(n), [1, 2, 3])

    def test_3(self):
        n = 1
        self.assertEqual(addends(n), [1])

    def test_4(self):
        n = randint(0, 10**5)
        self.assertEqual(n, sum(addends(n)))

if __name__ == '__main__':
    unittest.main()
