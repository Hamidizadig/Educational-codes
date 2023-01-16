'''
l=[x for x in range(1,100)]
print(l)
for i in l :
    print(i)
'''
'''
obj1=(x for x in range(1,100))
print(obj1)
for i in obj1:
    print(i,end="\t")
#lazy
'''
'''
def fib(n):
    a=0
    b=1
    yield b
    for i in range(1,n):
        a,b=b,a+b
        yield b
        
for item in fib(25):
    print(item,end='\t')
'''

def f():
    x=20
    yield x
    x+=6
    yield x
    x*=10
    yield x
    x=9999
    
ob1=f()
for item in ob1:
    print(item)