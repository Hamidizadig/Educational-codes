"""
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def showPersonInfo(self):
        print(self.name)
        print(self.age)
        
    @staticmethod    
    def sum(x,y):
        return x+y

p1=Person("yasha",27)
p1.showPersonInfo()
    
p2=Person("sina",27)
p2.showPersonInfo()
print(Person.sum(20,40))"""
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def showPersonInfo(self):
        print(self.name)
        print(self.age)
    @classmethod    
    def fun1(cls,x,y):
        return cls.sum(x+y)+2000
p1=Person("yasha",27)
p1.showPersonInfo()  
p2=Person("sina",27)
p2.showPersonInfo()
print(Person.sum(20,40))
print(Person.fun1(3,25))