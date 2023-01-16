class A:
    def __init__(self):
         print("run A")
         
    def showA(self):
        print("AAA")
        
class B(A):
    def __init__(self):
        A.__init__(self)
        print("run B")
        
    def showB(self):
        print("BBB")

class C(B):
    def __init__(self):
        B.__init__(self)
        print("run C")
    def showC(self):
        print("ccc")
       
c=C()
c.show(A)