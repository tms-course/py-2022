import time
import random
from multiprocessing import set_start_method
from multiprocessing import Process, Barrier, current_process

set_start_method('fork')

b = Barrier(5)

def f(bar):
    name = current_process().name
    sl = random.randint(2, 10)
    print(f'[{name}] - waiting {sl} seconds!')
    time.sleep(sl)
    bar.wait()
    print(f'{name} - complete')

if __name__ == '__main__':
    ##set_start_method('fork')
    processes = []
    for i in range(10):
        pr = Process(target=f, args=(b,))
        processes.append(pr)
        pr.start()

    # for pr in  processes:
    #     pr.join()

    print('All processes complete')
