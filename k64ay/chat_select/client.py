import sys
from socket import *

PLACE = ('localhost', 8888)

def client():
    with socket(AF_INET, SOCK_STREAM) as sock:
        sock.connect(PLACE)

        while True:
            message = input('Ваше сообщение: ')
            sock.send(message.encode('utf-8'))
            receive = sock.recv(1024).decode('utf-8')
            print('Ответ:', receive)

if __name__ == '__main__':
    client()
