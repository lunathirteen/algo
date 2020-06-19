import unittest
from coverpoint import coverpoint


class TestCoverPoint(unittest.TestCase):
    def test_1(self):
        segments = [(1, 3), (2, 5), (3, 6)]
        self.assertEqual(coverpoint(segments), [3])

    def test_2(self):
        segments = [(4, 7), (1, 3), (2, 5), (5, 6)]
        self.assertEqual(coverpoint(segments), [3, 6])


if __name__ == '__main__':
    unittest.main()
