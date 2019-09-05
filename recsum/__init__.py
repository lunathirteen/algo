"""
Рекурсивная сумма
"""


def recsum(array):
    if array == []:
        return 0
    else:
        return array[0] + recsum(array[1:])
