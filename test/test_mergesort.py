import pytest
from merge_sort import merge_sort, merge_sort_inv


@pytest.mark.parametrize('array', [
    ([2, 3, 9, 2, 9]),
    ([1]),
    ([]),
    ([5, 5, 5, 5, 5]),
    ([3000, 1500, 500, 100, 4, 1])
])
def test_merge_sort(array):
    print("test mergesort")
    sorted_array = merge_sort(array)
    assert sorted_array == sorted(array)


@pytest.mark.parametrize('array, invariants', [
    ([2, 3, 9, 2, 9], 2),
    ([1, 7, 4, 3], 3),
    ([7, 6, 5, 4, 3, 2, 1], 21),
    ([1, 2, 3, 5, 4], 1),
])
def test_merge_sort_inv(array, invariants):
    print("test invariants")

    inv_counts = merge_sort_inv(array)
    assert inv_counts == invariants
