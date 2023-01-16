from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def show(self):
        pass


class Student(Person):
    def __init__(self, stI, name, age):
        super().__init__(name, age)
        self.stI = stI

    def show(self):
        print(f"{self.name}\t{self.age}\t{self.stI}")


class Teacher(Person):
    def __init__(self, tC, name, age):
        super().__init__(name, age)
        self.tC = tC

    def show(self):
        print(f"{self.name}\t{self.age}\t{self.tC}")


s1 = Student(170, "anisa", 17)
t1 = Teacher(199, 'maxima', 41)
t1.show()
s1.show()
