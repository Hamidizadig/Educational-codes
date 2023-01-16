# Formul : s=(1/x)-(1/(x+2x))  +5 Times
sPlusMinus=1
pow=1.0
sum=0.0
sum1=0.0
x=int(input('Enter x : '))
for i in range(1,11):
    pow=pow*x
    sum1=sum1+i*pow
    sum=sum+sPlusMinus*1.0/sum1
    s=-sPlusMinus
print("Sum is : ",sum)
    
