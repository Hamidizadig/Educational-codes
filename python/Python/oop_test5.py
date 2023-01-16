
"""
class Person:
    def __init__(self, name, family, phone, address):
        self.name = name
        self.family = family
        self.phone = phone
        self.address = address
    def showInfo(self):
        print(self)
class Student(Person):
    def __init__(self, shNumber, name, family, phone, address):
        super().__init__(name, family, phone, address)
        self.shNumber = shNumber
    def __str__(self):
        return str(self.shNumber) + " "+self.name+" "+self.family+" "+self.phone+" "+self.address
class Teacher(Person):
    def __init__(self, teacherCode, name, family, phone, address):
        super().__init__(name, family, phone, address)
        self.teacherCode = teacherCode
    def __str__(self):
        return str(self.teacherCode) + " "+self.name+" "+self.family+" "+self.phone+" "+self.address
class Employee(Person):
    def __init__(self, employeeId, name, family, phone, address):
        super().__init__(name, family, phone, address)
        self.employeeId = employeeId
    def __str__(self):
        return str(self.employeeId) + " "+self.name+" "+self.family+" "+self.phone+" "+self.address
s1 = Student(1200, 'ali', 'rezaie', '0912000000', 'Tehran')
t1 = Teacher(11350, "mehdi", "abbasi", '09121111111', 'Malayer')
s1.showInfo()
t1.showInfo()
**************************
class person:
    def __init__(self,name,family,phone,address):
        self.name=n
        self.family=f
        self.phone=p
        self.address=a
    def showInfo(self):
        print(self)
        """
class room:
    def __init__(self,size):
        self.size=size
    def show(self):
        print(self)
class bedroom(room):
    def __init__(self ,name,size):
        super().__init__(size)
        self.name=name   
    def __str__(self):
        return str(self.name)+"self.size"
r1=room("aaa",12)
print(r1)
    