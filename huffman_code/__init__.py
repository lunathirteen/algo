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


def build_tree(s):

    freq = sorted(Counter(s).items(), key=lambda pair: pair[1], reverse=False)

    while len(freq) >= 2:
        F_i = freq.pop(0)
        F_j = freq.pop(0)
        item = ((F_i[0], F_j[0]), F_i[1] + F_j[1])
        freq.append(item)
        freq = sorted(freq, key=lambda pair: pair[1], reverse=False)

    return freq[0][0]


def walk_tree(tree, current_code='', codes={}):

    if type(tree[0]) == tuple:
        walk_tree(tree[0], current_code + '0', codes)
    else:
        codes[tree[0]] = current_code + '0'
    if type(tree[1]) == tuple:
        walk_tree(tree[1], current_code + '1', codes)
    else:
        codes[tree[1]] = current_code + '1'

    return(codes)

tree = build_tree(s)
huff = walk_tree(tree)
