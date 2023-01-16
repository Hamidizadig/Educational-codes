'''
def f(name):
    return "shasam"+name
print(f(" izad"))

f2=f
print(f2(" sarax"))
'''
'''
def fun1(text):
    return "*"+text+"#"

def fun2(text):
    str1=""
    for i in range (5):
        str1+=text
    return str1

def mainFun(func):
    print(func(" schax "))
    print("---------")
    
    
mainFun(fun1)
mainFun(fun2)
'''
'''
def fun1(text):
    return "*"+text+"#"

def fun2(text):
    str1=""
    for i in range (5):
        str1+=text
    return str1

def mainFun(funcA,funB,name):
    print(funcA(name))
    print("---------")
    print(funcB(name))
    
mainFun(fun1,fun2,"masx")
'''
'''
def mainFun(name):
    def fun1():
        print(name)
    print("------------------------")
    return fun1

k=mainFun("mehdi")
k()
'''

def calcFun(n):
    def sum(x,y):
        return(x+y)
    def sub(x,y):
        return(x-y)
    def mul(x,y):
        return(x*y)
    def div(x,y):
        return(x/y)
    if n==1:
        return sum
    elif n==2:
        return sub
    elif n==3:
        return mul
    elif n==4:
        return div
for i in range(1,5):
    k=calcFun(i)
    print(k(20,5))