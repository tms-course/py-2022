from multiprocessing import Process, Lock

def f(lock, i):
    with lock:
        print(f'hello world', i)

def main():
    lock = Lock()

    for i in range(10):
        Process(target=f, args=(lock, i)).start()

if __name__ == '__main__':
    main()