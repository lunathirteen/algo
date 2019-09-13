import unittest
from rec_max import rec_max
from random import randint


class TestRecMax(unittest.TestCase):
    def test_1(self):
        array = [randint(0, 10) for _ in range(randint(1, 5))]
        self.assertEqual(rec_max(array), max(array),
                         msg="array {}".format(array))

    def test_2(self):
        array = [randint(0, 10) for _ in range(1)]
        self.assertEqual(rec_max(array), max(array),
                         msg="array {}".format(array))

if __name__ == '__main__':
    unittest.main()
