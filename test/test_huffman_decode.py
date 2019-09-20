import unittest
from huffman_decode import huffman_decode


class TestHuffmanDecode(unittest.TestCase):
    def test_1(self):
        s = '0'
        codes_dict = {'a': '0'}
        self.assertEqual(huffman_decode(s, codes_dict), 'a')

    def test_2(self):
        s = '01001100100111'
        codes_dict = {'a': '0', 'b': '10', 'c': '110', 'd': '111'}
        self.assertEqual(huffman_decode(s, codes_dict), 'abacabad')

    def test_3(self):
        s = '0000000'
        codes_dict = {'a': '0'}
        self.assertEqual(huffman_decode(s, codes_dict), 'aaaaaaa')

    def test_4(self):
        s = '01101110100010101101110'
        codes_dict = {'a': '0', 'c': '100', 'd': '101', 'b': '110', 'r': '111'}
        self.assertEqual(huffman_decode(s, codes_dict), 'abracadabra')


if __name__ == '__main__':
    unittest.main()
