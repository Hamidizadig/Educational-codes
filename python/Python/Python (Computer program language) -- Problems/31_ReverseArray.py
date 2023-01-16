from array import *


def input1(a, n):
    for i in range(0, n):
        a.append(int(input('Enter a['+str(i+1)+']:')))


def convert(a, n):
    for i in range(0, n//2):
        temp = a[i]
        a[i] = a[n-i-1]
        a[n-i-1] = temp


def print1(a, n):
    for i in range(0, n):
        print(' ', a[i], end='')


def main():
    n = int(input('Enter n : '))
    num = array('i', [])
    input1(num, n)
    print('Input is ', end='')
    print1(num, n)
    convert(num, n)
    print('\nOnvert is ', end='')
    print1(num, n)


main()
