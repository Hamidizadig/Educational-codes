from reprlib import aRepr
import numpy as np

arr1=np.array([5,4,5,9,8,7,6,2,0,5,9,1])
arr2=np.array([[1,2,3,4,5],[6,7,8,9,0],[10,11,12,13,14]])
arr3=np.array([[[4,2,8], [3,7,9], [5,4,3]], [[1,7,4], [6,7,4,9], [9,2,6,1]], [[4,7,7,9], [1,4,9], [1,5,7]]])
# print(arr1.ndim)
# print(arr2.ndim)
# print(arr3.ndim)

# print(arr1.shape)
# print(arr2.shape)
# print(arr3.shape)

# print(arr1.reshape(3,4))
# print(arr1.reshape(2,6))
# print(arr1.reshape(4,3))
# print(arr1.reshape(12,1))
# print(arr1.reshape(1,12))
# print(arr2.reshape(-1))

# for item in arr1:
#     print(item)
    

# for row in arr2:
#     for col in row:
#         print(col,end='\t')
#     print()

# arr1=np.array([1,2,3])
# arr2=np.array([9,8,7,6])
# arr3=np.concatenate((arr1,arr2))
# print(arr3)


# arr1=np.array([[1,2,3],[9,8,7]])
# arr2=np.array([[4,5,6],[2,5,8]])
# arr3=np.concatenate((arr1,arr2))
# arr3=np.concatenate((arr1,arr2),axis=1)
# print(arr3)
# print(arr3.shape)

arr1=np.array([[1,2,3],[9,8,7]])
arr2=np.array([[4,5,6],[2,5,8]])
arr3=np.stack((arr1,arr2),axis=1)
print(arr3)
print(arr3.shape)
