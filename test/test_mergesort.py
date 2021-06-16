import pytest
from merge_sort import merge_sort, find_invariants

@pytest.mark.parametrize('array', [
    ([2, 3, 9, 2, 9]),
    ([1]),
    ([]),
    ([5,5,5,5,5]),
    ([3000, 1500, 500, 100, 4, 1])
])
def test_merge_sort(array):
    print("test mergesort")
    sorted_array = merge_sort(array)
    assert sorted_array == sorted(array)


@pytest.mark.parametrize('array, invariants', [
    ([2, 3, 9, 2, 9], 2),
])
def test_find_invariants(array, invariants):
    print("test invariants")
    
    inv = find_invariants(array)
    assert inv == invariants