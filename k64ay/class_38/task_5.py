import time
from multiprocessing import Process, Event

event = Event()

def test():
    print('test func is starting...')
    while True:
        event.wait()
        print('test')
        time.sleep(1)

def test_event():
    while True:
        time.sleep(2)
        event.set()
        print('Event True')
        time.sleep(2)
        event.clear()
        print('Event False')

if __name__ == '__main__':
    Process(target=test).start()
    Process(target=test_event).start()