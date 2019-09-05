import unittest
from recsum import recsum
from random import randint


class TestRecsum(unittest.TestCase):
    def test_1(self):
        array = [randint(0, 10) for _ in range(randint(0, 5))]
        self.assertEqual(recsum(array), sum(array),
                         msg="array {}".format(array))


if __name__ == '__main__':
    unittest.main()
