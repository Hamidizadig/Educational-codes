from array import *
n=int(input('Enter n : '))
a=array('i',[])
j=0
for i in range (0,n):
    find=0
    num=int(input('Enter a['+str(i+1)+']:'))
    for j in range(0,i):
        if a[j]>num:           
            find=1
            break
    if find==1:
        a.insert(j,num)
    else:
        a.append(num)
print('Result is : ',end='')
for i in range(0,n):
    print(' ',a[i],end='')
     