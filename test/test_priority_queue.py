import unittest
from priority_queue import PriorityQueue


class TestPriorityQueue(unittest.TestCase):
    def test_1(self):
        a = PriorityQueue()
        a.insert(200)
        a.insert(10)
        self.assertEqual(a.array, [200, 10])

    def test_2(self):
        a = PriorityQueue()
        a.insert(200)
        a.insert(10)
        heap_max = a.extract_max()
        self.assertEqual(heap_max, 200)

    def test_3(self):
        a = PriorityQueue()
        a.insert(200)
        a.insert(10)
        a.extract_max()
        a.insert(5)
        a.insert(500)
        self.assertEqual(a.array, [500, 5, 10])
    
    def test_4(self):
        a = PriorityQueue()
        a.insert(200)
        a.insert(10)
        a.extract_max()
        a.insert(5)
        a.insert(500)
        heap_max = a.extract_max()
        self.assertEqual(heap_max, 500)


if __name__ == '__main__':
    unittest.main()
