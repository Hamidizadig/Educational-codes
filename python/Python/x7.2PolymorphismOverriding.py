"""
class A:
    def show(self):
        print("AAA")    
class B(A):
    def show(self):
        print("BBB")
        return A.show(self) 
b=B
b.show()
"""

"""
class A:
    def show(self):
        print("AAA")       
class B:
    def show(self):
        print("BBB")      
class C(B,A):
    def show(self):
        print("CCC")
        return A.show(self)   
c=C()
C.show()
super(C,c).show()
"""
class A:
    def show(self):
        print("AAA")
class B(A):
    def show(self):
        print("BBB")
        return A.show(self) 
class C(A):
    def show(self):
        print("CCC")
class D(B,C):
    def show(self):
        print("DDD")
        return C.show(self)
d=D()
d.show()
super(D,d).show()