from reprlib import aRepr
import numpy as np
# list1 = [54,2,9], [3,3,4], [5,4,7], [[1,0,6], [6,7,4], [9,8,2]]
# list2 = [[[1,4,2,8], [3,7,7,9], [5,4,3]], [[1,8,7,4], [6,7,4,9], [9,2,6,1]], [[4,7,7,9], [1,4,9], [1,5,2]]]
# list3 = (5, 4, 5, 9, 8, 7, 6, 2, 0, 5)
# arr1 = np.array(list1)
# arr2 = np.array(list2)
# arr3 = np.array(list3)
##Slice
# print(arr1[:2])
# print(arr1[:2,0:2])
# print(arr2[0:1:,1:2])
l1=(2,8,4,6,2,8,4,5,7)
l2=['d','w','g','s','w','p']
l3=[True,False,True,True]
l4=[2.4,8.47,4.77,6.0,2.01]
arr1=np.array(l1)
arr2=np.array(l2)
arr3=np.array(l3)
arr4=np.array(l4)
print(arr1.dtype)
print(arr2.dtype)
print(arr3.dtype)
print(arr4.dtype)
newArr1=arr1.astype('U5')
newArr4=arr4.astype('i')
newArr4=arr4.astype('f')
newArr4=arr4.astype('b')
print(newArr1)
print(newArr4)