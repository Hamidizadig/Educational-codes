import math
class Circle:
    PI=math.pi
    r=0
    def __init__(self):
        self.r=0
    def __init__(self,r):
        self.r=r
    def __del__(self):
        print('Object is deleted')
    def Area(self):
        return self.PI*(self.r*self.r)
    def Perime(self):
        return 2*self.PI*self.r
    def __str__(self):
        s='R : '+str(self.r)
        s+='\t\tArea : '+str(self.Area())
        s+='\t\tPerime:'+str(self.Perime())
        return s
r=int(input('Enter r : '))
c= Circle(0)
print(str(c))
c=Circle(r)
print(str(c))
del c