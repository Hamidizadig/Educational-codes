'''
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def showPI(self):
        print(self.__name)
        print(self.__age)
    def getName(self):
        return self.__name
    def setName(self,name):
        self.__name=name        
p1=Person("shans",30)
p1.showPI()
print(p1.getName())
p1.setName("Anastasia")
p1.showPI()'''


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.___age = age

    def showPI(self):
        print(self.__name)
        print(self.__age)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.___age

    @age.setter
    def age(self, age):
        self.__age = age


p1 = Person("sara", 19)
p1.showPI()
print(p1.name)
p1.name = "kamixia"
p1.showPI()
p1.age = 30
print(p1.age)
