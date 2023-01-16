class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def showPersonInfo(self):
        print(self.name)
        print(self.age)

p1=Person("yasha",27)
p1.showPersonInfo()
