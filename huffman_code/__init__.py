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


def huffman_code(s):

    freq = Counter(s)
    tree = OrderedDict()
    temp = {}

    while len(freq) > 1:
        min_key_i = min(freq, key=freq.get)
        F_i = freq.pop(min_key_i, None)
        temp[min_key_i] = F_i
        min_key_j = min(freq, key=freq.get)
        F_j = freq.pop(min_key_j, None)
        temp[min_key_j] = F_j
        node = min_key_i + min_key_j
        freq[node] = F_i + F_j
        tree[node] = [min_key_i, min_key_j]

    return tree
