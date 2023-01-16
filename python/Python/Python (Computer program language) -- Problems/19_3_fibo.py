def fibo(n):
    if (n == 1):
        return (1)
    if (n == 2):
        return (1)
    return(fibo(n-2)+fibo(n-1))

def main():
    n = int(input('Enter Nomber :'))
    print('Result is :')
    for i in range(1, n+1):
        print(fibo(i), end="    ")
main()