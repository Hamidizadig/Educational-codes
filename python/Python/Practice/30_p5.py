import collections
Person=collections.namedtuple('Person','Name Ave Age')
p1=Person('amixus',14.56,18)
p2=Person('shanix',18.25,24)
p3=Person('rasshef',12.30,19)
p4=Person('maximyas',19.78,48)
list1=[p1,p2,p3,p4]
print(list1)

list1.append('p5=Person("ana",17,22)')
print(list1)