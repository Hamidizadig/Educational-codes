'''
l1=[4,8,2,6]
print(sum(l1))
print(min(l1))

l2=sorted(l1)
print(l1)
print(l2)
'''
'''
l=('r',"p",'s')
for i in enumerate(l):
    print(i)
'''

class Counter:
    def __init__(self,start,end):
        self.start=start
        self.end=end       
    def __iter__(self):
        return self
    
    def __next__(self):
        current=self.start
        if current>self.end:
            raise StopIteration
        self.start+=1
        return current 
counter1=Counter(0,20)  
for i in counter1:
    print(i)