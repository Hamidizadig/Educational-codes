def pow(x,n):
    if n==0:
        return 1
    else:
        return x*pow(x,n-1)
def main():
    print('Result is : ',end='')
    for i in range(1000,10000):
        n1=i % 10
        temp= i//10
        n2=temp % 10
        temp //=10        
        n3=temp % 10
        temp //=10
        n4=temp%10
        if(n1+pow(n4,4))==(n2*n2+pow(n3,3)):
            print('    ',i,end='')
main()