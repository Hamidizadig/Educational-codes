class Person:
    def __init__(self,name,family,age):
        self.__name = self.__toPascalCase(name)
        self.__family = self.__toPascalCase(family)
        self.__age = age
    def __toPascalCase(self,str1):
        strList=list(str1)
        strList[0]=chr(ord(strList[0])-32)
        return ''.join(strList)
    def _showPersonInfo(self):
        print(f" Name: {self.__name}")
        print(f" Family: {self.__family}")
        print(f" Age: {self.__age}")
    def _getFulnameLenght(self):
        return len(self.__name)+len(self.__family)    
class Student(Person):
    def __init__(self,name,family,age,studentId):
        super().__init__(name,family,age)
        self.__studentId = studentId
    
    def showStudentInfo(self):
        print(f"studentId: {self.__studentId}")
        self._showPersonInfo()         
class Teacher(Person):
    def __init__(self,name,family,age,teacherCode):
        super().__init__(name,family,age)
        self.__teacherCode=teacherCode     
    def showTeacherInfo(self):
        print(f"teacgher Code is: {self.__teacherCode}")
        print(f"fullName lenght: {self._getFulNameLenght()}")
st1=Student("sonya","schmit",31,7)
st1.showStudentInfo()      
print("-------------------------------------")
teacher1=Teacher("siax","kushes",40,454)
teacher1.showTeacherInfo()