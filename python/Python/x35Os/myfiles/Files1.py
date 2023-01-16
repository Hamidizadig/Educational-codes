# file1=open('myfiles/f1.txt','r')
# print(file1.tell())
# print(file1.read())
# print(file1.tell())
# file1.close()


# file1=open('myfiles/f1.txt','r+')
# file1.seek(5,0)
# print(file1.readline())
# print(file1.tell())
# file1.seek(3,0)
# file1.write('****')
# file1.close()


# file1=open('myfiles/f1.txt','r+')
# print(file1.tell())
# print(file1.readline())
# file1.seek(0,0)
# print(file1.readline())
# file1.close()


# file1=open('myfiles/f1.txt','rb')
# print(file1.tell())
# print(file1.readline())
# file1.seek(-7,2)
# print(file1.readline())
# file1.close()


file1 = open('myfiles/f1.txt', 'r')
print(file1.read(5))
print(file1.name)
print(file1.mode)
print(file1.closed)
file1.close()
