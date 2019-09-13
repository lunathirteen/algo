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
    freq_array = list(freq.values()).sort()
    tree = {}

    while len(freq_array) > 1:
        f_i = freq_array.pop(0)
        f_j = freq_array.pop(0)
        node = f_i + f_j
        tree[node] = (f_i, f_j)
        freq_array.append(node)
        freq_array.sort()

    return tree
