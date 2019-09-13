import unittest
from huffman_code import huffman_code


class TestHuffmanCode(unittest.TestCase):
    def test_1(self):
        s = 'a'
        self.assertEqual(huffman_code(s), 0)


if __name__ == '__main__':
    unittest.main()
