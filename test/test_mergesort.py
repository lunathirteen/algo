
from merge_sort import merge_sort, find_invariants

def test_merge_sort_1():
    print("test mergesort")
    array = [2, 3, 9, 2, 9]
    sorted_array = merge_sort(array)
    assert sorted_array == sorted(array)

def test_merge_sort_2():
    print("test mergesort")
    array = [1]
    sorted_array = merge_sort(array)
    assert sorted_array == sorted(array)

def test_merge_sort_3():
    print("test mergesort")
    array = []
    sorted_array = merge_sort(array)
    assert sorted_array == sorted(array)

def test_merge_sort_4():
    print("test mergesort")
    array = [5,5,5,5,5]
    sorted_array = merge_sort(array)
    assert sorted_array == sorted(array)

def test_merge_sort_5():
    print("test mergesort")
    array = [3000, 1500, 500, 100, 4, 1]
    sorted_array = merge_sort(array)
    assert sorted_array == sorted(array)

def test_find_invariants_1():
    print("test invariants")
    array = [2, 3, 9, 2, 9]
    inv = find_invariants(array)
    assert inv == 2