import unittest
import random
from gcd import gcd


class TestGCD(unittest.TestCase):

    def test_1(self):
        print('Test gcd a = 18, b = 35')
        self.assertEqual(gcd(18, 35), 1)

    def test_2(self):
        print('Test gcd a = 14159572, b = 63967072')
        self.assertEqual(gcd(14159572, 63967072), 4)

    def test_3(self):
        print('Test gcd with random')
        c = random.randint(0, 1024)
        a = c * random.randint(0, 128)
        b = c * random.randint(0, 128)

        self.assertEqual(gcd(a, a), gcd(a, 0),
                         msg='Test failed: gcd(a, a) != gcd(a, 0)')
        self.assertEqual(gcd(a, a), a,
                         msg='Test failed: gcd(a, a) != a')
        self.assertEqual(gcd(a, 1), 1,
                         msg='Test failed: gcd(a, 1) != 1')
        self.assertEqual(gcd(b, b), gcd(0, b),
                         msg='Test failed: gcd(b, b) != gcd(0, b)')
        self.assertEqual(gcd(b, b), b,
                         msg='Test failed: gcd(b, b) != b')
        self.assertEqual(gcd(1, b), 1,
                         msg='Test failed: gcd(1, b) != 1')

        d = gcd(a, b)
        self.assertEqual(a % d, 0,
                         msg='Test failed: a % d != 0')
        self.assertEqual(b % d, 0,
                         msg='Test failed: b % d != 0')

if __name__ == '__main__':
    unittest.main()
