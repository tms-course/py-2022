import socket

from common import Payload

sock = socket.socket()
sock.bind(('', 9092))
sock.listen(1)
conn, address = sock.accept()
print('S', conn, address)

while True:
    data = conn.recv(1024)
    if not data:
        break
    
    in_payload = Payload.from_bytes(data)
    print('Receive', in_payload)
    
    text = input()
    out_payload = Payload(text)
    conn.send(bytes(out_payload))
    
conn.close()