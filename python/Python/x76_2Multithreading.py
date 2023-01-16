from time import sleep
from threading import Thread,current_thread,Lock

# counter=0
# lock=Lock()
# def increment():
#     global counter
#     lock.acquire()
#     counter+=1
#     sleep(1)
#     print(f'counter : {current_thread().name} : {counter}')
#     lock.release()
    
# t1=Thread(target=increment)
# t2=Thread(target=increment)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print('END')



counter=0
lock=Lock()
def increment():
    global counter
    with lock:
        counter+=1
        sleep(1)
        print(f'counter : {current_thread().name} : {counter}')
        
    
t1=Thread(target=increment)
t2=Thread(target=increment)

t1.start()
t2.start()

t1.join()
t2.join()

print('END')
