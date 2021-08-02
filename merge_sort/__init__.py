"""
Первая строка содержит число 1≤n≤10^5,
вторая — массив A[1…n], содержащий натуральные числа, не превосходящие 10^9.
Необходимо посчитать число пар индексов 1≤i<j≤n, для которых A[i]>A[j].
Такая пара элементов называется инверсией массива
Количество инверсий в массиве является в некотором смысле его мерой неупорядоченности:
например, в упорядоченном по неубыванию массиве инверсий нет вообще,
а в массиве, упорядоченном по убыванию, инверсию образуют каждые два элемента.)
"""
from typing import List


def merge_sort(array: List) -> None:
    if len(array) > 1:
        m = (len(array)) // 2

        l_array = array[:m]
        r_array = array[m:]
        merge_sort(l_array)
        merge_sort(r_array)
        i = 0
        j = 0
        k = 0
        while i < len(l_array) and j < len(r_array):
            if l_array[i] <= r_array[j]:
                array[k] = l_array[i]
                i += 1
            else:
                array[k] = r_array[j]
                j += 1
            k += 1

        if i >= len(l_array):
            array[k:] = r_array[j:]
        elif j >= len(r_array):
            array[k:] = l_array[i:]

    return array


def merge_sort_inv(array: List) -> int:
    if len(array) > 1:
        m = (len(array)) // 2

        l_array = array[:m]
        r_array = array[m:]
        l_inv = merge_sort_inv(l_array)
        r_inv = merge_sort_inv(r_array)
        i = 0
        j = 0
        k = 0
        inversion = 0 + l_inv + r_inv
        while i < len(l_array) and j < len(r_array):
            if l_array[i] <= r_array[j]:
                array[k] = l_array[i]
                i += 1
            else:
                array[k] = r_array[j]
                j += 1
                inversion += len(l_array) - i
            k += 1

        if i >= len(l_array):
            array[k:] = r_array[j:]
        elif j >= len(r_array):
            array[k:] = l_array[i:]
        return inversion
    return 0


if __name__ == "__main__":
    n = input().split()
    input_string = input().split()
    array = [int(el) for el in input_string]
    print(merge_sort_inv(array))
