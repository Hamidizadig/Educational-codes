import itertools
import operator

list1 = [('silias', 89), ('shiraxas', 45), ('lusius', 98),
         ('sarixmix', 49), ('azikix', 78)]
list2 = sorted(list1, key=operator.itemgetter(1), reverse=True)
list3 = operator.itemgetter(0, 1, 2, 3)(list2)
list4 = [item[0] for item in list3]
list4_1 = [item[1] for item in list3]
list5 = list(itertools.combinations(list4, 3))
list6 = list(itertools.permutations(list4, 3))
print(list2)
print(70*'_')
print(list3)
print(70*'_')
print(list4)
print(70*'_')
print(list4_1)
print(70*'_')
print(len(list5))
print((list5))
print(70*'_')
print(len(list6))
print(list6)
