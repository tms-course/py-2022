import os
from subprocess import Popen

# Список клиентский процессов
process_list = []

while True:
    user = input('"start" - запустить 10 клиентов\n"close" - закрыть клиентов\n"quit" - выйти\n')

    if user == 'quit':
        break
    elif user == 'start':
        for _ in range(10):
            # Открывает каждого клиента в новой консоли
            process_list.append(Popen('python3 client.py', shell=True))

        print('Запущено 10 клиентов')
    elif user == 'close':
        # Уничножаем процессы
        for process in process_list:
            process.kill()
        process_list.clear()
