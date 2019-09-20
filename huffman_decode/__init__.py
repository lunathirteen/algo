"""
По данной непустой строке s длины не более 10^4,
состоящей из строчных букв латинского алфавита,
постройте оптимальный беспрефиксный код.

В первой строке выведите количество различных букв k,
встречающихся в строке, и размер получившейся закодированной строки.
В следующих k строках запишите коды букв в формате "letter: code".
В последней строке выведите закодированную строку.
"""
from collections import Counter
from typing import Dict

Codes = Dict[str, str]


def huffman_decode(string: str, codes: Codes, current_code: str ='') -> str:

    reversed_codes = {v: k for k, v in codes.items()}

    decoded_string = ''

    for char in string:
        current_code += char
        if reversed_codes.get(current_code):
            decoded_string += reversed_codes.get(current_code)
            current_code = ''

    return decoded_string


def main():

    n, b = list(map(int, input().split()))
    codes_dict = {}

    for i in range(n):
        k, v = input().split(': ')
        codes_dict[k] = v
    string = input()

    print(huffman_decode(string, codes_dict))

if __name__ == "__main__":
    main()
