def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
def main():
    print('Result is : ',end =' ')
    for i in range(100,1000):
        n1=i%10
        temp=i//10
        n2=temp%10
        temp//=10
        n3=temp%10
        sum=fact(n1)+fact(n2)+fact(n3)
        if(sum==i):
            print('     ',i)
main()