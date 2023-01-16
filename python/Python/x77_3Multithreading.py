from threading import Timer, current_thread


def fun1(name):
    print(current_thread().name)
    print('hello '+name)


t1 = Timer(5, fun1, args=['mersix'])

t1.start()
t1.join()

print('END')
