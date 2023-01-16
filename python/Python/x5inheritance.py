class A:
    def __init__(self):
         print("run A")
         
    def showA(self):
        print("AAA")
        
class B:
    def __init__(self):
        print("run B")
        
    def showB(self):
        print("BBB")

class C(A,B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print("run C")
    def showC(self):
        print("ccc")
       
c=C()
c.showC()