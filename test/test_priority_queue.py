import unittest
from random import randint
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
        array = [randint(0, 100) for i in range(randint(1, 30))]
        array_max = max(array)
        queue = PriorityQueue()
        for element in array:
            queue.insert(element)
        max_element = queue.extract_max()
        self.assertEqual(max_element, array_max, msg=array)

    def test_4(self):
        array = [randint(100000, 150000) for i in range(randint(30, 60))]
        array_max = max(array)
        queue = PriorityQueue()
        for element in array:
            queue.insert(element)
        max_element = queue.extract_max()
        self.assertEqual(max_element, array_max, msg=array)


if __name__ == '__main__':
    unittest.main()
