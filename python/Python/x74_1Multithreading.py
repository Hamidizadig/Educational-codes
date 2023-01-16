from time import sleep
from threading import Thread

# def fun(name):
#     print('Start'+name)
#     for i in range(1,11):
#         sleep(0.5)
#         print(name+'_'+str(i))
#     print('End'+name)
# fun('xpaxis')
# fun('silapus')




# def fun(name):
#     print('Start'+name)
#     for i in range(1,11):
#         sleep(0.5)
#         print(name+'_'+str(i))
#     print('End'+name)

# t1 = Thread(target=fun, args=['xpaxis'])
# t2 = Thread(target=fun, args=['silapus'])

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print('End')





def fun(name,delay):
    print('Start'+name)
    for i in range(1,11):
        sleep(0.5)
        print(name+'_'+str(i))
    print('End'+name)

t1 = Thread(target=fun, args=['xpaxis',0.5])
t2 = Thread(target=fun, args=['silapus',0.3])

t1.start()
t2.start()

t1.join()
t2.join()

print('End')