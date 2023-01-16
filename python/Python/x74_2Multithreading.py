from time import sleep
from threading import Thread

# def fun(name):
#     print('Start:'+name)
#     sleep(4)
#     print('End  :'+name)

# class MyThread(Thread):
#     def __init__(self,name):
#         super().__init__()
#         self.name = name
#     def run(self):
#         fun(self.name)

# t1=Thread(target=fun, args=['  ashax'])
# t2=Thread(target=fun, args=['  kisso'])

# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print('END...')



def fun(name,delay):
    print('Start:'+name)
    for i in range(1,11):
        sleep(delay)
        print(name+'_'+str(i))
    print('End  :'+name)

t1=Thread(target=fun, args=['  ashax',0.5])
t2=Thread(target=fun, args=['  kisso',0.3])

t1.start()
t2.start()

t1.join()
t2.join()
print('END...')