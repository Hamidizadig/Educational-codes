# l=[1,8,3,7]
# print(l)

# l=[1,8,[4,2,5,8],3,7]
# print(l)
# print(*l)

# def f1(*args):
#     for i in args:
#         print(i)
# f(9,8,5)

# def f(a,b,c):
#     print(a,b,c)
# l=[2,5,8]
# f(*l)

# def f(**kwargs):
#     for key in kwargs:
#         print(key,kwargs[key])
# f(x=10,y=55,z=45)

# def f2(a,b,c):
#     print(a,b,c)
# def f1(*args):
#     l1=list(args)
#     l1[0]="sr"
#     l1[1]='ff'
#     f2(*l1)
#     pass
# f1('a','b','c')


# def fun(z,s):
#     print(z)
#     print(s)

# dic1={'z':1,'s':2}
# fun(**dic1)


def f2(x, y, z):
    print(x, y, z)


def f(*args):
    list1 = list(args)
    list1[2] = 0
    f2(*list1)
    pass


f(180, 180, 180)
