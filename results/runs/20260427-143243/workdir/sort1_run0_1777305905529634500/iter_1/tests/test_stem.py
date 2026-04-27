from source import Sort
import pytest

def test_selection_sort():
    assert Sort.selection_sort([]) == []
    assert Sort.selection_sort([1]) == [1]
    assert Sort.selection_sort([3, 2, 1]) == [1, 2, 3]
    assert Sort.selection_sort([1, 2, 3]) == [1, 2, 3]
    assert Sort.selection_sort([1, 3, 2]) == [1, 2, 3]
    assert Sort.selection_sort([2, 2, 2]) == [2, 2, 2]
    assert Sort.selection_sort([5, 3, 5, 2, 5]) == [2, 3, 5, 5, 5]

def test_insertion_sort():
    assert Sort.insertion_sort([]) == []
    assert Sort.insertion_sort([1]) == [1]
    assert Sort.insertion_sort([3, 2, 1]) == [1, 2, 3]
    assert Sort.insertion_sort([1, 2, 3]) == [1, 2, 3]
    assert Sort.insertion_sort([1, 3, 2]) == [1, 2, 3]
    assert Sort.insertion_sort([2, 2, 2]) == [2, 2, 2]
    assert Sort.insertion_sort([5, 3, 5, 2, 5]) == [2, 3, 5, 5, 5]

def test_merge_sort():
    assert Sort.merge_sort([]) == []
    assert Sort.merge_sort([1]) == [1]
    assert Sort.merge_sort([3, 2, 1]) == [1, 2, 3]
    assert Sort.merge_sort([1, 2, 3]) == [1, 2, 3]
    assert Sort.merge_sort([1, 3, 2]) == [1, 2, 3]
    assert Sort.merge_sort([2, 2, 2]) == [2, 2, 2]
    assert Sort.merge_sort([5, 3, 5, 2, 5]) == [2, 3, 5, 5, 5]
    assert Sort.merge_sort([1, 2, 3, 1, 2, 3]) == [1, 1, 2, 2, 3, 3]

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
    arr = [2, 2, 2]
    Sort.quick_sort(arr, 0, len(arr) - 1)
    assert arr == [2, 2, 2]
    arr = [5, 3, 5, 2, 5]
    Sort.quick_sort(arr, 0, len(arr) - 1)
    assert arr == [2, 3, 5, 5, 5]
    arr = [1, 2, 3, 1, 2, 3]
    Sort.quick_sort(arr, 0, len(arr) - 1)
    assert arr == [1, 1, 2, 2, 3, 3]

def test_selection_sort_edge_cases():
    assert Sort.selection_sort([1, 2, 2, 3, 3, 3]) == [1, 2, 2, 3, 3, 3]
    assert Sort.selection_sort([3, 3, 3, 3, 3]) == [3, 3, 3, 3, 3]

def test_insertion_sort_edge_cases():
    assert Sort.insertion_sort([1, 2, 2, 3, 3, 3]) == [1, 2, 2, 3, 3, 3]
    assert Sort.insertion_sort([3, 3, 3, 3, 3]) == [3, 3, 3, 3, 3]

def test_merge_sort_edge_cases():
    assert Sort.merge_sort([1, 2, 2, 3, 3, 3]) == [1, 2, 2, 3, 3, 3]
    assert Sort.merge_sort([3, 3, 3, 3, 3]) == [3, 3, 3, 3, 3]

def test_merge_with_duplicates():
    left = [1, 2, 2, 3]
    right = [2, 3, 4]
    assert Sort.merge(left, right) == [1, 2, 2, 2, 3, 3, 4]

def test_merge_sort_large_duplicates():
    assert Sort.merge_sort([5] * 1000) == [5] * 1000
    assert Sort.merge_sort([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1] * 10