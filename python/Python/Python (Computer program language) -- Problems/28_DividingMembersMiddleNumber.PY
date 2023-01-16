from array import *
def action(a,loc,n):
    for i in range(0,n):
        print(a[i],'/',a[loc],'=',a[i]/a[loc])
def main():
        sign=1
        a=array('i',[])
        n=int(input('Enter n : '))
        mid=n//2
        for i in range(0,n):
            a.append(int(input('Enter a['+str(i+1)+']:')))
        j=0
        for i in range(0,mid+1):
            if a[mid+(sign*j)]!=0:
                action(a,mid+(sign*j),n)
                return
            if sign==1:
                j=j+1
                sign=-sign
        print('All elements are 0 ')
main()    
        