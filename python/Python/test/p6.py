# import p6


# class TestCode:
#     def test_sum(self):
#         assert p6.sum(23, 5) == 28

#     def test_mul(self):
#         assert p6.mul(10, 2) == 20

#     def test_search_to_list(self):
#         assert p6.search_to_list([10, 20, 30, 40, 50], 40) == [
#             10, 20, 30, 40, 50]
#         assert p6.search_to_list(
#             ['sami', 'shasma', 'sipus'], 'kasfas') == False


# class TestCode2:
#     def test_mul(self):
#         assert p6.mul(200, 4) == 800


import p6
import pytest


class TestCode:
    @pytest.mark.A
    def test_sum(self):
        assert p6.sum(23, 5) == 28

    @pytest.mark.B
    def test_mul(self):
        assert p6.mul(10, 2) == 20

    @pytest.mark.A
    def test_search_to_list(self):
        assert p6.search_to_list([10, 20, 30, 40, 50], 40) == [
            10, 20, 30, 40, 50]
        assert p6.search_to_list(
            ['sami', 'shasma', 'sipus'], 'kasfas') == False


class TestCode2:
    @pytest.mark.A
    def test_mul(self):
        assert p6.mul(200, 4) == 800
