# file1=open('f1.txt','a')
# print(file1.readline())
# file1.close()
# #error


# file1=open('htbgfvd.tx','a')
# try:
#     print(file1.readline())
# except Exception as error:
#     print('error:',error)
# finally:
#     file1.close()
#     print('end')


# with open('ghjk.txt','a') as file1:
#     try:
#         print(file1.readline())
#     except Exception as error:
#         print('Error :', error)
#     finally:
#         file1.close()
# print("end")


# try:
#     with open('myfiles/f1.txt','r') as file1 , open('myfiles/backupf1.txt','w') as file2:
#         for line in file1.readlines():
#             file2.write(line)
#         file1.close()
#         file2.close()
# except Exception as error :
#     print('Error :', error)


# try:
#     with open('myfiles/f1.txt','r') as file1 , open('myfiles/backupf1.txt','w') as file2:
#         for line in file1.readlines():
#             file2.write(line)
#         file1.close()
#         file2.close()
# except Exception as error :
#     print('Error :', error)
# finally:
#     file1.close()
#     file2.close()


# class Writable:
#     def __init__(self,filePath):
#         self.filePath=filePath

#     def __enter__(self):
#         self.fileObject=open(self,filePath,'w')
#         return self.fileObject

#     def __exit__(self, *exc):
#         if(self.fileObject):
#             self.fileObject.close()

# #f1=FileWritable('myfiles/f1.txt')
# with FileWritable('myfiles/f1.txt') as f1:
#     f1.write('hello python')


# class Files:
#     def __init__(self,filePath,fileMode):
#         self.filePath=filePath
#         self.fileMode=fileMode
#     def __enter__(self):
#         self.fileObject=open(self.filePath,self.fileMode)
#         return self.fileObject
#     def __exit__(self, *exc):
#         if(self.fileObject):
#             self.fileObject.close()
# #f1=FileWritable('myfiles/f1.txt')
# with Files('myfiles/f1.txt','a') as f1:
#     f1.write('  hello python')


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __enter__(self):
        print('Start')
        return self

    def __exit__(self, *exc):
        print('Finish')
        return False

    def getage(self):
        return self.age


with Person('sammix', 13)as person1:
    print(person1.getAge())
