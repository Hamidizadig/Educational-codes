# 5!=1*2*3*4*5=120
# 6!=1*2*3*4*5*6

# def fun1():
#     value=yield 120
# send(6)

# --------------------------


# def fact(n):
#     f=1
#     for i in range(1,n+1):
#         f*=i
#     return f
# for i in range(1,20):
#     print(fact(i))

# --------------------------

def fun1():
    fact = 1
    value = None
    while True:
        value = yield fact
        fact *= value


g1 = fun1()
next(g1)
for i in range(1, 20):
    print(g1.send(i))
