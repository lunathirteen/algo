import unittest
from binary_search import binary_search


class TestBinarySearch(unittest.TestCase):
    def test_1(self):
        array = [1, 5, 8, 12, 13]
        numbers = [8, 1, 23, 1, 11]
        result = []
        for n in numbers:
            result.append(binary_search(array, n))
        self.assertEqual(result, [3, 1, -1, 1, -1])


if __name__ == '__main__':
    unittest.main()
