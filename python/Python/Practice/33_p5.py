def incNumber(str1):                       #  '0000'
    list1=[ord(ch) for ch in str1]         #  [0,0,0,0]
    j=len(list1)-1
    while True:
        if list1[j]+1<ord('z')+1:
            break
        list1[j]=ord('a')
        j-=1
    list1[j]+=1
    list1=[chr(item) for item in list1]
    return ''.join(list1) 
    
def printNumber(str1):
    if(int!='zzz'):
       print(str1)    
       str1=incNumber(str1)                     #  '0001'+
       printNumber(str1)
       
printNumber('aaa')

