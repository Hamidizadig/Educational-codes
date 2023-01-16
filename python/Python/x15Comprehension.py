"""
def getColor(n):
    if n==1:
        return "red"
    elif n==2:
        return "blue"
    return "Green"
list1=[1,2,3,4,5,6]
dic1={x*x:getColor(x) for x in list1}
print(dic1)
"""
"""
list=[1,2,3,4,5]
l=["a","f","e","m","s"]
zip1=zip(list,l)
print(zip1)
print(type(zip1))

for key,value in zip1:
    print(f"{key} : {value}")
"""
"""
l=[1,3,2,1,2,1,2,3,4,3,2,1,7]
set1={x for x in l}
s2={x*x for x in l}
print(l)
print(set1)
print(s2)
"""
"""
matrix=[]
for i in range(0,3):
    matrix.append([])
    for j in range(1,6):
            matrix[i].append(j)
print(matrix)  
"""
'''
matrix = [[j for j in range(1,6)]for i in range(0,3)]
print(matrix)
'''
'''
def printMatrix(matrix):
    for row in matrix:
        for col in row:
            print(col,end='\t')
        print()
        
matrix=[[j*i for j in range(1,11)]for i in range(1,11)]
printMatrix(matrix)
'''
'''
def printMatrix(matrix):
    for row in matrix:
        for col in row:
            print(col,end='\t')
        print()
m1=[[j for j in range(1,11)]for i in range(1,6)]
printMatrix(m1)
'''


def print3D(m):
    for v in m:
        for row in v:
            for col in row:
                print(col, end='\t')
            print()


m1 = [[[j for j in range(1, 4)] for i in range(1, 11)] for k in range(1, 6)]
print3D(m1)
