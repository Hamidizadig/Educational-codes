class Teacher:
    id = ''
    firstName = ''
    lastName = ''
    hour = 0
    payPerOneHour = 0

    def getID(self):
        return self.id

    def setID(self, value):
        self.id = value

    def getFirstName(self):
        return self.firstName

    def setFirstName(self, value):
        self.firstName = value

    def getLastName(self):
        return self.lastName

    def setLastName(self, value):
        self.lastName = value

    def getHour(self):
        return self.hour

    def setHour(self, value):
        if(value > 0):
            self.hour = value
        else:
            self.hour = 0

    def getPayPerOneHour(self):
        return self.payPerOneHour

    def setPayPerOneHour(self, value):
        if value > 0:
            payPerOneHour = value
        else:
            payPerOneHour = 0

    def __init__(self, i='', f='', l='', h=0, p=0):
        self.setID(i)
        self.setFirstName(f)
        self.setLastName(l)
        self.setHour(h)
        self.setPayPerOneHour(p)

    def Payment(self):
        return self.hour*self.payPerOneHour

    def __str__(self):
        return self.id+'   '+self.firstName+'  ' +\
            self.lastName+'   '+str(self.hour)+'   ' +\
            str(self.payPerOneHour)+'  '+str(self.Payment())


def main():
    t1 = Teacher()
    print(str(t1))
    t2 = Teacher('12', 'sashixia', 'shouts', 140, 100)
    print(str(t2))


main()
