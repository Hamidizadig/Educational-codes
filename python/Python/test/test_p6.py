# import p6
# import pytest


# def test_sum():
#     assert p6.sum(23, 5) == 28


# def test_mul():
#     assert p6.mul(10, 2) == 20


# def test_search_to_list():
#     assert p6.search_to_list([10, 20, 30, 40, 50], 40) == [10, 20, 30, 40, 50]
#     assert p6.search_to_list(['sami', 'shasma', 'sipus'], 'kasfas') == False
# # pytest test_p5.py -m A


import p6
import pytest


def test_sum():
    assert p6.sum(23, 5) == 28


def test_mul():
    assert p6.mul(10, 2) == 20


def test_search_to_list():
    assert p6.search_to_list([10, 20, 30, 40, 50], 40) == [10, 20, 30, 40, 50]
    assert p6.search_to_list(['sami', 'shasma', 'sipus'], 'kasfas') == False
# pytest test_p5.py -m A
# test_p6.py --durations=3 --durations-min=1.0