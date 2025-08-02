import pytest
from practica.main import bubble_sort, merge_sort

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