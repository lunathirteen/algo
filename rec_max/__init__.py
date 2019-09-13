"""Найти наибольшее число в списке"""


def rec_max(array):

    if len(array) == 1:
        return array[0]

    elif len(array) == 2:
        return array[0] if array[0] > array[1] else array[1]

    r_array = rec_max(array[1:])
    return array[0] if array[0] > r_array else r_array
