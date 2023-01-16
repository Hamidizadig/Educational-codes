'''
def mainFun(func):
    def fun1():
        print("********************")
        func()
        print("#####################")
    return fun1

def printName():
    print("mehdi")

k=mainFun(printName)
k()
'''
'''
def mainFun(func):
    def fun1():
        for i in range(8):
            func()
    return fun1
               
def printStar():
    print("***********************")

myFunction=mainFun(printStar)
myFunction()
'''
'''
def mainFun(func):
    def fun1():
        print("##################")
        for i in range(6):
            func()
        print("##################")
    return fun1

@mainFun
def printStar():
    print("*************************")
    

printStar()
'''
'''
def mainFun(func):
    def fun1(*args,**kwargs):
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print(f"{func(*args,**kwargs)}")
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    return fun1
        
@mainFun       
def sum(x,y):
    return x+y

@mainFun
def mul(x,y,z,k):
    return x*y*z*k

sum(23,4)
mul(4,8,5,1)
'''


def decor1(func):
    def fun1():
        x = func()
        return x*x
    return fun1


def decor2(func):
    def fun1():
        x = func()
        return x*2
    return fun1


def decor3(func):
    def func1():
        x = func()
        return x+5
    return func1


@decor1
@decor2
@decor3
def myFunction():
    return 20


print(myFunction())
