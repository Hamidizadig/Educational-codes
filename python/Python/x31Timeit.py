from random import random
import timeit
# startTime=timeit.default_timer()
# print()
# x=300*9000*1000000
# endTime=timeit.default_timer()
# print(endTime-startTime)


# print(timeit.timeit('x=3*100+500'))


# print(timeit.timeit(stmt='x=3*100+500'))


# print(timeit.timeit(setup='y=2000;z=400;', stmt='x=3*y+z'))

# codeSetup='import random'
# myCode='''
# def fun():
#     l1=[]
#     for i in range(500):
#         l1.append(random.rand(1,100))
# '''
# print(timeit.timeit(setup=codeSetup , stmt=myCode))
# print(timeit.timeit(setup=codeSetup , stmt=myCode,number=10))


codeSetup = 'import random'
myCode = '''
def fun():
    l1=[]
    for i in range(500):
        l1.append(random.rand(1,100))
'''
print(timeit.repeat(setup=codeSetup, stmt=myCode, number=10))
print(timeit.repeat(setup=codeSetup, stmt=myCode, number=10))
