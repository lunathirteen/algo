import unittest
from fib_mod import fib_mod


class TestFibMod(unittest.TestCase):

    def test_large_n_m0(self):
        self.assertEqual(fib_mod(10, 2), 1)

if __name__ == '__main__':
    unittest.main()
