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

    def __hash__(self) -> int:
        return hash(self.__name)*hash(self.__age)


x = 100
y = "mehdi"
z = 12.34
print(hash(x))
print(hash(y))
