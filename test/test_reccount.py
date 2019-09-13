import unittest
from reccount import reccount
from random import randint


class TestReccount(unittest.TestCase):
    def test_1(self):
        array = [randint(0, 10) for _ in range(randint(0, 5))]
        self.assertEqual(reccount(array), len(array),
                         msg="array {}".format(array))


if __name__ == '__main__':
    unittest.main()
