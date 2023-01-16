class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

        def SPI(self):
            print(self.__name)
            print(self.__age)

        def __eq__(self, obj2):
            if not isinstance(obj2, Person):
                return False
            return self.__name == obj2.__name and self.__age == obj2.__age

        def __str__(self) -> str: return f"{self.__name}\t{self.__age}"


class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("shomax", 22)
p2 = Person("spex", 30)
p3 = Person("shomax", 22)
if p1 == p3:
    print("True")
else:
    print("no")
m1 = MyClass("kata", 32)
if p1 == m1:
    print("yess")
else:
    print("no")
print(str(p1))
print(p1.__str__())
print(p1)
