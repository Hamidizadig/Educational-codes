class Employee:
    def __init__(self, name, family, mobile, address):
        self.name = name
        self.family = family
        self.mobile = mobile
        self.address = address

    def showInfo(self):
        print(f"{self.name}\t{self.family}\t{self.mobile}\t{self.address}")
# ---------------------------------------------------


class OfficialEmployee(Employee):
    def __init__(self, name, family, mobile, address, basicSalery, oneHourSalery, numberOvertime):
        super().__init__(name, family, mobile, address)
        self.__basicSalery = basicSalery
        self.__oneHourSalery = oneHourSalery
        self.__numberOvertime = numberOvertime
        
        

    def __premium(self):
        return self.__basicSalery*0.12

    def __overTime(self):
        if(self.__numberOvertime > 30):
            self.__numberOvertime = 30
        return(self.__oneHourSalery*self.__numberOvertime)

    def SalaryCalc(self):
        sum = self.__basicSalery + self.__overTime()-self.__premium()
        return sum

    def salaryInfo(self):
        print(
            f"basicSalery : {self.__basicSalery}\t premium: {self.__premium()}\t\t overTime : {self.__overTime()}")
# ---------------------------------------------------

oe1 = OfficialEmployee('shixas', 'fits', '0719000000',
                       'Hamburg', 17000, 100, 16)
oe1.showInfo()
oe1.salaryInfo()
print(oe1.SalaryCalc())
