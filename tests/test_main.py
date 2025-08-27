import pytest
from src.main import bubble_sort, merge_sort, quick_sort, heap_sort

def test_bubble_sort():
    assert bubble_sort([5, 2, 9, 1, 5, 6]) == [1, 2, 5, 5, 6, 9]
    assert bubble_sort([3, 0, 2, 5, -1, 4, 1]) == [-1, 0, 1, 2, 3, 4, 5]
    assert bubble_sort([]) == []
    assert bubble_sort([1]) == [1]

def test_merge_sort():
    assert merge_sort([5, 2, 9, 1, 5, 6]) == [1, 2, 5, 5, 6, 9]
    assert merge_sort([3, 0, 2, 5, -1, 4, 1]) == [-1, 0, 1, 2, 3, 4, 5]
    assert merge_sort([]) == []
    assert merge_sort([1]) == [1]

def test_quick_sort():
    assert quick_sort([5, 2, 9, 1, 5, 6]) == [1, 2, 5, 5, 6, 9]
    assert quick_sort([3, 0, 2, 5, -1, 4, 1]) == [-1, 0, 1, 2, 3, 4, 5]
    assert quick_sort([]) == []
    assert quick_sort([1]) == [1]
    # Test con duplicados
    assert quick_sort([4, 4, 4, 3, 3, 2, 1]) == [1, 2, 3, 3, 4, 4, 4]

def test_heap_sort():
    assert heap_sort([5, 2, 9, 1, 5, 6]) == [1, 2, 5, 5, 6, 9]
    assert heap_sort([3, 0, 2, 5, -1, 4, 1]) == [-1, 0, 1, 2, 3, 4, 5]
    assert heap_sort([]) == []
    assert heap_sort([1]) == [1]
    # Test con duplicados
    assert heap_sort([4, 4, 4, 3, 3, 2, 1]) == [1, 2, 3, 3, 4, 4, 4]