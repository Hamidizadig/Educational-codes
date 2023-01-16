# def fun1(n):
#     return n*n*n
# list1=[1,5,3]
# print(list(map(fun1.list1)))


# def fun1(n):
#     return n*n*n
# list1=[1,5,3]
# list2=list(map(lambda x:x+100,list1))
# print(list2


# l1=[2,3,5]
# l2=list(map(print,l1))


# a=[12,18.25,19]
# b=[11.5,16,18]
# def getAvg(*args):
#     return sum(args)/len(args)
# print(list(map(getAvg,a,b)))


# def fun1(n):
#     return n%3==0
# l1=[5,9,8,6,2,4,12,9,3]
# print(list(filter(fun1,l1)))


# def fun1(n):
#     return n%3==0
# l1=[5,9,8,6,2,4,12,9,3]
# print(list(filter(lambda x :x>10,l1)))


# l1=['s','2','1.75','True','5z','-9']
# print(list(filter(lambda x:x.isnumeric(),l1)))
# print(list(filter(lambda x:x.isalpha(),l1)))


# l1=[57,95,4,46,23788,25,48,8784,45,7,54]
# print(list(filter(lambda x:str(x).find('7')!=-1,l1)))


# from functools import reduce
# def add(x,y):
#     return x+y
# l1=[5,8,3,9]
# print(reduce(add,l1))


from functools import reduce


def add(x, y):
    return x+y


def mul(x, y):
    return x*y


l1 = [5, 8, 3, 9]
print(reduce(add, l1))
print(reduce(mul, l1))
print(reduce(lambda x, y: x-y, l1))
