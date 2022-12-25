import socket

sock = socket.socket()
sock.connect(('', 8080))
while True:
    choice = int(input('Enter "1" to add user\nEnter "2" to edit user\nEnter "3" to delete user\n'))
    match choice:
        case 1:
            data = "add " + input('Enter username:\n') + " " + input('Enter user\'s fullname:\n')
            sock.send(data.encode())
        case 2:
            op = "edit " + input('Enter username that you want to edit\n')
            field_to_change = input('What field you want to edit (username, first_name or last_name)\n')
            new_value = input('Enter new value\n')
            sock.send("{} {} {}".format(op, field_to_change, new_value).encode())
        case 3:
            data = "delete " + input('Enter username that you want to delete\n')
            sock.send(data.encode())
        case _:
            print('Invalid input')
            continue

    response = sock.recv(1024)
    print(response)

sock.close()
