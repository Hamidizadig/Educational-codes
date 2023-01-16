a=int(input('Inter nommber 1 : '))
b=int(input('Inter nommber 2 : '))
c=int(input('Inter nommber 3 : '))
if a>b:
    temp=a
    a=b
    b=temp
if a>c:
    temp=a
    a=c
    c=temp
if a>c:
    temp=a
    a=c
    c=temp
if b>c:
    temp=b
    b=c
    c=temp
print('Sorted is : ',a,b,c)