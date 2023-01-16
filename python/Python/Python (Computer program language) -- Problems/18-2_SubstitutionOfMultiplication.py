while True:
    sum=0
    x=int(input("Enter x : "))
    y=int(input("Enter y : "))
    if(x==0 and y==0):
        break
    temp =y
    if(y<0):
        temp=-y
    for i in range(1,temp+1):
        sum=sum+x
    if (y<0):
        sum=-sum
    print(x,"*",y,"=",sum) 
           