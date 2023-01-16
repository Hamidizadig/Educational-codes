# from time import sleep
# from threading import Thread,current_thread,Semaphore


# counter=0
# lock=Semaphore(value=2)

# def fun1():
#     global counter
#     lock.acquire()
#     counter+=1
#     sleep(1)
#     print(f'counter : {current_thread().name} : {counter}')
#     lock.release()

# thread_list=[]
# for i in range(8):
#     thread_list.append(Thread(target=fun1))
    
# for i in range(8):
#     thread_list[i].start()
        
# for i in range(8):
#     thread_list[i].join()
# print('END')



from time import sleep
from threading import Thread,current_thread,BoundedSemaphore


counter=0
lock=BoundedSemaphore(value=2)

def fun1():
    global counter
    lock.acquire()
    counter+=1
    sleep(1)
    print(f'counter : {current_thread().name} : {counter}')
    lock.release()
    lock.release()
# Error 

thread_list=[]
for i in range(8):
    thread_list.append(Thread(target=fun1))
    
for i in range(8):
    thread_list[i].start()
        
for i in range(8):
    thread_list[i].join()
print('END')