class Time:
    hour=0
    minute=0
    second=0
    def __init__(self,hour=0,minute=0,second=0):
        self.hour=hour
        self.minute=minute
        self.second=second
    def isEqual (self , t):
        return self.hour==t.hour and self.minute== t.minute and self.second==t.second
t1=Time()
t2=Time(10,55,44)
if t1.isEqual(t2)==True:
    print('t1 Equal t2')
else:
    print('t1 Not Equals t2')
if t2.isEqual (t2)==True:
    print('t2 Equals t2')
else:
    print('t2 Not Equals t2')
