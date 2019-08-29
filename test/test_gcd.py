import unittest
from gcd import gcd


class TestGCD(unittest.TestCase):

    def test_1(self):
        print('Test gcd a = 18, b = 35')
        self.assertEqual(gcd(18, 35), 1)

    def test_2(self):
        print('Test gcd a = 14159572, b = 63967072')
        self.assertEqual(gcd(14159572, 63967072), 4)


if __name__ == '__main__':
    unittest.main()
