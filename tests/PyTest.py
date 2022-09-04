from calc import division
import pytest


@pytest.mark.parametrize(x,y,expected_result,[(10,2,5),(20,5,4),(100,10,10),(5,2,2.5)])
def test_division_good(x,y,expected_result):
    assert division(x,y)==expected_result



