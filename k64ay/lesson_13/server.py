import socket
from threading import Thread

def handle_client(conn, address):
    print("Connection from: " + str(address))
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("from connected user: " + str(data))
        data = input(' -> ')
        conn.send(data.encode())

    conn.close()

host = socket.gethostname()
port = 2000

server_socket = socket.socket()
server_socket.bind((host, port))

server_socket.listen(2)

while True:
    conn, address = server_socket.accept()
    Thread(target=handle_client, args=(conn, address)).start()