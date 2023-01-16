# matrix1=[
#     [2,5,4],
#     [4,8,9],
#     [2,5,6],
#     [9,7,1]
# ]

# list1='\n'.join(['\t'.join([f'{col}' for col in row]) for row in matrix1])
# print(matrix1)
# print(list1)


def printMatrix(matrix):
    print ('\n'.join(['\t'.join([f'{col}' for col in row]) for row in matrix1]))

matrix1=[
    [2,5,4],
    [4,8,9],
    [2,5,6],
    [9,7,1]
]

matrix2=[[col+(2*col) if col>5 else  col for col in row] for row in matrix1]


printMatrix(matrix1)
print(70*'_')
printMatrix(matrix2)