# def sum(num1,num2,num3):
#     """

#     Args:
#         num1 (_type_): _description_
#         num2 (_type_): _description_
#         num3 (_type_): _description_

#     Returns:
#         _type_: _description_
#     """

#     return num1+num2+num3


# def sum(num1,num2,num3):
#     """
#     >>> sum(10,20,30)
#     60
#     >>> sum(0,10,0)
#     10
#     >>>sum(0,0,0)
#     10
#     >>>sum(-7,2,3)
#     -2
#     """

#     return num1+num2+num3

# import doctest
# doctest.testmod


def fun(list1):
    """_summary_

    Args:
        list1 (_type_): _description_
    REturns:
        _type_: _description_
    >>> fun([1,2,3])
    6
    >>> fun([10,20,30,40])
    240000
    >>> fun([1,0,34,6,4,64,654,684,65,655,4,48])
    0
    >>> fun([2,-4,5])
    -40

        """
    f = 1
    for item in list1:
        f*= item
    return f
