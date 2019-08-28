import unittest
from fib import fib


class TestFib(unittest.TestCase):
    def test_n0(self):
        print('Test fibbonacci n = 0')
        self.assertEqual(fib(0), 0)

    def test_n1(self):
        print('Test fibbonacci n = 1')
        self.assertEqual(fib(1), 1)

    def test_n3(self):
        print('Test fibbonacci n = 3')
        self.assertEqual(fib(3), 2)

    def test_n10(self):
        print('Test fibbonacci n = 10')
        self.assertEqual(fib(10), 55)


if __name__ == '__main__':
    unittest.main()
