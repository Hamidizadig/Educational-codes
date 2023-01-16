s=input("Enter numbers : ")
numbers=s.split()
nums=[]
for i in numbers:
    nums.append(int(i))
values=bytearray(nums)
print('Result is : ',end="")
for x in values:print(x,end='\t')
