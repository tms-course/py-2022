import socket
from repository import Table

sock = socket.socket()
sock.bind(('localhost', 8080))
sock.listen(1)
conn, address = sock.accept()
print('S', conn, address)

while True:
    try:
        operation, *data = conn.recv(1024).decode().split()
        if operation == "add": Table.login(*data)
        elif operation == "edit": Table.edit_user(*data)
        else: Table.delete_user(*data)
    except Exception as e:
        response = str(e)
        conn.send(response.encode())
        continue

    conn.send('Ok'.encode())

conn.close()