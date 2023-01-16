while True:
    num=int(input('Enter a number : '))
    sum=0
    for i in range (1,num):
        if (num%i==0):
            sum+=i
    if (sum==num):
        print('\t','Prefect')
    else:
        print('\t','not Prefect')
    yes=input('Continue ?')
    if(yes[0]=='N'or yes[0]=='n'):
        break