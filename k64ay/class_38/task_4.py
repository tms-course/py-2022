from multiprocessing import Process, Lock, RLock

def f(lock, i):
    with lock:
        print(f'hello world', i)

def g(lock, j):
    lock.release()

def main():
    lock = Lock()

    for i in range(10):
        Process(target=f, args=(lock, i)).start()

if __name__ == '__main__':
    main()