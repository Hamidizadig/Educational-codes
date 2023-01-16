'''
L=[4,2,9]
x,y,z=L
print(x)
print(y)
'''
'''
start=0
def getSubString(str1):
    return str1[start]

str1="asdfghj"
itStr1=iter(lambda: getSubString(str1), ' ')
    
for item in itStr1:
        print(iter)
        start+=1
'''
'''
count=1
def Counter():
    return count
counter=iter(lambda:Counter(),31)
for i in counter:
    print(i)
    count+=1 
    '''
    
class TestIter:
    def __init__(self,list1):
        self.list1=list1
        self.itlist1=iter(self.list1)
        
    def __iter__(self):
        return self.itlist1

    def __call__(self):
        return next(self.itlist1)
'''
t1=TestIter([4,2,6,90.45])
iter1=iter(t1,90)
for i in iter1:
    print(i)    '''
    
t1=TestIter([4,2,6,90,45])
iter1=iter(t1)
for i in iter1:
    print(i) 