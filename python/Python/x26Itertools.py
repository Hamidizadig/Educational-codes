import itertools

l = [2, 9, 4, 5, 5, 98, 8, 5, 5, 5, 5, 55, ]
print(l(itertools.islice(l, 2, 8, 2)))

# l=[2,9,4,5,5,98,8,5,5,5,5,55,]
# print(list(itertools.filterfalse(lambda x: x%2==0,l)))


# l=[2,9,4,5,5,98,8,5,5,5,5,55,]
# print(list(itertools.takewhile(lambda x: x%2==0,l)))


# l=[2,9,4,5,5,98,8,5,5,5,5,55,]
# print(list(itertools.dropwhile(lambda x: x%2==0,l)))


# print(list(itertools.compress("shahaz",[1,0,1,0,0,0])))


# l1=[1,2,3]
# l2=['a','b','c']
# l3=[12,True]
# l4=[True,False,True]
# mainlist=[l1,l2,l3,l4]
# print(mainlist)
# chainlist=list(itertools.chain.from_iterable(mainlist))
# print()


# list1=[8,6,3,2]
# list2=list(itertools.accumulate(list1))
# print(list2)
# accumulate=>nomber+add+....

# print(list(itertools.permutations([1, "a", 7, "b", 2, "c"], 6)))
# print(list(itertools.combinations_with_replacement(
#     [1, "a", 7, "b", 2, "c"], 6)))


# print(list(itertools.product([1,3,2],['a','b'])))
# print(list(itertools.product([1,3,2],"sepsi")))
# print(list(itertools.product([1,3,2],repeat=5)))


# for i in itertools.repeat("simix",4):
#     print(i,end=" ")
7

# for i in itertools.cycle([5,8,7,6,4,74,97,8,]):
#     if i>10:
#         break
#     print(i,end=" ")


# counter=0
# for i in itertools.cycle("shuxes  "):
#     if counter>15:
#         break
#     print(i,end=" ")
#     counter+=1


# print(dir(itertools))
# for i in itertools.count(0,8):
#     if i>100:
#         break
#     print(i,end="  ")
