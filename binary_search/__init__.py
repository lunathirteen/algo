"""
В первой строке даны целое число 1≤n≤10^5
и массив A[1…n] из n различных натуральных чисел,
не превышающих 10^9, в порядке возрастания,
во второй — целое число 1≤k≤10^5 и
k натуральных чисел b1,…,bk, не превышающих 10^9.

Для каждого i от 1 до k необходимо вывести индекс 1≤j≤n,
для которого A[j]=bi, или −1, если такого j нет.
"""


def binary_search(array, element):
    """Function searches element in array using binary search algorithm"""
    left = 1
    right = len(array)

    while left <= right:
        m = (left+right) // 2
        if array[m-1] == element:
            return m
        elif array[m-1] > element:
            right = m - 1
        else:
            left = m + 1
    return -1


if __name__ == "__main__":
    input_string = input().split()
    n = input_string.pop(0)
    array = [int(el) for el in input_string]

    input_string = input().split()
    n = input_string.pop(0)

    idx = []
    for el in input_string:
        idx.append(binary_search(array, int(el)))

    print(" ".join([str(i) for i in idx]))
