def incNumber(str1):                       #  '0000'
    list1=[int(ch) for ch in str1]         #  [0,0,0,0]
    j=len(list1)-1
    while True:
        if list1[j]+1<10:
            break
        list1[j]=0
        j-=1
    list1[j]+=1
    list1=[str(item) for item in list1]
    return ''.join(list1) 
    
def printNumber(str1):
    if(str1!='444'):
       print(str1)    
       str1=incNumber(str1)                     #  '0001'+
       printNumber(str1)
       
printNumber('0000')

