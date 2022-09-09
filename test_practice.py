from my_practice import People, Coworker, Algoritms
import pytest


def test_get_person_info():
    person = People('andrey', 'male', 33)
    result = person.get_person_info()
    assert result == 'INFO:\nName: andrey\nSex: male\nAge: 33'


def test_estimate_sallary():
    person = Coworker('denshik ruslan', 'male', 40, 'engineer')
    result = person.estimate_sallary(23)
    expect = 14375.0
    assert result == expect


def test_estimate_sallary_bad():
    person = Coworker('denshik ruslan', 'male', 40, 'engineer')
    with pytest.raises(TypeError):
        result = person.estimate_sallary("23")


def test_binary_search():
    user = Algoritms('binary search')
    result = user.binary_search([1, 2, 3, 4, 5], 4)
    expected_result = 'Here is index of <4> --- 3!'
    assert result == expected_result


def test_binary_search_errors():
    user = Algoritms('binary search')
    with pytest.raises(TypeError):
        result = user.binary_search([1, 2, 3, 4, 5], "4")


def test_fast_sort():
    user = Algoritms('fast sort')
    result = user.fast_sort([10, 3, 1, 7, -2])
    expected_result = [-2, 1, 3, 7, 10]
    assert result == expected_result

def test_bubble_sort():
    user=Algoritms('bubble sort')
    result=user.bubble_sort([3,1,7,2,100])
    expected_result=[1,2,3,7,100]
    assert result==expected_result

def test_merge_sort():
    user=Algoritms('merge sort')
    result=user.merge_sort([1,3],[2,4])
    expected_result=[1,2,3,4]
    assert result==expected_result