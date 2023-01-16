import numpy as np
import random
import numpy.matlib
def createRandom(arr,n,m):
    for i in range(0,n):
        for j in range(0,m):
            arr[i,j]=random.randint(0,20)
    return arr
def printArray(arr,n,m):
    for i in range(0,n):
        for j in range(0,m):
            print(arr[i,j],end='\t')
        print()
def main():
    n=m=3
    a=np.matlib.empty((n,m),dtype='i')
    a=createRandom(a,n,m)
    printArray(a,n,m)
    print('=====================')
    print('sum is ',np.sum(a))
    print('Average is ', np.average(a))
    print('Max rows are ',np.amax(a,axis=1))
    print('Mix cloums are', np.amin(a,axin=0))
main()
