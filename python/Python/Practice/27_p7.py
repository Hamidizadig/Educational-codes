class MyExeption1(Exception):
    def __init__(self,message):
        super().__init__(message='MyExeption1')
        self.message=message
        
    def __str__(self):
        return self.message

class MyExeption2(Exception):
    def __init__(self,message):
        super().__init__(message='MyExeption1')
        code=1
        self.message=message+" "+code


class MyExeption3(Exception):
    pass



def dateTypeValidate():
    pass


# class Student:
#     def dataTypeValidate(dataType1):
#         if dataType1==0:
#             obj1=MyExeption1("xedcrfvtgbyhnjmk")
#                 raise obj1