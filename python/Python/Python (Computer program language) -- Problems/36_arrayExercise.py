import numpy as np
a=np.arange(0,10,2)
print('A = ',a)
b=np.arange(1,10,2)
print('B = ',b)
print('A+B= ',a+b)
print('A-B= ',a-b)
print('A*B= ',a*b)
print('A/B= ',a/b)
a=np.append(a,b)
print('A = ',a)
b=np.insert(b,0,a)
print('B =',b)
b=np.unique(a)
print('B= ',b)
b=np.delete(b,2)
print('B= ',b)
b=np.delete(b,2)
print('B= ',b)
print('Min(B)= ',np.amin(a),'\tMin(b)=',np.amin(b))
print('Max(B)= ',np.amax(a),'\tMax(b)=',np.amax(b))
print('Average(A)= ',np.average(a),'\tAverage(B)=',np.average(b))
print('Median(A)= ',np.median(a),'\t Var(B)= ',np.var(b))
print('Var(A)= ',np.var(a),'\t Var(B)= ',np.var(b))
a=np.copy(a)
print('A =',a)
c=np.copy(a)
print('C= ',c)
print('C is A ',c is a)
c=b
print('C= ',c)
print('C is B= ',c is b)
print('A>5= ',a>5)
print('Sqrt(B)= ',np.sqrt(b))

