import numpy.matlib
import numpy as np
def rangeXY(i1,j1,n):
    if l1>n:
        l1=0
    if l1<0:
        l1=n
    if j1>n:
        j1=0
    if j1<0:
        j1=n
    return[i1,j1]
def fill_matrix(matrix,n):
    i=0
    n=n-1
    j=n//2
    matrix[i,j]=1
    for m in range(1,(n+1)*(n+1)):
        i1=i-1
        j1=j-1
        [i1,j1]=rangeXY(i1,j1,n)
        if matrix[i1,j1] !=0:
            i1=i+1
            j1=j
            [i1,j1]=rangeXY(i1,j1,n)
        matrix[i1,j1]=m+1
        i=i1; j=j1
def disp_matrix(matrix,n):
    for i in range(0,n):
        for j in range(0,n):
            if matrix[i,j]<10:
                print(" ",matrix[i,j],end='')
            elif matrix[i,j]<100:
                print("     ",matrix[i,j],end='')
            else:
                print(' ',matrix[i,j],end='')
        print()
def main():
    n=int(input('Enter n : '))
    matrix=np.matlib.zeros ((n,n))
    fill_matrix(matrix,n)
    disp_matrix(matrix,n)
    main()
    