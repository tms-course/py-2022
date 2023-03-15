import socket

print('Для выхода из чата наберите: `exit`, `quit` или `q`.')
# Удаленный хост
HOST = '192.168.31.5'
# тот же порт, что и у сервера
PORT = 8008
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        mess = input('\nВведите что нибудь >>> ')
        if any(mess.lower() in ext for ext in ['quit', 'exit', 'q']):
            break  
        mess = mess.encode('utf-8')
        s.sendall(mess)
        data = s.recv(1024)
        print('\nПолучено: ', data.decode('utf-8'))
