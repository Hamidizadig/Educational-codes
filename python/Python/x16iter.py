'''
l1=[2,5,8]
it_l1=iter(l1)
printnext(it_l1)
'''
'''
a='asdfg'
it_a=iter(a)
while True:
    try:
        print(next(it_a))
    except:
        break
'''
'''
list1=[3,5,2]
for i in list1:
    print(i,end='\t')

itList1=iter(list1)
for i in range(len(list1)):
    print(next(itList1))
'''
'''
def checkIterable(obj):
    try:
        iter(obj)
    except:
        return False
    return
x=45
y=1.45
f=True
s='dfghjk'
a=['fef','wefew',5,8]
k=[5,2,3]
print(checkIterable(x))
print(checkIterable(y))
print(checkIterable(f))
print(checkIterable(s))
print(checkIterable(a))
print(checkIterable(k))
'''

def checkIterable(obj):
    try:
        iter(obj)
        return True
    except:
        return False
class Person:
    def __init__(self,name ,age):
        self.name=name
        self.age=age
        
    def __str__(self) -> str:
        return f"{self.name}\t{self.age}"
p1=Person("ana",40)
p2=Person("sanas",30)
p3=Person("ashsi",12)
    
people=[p1,p2,p3]
itPeople=iter(people)
print(next(itPeople))
print(next(itPeople))
print(next(itPeople))