import socket

from common import Payload

sock = socket.socket()
sock.connect(('127.0.0.1', 9092))

while True:
    text = input()
    out_payload = Payload(text)
    sock.send(bytes(out_payload))

    data = sock.recv(1024)
    if not data:
        break
    in_payload = Payload.from_bytes(data)
    print('Receive', in_payload)
sock.close()