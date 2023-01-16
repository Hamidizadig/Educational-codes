from time import sleep
from threading import Thread
# def fun(name):
#     print('Start'+name)
#     sleep(4)
#     print('End'+name)
# fun('xpaxis')
# fun('silapus')


def fun(name):
    print('Start'+name)
    sleep(4)
    print('End'+name)


t1 = Thread(target=fun, args=['xpaxis'])
t2 = Thread(target=fun, args=['silapus'])

t1.start()
t2.start()
t1.join()
t2.join()

print('End')
