"""
Первая строка содержит число 1≤n≤10^5,
вторая — массив A[1…n], содержащий натуральные числа, не превосходящие 10^9.
Необходимо посчитать число пар индексов 1≤i<j≤n, для которых A[i]>A[j].
(Такая пара элементов называется инверсией массива. 
Количество инверсий в массиве является в некотором смысле его мерой неупорядоченности:
например, в упорядоченном по неубыванию массиве инверсий нет вообще, 
а в массиве, упорядоченном по убыванию, инверсию образуют каждые два элемента.)
"""

def _merge(a, b):
    sorted_array = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            sorted_array.append(a[i])
            i += 1
        else:
            sorted_array.append(b[j])
            j += 1

    if i >= len(a):
        sorted_array += b[j:]
    elif j >= len(b):
        sorted_array += a[i:]

    return sorted_array


def merge_sort(array):
    if len(array) > 1:
        m = (len(array))//2
        l_array = merge_sort(array[:m])
        r_array = merge_sort(array[m:])
        return _merge(l_array, r_array)
    else:
        return array


def find_invariants(array):
    pass