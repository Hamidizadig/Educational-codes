nums=[34,1,0,-23,7,-99,90,-88]
print('Original numbers in the list : ',nums)
new_nums = list(filter(lambda x: x>0,nums))
print('Positive numbers in the list : ',new_nums)