from source import Sort
import pytest

def test_selection_sort():
    assert Sort.selection_sort([]) == []
    assert Sort.selection_sort([1]) == [1]
    assert Sort.selection_sort([3, 2, 1]) == [1, 2, 3]
    assert Sort.selection_sort([1, 2, 3]) == [1, 2, 3]
    assert Sort.selection_sort([1, 3, 2]) == [1, 2, 3]
    assert Sort.selection_sort([2, 2, 1, 1]) == [1, 1, 2, 2]
    assert Sort.selection_sort([5, 3, 5, 2, 5]) == [2, 3, 5, 5, 5]
    assert Sort.selection_sort([1, 2, 2, 1]) == [1, 1, 2, 2]
    assert Sort.selection_sort([1, 1, 1]) == [1, 1, 1]
    assert Sort.selection_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_insertion_sort():
    assert Sort.insertion_sort([]) == []
    assert Sort.insertion_sort([1]) == [1]
    assert Sort.insertion_sort([3, 2, 1]) == [1, 2, 3]
    assert Sort.insertion_sort([1, 2, 3]) == [1, 2, 3]
    assert Sort.insertion_sort([1, 3, 2]) == [1, 2, 3]
    assert Sort.insertion_sort([2, 2, 1, 1]) == [1, 1, 2, 2]
    assert Sort.insertion_sort([5, 3, 5, 2, 5]) == [2, 3, 5, 5, 5]
    assert Sort.insertion_sort([1, 2, 2, 1]) == [1, 1, 2, 2]
    assert Sort.insertion_sort([1, 1, 1]) == [1, 1, 1]
    assert Sort.insertion_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_merge_sort():
    assert Sort.merge_sort([]) == []
    assert Sort.merge_sort([1]) == [1]
    assert Sort.merge_sort([3, 2, 1]) == [1, 2, 3]
    assert Sort.merge_sort([1, 2, 3]) == [1, 2, 3]
    assert Sort.merge_sort([1, 3, 2]) == [1, 2, 3]
    assert Sort.merge_sort([2, 2, 1, 1]) == [1, 1, 2, 2]
    assert Sort.merge_sort([5, 3, 5, 2, 5]) == [2, 3, 5, 5, 5]
    assert Sort.merge_sort([1, 2, 2, 1]) == [1, 1, 2, 2]
    assert Sort.merge_sort([1, 1, 1]) == [1, 1, 1]
    assert Sort.merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_merge():
    assert Sort.merge([], []) == []
    assert Sort.merge([1], []) == [1]
    assert Sort.merge([], [1]) == [1]
    assert Sort.merge([1], [2]) == [1, 2]
    assert Sort.merge([2], [1]) == [1, 2]
    assert Sort.merge([1, 3], [2]) == [1, 2, 3]
    assert Sort.merge([1], [1]) == [1, 1]
    assert Sort.merge([1, 1], [1, 1]) == [1, 1, 1, 1]
    assert Sort.merge([1, 2, 3], [4, 5]) == [1, 2, 3, 4, 5]

def test_quick_sort():
    arr = []
    Sort.quick_sort(arr, 0, len(arr) - 1)
    assert arr == []
    arr = [1]
    Sort.quick_sort(arr, 0, len(arr) - 1)
    assert arr == [1]
    arr = [3, 2, 1]
    Sort.quick_sort(arr, 0, len(arr) - 1)
    assert arr == [1, 2, 3]
    arr = [1, 2, 3]
    Sort.quick_sort(arr, 0, len(arr) - 1)
    assert arr == [1, 2, 3]
    arr = [1, 3, 2]
    Sort.quick_sort(arr, 0, len(arr) - 1)
    assert arr == [1, 2, 3]
    arr = [2, 2, 1, 1]
    Sort.quick_sort(arr, 0, len(arr) - 1)
    assert arr == [1, 1, 2, 2]
    arr = [5, 3, 5, 2, 5]
    Sort.quick_sort(arr, 0, len(arr) - 1)
    assert arr == [2, 3, 5, 5, 5]
    arr = [1, 2, 2, 1]
    Sort.quick_sort(arr, 0, len(arr) - 1)
    assert arr == [1, 1, 2, 2]
    arr = [1, 1, 1]
    Sort.quick_sort(arr, 0, len(arr) - 1)
    assert arr == [1, 1, 1]
    arr = [1, 2, 3, 4, 5]
    Sort.quick_sort(arr, 0, len(arr) - 1)
    assert arr == [1, 2, 3, 4, 5]

def test_selection_sort_performance():
    large_input = list(range(1000, 0, -1))
    assert Sort.selection_sort(large_input) == list(range(1, 1001))

def test_insertion_sort_performance():
    large_input = list(range(1000, 0, -1))
    assert Sort.insertion_sort(large_input) == list(range(1, 1001))

def test_merge_sort_performance():
    large_input = list(range(1000, 0, -1))
    assert Sort.merge_sort(large_input) == list(range(1, 1001))

def test_merge_sort_stability():
    assert Sort.merge_sort([1, 2, 2, 1]) == [1, 1, 2, 2]

def test_quick_sort_stability():
    arr = [1, 2, 2, 1]
    Sort.quick_sort(arr, 0, len(arr) - 1)
    assert arr == [1, 1, 2, 2]

def test_partition_edge_case():
    arr = [1, 2, 3]
    pivot_index = Sort.partition(arr, 0, len(arr) - 1)
    assert arr[pivot_index] == 3
    assert arr == [1, 2, 3]

def test_merge_edge_case():
    assert Sort.merge([1, 2, 3], [1, 2, 3]) == [1, 1, 2, 2, 3, 3]
    assert Sort.merge([1, 1, 1], [2, 2, 2]) == [1, 1, 1, 2, 2, 2]

def test_selection_sort_with_greater_than():
    assert Sort.selection_sort([3, 2, 1]) == [1, 2, 3]
    assert Sort.selection_sort([1, 2, 3]) == [1, 2, 3]

def test_insertion_sort_with_greater_than():
    assert Sort.insertion_sort([3, 2, 1]) == [1, 2, 3]
    assert Sort.insertion_sort([1, 2, 3]) == [1, 2, 3]

def test_merge_sort_with_greater_than():
    assert Sort.merge_sort([3, 2, 1]) == [1, 2, 3]
    assert Sort.merge_sort([1, 2, 3]) == [1, 2, 3]

def test_quick_sort_with_equal_elements():
    arr = [1, 1, 1]
    Sort.quick_sort(arr, 0, len(arr) - 1)
    assert arr == [1, 1, 1]

def test_partition_with_equal_elements():
    arr = [1, 1, 1]
    pivot_index = Sort.partition(arr, 0, len(arr) - 1)
    assert arr[pivot_index] == 1
    assert arr == [1, 1, 1]