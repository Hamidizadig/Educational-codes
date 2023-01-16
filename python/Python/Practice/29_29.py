import datetime
import khayyam

# d1=datetime.date.today()
# print(d1)
# jd1=khayyam.JalaliDate(d1)
# print(jd1)
# d2=jd1.todate()
# print(d2)



def dec1(func):
    def inner(*args):    
        # print(f'{func(*args)}')
        dt=(datetime.datetime.today().strftime('%H:%M:%S  %d-%m-%Y '))
        print(f'{func(*args)}\t{dt}')
    return inner
@dec1
def send(message):
    return message

@dec1
def resive(message):
    return message

send   ("send   2000 € ")
resive ("resive 2500 € ")
