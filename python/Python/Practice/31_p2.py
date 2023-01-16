def pack1(**kwargs):
    print(kwargs)

def unpack2(name,age,job):
    print(name)
    pack1(name=name,age=age,job=job)
    
def unpack1(person1,person2,person3):
    unpack2(*person1)
    unpack2(*person2)
    unpack2(*person3)

list1=[
       ('sishap',18,'Teacher'),
       ('misart',43,'Employee'),
       ('haspox',37,'Manager')
       ]
unpack1(*list1)



print('_'*50)




def f(*args):#1: packing
    sum=0
    for i in args:#2: unpacking
        sum+=i
    print(sum)
    
f(5,5)
f(5,3,9,87,2,5,5,84,8)
f(555,8.35,0.58)
f(65,2,5,8,5)
f()