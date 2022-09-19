from my_practice import Algoritms, BinarySearch, FastSort, BFS, BubbleSort, MergeSort
import pytest

def test_binary_algorithm():
    result=BinarySearch('binary_search')
    result=result.execute([1,5,8,90,100],8)
    relevant='We have found this number! It\'s index = 2'
    assert result==relevant

def test_fast_sort():
    result=FastSort('fast_sort')
    result=result.execute([3,1,79,34,0])
    relevant=[0,1,3,34,79]
    assert result==relevant

def test_bubble_sort():
    result=BubbleSort('bubble_sort')
    result=result.execute([6,11,-19,0,100])
    relevant=[-19,0,6,11,100]
    assert result==relevant

def test_merge_sort():
    result=MergeSort('merge_sort')
    result=result.execut([1,3,5,7,9],[2,4,6,8,110,120])
    relevant=[1,2,3,4,5,6,7,8,9,110,120]
    assert result==relevant


