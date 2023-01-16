import pytest


# @pytest.mark.parametrize("num1,num2,res" [(10, 20, 30),
#                                           (1, 5, 6),
#                                           (2, 9, 11),
#                                           (0, 10, 10),
#                                           (-3, 5, 2)
#                                           ])
# def test_sum(num1, num2, res):
#     assert num1+num2 == res


class Person:
    def __init__(self, name, family, age):
        self.name = name
        self.family = family
        self.age = age


@pytest.mark.parametrize("person,l,a", [
    (Person('asam,simmas', 40)4, 20),
    (Person('ana,sira', 35)3, 18),
])
def test_fun(person, l, a):
    assert len(person.name) > l and (person.age >= a)
