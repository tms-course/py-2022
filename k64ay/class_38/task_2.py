import time
from threading import Thread, Lock, currentThread

value = 0
locker = Lock()

def inc_value():
    global value
    for _ in range(10):
        locker.acquire()
        value += 1
        print(f'{currentThread().name} => {value}')
        locker.release()

if __name__ == '__main__':
    for _ in range(5):
        Thread(target=inc_value).start()