class O:
    __a=None
    def __init__(self,a):
        self.__a=a
    def geta(self):
        return self.__a
    def seta(self,newa):
        self.__a=newa
    def _showOInfo(self):
        print(f"{self.__a}")
        
class C(O):
    __I=None
    def __init__(self,I,a):
        super .__init__(a)
        self.__I=I
    deff=C(5,3)
    c1.S()
    
    
        