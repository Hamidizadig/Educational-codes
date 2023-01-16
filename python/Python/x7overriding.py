class A:
    def fun1(self):
        print("A class Fun1")
        
    def fun2(self):
        print("A class Fun2")
        
    def fun3(self):
        print("A class Fun3")
        
    def mul(self,a,b):
        print(a*b)
        
        
class B:
    def fun1(self):
        print("B class Fun1")
        
    def fun2(self):
        print("B class Fun2")
        
    def sum(self,a,b):
        print(a+b)
    
    def mul(self,a,b):
        print((a-b)*1000)
        
 
def func(obj):
    obj.fun1()
    obj.fun2()
    obj.mul(30,4)
    
a=A()
b=B()

func(a)
func(b)
           