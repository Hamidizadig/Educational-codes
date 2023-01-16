# def fun1():
#     x=10
#     yield x
#     yield x+2
#     yield x*5

# g=fun1()
# print(next(g))
# print(next(g))
# print(next(g))


# def fun1():
#     x=10
#     x=yield x
#     x=yield x+2
#     yield x*5
# g=fun1()
# print(next(g))
# print(g.send(25))
# print(g.send(1))


# def fun1():
#     while True:
#         x=yield 500
#         yield x*10
# g=fun1()
# print(next(g))
# print(g.send(15))
# print(g.send(3))


import random


def fun1():
    while True:
        x = yield
        print(x, end='\t')


def fun2(func):
    while True:
        r = random.randint(1, 100)
        func.send(r)
        yield


g1 = fun1()
g1.send(None)
g2 = fun2(g1)
next(g2)
next(g2)
next(g2)
next(g2)
next(g2)
