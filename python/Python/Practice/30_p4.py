import collections
list1=[
    {'name':'oskis','age':30},
    {'name':'ruwsuf','age':25},
    {'name':'smaxis','age':18},
    {'name':'mispix','age':25},
    {'name':'asmash','age':25}
       
       ]

list2=[dic['age']for dic in list1]
print(list2)

print(collections.Counter(list2))
print(collections.Counter(list2).most_common(1))