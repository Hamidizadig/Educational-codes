from time import sleep
from threading import Thread,current_thread

# def fun(name):
#     print('Start:'+name)
#     print(current_thread())
#     sleep(4)
#     print('End  :'+name)

# t1=Thread(target=fun, args=['  ashax'])
# t2=Thread(target=fun, args=['  kisso'])

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print('END...')


# from time import sleep
# from threading import Thread,current_thread

# def fun(name):
#     print('Start:'+name)
#     print(current_thread().name)
#     sleep(4)
#     print('End  :'+name)

# t1=Thread(target=fun, args=['  ashax'])
# t2=Thread(target=fun, args=['  kisso'])

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print('END...')


# from time import sleep
# from threading import Thread,current_thread

# def fun(name):
#     print('Start:'+name)
#     print(current_thread().ident)
#     sleep(4)
#     print('End  :'+name)

# t1=Thread(target=fun, args=['  ashax'])
# t2=Thread(target=fun, args=['  kisso'])

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print('END...')



# from time import sleep
# from threading import Thread,current_thread

# def fun(name):
#     print('Start:'+name)
#     print(current_thread().name)
#     sleep(4)
#     print('End  :'+name)

# t1=Thread(target=fun, args=['  ashax'])
# t2=Thread(target=fun, args=['  kisso'])

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print(current_thread().name)
# print('END...')





from time import sleep
from threading import Thread,current_thread

def fun(name):
    print('Start:'+name)
    print(current_thread().name)
    sleep(4)
    print('End  :'+name)

t1=Thread(target=fun, args=['  ashax'],name='T1')
t2=Thread(target=fun, args=['  kisso'],name='T2')

t1.start()
t2.start()

t1.join()
t2.join()

print(current_thread().name)
print('END...')


