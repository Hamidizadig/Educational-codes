def multiply(numbers):
    total=1
    for x in numbers:
        total*=x
    return total
s=input('Enter numbers : ')
numbers = s.split()
nums=[]
for i in numbers: nums.append(int(i))
print('Multiply is : ',multiply(nums))