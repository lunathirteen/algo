import unittest
import random
from priority_queue import PriorityQueue


class TestPriorityQueue(unittest.TestCase):
    def test_1(self):
        queue = PriorityQueue()
        queue.insert(200)
        queue.insert(10)
        max_element = queue.extract_max()
        self.assertEqual(max_element, 200)

    def test_2(self):
        queue = PriorityQueue()
        queue.insert(200)
        queue.insert(10)
        max_element = queue.extract_max()
        queue.insert(5)
        queue.insert(500)
        max_element = queue.extract_max()
        self.assertEqual(max_element, 500)

    def test_3(self):
        array = [random.randint(0, 100) for i in range(random.randint(1, 30))]
        array_max = max(array)
        queue = PriorityQueue()
        for element in array:
            queue.insert(element)
        max_element = queue.extract_max()

        self.assertEqual(max_element, array_max, msg=array)
# test_array = [98, 94, 97, 81, 86, 91, 90, 77, 53, 54, 64, 66, 83, 79, 79, 51, 67, 37, 40, 16, 52, 14, 52, 3, 4, 26, 79, 47, 52, 66, 67, 13, 30, 48, 60, 32, 15, 17]


if __name__ == '__main__':
    unittest.main()
