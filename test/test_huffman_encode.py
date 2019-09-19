import unittest
from huffman_encode import huffman_encode


class TestHuffmanCode(unittest.TestCase):
    def test_1(self):
        s = 'a'
        _, s = huffman_encode(s)
        self.assertEqual(s, '0')

    def test_2(self):
        s = 'abacabad'
        _, s = huffman_encode(s)
        self.assertEqual(s, '01001100100111')

    def test_3(self):
        s = 'aaaaaaa'
        _, s = huffman_encode(s)
        self.assertEqual(s, '0000000')


if __name__ == '__main__':
    unittest.main()
