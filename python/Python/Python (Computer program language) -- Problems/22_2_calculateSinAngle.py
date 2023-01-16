def fact (n):
    if n == 1:
        return 1.0
    else:
        return n * fact (n - 1)
def pow (x, n):
    if n == 0:
        return 1.0
    else:
        return x * pow (x, n - 1)
def main():
    sign = 1
    sum = 0
    x = float(input("Enter x:"))
    n = int (input ("Enter n:"))
    for i in range(1, n+1, 2):
        sum+=sign*pow(x,i)/fact(i)
        sign=-sign
    print('Sin(",X,")=',sum)
main()