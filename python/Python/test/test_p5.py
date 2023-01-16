import p5
import pytest


@pytest.mark.A
def test_sum():
    assert p5.sum(23, 5) == 28


@pytest.mark.B
def test_mul():
    assert p5.mul(10, 2) == 20


@pytest.mark.A
def test_search_to_list():
    assert p5.search_to_list([10, 20, 30, 40, 50], 40) == [10, 20, 30, 40, 50]
    assert p5.search_to_list(['sami', 'shasma', 'sipus'], 'kasfas') == False
# pytest test_p5.py -m A