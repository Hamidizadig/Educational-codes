from functools import reduce
s= input('Enter numbers : ')
numbers=s.split()
nums=[]
for i in numbers:
    nums.append(int(i))
nums_product=reduce((lambda x,y:x*y),nums)
print('product numbers : ',nums_product)