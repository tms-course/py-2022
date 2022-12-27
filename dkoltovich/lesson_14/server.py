import os
import socket
from dotenv import load_dotenv
from db import connector
from repository import UserRepo, MySqlException
import json
load_dotenv()


class Server:

    def __init__(self):
        self.sock = socket.socket()
        self.sock.bind((os.getenv('SOCKET_HOST'), int(os.getenv('SOCKET_PORT'))))
        self.sock.listen(1)
        self.user_repo = UserRepo(next(connector))

    def run(self):
        conn, address = self.sock.accept()
        self.handle_client(conn)

    def handle_client(self, conn: socket):
        """
        Main method that represents server performance
        Returns: None
        """
        try:
            while True:
                try:
                    data = conn.recv(1024).decode()
                    if not data:
                        break
                    data_dict = json.loads(data)
                    self.process_operation(data_dict)
                except MySqlException as e:
                    response = str(e)
                    conn.send(response.encode())
                    continue
                conn.send('Ok'.encode())
        finally:
            conn.close()

    def process_operation(self, data: dict):
        """
        Process client's operation
        Args:
            data: dictionary with user's operation and values in case edit or create operations,
            dictionary with operation and unique key (username) otherwise

        Returns: None

        """
        match data.get('operation'):
            case 1: self.user_repo.create(data)
            case 2: self.user_repo.edit(data)
            case 3: self.user_repo.delete(data['username'])


Server().run()
