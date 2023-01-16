from array import *
def readArray (id,n):
    for i in range(0,n):
        id.append(int(input('Enter ID['+str(i+1)+']')))
def select_sort (id,n):
    for i in range(0,n):
        max=i
        for j in range(i+1,n):
            if id[max] > id[j]:
                max=j
        temp=id[i]
        id[i]=id[max]
        id[max]=temp
def writeArray(id,n):
    print('Sorted output : ',end='')
    for i in range(0,n):
        print(' ',id[i],end='')
def main():
    id=array('i',[])
    n=int(input('Enter n :'))
    readArray(id,n) 
    select_sort(id,n)
    writeArray(id,n)
main()    