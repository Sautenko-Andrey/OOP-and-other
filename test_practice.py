from my_practice import People, Coworker
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
