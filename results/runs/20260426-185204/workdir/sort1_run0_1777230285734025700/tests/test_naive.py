import pytest
from source import Sort

class TestSort:

    def test_selection_sort(self):
        assert Sort.selection_sort([]) == []
        assert Sort.selection_sort([1]) == [1]
        assert Sort.selection_sort([3, 2, 1]) == [1, 2, 3]
        assert Sort.selection_sort([1, 2, 3]) == [1, 2, 3]
        assert Sort.selection_sort([3, 1, 2, 1]) == [1, 1, 2, 3]
        assert Sort.selection_sort([5, 5, 5]) == [5, 5, 5]

    def test_insertion_sort(self):
        assert Sort.insertion_sort([]) == []
        assert Sort.insertion_sort([1]) == [1]
        assert Sort.insertion_sort([3, 2, 1]) == [1, 2, 3]
        assert Sort.insertion_sort([1, 2, 3]) == [1, 2, 3]
        assert Sort.insertion_sort([3, 1, 2, 1]) == [1, 1, 2, 3]
        assert Sort.insertion_sort([5, 5, 5]) == [5, 5, 5]

    def test_merge_sort(self):
        assert Sort.merge_sort([]) == []
        assert Sort.merge_sort([1]) == [1]
        assert Sort.merge_sort([3, 2, 1]) == [1, 2, 3]
        assert Sort.merge_sort([1, 2, 3]) == [1, 2, 3]
        assert Sort.merge_sort([3, 1, 2, 1]) == [1, 1, 2, 3]
        assert Sort.merge_sort([5, 5, 5]) == [5, 5, 5]

    def test_quick_sort(self):
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
        arr = [3, 1, 2, 1]
        Sort.quick_sort(arr, 0, len(arr) - 1)
        assert arr == [1, 1, 2, 3]
        arr = [5, 5, 5]
        Sort.quick_sort(arr, 0, len(arr) - 1)
        assert arr == [5, 5, 5]