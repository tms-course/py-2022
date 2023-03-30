import time
from threading import Thread, Timer, currentThread

def delayed():
    print(f'{currentThread().name} - hello')

if __name__ == '__main__':
    threads = []
    for _ in range(3):
        t = Timer(3, delayed)
        threads.append(t)
        t.start()

    for i in range(3):
        print(f'{currentThread().name} {i}')
        time.sleep(1)

    for thr in threads:
        thr.cancel()