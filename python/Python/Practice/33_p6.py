# def fun1(n):
#     return n+1

# map(fun1,[10,24,78,56])

names = ['suirix', 'shixkop', 'askifix', 'shahyas',
         'sssssssssssssssssssssssssssssssssssssssssssss']

list2 = [[ch for ch in item if ch != 's']for item in list(map(list, names))]
print(list2)
