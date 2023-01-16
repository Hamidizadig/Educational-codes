# x=1
# def fun ():
#     x=0
#     print(f"X is: {x}")

# x+=5
# fun()
# print(f'x : {x}')


# x=1
# def fun ():
#     x=0
#     print(f"X is: {x}")

# x+=5
# fun()
# print(f'x : {x}')


# # errors:
# def fun1():
#     print(f'x : {x}')
#     x=20
# x=50
# def fun1()
# print(f'x is : {x}')


# x=1
# def fun1():
#     print{f'x is : {x}'}
#     x=20
# fun1()
# print(f'x is : {x}')


x = 1


def fun1():
    global x
    x = 20
    print(f'x is : {x}')


def fun2():
    global x
    x *= 4
    print(x)


def fun3():
    x = 450
    print(x)


fun1()
fun2()
fun3()
print(f'x is : {x}')
