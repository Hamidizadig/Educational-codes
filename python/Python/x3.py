class Person:
    id = None
    _name = None
    __family = None

    def __init__(self,id, name, family):
        self.id =id
        self._name = name
        self.__family = family

    def getFamily(self):
        return(self).__family

    def setFamily(self, newFamily):
        self.__family = newFamily

    def _showPersonInfo(self):
        print(f"{self.id}\t{self._name}\t{self.__family}")


class Student(Person):
    __studentId = None

    def __init__(self, studentId, i, name, family):
        super().__init__(i, name, family)
        self.__studentId = studentId

    def showStudentInfo(self):
        print(self.__studentId)
        self._showPersonInfo()


student1 = Student(123, 1, "rasha ", "sinapx")
student1.showStudentInfo()