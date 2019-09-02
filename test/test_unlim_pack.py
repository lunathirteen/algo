import unittest
from unlim_pack import unlim_pack


class TestUnlimPack(unittest.TestCase):
    def test_1(self):
        items = [(60, 20), (100, 50), (120, 30)]
        W = 50
        self.assertEqual(unlim_pack(W, items), 180.000)

if __name__ == '__main__':
    unittest.main()
