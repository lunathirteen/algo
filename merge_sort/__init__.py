"""
Первая строка содержит число 1≤n≤10^5,
вторая — массив A[1…n], содержащий натуральные числа, не превосходящие 10^9.
Необходимо посчитать число пар индексов 1≤i<j≤n, для которых A[i]>A[j].
Такая пара элементов называется инверсией массива
Количество инверсий в массиве является в некотором смысле его мерой неупорядоченности:
например, в упорядоченном по неубыванию массиве инверсий нет вообще,
а в массиве, упорядоченном по убыванию, инверсию образуют каждые два элемента.)
"""


def merge_sort(array):
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


def _merge(l_array, r_array):
    sorted_array = []
    i = 0
    j = 0
    while i < len(l_array) and j < len(r_array):
        if l_array[i] <= r_array[j]:
            sorted_array.append(l_array[i])
            i += 1
        else:
            sorted_array.append(r_array[j])
            j += 1

    if i >= len(l_array):
        sorted_array += r_array[j:]
    elif j >= len(r_array):
        sorted_array += l_array[i:]

    return sorted_array


def merge_sort_inv(array, invariants=0):

    if len(array) > 1:
        m = (len(array)) // 2

        l_array = array[:m]
        r_array = array[m:]
        invariants += merge_sort_inv(l_array, invariants)
        invariants += merge_sort_inv(r_array, invariants)
        i = 0
        j = 0
        k = 0
        while i < len(l_array) and j < len(r_array):
            if l_array[i] <= r_array[j]:
                array[k] = l_array[i]
                i += 1
            else:
                array[k] = r_array[j]
                invariants += 1
                j += 1
            k += 1

        if i >= len(l_array):
            array[k:] = r_array[j:]
        elif j >= len(r_array):
            array[k:] = l_array[i:]
