class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __add__(self, obj2):
        return self.age+obj2.age

    def __mul__(self, obj2):
        return self.age*obj2.name+"  yesss"


p1 = Person("a", 5)
p2 = Person("b", 7)
print(p1+p2)
print(p1*p2)
