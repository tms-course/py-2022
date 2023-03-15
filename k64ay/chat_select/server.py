import select
from socket import socket, AF_INET, SOCK_STREAM

def clients_read(r_clients, all_clients):
    # Словарь ответов {сокет: запрос}
    responses = {}

    for sock in r_clients:
        try:
            data = sock.recv(1024).decode('utf-8')
            responses[sock] = data
        except:
            print(f'Клиент {sock.fileno()} {sock.getpeername()} отключился')
            all_clients.remove(sock)

    return responses

def clients_write(requests, w_clients, all_clients):
    """Отвечает клиентам на их запросы"""
    for sock in w_clients:
        if sock in requests:
            try:
                response = requests[sock].encode('utf-8')
                sock.send(response.lower())
            except:
                print(f'Клиент {sock.fileno()} {sock.getpeername()} отключился')
                sock.close()
                all_clients.remove(sock)

def main_server():
    address = ('localhost', 8888)
    clients = []

    s = socket(AF_INET, SOCK_STREAM)
    s.bind(address)
    s.listen(5)
    s.settimeout(0.6)

    while True:
        print('cicle')
        try:
            conn, addr = s.accept()
        except OSError as e:
            pass
        else:
            print(f'Получаем запрос на соединение от {str(addr)}')
            clients.append(conn)
        finally:
            wait = 10
            r = []
            w = []

        try:
            r, w, e = select.select(clients, clients, [], wait)
        except:
            pass

        requests = clients_read(r, clients)
        if requests:
            clients_write(requests, w, clients)

main_server()
