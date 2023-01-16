from time import sleep
from threading import Thread

def fun(name):
    print('Start:'+name)
    sleep(4)
    print('End  :'+name)

class MyThread(Thread):
    def __init__(self,name):
        super().__init__()
        self.name=name
        
    def run(self):
        fun(self.name)
        
t1=MyThread('shitz')
t2=MyThread('susha')

t1.start()
t2.start()

t1.join()
t2.join()
print('END...')