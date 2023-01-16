# def fun(n):
#     if n==0:
#         return 1
#     else:
#         return fun(n-1)+3
# print(fun(4))


# def mul(n,m):
#     if n==0:
#         return 0
#     return m+mul(n-1,m)
# print(mul(4,8))


# def fib(n):
#     if n==1 or n==2:
#         return 1
#     return fib(n-1)+fib(n-2)
# for i in range(1,20):
#     print(fib(i) ,end='\t')


# def printl(l1):
#     if len (l1)==0:
#         print (end="")
#     else:
#         print(l1[0])
#         printl(l[1:])

# l1=[1,2,3,4]
# printl(l1)


def printl(l1):
    if len(l1) == 0:
        print(end="")
    else:
        printl(l1[1:])
        print(l1[0:])


l1 = [1, 2, 3, 4]
printl(l1)
