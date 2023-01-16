pow=10
sum=0
num=int(input('Enter Number : '))
temp=num
while temp > 0:
    sum=(pow*sum)+temp%10
    temp=temp//10
if(sum==num):
    print('Yes')
else:
    print('No')
    