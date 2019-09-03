import unittest
from unlim_pack import unlim_pack


class TestUnlimPack(unittest.TestCase):
    def test_1(self):
        items = [(60, 20), (100, 50), (120, 30)]
        W = 50
        self.assertEqual(unlim_pack(W, items), 180.000)

    def test_2(self):
        items = [(100, 10)]
        W = 9
        self.assertEqual(unlim_pack(W, items), 90.000)

    def test_3(self):
        items = [(100, 30), (120, 20), (100, 10)]
        W = 0
        self.assertEqual(unlim_pack(W, items), 0.000)

if __name__ == '__main__':
    unittest.main()
