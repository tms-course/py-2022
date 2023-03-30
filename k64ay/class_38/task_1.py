from time import sleep
from threading import Thread, currentThread

def func():
    for i in range(10):
        print(f"{currentThread().name}: {i}")
        sleep(1)

th = Thread(target=func)
th.start()

for i in range(5):
    print(f'{currentThread().name}: {i}')
    sleep(1)