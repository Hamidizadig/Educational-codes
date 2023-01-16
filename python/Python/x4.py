class Person:
    __x=None

    def __init__(self,name,family,age):
        self.__name=self.__toPascalC(name)
        self.__family=self.__toPascalC(family)
        self.__age=age
        print(f"x:{self.__x}")

    def __toPascalC(self,str1):
        strList=list(str1)
        strList[0]=chr(ord(strList[0])-32)
        self.__x=2000
        return "".join(strList)
    
    def showPI(self):
        print(f"Name : {self.__Name}")  
        print(f"Family : {self.__Family}") 
        print(f"Age : {self.__Age}") 
        self.__x=4000
        
    def showTeacherI(self):
        print(f"Teachercode is : {self.__TeacherC")


st1=Student("ana","lens",25,99)
st1.showStudentI()
print(f"z: {st1.1z}")

t1=Teacher("anosax","shux"29,987)
t1.showTeacherI()
print(f"z: {t1.z")