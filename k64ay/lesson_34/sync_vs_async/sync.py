from time import time, sleep


def first(x: int) -> None:
    print(x**2)
    sleep(3)
    print('first завершена')
    
def second(x: int) -> None:
    print(x**0.5)
    sleep(3)
    print('second завершена')
    
def main():
    first(4)
    second(4)
    
start = time()
main()
print('Выполнилось за {:2.4f} секунд'.format(time() - start))

    