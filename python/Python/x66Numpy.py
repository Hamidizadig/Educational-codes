import numpy as np
from numpy import random

# x=random.rand(5)
# print(x)

# x=random.rand(3,5)
# print(x)

# x=random.randint(100,size=(3,5))
# print(x)

# x=random.randint(2,size=(3,5))
# print(x)

# x=random.randint(100,size=(20,30))
# print(x)

# print(random.choice([10,2,20,34,94,123,17],size=(2,3)))

# print(random.choice([10,2,20,7],p=[0.1,0.1,0.5,0.3],size=(30)))

# arr1=np.array([1,2,3,4,5])
# random.shuffle(arr1)
# print(arr1)

# arr1=np.array([1,2,3,4,5])
# print(random.permutation(arr1))
# print(arr1)


arr1 = np.array([1, 2, 3, 4, 5])
arr2 = random.permutation(arr1)
print(random.permutation(arr1))
print(arr2)
print(arr1)
