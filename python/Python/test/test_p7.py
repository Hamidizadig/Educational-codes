import p7
import pytest


@pytest.fixture
def ibput_value():
    list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    return list


def test_sum(input_value):
    assert p7.sum(10, 20) == input_value[2]
    assert p7.sum(45, 25) in input_value
    assert p7.sum(1, 9) == len(input_value)
