def repeat(n,m):
    count=0
    while n>0:
        if (n%10)==m:
            count=count+1
            n//=10
    return count
def main():
    n=int(input('Enter nomber : '))
    m=int(input('Enter Search nomber : '))
    print(m,'Repeat ' ,repeat(n,m),'times ')
main()