from threading import Thread,Event
from time import sleep

# def fun1():
#     print('Start fun1...')
#     sleep(5)
#     print('End fun1')
    

# def fun2():
#     print('Start fun1...')
#     sleep(2)
#     print('End fun2')
    
# t1=Thread(target=fun1)
# t2=Thread(target=fun2)

# t1.start()
# t2.start()



def fun1():
    print('Start fun1...')
    sleep(2)
    e1.set()
    e2.wait()
    print('End fun1')
    e1.clear()
    

def fun2():
    print('Start fun1...')
    sleep(10)
    e2.set()
    e1.wait()
    print('End fun2')
    e2.clear()
    
e1=Event()
e2=Event()
    
t1=Thread(target=fun1)
t2=Thread(target=fun2)

t1.start()
t2.start()