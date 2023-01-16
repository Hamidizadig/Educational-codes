from array import *
def main():
    table = array('i',[1000,2000,3000,4000,5000,8000,10000,20000,30000,50000])
    sum=0
    while True:
        number = int(input('Enter number : '))
        if number==-999:
            break
        n=int(input('Enter n : '))
        sum=0.0
        i=1
        while i<=n:
            code = int(input('Enter code : '+str(i)+':'))
            if code >=0 and code <10:
                sum+=table[code]
            else:
                print('Enter code between 0 to 9 ')
                continue
            i=i+1
        print('*** Number is ',number,"   Sum is ",sum)
main()