import p4


def test_sum():
    assert p4.sum(10, 20) == 30
    assert p4.sum(0, 100) == 100
    assert p4.sum(-3, 5) == 2
    assert p4.sum(1, 8) == 9
    assert p4.sum(1000, 8) == 1008


def test_mul():
    assert p4.mul(10, 2) == 20


def test_search_to_list():
    assert p4.search_to_list([10, 20, 30, 40, 50]) == [10, 20, 30, 40, 50]
    assert p4.search_to_list(['sami', 'shasma', 'sipus'], 'kasfas') == False
