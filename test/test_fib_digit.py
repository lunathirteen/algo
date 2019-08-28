import unittest
from fib_digit import fib_digit


class TestFibDigit(unittest.TestCase):
    def test_large_number(self):
        print('Test fibbonacci n = 696352')
        self.assertEqual(fib_digit(696352), 9)

    def test_n0(self):
        print('Test fibbonacci n = 0')
        self.assertEqual(fib_digit(0), 0)

    def test_n1(self):
        print('Test fibbonacci n = 1')
        self.assertEqual(fib_digit(1), 1)

    def test_n10(self):
        print('Test fibbonacci n = 10')
        self.assertEqual(fib_digit(10), 5)

if __name__ == '__main__':
    unittest.main()
