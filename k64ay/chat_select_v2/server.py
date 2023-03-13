# server.py
import select, socket

print('Для выключения сервера нажмите Ctrl+C.')
sock = socket.socket()
sock.bind(('localhost', 8008))
sock.listen(5)
sock.setblocking(False)
inputs = [sock]  # сокеты, которые будем читать
outputs = []  # сокеты, в которые надо писать
messages ={} # здесь будем хранить сообщения для сокетов

print('\nОжидание подключения...')
while True:
    # вызов `select.select` который проверяет сокеты в 
    # списках: `inputs`, `outputs` и по готовности, хотя бы
    # одного - возвращает списки: `reads`, `send`, `excepts`
    reads, send, excepts = select.select(inputs, outputs, inputs)

    # Далее проверяются эти списки, и принимаются 
    # решения в зависимости от назначения списка

    # список READS - сокеты, готовые к чтению
    for conn in reads:
        if conn == sock:
            # если это серверный сокет, то пришел новый
            # клиент, принимаем подключение
            new_conn, client_addr = conn.accept()
            print('Успешное подключение!')
            # устанавливаем неблокирующий сокет
            new_conn.setblocking(False)
            # поместим новый сокет в очередь 
            # на прослушивание
            inputs.append(new_conn)
            
        else:
            # если это НЕ серверный сокет, то 
            # клиент хочет что-то сказать
            data = conn.recv(1024)
            if data:
                # если сокет прочитался и есть сообщение 
                # то кладем сообщение в словарь, где 
                # ключом будет сокет клиента
                if messages.get(conn, None):
                    messages[conn].append(data)
                else:
                    messages[conn] = [data]

                # добавляем соединение клиента в очередь 
                # на готовность к приему сообщений от сервера
                if conn not in outputs:
                    outputs.append(conn)
            else:
                print('Клиент отключился...')
                # если сообщений нет, то клиент
                # закрыл соединение или отвалился 
                # удаляем его сокет из всех очередей
                if conn in outputs:
                    outputs.remove(conn)
                inputs.remove(conn)
                # закрываем сокет как положено, тем 
                # самым очищаем используемые ресурсы
                conn.close()
                # удаляем сообщения для данного сокета
                del messages[conn]

    # список SEND - сокеты, готовые принять сообщение
    for conn in send:
        # выбираем из словаря сообщения
        # для данного сокета
        msg = messages.get(conn, None)
        if len(msg):
            # если есть сообщения - то переводим 
            # его в верхний регистр и отсылаем
            temp = msg.pop(0).decode('utf-8').upper()
            conn.send(temp.encode())
        else:
            # если нет сообщений - удаляем из очереди
            # сокетов, готовых принять сообщение 
            outputs.remove(conn)

    # список EXCEPTS - сокеты, в которых произошла ошибка
    for conn in excepts:
        print('Клиент отвалился...')
        # удаляем сокет с ошибкой из всех очередей
        inputs.remove(conn)
        if conn in outputs:
            outputs.remove(conn)
        # закрываем сокет как положено, тем 
        # самым очищаем используемые ресурсы
        conn.close()
        # удаляем сообщения для данного сокета
        del messages[conn]
