"""Напищите рекрсивную функцию для подсчета элементов в списке"""


def reccount(array):
    if array == []:
        return 0
    else:
        return 1 + reccount(array[1:])
