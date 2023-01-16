import operator

# print(operator.rshift(17,2))
# print(operator.lshift(17,2))

# print(operator.contains("dtfghj'vgbhnj","ghj")) =>true
# print(operator.contains(str(256254784),str(2)))

people = [("ani", "sonjas", 30), ("ds", 'jk', 77),
          ("gg", "sd", 4), ("ds", 'jk', 87)]
l = [5, 5, 8, 9, 5, 2, 7, 6, 3, 2]
print(sorted(people, key=operator.itemgetter(0)))


# l=[5,5,8,9,5,2,7,6,3,2]
# t=('gf','tr',"se","ee","poi")
# getter=operator.itemgetter(1,3)
# print(getter(l))
# print(getter(t))
# print(operator.itemget)

'''
l1=[5,5,8,9,5,2,7,6,3,2]
operator.delitem(l1,3)
print(l1)
'''
# print(operator.countOf([4,6,8,2,3,4,9,1,5,8,74,5,2,1,5,4],4))
# print(operator.countOf("tfuygtfuhjjuiyudtfghgfdtyrfgbvhjfjg","h"))
# print(dir(operator))
# print(operator.add(3,1))
# print(operator.sub(3,1))
# print(operator.mul(3,1))
# print(operator.truediv(3,1))
# print(operator.floordiv(3,1))
# print(operator.truediv(3,1))
# print(operator.le(7,3))
# print(operator.ge(7,3))
# print(operator.eq(7,3))
# print(operator.gt(7,3))
# print(operator.lt(7,3))

# print(operator.not_(False))
# print(operator.not_(34>5))
