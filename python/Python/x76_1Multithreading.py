from concurrent.futures import ThreadPoolExecutor
from threading import Thread,current_thread,enumerate
from time import sleep
from tkinter.font import families

def fun(name,family):
    print("Start"+name+" "+family)
    sleep(1)
    print("End"+name+" "+family)
    
with ThreadPoolExecutor(max_workers=1) as executor:   
    names=['shkof','sanas','sirox','p','x']
    families=['astonos','hanas','asisos','s','h']
    executor.map(fun,names,families)
    
    
    
     
